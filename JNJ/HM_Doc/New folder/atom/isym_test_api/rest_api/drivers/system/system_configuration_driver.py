from isym_test_api.rest_api.api.system.system_configuration_response import SystemConfigurationResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger
from utilities.requests_helper import urljoin


class SystemConfigurationDriver:
    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.system_configuration_url = urljoin(base_url, "api/system/configuration")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_system_configuration(self) -> SystemConfigurationResponse:
        return self._request.get_request(self.system_configuration_url, SystemConfigurationResponse).data
