"""
File_Name: isym_log_collector.py
Desc: Class to collect the logs for isym.

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Ionel Luca" Initial check-in - Jan 12, 2023
__modified__ = "Oleksii Cherniavskyi" Refactor to support localhost execution - Jul 13, 2023
"""

import os
from typing import Dict, Optional

from utilities.file_handler import create_folder
from utilities.universal_text_file_tool import TextFileToolInterface
from utilities.logger import Logger
from utilities.logs.logs_collector_interface import LogsCollectorInterface

logger = Logger(os.path.basename(__file__))


class IsymLogCollector(LogsCollectorInterface):
    """Collect log files for real system environment."""
    _isym_logs: Dict[str, Optional[int]] = {
        "/var/log/waters/isym.log": None
        # "/var/log/syslog" - will be investigated as part of ATOM-370
    }
    _isym_logs_dict = {}

    def __init__(self, file_handler: TextFileToolInterface, results_folder):
        self.results_folder = os.path.join(results_folder, 'isym')
        self.file_handler: TextFileToolInterface = file_handler

    def start_logging(self):
        """Overrides LogsCollectorFormalInterface.set_log_starting_milestone()"""
        logger.debug("=== Isym log collector init - START ===")

        create_folder(self.results_folder, delete_if_exists=True)

        for log_name in self._isym_logs.keys():
            starting_milestone = self.file_handler.get_file_lines_count(log_name)
            self._isym_logs[log_name] = starting_milestone

        logger.debug("=== Isym log collector init - END ===")

    def stop_logging(self):
        """Overrides LogsCollectorFormalInterface.collect_logs()"""
        logger.debug("=== Isym log collector teardown - START ===")

        for log_file, milestone in self._isym_logs.items():
            try:
                if milestone is None:
                    logger.error(f"Failed to obtain {log_file} content, milestone was not set")
                log = self.file_handler.get_file_slice(log_file, milestone)
                log_path = os.path.join(self.results_folder, os.path.basename(log_file))
                with open(log_path, "w+") as file:
                    file.writelines(log)
            except Exception as e:
                logger.error(f"Logs collection for Isym file [{log_file}] failed with exception: [{e}]")

        logger.debug("=== Isym log collector teardown - END ===")
