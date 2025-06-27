import abc
import os
import subprocess

from utilities.logger import Logger
from utilities.ssh_connection import SSh

logger = Logger(os.path.basename(__file__))


class CmdToolInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute_command(self, *args):
        """Return lines count of text file"""
        raise NotImplementedError


class LocalHostCmdTool(CmdToolInterface):

    def execute_command(self, *args):
        result = subprocess.run(args, stdout=subprocess.PIPE, shell=True, check=True).stdout.decode().strip()
        return result


class SshCmdTool(CmdToolInterface):

    def __init__(self, ssh: SSh):
        self._ssh = ssh

    def execute_command(self, *args):
        command = " ".join(args)
        with self._ssh:
            try:
                _, value, _ = self._ssh.execute(command, fail_on_exit_code=True)
            except Exception as e:
                logger.error(f"Command: [{command}] failed with error: {e}")
                value = None
            return value
