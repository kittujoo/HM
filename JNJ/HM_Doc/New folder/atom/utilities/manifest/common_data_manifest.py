"""
File_Name: common_data_manifest.py

Desc: Creates general data for manifest file

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Oleksii Cherniavskyi" Initial Check-in 07/11/2023
"""

import os
from datetime import datetime

from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface

logger = Logger(os.path.basename(__file__))


class CommonDataManifestCollector(ManifestCollectorInterface):

    def __init__(self, environment_type):
        self.__time_stamp = format(datetime.now().astimezone(), "%Y-%B-%d %H:%M:%S %z")
        self._environment = environment_type.name

    def enrich_manifest(self, manifest_dict):
        manifest_dict["Environment"] = self._environment
        manifest_dict["Execution_start_time"] = self.__time_stamp
