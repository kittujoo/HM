from dataclasses import dataclass, field
from logging import config

from config.logger_config import get_log_config
from utilities.configuration_models import EnvironmentType


def configure_logger(path_to_config):
    log_config = get_log_config(path_to_config)
    config.dictConfig(log_config)


@dataclass
class AtomStartArgs:
    host_atom_folder: str = field(default='ATOM', metadata=dict(
        args=['--host_atom_folder'],
        type=str,
        help='Remote folder id number. Example: ATOM -> A new folder ATOM will be created on the selected target env'
    ))
    environment: EnvironmentType = field(default=EnvironmentType.DEFAULT, metadata=dict(
        args=['--environment'],
        type=EnvironmentType,
        help='Type of the target environment REAL, SIMULATION or CDS'
    ))
    host: str = field(default='', metadata=dict(
        args=['--host'],
        type=str,
        help='Host name of the target real or simulation env for test execution'
    ))
    port: int = field(default=22, metadata=dict(
        args=['--port'],
        type=int,
        help='Target shh host port. Default to 22.'
    ))
    host_username: str = field(default='', metadata=dict(
        args=['--host_username'],
        type=str,
        help='User name for ssh connection to target atom execution host'
    ))
    host_password: str = field(default='', metadata=dict(
        args=['--host_password'],
        type=str,
        help='Password for ssh connection to target atom execution host'
    ))
    isym_interface_repo_password: str = field(default='', metadata=dict(
        args=['--isym_interface_repo_password'],
        type=str,
        help='Isym repository user token/password for the isym interface cloning'
    ))
    isym_interface_version: str = field(default='', metadata=dict(
        args=['--isym_interface_version'],
        type=str,
        help='Version (branch name/tag) of isym-interface to clone'
    ))
    ics_version: str = field(default='', metadata=dict(
        args=['--ics_version'],
        type=str,
        help='Version of ICS to download'
    ))
    isym_interface_download_only: bool = field(default=False, metadata=dict(
        args=['--isym_interface_download_only'],
        action='store_true',
        help='Configure atom script to clone and build isym interface only, test copying and execution will be skipped'
    ))
    test_filter: str = field(default=None, metadata=dict(
        args=['--test_filter'],
        type=str,
        help='filter for test execution'
    ))
    system_network_name: str = field(default=None, metadata=dict(
        args=['--system_network_name'],
        type=str,
        help='instrument system unit ispp network name'
    ))
    jump_server_host: str = field(default=None, metadata=dict(
        args=['--jump_server_host'],
        type=str,
        help='Hostname or ip address of ssh jump server. Used to connect to instrument'
    ))
    jump_server_username: str = field(default='', metadata=dict(
        args=['--jump_server_username'],
        type=str,
        help='Username of ssh jump server'))
    jump_server_password: str = field(default='', metadata=dict(
        args=['--jump_server_password'],
        type=str,
        help='Password of ssh jump server'
    ))
    jump_server_port: int = field(default=22, metadata=dict(
        args=['--jump_server_port'],
        type=int,
        help='Port of ssh jump server'
    ))
    delete: bool = field(default=False, metadata=dict(
        args=['--delete'],
        action='store_true',
        help='When set - atom remote folder will be deleted after test execution'
    ))
    run_in_docker_password: str = field(default=None, metadata=dict(
        args=['--run_in_docker_password'],
        type=str,
        help='Password for Docker registry in Artifactory.'
    ))
    run_in_docker_registry: str = field(default='waters-ics-lc-docker-local.jfrog.io', metadata=dict(
        args=['--run_in_docker_registry'],
        type=str,
        help='Configure docker registry name'
    ))
    run_in_docker_image: str = field(default='atom:latest', metadata=dict(
        args=['--run_in_docker_image'],
        type=str,
        help='Configure docker image name to run test'
    ))
    skip_atom_copying: bool = field(default=False, metadata=dict(
        args=['--skip_atom_copying', '-s'],
        action='store_false',
        help='Indicates that atom source code should not be copied to target host (useful for debugging)'
    ))
    isym_application_version: str = field(default='', metadata=dict(
        args=['--isym_application_version'],
        type=str,
        help='Version/Tag of isym application'
    ))
    timeout: int = field(default=7200, metadata=dict(
        args=['--timeout'],
        type=int,
        help='Overall test execution timeout in seconds'
    ))
    run_on_local: bool = field(default='', metadata=dict(
        args=['--run_on_local'],
        action='store_true',
        help='Start test execution on local machine'
    ))
    generate_allure_single_file: bool = field(default='', metadata=dict(
        args=['--generate_allure_single_file'],
        action='store_true',
        help='Generate singlefile allure report'
    ))
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
    enable_dev_mode: bool = field(default='', metadata=dict(
        args=['--enable_dev_mode'],
        action='store_true',
        help='Enable development mode on empower vm'
    ))
