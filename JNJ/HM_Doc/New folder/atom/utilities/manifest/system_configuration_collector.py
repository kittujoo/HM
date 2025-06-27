import json
import os

from isym_test_api.rest_api.api.system.system_configuration_response import SystemConfigurationResponse
from utilities.json_utility import as_dict
from utilities.logger import Logger
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface

logger = Logger(os.path.basename(__file__))


class SystemConfigurationCollector(ManifestCollectorInterface):
    """Collects instruments versions into manifest file"""

    def __init__(self, system_configuration: SystemConfigurationResponse):
        self.system_configuration = system_configuration

    def enrich_manifest(self, manifest_dict):
        system_configuration = as_dict(self.system_configuration)
        for module in system_configuration["modules"]:
            module["config"] = json.loads(module["config"])
        manifest_dict["system_configuration"] = system_configuration
