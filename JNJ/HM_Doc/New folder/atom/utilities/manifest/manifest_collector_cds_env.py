"""
File_Name: manifest_collector_cds_env.py
Desc: Collecting CDS env related data for manifest file

__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Adriano Barcelos" Initial check-in - May 05, 2023
"""

import os
import re

from utilities.constants import EMPOWER_INSTRUMENTS_FOLDER
from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.universal_cmd_execution import CmdToolInterface
from utilities.universal_registry_tool import RegistryToolInterface
from utilities.universal_text_file_tool import TextFileToolInterface

logger = Logger(os.path.basename(__file__))


class ManifestCollectorCdsEnv(ManifestCollectorInterface):
    """Collecting CDS environment related data for manifest file"""

    def __init__(self, registry_tool: RegistryToolInterface, text_file_tool: TextFileToolInterface, cmd_tool: CmdToolInterface):
        self.registry_tool = registry_tool
        self.text_file_tool = text_file_tool
        self.cmd_tool = cmd_tool

    def _get_method_editor_version(self):
        """Extracts method_editor_version from file."""
        version = "Failed while capturing version"
        try:
            version = self.text_file_tool.get_file_text(f"{EMPOWER_INSTRUMENTS_FOLDER}\\HTML\\Orion\\orion-method-editor\\version.txt").strip()
        except Exception as e:
            logger.error(f"While catching [method_editor_version] exception raised =>  {e}")
        return version

    def _get_ics_version(self):
        """Extracts ics version from file"""
        version = "Failed while capturing version"
        try:
            orion_server_exe = f"{EMPOWER_INSTRUMENTS_FOLDER}\\Bin\\OrionICS.OrionServer.exe"
            version = self.cmd_tool.execute_command("powershell", f"(Get-Item -Path '{orion_server_exe}').VersionInfo.ProductVersion")
        except Exception as e:
            logger.error(f"While catching [ics_version] exception raised =>  {e}")
        return version

    def _get_empower_version(self):
        """Extracts empower version from registry"""
        default = "Failed while capturing version"
        value = self.registry_tool.get_registry_item_value(path='SOFTWARE\\WOW6432Node\\Waters\\Empower', property_name='SoftwareVersion')

        return value or default

    def _get_winappdriver_version(self):
        """Extracts winappdriver version from command"""
        version = "Failed while capturing version"
        try:
            version = self.cmd_tool.execute_command("winget", "list", '--name="Windows Application Driver"')
            version = re.search(r'\d+.\d+.\d+.\d+', version)[0]
        except Exception as e:
            logger.error(f"While catching [winappdriver_version] exception raised =>  {e}")
        return version

    def enrich_manifest(self, manifest_dict):
        manifest_dict['method_editor_version'] = self._get_method_editor_version()
        manifest_dict['ics_version'] = self._get_ics_version()
        manifest_dict['empower_version'] = self._get_empower_version()
        manifest_dict['winappdriver_version'] = self._get_winappdriver_version()
