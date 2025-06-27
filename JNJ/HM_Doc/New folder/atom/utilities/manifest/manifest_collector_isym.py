"""
File_Name: manifest_collector_isym.py

Desc: Collects isym version for manifest file.

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


class IsymManifestCollector(ManifestCollectorInterface):
    """Collects isym version for manifest file"""

    def __init__(self, linux_tool: LinuxToolInterface):
        self.linux_tool = linux_tool

    def _collect_isym_data(self):
        isym_version = self.linux_tool.get_dpkg_version("isym")
        return isym_version or "not available"

    def enrich_manifest(self, manifest_dict):
        logger.debug("Getting isym version for manifest file")
        manifest_dict['isym'] = self._collect_isym_data()
