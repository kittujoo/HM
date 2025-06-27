"""
File_Name: chromium_browser_manifest_collector.py
Desc: Collecting chromium browser version for manifest file

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Adriano Barcelos" Initial check-in - May 05, 2023
__modified__  = "Oleksii Cherniavskyi" Refactored to support new manifest creation approach July 11, 2023
"""

import os

from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.universal_linux_tool import LinuxToolInterface

logger = Logger(os.path.basename(__file__))


class ChromiumBrowserManifestCollector(ManifestCollectorInterface):
    """Collects chromium browser version for manifest file"""

    def __init__(self, linux_universal_tool: LinuxToolInterface):
        self.linux_universal_tool = linux_universal_tool

    def _collect_chromium_version(self):
        version = self.linux_universal_tool.get_application_version("chromium-browser")
        return version.split(' ')[1] if version else "not available"

    def enrich_manifest(self, manifest_dict):
        logger.debug("Collecting chromium version for manifest file")
        manifest_dict['chromium'] = self._collect_chromium_version()
