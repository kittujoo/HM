"""
File_Name: telnet_connection.py

Desc:
This file is created to provide telnet utility

You can consider this class as wrapper class for telnetlib

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Ionel Luca"- Initial Check-in 11/28/2022
__modified__ = " Imran Abbas" Modified on 12/06/2022

"""

import os
import telnetlib

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class TelnetConnection:
    """
    Class for using telnet to connect to instruments.

    """

    CONSOLE_AVAILABLE_MESSAGE = b"CONSOLE:#"

    def __init__(self, ip, username, password, port=23):
        self._ip = ip
        self._username = username
        self._password = password
        self._port = port
        # noinspection PyTypeChecker
        self._session: telnetlib.Telnet = None

    def start(self):
        self._session = telnetlib.Telnet(self._ip, self._port, timeout=5)
        self._authenticate(self._username, self._password)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def send_command(self, command):
        """
        Sends an ascii formatted command to the telnet session
        :param command: command to be executed in telnet session
        :return: N/A
        """
        try:
            self._session.write((command + "\r\n").encode("ascii"))
        except ConnectionResetError:
            logger.error(f"Connection Reset Error during [{command}] command execution")

    def read_until(self, text, timeout=3):
        """
        Collects binary data from telnet session until a given prompt has been found
        :param text: text to wait for
        :param timeout: timeout to wait for prompt - default None uses global timeout
        :return: Binary Data collected or Connection Error to be logged
        """
        try:
            return self._session.read_until(text, timeout)
        except ConnectionResetError:
            return "**Connection Reset Error - No console output received**"
        except KeyboardInterrupt:
            logger.debug("Telnet Session closing due to Keyboard Interrupt (Ctrl+C)")
            self.close()

    def read_until_console_available(self):
        output = self.read_until(self.CONSOLE_AVAILABLE_MESSAGE)
        return output

    def close(self):
        """
        Closes the telnet session
        :return: None
        """
        self._session.close()

    def _authenticate(self, username, password):
        try:
            self.read_until(b"login:")
            self.send_command(username)

            self.read_until(b"password:")
            self.send_command(password)

            self.read_until(self.CONSOLE_AVAILABLE_MESSAGE)
        except TimeoutError as ex:
            logger.error("Timeout Error when trying to open Telnet Session")
            raise ex
        except ConnectionRefusedError as ex:
            logger.error("Connection Refused Error:")
            logger.error("No connection could be made because the target machine actively refused it.")
            logger.error("Verify the correct ip address was entered.")
            raise ex
