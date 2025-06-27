import abc
import subprocess

from utilities.ssh_connection import SSh


class PsExecInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def start_exe(self, path, ps_args: str = "", program_args: str = ""):
        """Return lines count of text file"""
        raise NotImplementedError


class PsExecRemoteTool(PsExecInterface):

    def __init__(self, ssh: SSh, username: str, password: str):
        self._ssh = ssh
        self._username = username
        self._password = password

    def start_exe(self, path, ps_args: str = "", program_args: str = ""):
        command = f"psexec -u {self._username} -p {self._password} -d -i 1 {ps_args} /accepteula {path} {program_args}"
        with self._ssh:
            moo, command_output, foo = self._ssh.execute(command)
            return command_output


class PsExecLocalTool(PsExecInterface):
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def start_exe(self, path, ps_args: str = "", program_args: str = ""):
        command = f"psexec -u {self._username} -p {self._password} -d -i 1 {ps_args} /accepteula {path} {program_args}"
        subprocess.run(command)
