from urllib.parse import urljoin

from isym_test_api.rest_api.api.system.leak_sensors_configuration_request import LeakSensorsConfiguration
from isym_test_api.rest_api.api.system.leak_sensors_response import LeakSensorsStatus
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class LeakSensorsDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.leak_sensors_url = urljoin(base_url, "api/system/leaksensors/status")
        self.leak_sensors_config_url = urljoin(base_url, "api/system/leaksensors/configuration")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_leak_sensors_config(self, payload: LeakSensorsConfiguration):
        self.logger.debug(f"Post Request Leak Sensors Configuration: \n{payload}")
        self._request.put_request(self.leak_sensors_config_url, payload)

    def get_leak_sensors(self) -> LeakSensorsStatus:
        return self._request.get_request(self.leak_sensors_url, LeakSensorsStatus).data
