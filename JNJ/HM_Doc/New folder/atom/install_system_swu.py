import glob
import os
import shutil
import sys
import zipfile
from dataclasses import field, dataclass
from os.path import basename, join
from time import time

from argparse_dataclass import ArgumentParser
from requests import RequestException

from isym_test_api.rest_api.api.base_response import ServerRestApiException
from isym_test_api.rest_api.api.system.system_state_response import SystemStateEnum
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from utilities.assert_timeout import AssertTimeout
from utilities.atom.configurations import configure_logger
from utilities.atom.constants import ATOM_ROOT_FOLDER, RESULTS_FOLDER
from utilities.common_utilities import task
from utilities.constants import DHCP_CONFIG_PATH, CURRENT_PROJECT_BRANCH, JFROG_REPO
from utilities.empower_utility import extract_instruments_dhcp_lease
from utilities.jfrog.jfrog_client import get_client
from utilities.logger import Logger
from utilities.requests_helper import upload_file
from utilities.rest_client import rest_session

if not os.path.exists(RESULTS_FOLDER):
    # create results directory if missing
    os.makedirs(RESULTS_FOLDER)

logger = Logger(basename(__file__))

swu_file_folder = "C:\\atom\\swu"
swu_file_name = "install.swu"


def swu_latest_aql(branch):
    return [
        "items.find",
        {
            "$and": [
                {"type": "file"},
                {"repo": JFROG_REPO},
                {"path": "orion-yocto-bsp/swu"},
                {"@branch": branch}
            ]
        },
        ".sort",
        {"$desc": ["created"]},
        ".limit(1)"
    ]


def swu_version_aql(branch, version):
    return [
        "items.find",
        {
            "$and": [
                {"type": "file"},
                {"repo": JFROG_REPO},
                {"path": "orion-yocto-bsp/swu"},
                {"@branch": branch},
                {"@version": version}
            ]
        }
    ]


@dataclass
class SwuInstallationArgs:
    system_swu_version: str = field(default=None, metadata=dict(
        args=['--system_swu_version'],
        type=str,
        help='Start updating system with the given swu file version'
    ))
    jfrog_token: str = field(default=None, metadata=dict(
        args=['--jfrog_token'],
        type=str,
        help='Token to jfrog artifactory'
    ))


def main() -> None:
    configure_logger(RESULTS_FOLDER)
    parser = ArgumentParser(
        SwuInstallationArgs,
        description='Installing swu file'
    )
    args, extra_args = parser.parse_known_args()
    swu_file_version = args.system_swu_version

    jfrog_client = get_client(args.jfrog_token)

    if swu_file_version.lower() == "latest":
        query = swu_latest_aql(branch=CURRENT_PROJECT_BRANCH)
    else:
        query = swu_version_aql(branch=CURRENT_PROJECT_BRANCH, version=swu_file_version)

    artifacts = jfrog_client.aql_search_artifact(query=query)

    assert len(artifacts) > 0, f"No artifacts found for given query: [{query}]"
    assert len(artifacts) <= 1, f"More that one artifact found for given query. Query: [{query}]. Artifacts: {[artifact.name for artifact in artifacts]}"
    artifact = artifacts[0]

    swu_file_version = artifact.properties['version']
    swu_file_version = swu_file_version[0] if isinstance(swu_file_version, list) else swu_file_version

    print(f"Swu file to be downloaded. Version: [{swu_file_version}], File name: [{artifact.name}]")

    swu_folder = join(swu_file_folder, swu_file_version)
    if os.path.exists(swu_folder):
        shutil.rmtree(swu_folder)
    os.makedirs(swu_folder, exist_ok=True)

    local_artifact_path = join(swu_folder, artifact.name)
    local_swu_file_path = join(swu_folder, swu_file_name)

    with task(f"Downloading swu file. File name: [{artifact.name}]. Version: [{swu_file_version}]"):
        jfrog_client.download_artifact_in_chunks(artifact, local_artifact_path)

        file_extension = artifact.suffix
        if file_extension == ".swu":
            os.rename(local_artifact_path, local_swu_file_path)
        elif file_extension == ".zip":
            with task(f"Unzipping [{local_artifact_path}] to [{swu_folder}] folder"):
                with zipfile.ZipFile(local_artifact_path) as zip_file:
                    zip_file.extractall(swu_folder)
                found_file = next(iter(glob.glob(join(swu_folder, '*.swu'))), None)
                if not found_file:
                    raise ValueError(f"Failed to find swu file in [{swu_folder}] directory.")
                os.rename(found_file, local_swu_file_path)
                os.remove(local_artifact_path)
        else:
            raise ValueError(f"Unexpected file name: [{artifact.name}]")

    with task(f"Obtaining system ip from dhcp file"):
        with open(DHCP_CONFIG_PATH) as f:
            dhcp_config = f.read()
        lease = extract_instruments_dhcp_lease(content=dhcp_config)
        ispp_ip = lease["ip"]

    with task(f"Uploading swu file to ISPP with IP: [{ispp_ip}]"):
        upload_url = f"https://{ispp_ip}:8081/upload"
        upload_file(url=upload_url, file_path=local_swu_file_path)

    assert_timout = AssertTimeout(timeout=10, poll=10)

    api_base_url = f"http://{ispp_ip}:80"

    system_state_driver = SystemStateDriver(RestAPIDriver(rest_session()), api_base_url)
    start_time = time()
    total_wait_in_seconds = 10800
    with task(f"Waiting for system to become IDLE"):

        assert_timout.are_equal(lambda: system_state_driver.get_system_state().state, SystemStateEnum.SystemStateEnum_INITIALIZING,
                                timeout_in_seconds=total_wait_in_seconds,
                                message="Unexpected system state",
                                ignored_exceptions=(ServerRestApiException, RequestException))

        wait_for_idle = max(0, int(total_wait_in_seconds - (time() - start_time)))

        assert_timout.are_equal(lambda: system_state_driver.get_system_state().state, SystemStateEnum.SystemStateEnum_IDLE,
                                timeout_in_seconds=wait_for_idle,
                                message="Unexpected system state",
                                ignored_exceptions=(ServerRestApiException,))

    exit(0)


if __name__ == "__main__":
    if ATOM_ROOT_FOLDER not in sys.path:
        sys.path.append(ATOM_ROOT_FOLDER)
    main()
