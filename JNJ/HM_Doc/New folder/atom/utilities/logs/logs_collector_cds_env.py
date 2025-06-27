"""
File_Name: logs_collector_cds_env.py
Desc: Collect log files specific for the CDS environment.
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Yugal Shah" Initial check-in - May 04, 2023
__modified__ = "Oleksii Cherniavskyi" Refactor to support localhost execution - Jul 12, 2023
"""
import glob
import os
import shutil
import tempfile
from datetime import datetime

from utilities.constants import EMPOWER_INSTRUMENTS_FOLDER
from utilities.file_handler import get_file_lines_count, copy_trimmed_file
from utilities.logger import Logger
from utilities.logs.logs_collector_interface import LogsCollectorInterface

logger = Logger(os.path.basename(__file__))


class LogsCollectorCDSEnv(LogsCollectorInterface):
    """Collect log files for CDS environment."""

    _cds_logs = [
        f"{EMPOWER_INSTRUMENTS_FOLDER}\\Nginx\\logs\\access.log",
        f"{EMPOWER_INSTRUMENTS_FOLDER}\\Nginx\\logs\\error.log",
        f"{EMPOWER_INSTRUMENTS_FOLDER}\\Log\\OrionICS\\Information.txt",
        f"{EMPOWER_INSTRUMENTS_FOLDER}\\Log\\OrionICS\\NGNIXInstrumentService.txt",
        f"{EMPOWER_INSTRUMENTS_FOLDER}\\Log\\OrionICS\\Trace.txt"
    ]

    _temp_logs = os.path.join(tempfile.gettempdir(), "Alliance_iS_Deployment_Manager_*.log")
    _empower_log = "C:\\Windows\\empower.log"
    _logs_milestones = {}

    def __init__(self, results_folder):
        super().__init__()
        self.results_folder = os.path.join(results_folder, "ICS")
        self.log_from = datetime.now()

    def collect_temp_logs(self) -> None:
        """
        Collect Temp Logs from Empower Machine and Save it to Results Folder
        :return: None
        """
        logger.debug("=== Collect ICS Environment Temp logs START ===")

        temp_logs_dir = os.path.join(self.results_folder, "temp_logs")

        if not os.path.exists(temp_logs_dir):
            os.makedirs(temp_logs_dir)

        # Retrieve latest 3 files containing Alliance_iS_Deployment_Manager in the file name
        list_of_files = sorted(filter(os.path.isfile, glob.glob(self._temp_logs)), reverse=True)[:3]
        for file in list_of_files:
            destination = os.path.join(temp_logs_dir, os.path.basename(file))
            try:
                shutil.copy(file, destination)
            except Exception as e:
                logger.error(f"Could not copy log: {e}")

        logger.debug("=== Collect ICS Environment Temp logs END ===")

    def collect_empower_log(self):
        """
        Collect Empower Log from Empower Machine and Save it to Results Folder
        :return: None
        """
        logger.debug("=== Collect ICS Environment Empower Log START ===")

        destination = os.path.join(self.results_folder, os.path.basename(self._empower_log))
        try:
            shutil.copy(self._empower_log, destination)
        except Exception as e:
            logger.error(f"Could not copy empower log: {e}")

        logger.debug("=== Collect ICS Environment Empower Log END ===")

    def start_logging(self):
        """Overrides LogsCollectorFormalInterface.set_log_starting_milestone()"""
        logger.debug("=== Set CDS logs starting milestone - START ===")

        # Create ICS Folder if not created in results folder
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)

        for log_path in self._cds_logs:
            self._logs_milestones[log_path] = get_file_lines_count(log_path)

        logger.debug("=== Set CDS logs starting milestone - END ===")

    def stop_logging(self):
        """Overrides LogsCollectorFormalInterface.collect_logs()"""

        logger.debug("=== Collect CDS logs START ===")

        # Create ICS Folder if not created in results folder
        if not os.path.exists(self.results_folder):
            os.makedirs(self.results_folder)

        # Method to collect temp logs separately because of its new generated
        # self.collect_temp_logs(cds_log_dir)
        self.collect_empower_log()
        for log_path, length in self._logs_milestones.items():
            try:
                log_parent = os.path.dirname(log_path).replace(EMPOWER_INSTRUMENTS_FOLDER, "").lstrip("\\")
                target_dir = os.path.join(self.results_folder, log_parent)
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                write_file_path = os.path.join(target_dir, os.path.basename(log_path))
                copy_trimmed_file(log_path, write_file_path, length)
            except Exception as e:
                logger.error(f"Logs collection for CDS file [{log_path}] failed with exception: [{e}]")
        logger.debug("=== Collect CDS logs END ===")
