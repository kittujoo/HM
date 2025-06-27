import abc
import os

from utilities.logger import Logger
from utilities.ssh_connection import SSh
from utilities.windows_registry_utility import get_registry_key_value

logger = Logger(os.path.basename(__file__))


class RegistryToolInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_registry_item_value(self, path, property_name, hkey_type=None):
        """Return lines count of text file"""
        raise NotImplementedError


class LocalHostRegistryTool(RegistryToolInterface):

    def get_registry_item_value(self, path, property_name, hkey_type=None):
        import winreg
        hkey_type = hkey_type or winreg.HKEY_LOCAL_MACHINE
        value = get_registry_key_value(reg_name=property_name, key=path, hkey_type=hkey_type)
        return value
    

class SshRegistryTool(RegistryToolInterface):

    def __init__(self, ssh: SSh):
        self._ssh = ssh

    def get_registry_item_value(self, path, property_name, hkey_type="HKLM"):
        with self._ssh:
            try:
                _, value, _ = self._ssh.execute(f"powershell Get-ItemPropertyValue -Path '{hkey_type}:\\{path}' -Name {property_name}", fail_on_exit_code=True)
            except Exception as e:
                logger.error(f"Failed to get {property_name} value from {path} key with error: {e}")
                value = None
            return value
