import os
import textwrap
from logging import INFO

from paramiko.client import SSHClient, AutoAddPolicy

from utilities.atom.configurations import AtomStartArgs
from utilities.atom.constants import ATOM_ROOT_FOLDER
from utilities.common_utilities import task
from utilities.logger import Logger
from utilities.ssh_connection import SSh
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))


def prepare_channel_to_jump_server(arguments: AtomStartArgs):
    ssh_client = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    ssh_client.connect(hostname=arguments.jump_server_host, port=arguments.jump_server_port, username=arguments.jump_server_username,
                       password=arguments.jump_server_password, timeout=arguments.timeout, look_for_keys=False)

    transport = ssh_client.get_transport()
    dest_addr = (arguments.host, 22)
    local_addr = ('localhost', 22)
    return transport.open_channel('direct-tcpip', dest_addr, local_addr, timeout=arguments.timeout)


def copy_atom_to_target(ssh, local_atom_path, remote_atom_path):
    skip_directories = ["^\\.\\w+", "devops-config", "build", "results", ".*__pycache__", "venv",
                        "docker"]

    with task(f"Copying atom source code from local folder [{local_atom_path}] to remote folder: [{remote_atom_path}]"):
        ssh.copy_folder_to_remote_host_using_archive(local_atom_path, remote_atom_path, skip_directories)
    if ssh.is_linux:
        logger.debug(f"Changing permissions to all files from '{remote_atom_path}'.")
        ssh.execute(f"chmod -R 777 {remote_atom_path}", fail_on_exit_code=True)


@task("Configuring linux machine for test execution")
def configure_linux_machine(ssh: SSh, remote_folder):
    _, output, _ = ssh.execute(f"""if command -v chromedriver &> /dev/null; then echo true; else echo false; fi""")

    if str_to_bool(output):
        logger.info(
            "Chromium driver already installed, therefore assuming all dependencies are installed, no need for extra environment setup")
    else:
        command = r"""
            sudo apt-get update && \
            sudo apt-get --fix-broken install -y && \
            sudo apt-get install -y python3-pip python3-dev python3.8-venv chromium-chromedriver"""
        ssh.execute(textwrap.dedent(command), fail_on_exit_code=True)
    logger.info("Creating virtual env and installing required pip dependencies")
    command = fr"""
        cd {remote_folder} && \
        python3 -m venv venv && \
        source ./venv/bin/activate && \
        python -m pip install --upgrade pip && \
        python -m pip install -r ./requirements/tests_execution.txt"""
    ssh.execute(textwrap.dedent(command), fail_on_exit_code=True)
    ssh.execute(
        "if [ -d \"/var/log/nginx\" ]; then sudo chmod -R 755 /var/log/nginx; fi && "
        "if [ -d \"/var/log/waters\" ]; then sudo chmod -R 755 /var/log/waters; fi",
        fail_on_exit_code=True
    )


@task("Configuring windows machine for test execution")
def configure_windows_machine(ssh, remote_folder):
    logger.info("Creating virtual env and installing required pip dependencies")
    ssh.execute(f"cd {remote_folder} && "
                f"python -m venv venv && "
                f"venv\\Scripts\\activate.bat && "
                f"python -m pip install --upgrade pip && "
                f"python -m pip install -r .\\requirements\\tests_execution.txt", fail_on_exit_code=True)


def run_on_remote(args: AtomStartArgs, command: str):
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

        if ssh.is_linux:
            configure_linux_machine(ssh, remote_folder)
            command = f"cd {remote_folder} && source ./venv/bin/activate && {command}"
        else:
            configure_windows_machine(ssh, remote_folder)
            command = f"cd {remote_folder} && venv\\Scripts\\activate.bat && {command}"

        with task(f"Start test execution via SSH command: [{command}]"):
            exit_code, output, err = ssh.execute(command, log_level=INFO, stdout_callback=lambda x: print(x, flush=True),
                                                 stderr_callback=lambda x: print(x, flush=True))

        logger.info(f"Test execution finished with exit code [{exit_code}]")

        # Delete folder contents
        if args.delete:
            ssh.delete_folder(remote_folder)

        return exit_code
