from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.solvent_management.bottle_config_request import SolventBottleConfig
from isym_test_api.rest_api.api.solvent_management.bottle_volume_request import SolventBottleVolume
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class BottleConfigurationDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.bottle_configuration_url = urljoin(base_url, "/api/system/solvent/bottleconfig")
        self.bottle_volume_url = urljoin(base_url, "/api/system/solvent/bottlevolume")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_bottle_configuration(self, payload: SolventBottleConfig) -> RestResponse[SolventBottleConfig]:
        return self._request.put_request(self.bottle_configuration_url, payload, SolventBottleConfig)

    def get_bottle_configuration(self) -> RestResponse[SolventBottleConfig]:
        return self._request.get_request(self.bottle_configuration_url, SolventBottleConfig)

    def set_bottle_volume(self, payload: SolventBottleVolume) -> RestResponse[SolventBottleVolume]:
        return self._request.put_request(self.bottle_volume_url, payload, SolventBottleVolume)

    def get_bottle_volume(self) -> RestResponse[SolventBottleVolume]:
        return self._request.get_request(self.bottle_volume_url, SolventBottleVolume)
