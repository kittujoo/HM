"""
File_Name: manifest_collector_isym_hardware.py

Desc: Collects isym hardware information for manifest file.

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tiberiu Boscan" Initial Check-in 09/14/2023
"""
import os

from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.universal_linux_tool import LinuxToolInterface

logger = Logger(os.path.basename(__file__))


class IsymHardwareManifestCollector(ManifestCollectorInterface):
    """Collects hardware related data for manifest file"""

    def __init__(self, linux_tool: LinuxToolInterface):
        self.linux_tool: LinuxToolInterface = linux_tool

    def _collect_hardware_information(self):
        hardware_info_dict = {}
        hardware_info = self.linux_tool.get_hardware_information()
        for line in hardware_info.splitlines():
            if line:
                key, value = line.split(':', 1)
                hardware_info_dict[key.strip()] = value.strip()
        return hardware_info_dict or "not available"

    def enrich_manifest(self, manifest_dict):
        logger.debug("Getting hardware information for manifest file")
        manifest_dict['hardware_info'] = self._collect_hardware_information()
