"""
File_Name: logs_collector_simulator_env.py
Desc: Collect log files specific for the simulator environment.
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Ionel Luca" Initial check-in - Jan 12, 2023
__modified__ = "Oleksii Cherniavskyi" Refactor to support localhost execution - Jul 13, 2023
"""

import os

from utilities.file_handler import get_file_lines_count, copy_trimmed_file
from utilities.logger import Logger
from utilities.logs.logs_collector_interface import LogsCollectorInterface

logger = Logger(os.path.basename(__file__))


class LogsCollectorSimulatorEnv(LogsCollectorInterface):
    """Collect log files for Simulator environment."""
    __simulator_logs = [
        "/var/log/nginx/access.log",
        "/var/log/nginx/error.log",
        "/var/log/waters/isym.log"
    ]
    __logs = {}

    def __init__(self, results_folder):
        self.results_folder = results_folder

    def start_logging(self):
        """Overrides LogsCollectorFormalInterface.set_log_starting_milestone()"""

        logger.debug("=== Set simulator logs starting milestone - START ===")

        for log_path in self.__simulator_logs:
            self.__logs[log_path] = get_file_lines_count(log_path)
            logger.debug(f"Simulator log [{log_path} milestone: [{self.__logs[log_path]}]")

        logger.debug("=== Set simulator logs starting milestone - END ===")

    def stop_logging(self):
        """Overrides LogsCollectorFormalInterface.collect_logs()"""

        logger.debug("=== Collect simulator logs START ===")

        for log_path, length in self.__logs.items():
            try:
                parent_directory = os.path.basename(os.path.dirname(log_path))
                file_name = os.path.basename(log_path)
                write_file_path = os.path.join(self.results_folder, parent_directory, file_name)
                copy_trimmed_file(log_path, write_file_path, length)
            except Exception as e:
                logger.error(f"Logs collection for simulator file [{log_path}] failed with exception: [{e}]")

        logger.debug("=== Collect simulator logs END ===")
