import pytest

from utilities.configuration_models import EnvironmentType
from utilities.ssh_connection import SSh
from utilities.universal_cmd_execution import SshCmdTool, LocalHostCmdTool
from utilities.universal_linux_tool import SshLinuxTool, LocalHostLinuxTool, LinuxToolInterface
from utilities.universal_registry_tool import LocalHostRegistryTool, SshRegistryTool
from utilities.universal_text_file_tool import SshTextFileTool, LocalhostTextFileTool


@pytest.fixture(scope='session')
def registry_universal_tool(executing_host, run_on_local):
    if run_on_local:
        ssh = SSh(executing_host.hostname, executing_host.username, executing_host.password)
        return SshRegistryTool(ssh)
    else:
        return LocalHostRegistryTool()


@pytest.fixture(scope='session')
def text_file_universal_tool(executing_host, run_on_local):
    if run_on_local:
        ssh = SSh(executing_host.hostname, executing_host.username, executing_host.password)
        return SshTextFileTool(ssh)
    else:
        return LocalhostTextFileTool()


@pytest.fixture(scope='session')
def cmd_universal_tool(executing_host, run_on_local):
    if run_on_local:
        ssh = SSh(executing_host.hostname, executing_host.username, executing_host.password)
        return SshCmdTool(ssh)
    else:
        return LocalHostCmdTool()


@pytest.fixture(scope='session')
def isym_linux_universal_tool(isym_config, environment_type, run_on_local) -> LinuxToolInterface:
    """
    Generic linux related tool that could be used on localhost or over ssh (with isym specific configuration)
    :param isym_config: isym hostname, username and password for ssh connection
    :param environment_type: current environment type
    :return: LinuxToolInterface
    """
    if run_on_local or environment_type == EnvironmentType.REAL:
        ssh = SSh(isym_config.hostname, isym_config.username, isym_config.password)
        return SshLinuxTool(ssh)
    else:
        return LocalHostLinuxTool()


@pytest.fixture(scope='session')
def ispp_linux_universal_tool(ispp_config, environment_type, run_on_local) -> LinuxToolInterface:
    """
    Generic linux related tool that could be used on localhost or over ssh (with ispp specific configuration)
    :param ispp_config: ispp hostname, username and password for ssh connection
    :param environment_type: current environment type
    :return: LinuxToolInterface
    """
    if run_on_local or environment_type == EnvironmentType.REAL:
        ssh = SSh(ispp_config.hostname, ispp_config.username, ispp_config.password)
        return SshLinuxTool(ssh)
    else:
        return LocalHostLinuxTool()


@pytest.fixture(scope='session')
def localhost_linux_universal_tool() -> LinuxToolInterface:
    """
    Generic linux related tool to use on localhost
    :return: LinuxToolInterface
    """
    return LocalHostLinuxTool()
