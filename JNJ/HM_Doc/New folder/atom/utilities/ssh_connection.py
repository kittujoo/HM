"""
File_Name: ssh_connection.py
Desc: This file is created to provide ssh utility. You can consider this class as wrapper class for paramiko

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = " "I
__modified__ = " "
"""
import os
import uuid
from datetime import timedelta
from logging import DEBUG, ERROR
from timeit import default_timer as old_timer
from typing import List, Optional, Callable

import paramiko
import select
from paramiko import AutoAddPolicy, SSHClient, SSHException
from paramiko.channel import Channel
from retry import retry
from scp import SCPClient
from tqdm import tqdm

from utilities.archive_utility import make_archive, extract_tar_archive
from utilities.common_utilities import retrieve_http_request_status
from utilities.logger import Logger
from utilities.stopwatch import stopwatch
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))


class SSh:
    """
    Class to create SSH connections
    """

    def __init__(self, address: str, username: str, password: str, port: int = 22, sock: Channel = None, *args, **kwargs):
        self._is_linux: Optional[bool] = None
        logger.debug(f"Connecting to '{address}'...")
        self._address = address
        self._username = username
        self._password = password
        self._port = port
        self._sock = sock
        self._ssh: SSHClient
        self._scp: SCPClient
        self._timeout = kwargs.get("timeout", 20)

    def _connect(self):
        """
        Connect to remote host.
        """
        self._ssh = SSHClient()

        try:
            self._ssh.set_missing_host_key_policy(AutoAddPolicy())
            self._ssh.connect(self._address, port=self._port, username=self._username,
                              password=self._password, timeout=self._timeout, look_for_keys=False, sock=self._sock)

            self._scp = SCPClient(transport=self._ssh.get_transport(), progress=self._progress)
            logger.debug(f"Connected to remote host '{self._address}' via SSH")
        except paramiko.AuthenticationException:
            _ssh = None
            logger.error(f"Authentication to '{self._address}' failed , please check credentials.")
            raise
        except paramiko.SSHException as sshException:
            _ssh = None
            logger.error(f"Unable to connect to '{self._address}' via SSH: {sshException}")
            raise
        except Exception as e:
            _ssh = None
            logger.error(f"Unable to connect to '{self._address}' via SSH: {e}")
            raise

    def __enter__(self):
        self._connect()
        return self

    def connect(self):
        self._connect()

    def __exit__(self, *args):
        self._scp.close()
        self._ssh.close()
        if self._sock:
            self._sock.close()

    def send_command(self, command, log_level=DEBUG):
        """
        Sends commands to remote host.

        @param command: A single command, or a list of commands to be transferred.
        @type command: str
        @param log_level: Log level for command output, DEBUG by default
        """
        start_timer = old_timer()
        try:
            _, stdout, stderr = self._ssh.exec_command(command)
            output = b"0"

            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    output = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        output += prevdata
                        logger.log(log_level, f"{prevdata.decode().strip()}")

                    error = stderr.read().decode().strip()
                    if error:
                        logger.log(ERROR, error)

            exit_code = stdout.channel.recv_exit_status()
            return exit_code, output.decode()

        except SSHException as e:
            logger.error(f"Connection not opened. Exception: {e}")
            raise
        except Exception as e:
            logger.error(f"Exception while sending command: {e}")
            raise
        finally:
            end_timer = old_timer()
            logger.debug(f"Executed SSH command '{command}' in {timedelta(seconds=end_timer - start_timer)}")

    @staticmethod
    def _decode(data: bytes) -> str:
        for encoding in ["utf-8", "windows-1252", "ascii"]:
            try:
                return data.decode(encoding)
            except Exception as e:
                logger.warning(f"Failed to decode bytes with error: [{e}]")
        return data.decode(errors="replace")

    def _internal_exec(self, cmd, timeout=10, stdout_callback=None, stderr_callback=None, want_exitcode=False):
        # one channel per command
        stdin, stdout, stderr = self._ssh.exec_command(cmd)
        # get the shared channel for stdout/stderr/stdin
        channel = stdout.channel

        # we do not need stdin.
        stdin.close()
        # indicate that we're not going to write to that channel anymore
        channel.shutdown_write()

        # read stdout/stderr in order to prevent read block hangs
        stdout_chunks = [stdout.channel.recv(len(stdout.channel.in_buffer)).decode().strip()]
        stderr_chunks = []
        # stderr_chunks = [stderr.channel.recv(len(stderr.channel.in_buffer)).decode().strip()]
        # chunked read to prevent stalls
        while not channel.closed or channel.recv_ready() or channel.recv_stderr_ready():
            # stop if channel was closed prematurely, and there is no data in the buffers.
            got_chunk = False
            readq, _, _ = select.select([stdout.channel], [], [], timeout)
            for c in readq:
                if c.recv_ready():
                    chunk = self._decode(stdout.channel.recv(len(c.in_buffer)))
                    stdout_chunks.append(chunk)
                    if stdout_callback:
                        stdout_callback(chunk)
                    got_chunk = True
                if c.recv_stderr_ready():
                    # make sure to read stderr to prevent stall
                    chunk = stderr.channel.recv_stderr(len(c.in_stderr_buffer)).decode().strip()
                    if stderr_callback:
                        stderr_callback(chunk)
                    stderr_chunks.append(chunk)
                    got_chunk = True
            '''
            1) make sure that there are at least 2 cycles with no data in the input buffers in order to not exit too early (i.e. cat on a >200k file).
            2) if no data arrived in the last loop, check if we already received the exit code
            3) check if input buffers are empty
            4) exit the loop
            '''
            if not got_chunk \
                    and stdout.channel.exit_status_ready() \
                    and not stderr.channel.recv_stderr_ready() \
                    and not stdout.channel.recv_ready():
                # indicate that we're not going to read from this channel anymore
                stdout.channel.shutdown_read()
                # close the channel
                stdout.channel.close()
                break  # exit as remote side is finished and our bufferes are empty

        # close all the pseudofiles
        stdout.close()
        stderr.close()

        return stdout.channel.recv_exit_status(), ''.join(stdout_chunks), ''.join(stderr_chunks)

    def execute(self, command, fail_on_exit_code=False, log_level=DEBUG, stdout_callback: Optional[Callable] = None,
                stderr_callback: Optional[Callable] = None):
        """
        Sends commands to remote host.

        :param command: A single command, or a list of commands to be transferred.
        :type command: str
        :param log_level: Log level for command output, DEBUG by default
        :param fail_on_exit_code: raise exception in case exit code is not 0
        :type fail_on_exit_code: bool
        """

        def get_log_callback(level):
            def log(message):
                logger.log(level=level, msg=message)

            return log

        tmr = stopwatch().start()
        if log_level and not (stdout_callback or stderr_callback):
            stdout_callback = get_log_callback(log_level)
            stderr_callback = get_log_callback(ERROR)

        try:
            exit_code, output, errors = self._internal_exec(command, stdout_callback=stdout_callback, stderr_callback=stderr_callback)
            if exit_code and fail_on_exit_code:
                raise ValueError(f"Failed to execute command [{command}] it finished with exit code [{exit_code}]")
            return exit_code, output, errors
        except SSHException as e:
            logger.error(f"Connection not opened. Exception: {e}")
            raise e from None
        except Exception as e:
            logger.error(f"Exception while sending command: {e}")
            raise e from None
        finally:
            logger.debug(f"Executed SSH command '{command}' in {tmr} seconds")

    @retry(ValueError, delay=2, tries=3)
    def get_folders(self):
        """
        Folders are retrieved from remote host.
        """
        folders = []
        try:
            if self.is_linux:
                _, command_return = self.send_command("find . -type d")
            else:
                _, command_return = self.send_command("dir /s /b /o:n /ad")
            if command_return is None:
                raise ValueError("No folder retrieved from remote host. Retrying...")
            folders = str.split(command_return, "\n")
        except Exception as e:
            logger.warning(f"Error occurred during getting folders: [{e}]")

        if folders:
            logger.debug('The following remote folders were found on host:')
            logger.debug(", ".join(folders))
        return folders

    def delete_folder(self, folder_name: str):
        """
        Delete folder from remote host.
        @param folder_name: The name of the folder to be deleted.
        @type folder_name: str
        """
        try:
            logger.debug(f"Deleting folder '{folder_name}' from remote host.")
            if self.is_linux:
                self.send_command(f'rm -rf {folder_name}')
            else:
                self.send_command(f'rmdir /s /q {folder_name}')
        except Exception as e:
            logger.error(f"Exception raised during deleting folder '{folder_name}': {e}")
            raise

    def is_folder_exists(self, path) -> bool:
        if self.is_linux:
            _, output, _ = self.execute(f"if [ -d \"{path}\" ]; then echo true; else echo false; fi")
        else:
            _, output, _ = self.execute(f"if exist \"{path}\" (echo true) else (echo false)")

        return str_to_bool(output)

    def create_new_folder(self, remote_path: str, delete_if_exists=False):
        """
        Create remote folder.
        Existing folder would be removed and recreated.
        :param remote_path: str Remote folder to create
        :param delete_if_exists: bool Deletes folder if it was already existing
        """
        try:
            if self.is_folder_exists(remote_path):
                if delete_if_exists:
                    self.delete_folder(remote_path)
                else:
                    return

            if self.is_linux:
                exit_code, output, err_ = self.execute(f"mkdir -m 777 \"{remote_path}\"", fail_on_exit_code=True)
                logger.debug(f"New folder '{remote_path}' was created on '{self._address}'")
                return exit_code, output, err_
            else:
                exit_code, output, err_ = self.execute(f"mkdir \"{remote_path}\"", fail_on_exit_code=True)
                logger.debug(f"New folder '{remote_path}' was created on '{self._address}'")
                return exit_code, output, err_
        except Exception as e:
            logger.error(f"Exception raised during creating folder '{remote_path}': {e}")
            raise e from None

    def copy_folder_to_remote_host(self, local_path: str, remote_path: str, skip_directories: List[str] = None):
        """
        Folder is copied to remote host.
        Overwrites all files and changes all permissions to 777 recursively
        @param local_path: The path of the local folder.
        @param remote_path: The path of the remote host folder.
        @type skip_directories: list of folder names to skip
        """
        if skip_directories is None:
            skip_directories = []
        try:
            logger.debug(
                f"Copying from local path '{local_path}' to folder '{remote_path}' on remote host '{self._address}'")
            start_timer = old_timer()

            for root, dirs, files in os.walk(local_path):
                dirs[:] = [d for d in dirs if d not in skip_directories]
                for file in files:
                    logger.debug(f"Copying file '{file}'...                                                  ")
                    self._scp.put(os.path.join(local_path, file), remote_path=remote_path)
                for _dir in dirs:
                    if "." not in _dir:
                        logger.debug(f"Copying folder '{_dir}'...                                                  ")
                        self._scp.put(os.path.join(local_path, _dir), recursive=True, remote_path=remote_path)
                break
            end_timer = old_timer()
            logger.debug(f"Copy finished after {timedelta(seconds=end_timer - start_timer)}")

        except Exception as e:
            logger.error(
                f"Stopping the execution. Unable to upload folder '{local_path}' to remote path '{remote_path}': {e}")
            raise

    def copy_folder_to_remote_host_using_archive(self, local_folder, remote_folder, skip_directories):
        """
        Folder is copied to remote host, but uses and intermediate archiving step to speed up the copy.
        -> Archive the folder, copy the archive to the remote folder, extract it and remove local\remote archives.
        @param local_folder: The path of the local folder.
        @param remote_folder: The path of the remote host folder.
        @type skip_directories: list of folder names to skip
        """
        archive_name = "archive.tar.gz"
        make_archive(archive_name, local_folder, skip_directories)
        self.copy_file_to_remote_host(archive_name, remote_folder)
        os.remove(archive_name)

        if self.is_linux:
            copy_code_command = f"cd {remote_folder} && tar -zxf {archive_name} -C . && rm {archive_name}"
        else:
            copy_code_command = f"cd {remote_folder} && tar -zxf {archive_name} -C . && del \"{archive_name}\" /F /Q"
        _, extract_output, _ = self.execute(copy_code_command)
        if extract_output:
            logger.debug("Extract output:")
            logger.debug(extract_output)

    def join_path(self, *paths):
        separator = "/" if self.is_linux else "\\"
        return separator.join(paths)

    @staticmethod
    def create_tqdm_callback(*args, **kwargs):
        pbar = tqdm(*args, **kwargs)
        previous = [0]

        def viewBar(filename, total, sent):
            """Update callback: update total and n (current iteration)"""
            pbar.total = int(total)
            pbar.update(int(sent - previous[0]))
            previous[0] = sent

        # Return the callback
        return viewBar

    def copy_file_to_remote_host(self, local_file, remote_path):
        """
        File is copied to remote host.
        @param local_file: The path of the local file.
        @param remote_path: The path of the remote host folder.
        """
        viewBar = self.create_tqdm_callback(ascii=False, unit='B', unit_scale=True, ncols=100, colour="white")
        with SCPClient(transport=self._ssh.get_transport(), progress=viewBar) as scp:
            try:
                logger.debug(
                    f"Copying local file '{local_file}' to folder '{remote_path}' on remote host '{self._address}'")
                scp.put(local_file, remote_path=remote_path)
                logger.debug(f"Copy finished after")

            except Exception as e:
                logger.error(
                    f"Stopping the execution. Unable to upload file '{local_file}' to remote path '{remote_path}': {e}")
                raise e

    def copy_folder_from_remote_host(self, remote_path: str, local_path: str):
        """
        Files are retrieved from remote host.
        @param remote_path: The path of the remote folder.
        @type remote_path: str
        @param local_path: The path of the local host folder.
        @type local_path: str
        """
        try:
            logger.debug(
                f"Copying from folder '{remote_path}' on remote host '{self._address}' to local path '{local_path}'")
            start_timer = old_timer()

            self._scp.get(remote_path=remote_path, recursive=True, local_path=local_path)

            end_timer = old_timer()
            logger.debug(f"Copy finished after {timedelta(seconds=end_timer - start_timer)}")
        except Exception as e:
            logger.error(f"Unable to download remote folder '{remote_path}' to local path '{local_path}': {e}")
            raise

    def download_to_remote(self, url, remote_folder, replace_folder=False):
        """
        Download files using curl on remote machine
        Args:
            url (_type_): url to download
            remote_folder (_type_): remote folder to download to
            replace_folder (_type_): replace remote folder if exists
        """

        if replace_folder:
            logger.debug(f"Trying to download {url.split('/')[-1]} to {remote_folder} replacing folder if exists.")
        else:
            logger.debug(f"Trying to download {url.split('/')[-1]} to {remote_folder}.")

        logger.debug(f"Checking if file exists at: {url}")
        status = retrieve_http_request_status(url)

        if status != 200:
            raise FileNotFoundError(f"Resource not found! Status code: {status}")

        logger.debug(f"{url.split('/')[-1]} is available for download!")

        logger.debug(f"Creating {remote_folder} folder to remote machine...")
        exit_code, output, _ = self.create_new_folder(remote_folder, delete_if_exists=replace_folder)

        if exit_code != 0:
            raise ConnectionError("Cannot create remote folder! Output: " + str(output))

        logger.debug(f"{remote_folder} created successfully on remote machine! {output}")

        logger.debug(f"Downloading {url.split('/')[-1]} to remote machine...")
        _, output, _ = self.execute(f"pushd \"{remote_folder}\" &&"
                                    f"curl -O -S -s \"{url}\"", fail_on_exit_code=True)

        logger.debug(f"{url.split('/')[-1]} downloaded successfully to remote machine!")

    def extract_archive_remotely(self, archive_name: str, archive_path: str, delete_after_extraction: bool = False):
        """Extract archive remotely
        Args:
            archive_name (str): Archive name
            archive_path (str): Path to archive
        Raises:
            Exception: Archive extraction exception
        """
        logger.info(f"Extracting archive '{archive_name}' remotely...")
        output = ""

        try:
            if delete_after_extraction:
                _, output, _ = self.execute(
                    f"cd \"{archive_path}\"&&"
                    f"7z e \"{archive_name}\"&&"
                    f"del \"{archive_name}\"", fail_on_exit_code=True)
            else:
                _, output, _ = self.execute(
                    f"cd \"{archive_path}\"&&"
                    f"7z e \"{archive_name}\"", fail_on_exit_code=True)
            if (output.find("Everything is Ok") != -1):
                logger.debug(f"Archive extracted successfully to remote machine! You can find it here: {archive_path}")
            else:
                raise ConnectionError("Archive extraction failed. Command output: " + str(output))
        except Exception as e:
            logger.error(f"Failed to extract archive remotely with error: {e}")
            raise e

    def copy_folder_from_remote_host_with_archiving(self, remote_path: str, local_path: str):
        """
        Files are retrieved from remote host.
        @param remote_path: The path of the local folder.
        @type remote_path: str
        @param local_path: The path of the remote host folder.
        @type local_path: str
        """
        tmr = stopwatch().start()

        try:
            logger.debug(f"Copying from folder '{remote_path}' on remote host '{self._address}' to local path "
                         f"'{local_path}'")
            archive_name = f"{str(uuid.uuid4())}.tar.gz"
            archive_path = os.path.join(local_path, archive_name)
            if not os.path.exists(local_path):
                os.makedirs(local_path)

            if self.is_linux:
                self.execute(f"tar czf {archive_name} -C {remote_path} .", fail_on_exit_code=True)
                self._scp.get(remote_path=archive_name, recursive=False, local_path=local_path)
                self.execute(f"rm {archive_name}", fail_on_exit_code=True)
            else:
                self.execute(f"tar czf {archive_name} -C {remote_path} .", fail_on_exit_code=True)
                self._scp.get(remote_path=archive_name, recursive=False, local_path=local_path)
                self.execute(f"del /Q {archive_name}", fail_on_exit_code=True)

            extract_tar_archive(archive_path, local_path)
            os.remove(archive_path)

            logger.debug(f"Copy finished after {tmr.elapsed()} seconds")
        except Exception as e:
            logger.error(f"Unable to download remote folder '{remote_path}' to local path '{local_path}': {e}")
            raise

    def close_ssh_connection(self):
        try:
            self._ssh.close()
        except Exception as e:
            logger.error(f"Unable to close ssh connection : {e}")
            raise

    @staticmethod
    def _progress(filename, size, sent):
        """
        Reports the progress of file copy process.
        """
        if size == sent:
            logger.debug("File Copied %s                             \r" % filename)

    @property
    def is_linux(self):
        if self._is_linux is not None:
            return self._is_linux

        _, stdout, _ = self._ssh.exec_command("uname")
        exit_code = stdout.channel.recv_exit_status()
        host_os = stdout.readline().strip() if exit_code == 0 else "Windows"

        self._is_linux = host_os.lower() == "linux"
        return self._is_linux

    def get_file_text(self, file_path) -> List[str]:
        return self._ssh.open_sftp().open(file_path).readlines()
