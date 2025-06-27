import abc
import os
import subprocess
from typing import Optional

from utilities.logger import Logger
from utilities.ssh_connection import SSh

logger = Logger(os.path.basename(__file__))


class LinuxToolInterface(metaclass=abc.ABCMeta):
    """Common interface for linux related tools"""

    @abc.abstractmethod
    def get_dpkg_version(self, package_name):
        """
        Returns version of installed dpkg library using dpkg-query
        :param package_name:
        :return: str: Package version
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_application_version(self, tool_name: str) -> Optional[str]:
        """
        Returns version of installed application using "--version" argument
        :param tool_name: Name of installed application
        :return: str: Application version
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_hardware_information(self) -> str:
        """
        Returns hardware information
        :return: str: SOM, Carrier and Product information
        """
        raise NotImplementedError


class LocalHostLinuxTool(LinuxToolInterface):
    """Implementation of linux related tools specific to use on localhost"""

    def get_hardware_information(self) -> str:
        pass

    def get_dpkg_version(self, package_name):
        """
        Returns version of installed dpkg package using dpkg-query
        :param package_name: Name of installed dpkg package
        :return: str: Package version
        """
        command = f"dpkg-query --showformat='${{Version}}' --show {package_name} 2>/dev/null"
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, check=False)
        return result.stdout.decode().strip()

    def get_application_version(self, tool_name: str) -> Optional[str]:
        """
        Returns version of installed application using "--version" argument
        :param tool_name: Name of installed application
        :return: str: Application version
        """
        command = f"{tool_name} --version"
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, check=False)
        if result.returncode:
            return None
        return result.stdout.decode().strip()


class SshLinuxTool(LinuxToolInterface):
    """Implementation of linux related tools specific to use over ssh connection"""

    def __init__(self, ssh: SSh):
        self._ssh = ssh

    def get_dpkg_version(self, package_name: str) -> str:
        """
        Returns version of installed dpkg package using dpkg-query
        :param package_name: str: Name of installed dpkg package
        :return: str: Package version
        """
        command = f"dpkg-query --showformat='${{Version}}' --show {package_name} 2>/dev/null"
        with self._ssh:
            _, command_output = self._ssh.send_command(command)
            return command_output

    def get_application_version(self, tool_name: str) -> Optional[str]:
        """
        Returns version of installed application using "--version" argument
        :param tool_name: Name of installed application
        :return: str: Application version
        """
        command = f"{tool_name} --version"
        with self._ssh:
            return_code, command_output = self._ssh.send_command(command)
            if return_code:
                return None
            return command_output

    def get_hardware_information(self) -> str:
        """
        Returns hardware information
        :return: str: SOM, Carrier and Product information
        """
        command = f"echo {self._ssh._password} | sudo -S bash /waters_unit_tests/ig_config/config_read.sh"
        with self._ssh:
            _, command_output = self._ssh.send_command(command)
            return command_output
