import abc
import os
from itertools import islice

from utilities.ssh_connection import SSh


class TextFileToolInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_file_lines_count(self, file_path):
        """Return lines count of text file"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_file_slice(self, file_path, start_from: int = 0):
        """Gets sliced file content"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_file_text(self, file_path) -> str:
        """Gets sliced file content"""
        raise NotImplementedError


class SshTextFileTool(TextFileToolInterface):

    def __init__(self, ssh: SSh):
        self._ssh = ssh

    def get_file_lines_count(self, file_path) -> int:
        with self._ssh:
            _, output, _ = self._ssh.execute(f"wc -l < {file_path}", fail_on_exit_code=True)
            return int(output)

    def get_file_slice(self, file_path, start_from: int = 0) -> str:
        with self._ssh:
            if start_from is None or start_from < 0:
                raise ValueError("Start from should be positive int")
            _, output, _ = self._ssh.execute(f"tail --lines=+{start_from} {file_path}", fail_on_exit_code=True)
            return output

    def get_file_text(self, file_path):
        with self._ssh:
            _, output, _ = self._ssh.execute(f"cat {file_path}", fail_on_exit_code=True)
            return output


class LocalhostTextFileTool(TextFileToolInterface):

    def get_file_lines_count(self, file_path) -> int:
        lines = 0
        if os.path.exists(file_path):
            with open(file_path, encoding="utf-8") as f:
                for _ in f:
                    lines += 1
        else:
            raise ValueError(f"File [{file_path} does not exists")
        return lines

    def get_file_slice(self, file_path, start_from: int = 0) -> str:
        if start_from is None or start_from < 0:
            raise ValueError("Start from should be positive int")
        with open(file_path, encoding="utf-8") as source:
            lines = list(islice(source, start_from, None))
            return "\n".join(lines)

    def get_file_text(self, file_path):
        if not os.path.isfile(file_path):
            return None
        with open(file_path) as f:
            return "\n".join(f.readlines())
