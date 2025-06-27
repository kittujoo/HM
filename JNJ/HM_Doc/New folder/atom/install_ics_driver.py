import os
import shutil
import subprocess
import sys
from dataclasses import field, dataclass

from argparse_dataclass import ArgumentParser

from utilities.atom.configurations import configure_logger
from utilities.atom.constants import ATOM_ROOT_FOLDER, RESULTS_FOLDER
from utilities.common_utilities import task
from utilities.constants import CURRENT_PROJECT_BRANCH, JFROG_REPO
from utilities.jfrog.jfrog_client import get_client
from utilities.logger import Logger
from utilities.windows_shell_utilities import uninstall_application

if not os.path.exists(RESULTS_FOLDER):
    # create results directory if missing
    os.makedirs(RESULTS_FOLDER)

logger = Logger(os.path.basename(__file__))

ics_file_folder = "C:\\atom\\ics"
ics_download_url = "http://rdeidgart.rdeadmin.waters.com:8081/artifactory/orion-generic/OrionICS"
ics_executable_name = "AllianceiS.exe"
ics_instrument_type = "Alliance iS"


@dataclass
class IcsDriverInstallationArgs:
    ics_version: str = field(default='', metadata=dict(
        args=['--ics_version'],
        type=str,
        help='Version of ICS to download'
    ))
    jfrog_token: str = field(default=None, metadata=dict(
        args=['--jfrog_token'],
        type=str,
        help='Token to jfrog artifactory'
    ))


def ics_driver_latest_query(branch):
    return [
        "items.find",
        {
            "$and": [
                {"type": "file"},
                {"repo": JFROG_REPO},
                {"path": {"$match": "OrionICS/*"}},
                {"@branch": branch}
            ]
        },
        ".sort",
        {"$desc": ["created"]},
        ".limit(1)"

    ]


def ics_driver_version_query(branch, version):
    return [
        "items.find",
        {
            "$and": [
                {"type": "file"},
                {"repo": JFROG_REPO},
                {"path": {"$match": "OrionICS/*"}},
                {"@branch": branch},
                {"@version": version}
            ]
        }
    ]


def main() -> int:
    configure_logger(RESULTS_FOLDER)
    parser = ArgumentParser(
        IcsDriverInstallationArgs,
        description='Install ics driver'
    )
    args, extra_args = parser.parse_known_args()
    ics_version = args.ics_version

    jfrog_client = get_client(args.jfrog_token)

    if ics_version.lower() == "latest":
        query = ics_driver_latest_query(CURRENT_PROJECT_BRANCH)
    else:
        query = ics_driver_version_query(CURRENT_PROJECT_BRANCH, ics_version)

    artifacts = jfrog_client.aql_search_artifact(query=query)

    assert len(artifacts) > 0, f"No artifacts found for given query: [{query}]"
    assert len(artifacts) <= 1, f"More that one artifact found for given query. Query: [{query}]. Artifacts: {[artifact.name for artifact in artifacts]}"
    artifact = artifacts[0]

    ics_driver_version = artifact.properties['version']
    ics_driver_version = ics_driver_version[0] if isinstance(ics_driver_version, list) else ics_driver_version

    print(f"Ics driver file to be downloaded. Version: [{ics_driver_version}], File name: [{artifact.name}]")
    ics_installer_folder = os.path.join(ics_file_folder, ics_version)

    if os.path.exists(ics_installer_folder):
        shutil.rmtree(ics_installer_folder)
    os.makedirs(ics_installer_folder, exist_ok=True)

    ics_executable_path = os.path.join(ics_installer_folder, ics_executable_name)

    with task(f"Downloading ics driver file. Version: [{ics_version}]"):
        logger.info(f"Downloading ics driver file: [{ics_version}]")
        jfrog_client.download_artifact_in_chunks(artifact, ics_executable_path)

    with task(f"Uninstall current ics driver"):
        uninstall_application(ics_instrument_type)

    with task(f"Installing ics driver"):
        return subprocess.call([ics_executable_path, '/passive'], shell=True)


if __name__ == "__main__":
    if ATOM_ROOT_FOLDER not in sys.path:
        sys.path.append(ATOM_ROOT_FOLDER)
    main()
