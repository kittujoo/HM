"""
File_Name: manifest_collector_ispp.py

Desc: Collects ispp version for manifest file.

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Imran Abbas Satti" Initial Check-in 11/18/2022
__modified__ = "Imran Abbas Satti" replaced telnet with TelnetConnection wrapper - 11/30/2022
__modified__ = "Ionel Luca" Refactor to support framework for simulation as well - Jan 11, 2023
"""
import os

from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.universal_linux_tool import LinuxToolInterface

logger = Logger(os.path.basename(__file__))


class IsppManifestCollector(ManifestCollectorInterface):
    """Collects ispp version for manifest file"""

    def __init__(self, linux_tool: LinuxToolInterface):
        self.linux_tool = linux_tool

    def _collect_ispp_data(self):
        ispp_version = self.linux_tool.get_dpkg_version("ispp")
        return ispp_version or "not available"

    def enrich_manifest(self, manifest_dict):
        logger.debug("Getting ispp version for manifest file")
        manifest_dict['ispp'] = self._collect_ispp_data()
