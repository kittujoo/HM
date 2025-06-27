import json
import os
import subprocess
from logging import INFO
from typing import Tuple, Dict, Any

import pytest
import toml
from argparse_dataclass import ArgumentParser

from argument_constants import PATH_TO_TEMP_CONFIG, RUN_ON_LOCAL, ISPP_HOSTNAME, HARDWARE_SYSTEM_NAME, \
    EMPOWER_SYSTEM_NAME, ICS_INSTRUMENT_TYPE
# noqa: E402
from config.settings import get_settings
from utilities.atom.configurations import AtomStartArgs, configure_logger
from utilities.atom.constants import RESULTS_FOLDER, ATOM_ROOT_FOLDER
from utilities.atom.ssh_utilities import prepare_channel_to_jump_server, copy_atom_to_target, configure_windows_machine, \
    configure_linux_machine, run_on_remote
from utilities.common_utilities import task
from utilities.configuration_models import EnvironmentType
from utilities.empower_utility import get_remote_instruments_dhcp_lease
from utilities.git_utilities import get_repo_commit_id
from utilities.isym_interface_utility import download_isym_python_models
from utilities.logger import Logger
from utilities.ssh_connection import SSh
from utilities.type_converter import convert

VERSION = "2.0.0"
logger = Logger(os.path.basename(__file__))

# Paths


if not os.path.exists(RESULTS_FOLDER):
    # create results directory if missing
    os.makedirs(RESULTS_FOLDER)


def configure_git():
    try:
        check_config_command = ['git', 'config', '--local', '--get', 'include.path']
        config_output = subprocess.check_output(check_config_command, text=True)
    except subprocess.CalledProcessError as e:
        config_output = e.output.strip()

    if not config_output:
        set_config_command = ['git', 'config', '--local', 'include.path', '../.gitconfig']
        subprocess.run(set_config_command)


def create_args() -> Tuple[AtomStartArgs, Dict[str, Any]]:
    # Parse arguments
    parser = ArgumentParser(
        AtomStartArgs,
        description='Run test on specified environment'
    )
    args, extra_args = parser.parse_known_args()

    improper_args = []
    parsed_extra_args = {}
    for arg in extra_args:
        if not arg.startswith("--"):
            improper_args.append(arg)
            continue
        split_arg = arg.split("=")
        if len(split_arg) > 2:
            improper_args.append(arg)
            continue
        key = split_arg[0]
        value = split_arg[1] if len(split_arg) == 2 else None
        if value is None:
            if key.startswith("--no"):
                key = key.replace("--no", "").lstrip("_-")
                value = "false"
            else:
                value = "true"
        parsed_extra_args[key.lstrip("-")] = convert(value)
    if improper_args:
        raise ValueError(f"Improper args was provided: {improper_args}! All arguments should prefixed with '--'")

    return args, parsed_extra_args


def print_version_graphic():
    """
    Print starting graphic and version number
    """
    print(r'    ___  __________  __  ___')
    print(r'   /   |/_  __/ __ \/  |/  /')
    print(r'  / /| | / / / / / / /|_/ /')
    print(r' / ___ |/ / / /_/ / /  / /')
    print(r'/________________________   __________  ____  __')
    print(r' /_  __/ ____/ ___/_  __/  /_  __/ __ \/ __ \/ /')
    print(r'  / / / __/  \__ \ / /      / / / / / / / / / / ')
    print(r' / / / /___ ___/ // /      / / / /_/ / /_/ / /___')
    print(r'/_/ /_____//____//_/      /_/  \____/\____/_____/')
    print(f'\nVersion {VERSION} - Atom Team - Waters Corporation\n')


def update_manifest_with_atom_data(extra_manifest_data):
    try:
        with open(os.path.join(RESULTS_FOLDER, "manifest.json"), "r+") as file:
            content = file.read()
            manifest_data = json.loads(content) if content else {}
            manifest_data = {**manifest_data, **extra_manifest_data}
            file.seek(0)
            file.truncate()
            json.dump(manifest_data, file, indent=4)
    except (FileNotFoundError, IOError):
        logger.error("Failed to open manifest file")


def start_remote_test_execution(ssh: SSh, args):
    command = f"python -m pytest --test_filter=\"{args.test_filter}\" --timeout {args.timeout} --environment={args.environment.name}"

    target = args.host_atom_folder

    if args.environment == EnvironmentType.REAL:
        logger.debug("ISPP disk usage:")
        ssh.execute("df -h")

        image_name = f"{args.run_in_docker_registry}/{args.run_in_docker_image}"
        logger.debug(f"Using docker image: {image_name}.")
        command = f"""docker run --pull=always --user $(id -u):$(id -g) --rm --shm-size=256m -v $(pwd)/{target}:/ATOM -e "ATOM_ISYM_USERNAME={args.host_username}" -e "ATOM_ISYM_PASSWORD={args.host_password}" -w /ATOM {image_name} {command}"""
    elif ssh.is_linux:
        configure_linux_machine(ssh, target)
        command = f"cd {target} && source ./venv/bin/activate && {command}"
    else:
        configure_windows_machine(ssh, target)
        command = f"cd {target} && venv\\Scripts\\activate.bat && {command}"

    print(f"Start test execution via SSH command: [{command}]")
    exit_code, output, err = ssh.execute(command, log_level=INFO, stdout_callback=lambda x: print(x, flush=True),
                                         stderr_callback=lambda x: print(x, flush=True))

    logger.info(f"Test execution finished with exit code [{exit_code}]")

    logger.debug("Copy back test results and logs")
    with task("Copying tests results from remote host"):
        ssh.copy_folder_from_remote_host_with_archiving(f"{target}/results", os.path.join(ATOM_ROOT_FOLDER, "results"))
    return exit_code, output


def run_tests_on_remote(args: AtomStartArgs):
    channel = None

    if args.jump_server_host:
        channel = prepare_channel_to_jump_server(args)

    with SSh(args.host, args.host_username, args.host_password, args.port, sock=channel, timeout=args.timeout) as ssh:
        if args.run_in_docker_password:
            logger.debug(f"Login to the Docker registry.")
            command_docker_login = f"echo {args.run_in_docker_password} | docker login {args.run_in_docker_registry} --username lcics-cloud-robot@waters.com --password-stdin"
            ssh.execute(command_docker_login, fail_on_exit_code=True)

        remote_folder = args.host_atom_folder

        if args.skip_atom_copying:
            remote_results_folder = ssh.join_path(remote_folder, "results")
            ssh.create_new_folder(remote_results_folder, delete_if_exists=True)
        else:
            ssh.create_new_folder(remote_folder, delete_if_exists=True)
            copy_atom_to_target(ssh, ATOM_ROOT_FOLDER, remote_folder)

        # Start a command on remote host
        exit_code, output = start_remote_test_execution(ssh, args)

        # Delete folder contents
        if args.delete:
            ssh.delete_folder(remote_folder)

        return exit_code


def run_tests_on_local(args):
    python_args = [f"--test_filter={args.test_filter}", f"--timeout={args.timeout}", f"--environment={args.environment.name}", f"--{RUN_ON_LOCAL}"]
    result = pytest.main(python_args)
    return result


def create_temp_config_file(args, extra_args: Dict[str, Any]):
    with open(PATH_TO_TEMP_CONFIG, 'w+') as temp_config:
        env = args.environment.name
        default_settings = {env: extra_args}
        toml.dump(default_settings, temp_config)


def get_args() -> AtomStartArgs:
    args, extra_args = create_args()
    settings = get_settings(args.environment, **extra_args)
    if args.ics_version:
        extra_args["ics_version"] = args.ics_version

    if args.run_on_local:
        extra_args["host"] = args.host

    if args.environment == EnvironmentType.REAL and not args.host:
        args.jump_server_username = args.jump_server_username or settings.jump_server_username
        args.jump_server_password = args.jump_server_password or settings.jump_server_password
        lease = get_remote_instruments_dhcp_lease(host=args.jump_server_host, port=args.jump_server_port, username=args.jump_server_username,
                                                  password=args.jump_server_password, system_name=args.system_network_name)

        ip = lease["ip"]
        if not ip:
            raise ValueError(f"System ip was absent for lease: {lease}")
        args.host = ip
        args.host_username = args.host_username or settings.host_username
        args.host_password = args.host_password or settings.host_password

    elif args.environment == EnvironmentType.CDS and ISPP_HOSTNAME not in extra_args.keys():
        args.host_username = args.host_username or settings.host_username
        args.host_password = args.host_password or settings.host_password
        lease = get_remote_instruments_dhcp_lease(host=args.host, port=args.port, username=args.host_username,
                                                  password=args.host_password, system_name=args.system_network_name)

        ip = lease["ip"]
        system_type = lease["type"]
        hardware_system_name = lease["name"]
        if not ip:
            raise ValueError(f"System ip was absent for lease: {lease}")
        if system_type is None and hardware_system_name is None:
            raise ValueError(f"System type and / or name was absent for lease: {lease}")

        extra_args[ICS_INSTRUMENT_TYPE] = system_type
        extra_args[ISPP_HOSTNAME] = ip
        extra_args[HARDWARE_SYSTEM_NAME] = hardware_system_name
        extra_args.setdefault(EMPOWER_SYSTEM_NAME, extra_args[HARDWARE_SYSTEM_NAME])

    create_temp_config_file(args, extra_args)

    args.isym_interface_repo_password = args.isym_interface_repo_password or settings.get("isym_interface_repo_password", "")

    return args


def main():
    configure_git()
    configure_logger(RESULTS_FOLDER)
    print_version_graphic()

    args = get_args()

    if args.isym_interface_version:
        if args.skip_atom_copying and args.isym_interface_download_only:
            raise ValueError("--skip_atom_copying and --isym_interface_download_only should not be used together")
        elif args.skip_atom_copying:
            logger.info("Cloning isym-interface skipped due to --skip_atom_copying was enabled")
        else:
            target_path = os.path.join(ATOM_ROOT_FOLDER, "isym_test_api", "rest_api", "models")
            download_isym_python_models(target_path=target_path,
                                        token=args.isym_interface_repo_password,
                                        isym_interface_version=args.isym_interface_version,
                                        isym_application_version=args.isym_application_version)
            if args.isym_interface_download_only:
                exit(0)

    if args.system_swu_version or args.ics_version or args.enable_dev_mode:
        exit_code = 0
        if args.system_swu_version:
            args.timeout = 11000
            command = f"python install_system_swu.py --system_swu_version {args.system_swu_version} --jfrog_token {args.jfrog_token}"
            exit_code = run_on_remote(args, command)
        if args.ics_version:
            args.timeout = 600
            command = f"python install_ics_driver.py --ics_version {args.ics_version} --jfrog_token {args.jfrog_token}"
            exit_code = run_on_remote(args, command)
        if args.enable_dev_mode:
            command = f"python enable_development_mode.py"
            exit_code = run_on_remote(args, command)
        exit(exit_code)

    if args.run_on_local:
        exit_code = run_tests_on_local(args)
    else:
        exit_code = run_tests_on_remote(args)

    if args.system_network_name:
        update_manifest_with_atom_data({"system_network_name": args.system_network_name})

    update_manifest_with_atom_data(
        {
            "atom_commit_id": get_repo_commit_id(ATOM_ROOT_FOLDER)
        }
    )

    exit(exit_code)


if __name__ == "__main__":
    main()
