"""
File_Name: logs_collector_instrument.py
Desc: Class to collect the logs on real system environment.

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Adriano Barcelos"
__modified__ = "Imran Abbas Satti" replaced telnet with TelnetConnection wrapper - 11/30/2022
__modified__ = "Imran Abbas Satti" created private variables and functions - 11/30/2022
__modified__ = "Ionel Luca" Refactor to support framework for simulation as well - Jan 12, 2023
__modified__ = "Oleksii Cherniavskyi" Refactor to support localhost execution - Jul 11, 2023
"""

import os
import time
from datetime import datetime
from threading import Thread, Event

from utilities.file_handler import create_folder
from utilities.logger import Logger
from utilities.logs.logs_collector_interface import LogsCollectorInterface
from utilities.telnet_connection import TelnetConnection

logger = Logger(os.path.basename(__file__))


class LogsCollectorInstrument(LogsCollectorInterface):
    """
    How to use the logger:
        Create a new logger "logger = LogsCollector(ip, username, password, instrument)"
        Issue "logger.init_logger()" when the instrument is ready to be logged
    """

    def __init__(self, ip, port, username, password, instrument, results_folder):

        self._ip = ip
        self._port = port
        self._username = username
        self._password = password
        self._instrument = instrument
        self.results_folder = results_folder
        start_time_string = format(datetime.now(), "%Y-%m-%d_%H_%M_%S")

        log_file_name = f"Log_{self._instrument}_{start_time_string}.txt"
        self._log_file_path = os.path.join(self.results_folder, log_file_name)
        self.close_event = Event()

    def start_logging(self):
        create_folder(self.results_folder)
        try:
            Thread(target=self._start_instrument_logging, daemon=False).start()
            logger.debug(f"Telnet started to log at host: [{self._ip}]")
        except SystemExit:
            logger.error('LogsCollector failed to start')
            raise

    def stop_logging(self):
        self.close_event.set()

    def _start_instrument_logging(self):
        """
        Creates the telnet session and runs through the initial commands for getting the initial system information
        """
        with TelnetConnection(self._ip, self._username, self._password, self._port) as session:
            try:
                logger.debug("Initializing Telnet session for " + self._instrument)
                self._enable_instrument_logging(session)
                self._start_logging(session)
            except KeyboardInterrupt:
                logger.debug("LogsCollector closing due to Keyboard Interrupt (Ctrl+C)")
            except EOFError:
                logger.debug("LogsCollector closing due to connection loss for instrument " + self._instrument)

    def _enable_instrument_logging(self, session):
        # command "tracersetoutput all": To enable trace to cmd mon
        # command "banner": To dump instrument version info
        # command "header": To dump Header Info
        commands = ["tracersetoutput all", "banner", "header"]
        for command in commands:
            session.send_command(command)
            output = session.read_until_console_available()
            self._write_data(output)

    def _start_logging(self, session):
        """
            Main logger loop
            Sits in loop and creates a logfile with timestamp and logs all console output until it disconnects.
            It then waits for communication before starting a new log
        """
        # Read console until client disconnects
        while True:
            if self.close_event.is_set():
                logger.debug("Log collector stop even was set")
                break
            time.sleep(1)
            output = session.read_until_console_available()
            self._write_data(output)

    def _write_data(self, data):
        """
        Writes data to log file
        :param data: text to be written to the log
        :return N/A
        """
        # Attempt to Decode binary data to string if necessary
        try:
            data = data.decode("utf-8")
            logger.debug(f"Instrument data type was: [{type(data)}]")
        except UnicodeDecodeError:
            # If unable to decode continue and write raw data
            data = str(data)
        except AttributeError:
            # Exception expected if already a string
            pass

        if data:
            try:
                with open(self._log_file_path, mode='a+') as log_file:
                    timestamp = format(datetime.now(), "%Y-%m-%d %H:%M:%S")
                    log_file.write(f"\n({timestamp}): {data}")
            except OSError as e:
                logger.error("Invalid Directory or File Name: " + self._log_file_path)
                raise e
