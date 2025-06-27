"""
File_Name: ispp_log_collector.py
Desc: Class to collect the logs on ispp.

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__ = "Oleksii Cherniavskyi" Refactor to support localhost execution - Jul 13, 2023
"""

import os
from typing import Dict, Optional

from utilities.file_handler import create_folder
from utilities.universal_text_file_tool import TextFileToolInterface
from utilities.logger import Logger
from utilities.logs.logs_collector_interface import LogsCollectorInterface

logger = Logger(os.path.basename(__file__))


class IsppLogCollector(LogsCollectorInterface):
    """Collect log files for real system environment."""
    _isym_logs: Dict[str, Optional[int]] = {
        "/var/log/nginx/access.log": None,
        "/var/log/nginx/error.log": None
        # "/var/log/syslog" - will be investigated as part of ATOM-370
    }

    def __init__(self, file_handler: TextFileToolInterface, results_folder):
        self.results_folder = os.path.join(results_folder, 'ispp')
        self.file_handler: TextFileToolInterface = file_handler

    def start_logging(self):
        """Overrides LogsCollectorFormalInterface.set_log_starting_milestone()"""
        logger.debug("=== Ispp log collector init - START ===")

        create_folder(self.results_folder, delete_if_exists=True)

        for log_name in self._isym_logs.keys():
            starting_milestone = self.file_handler.get_file_lines_count(log_name)
            self._isym_logs[log_name] = starting_milestone

        logger.debug("=== Ispp log collector init - END ===")

    def stop_logging(self):
        """Overrides LogsCollectorFormalInterface.collect_logs()"""
        logger.debug("=== Ispp log collector teardown - START ===")

        for log_file, milestone in self._isym_logs.items():
            try:
                if milestone is None:
                    raise ValueError(f"Failed to obtain {log_file} content, milestone was not set")
                log = self.file_handler.get_file_slice(log_file, milestone)
                log_path = os.path.join(self.results_folder, os.path.basename(log_file))
                with open(log_path, "w+") as file:
                    file.writelines(log)
            except Exception as e:
                logger.error(f"Logs collection for Ispp file [{log_file}] failed with exception: [{e}]")

        logger.debug("=== Ispp log collector teardown - END ===")
