from urllib.parse import urljoin

from isym_test_api.rest_api.api.seperation.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.api.seperation.leak_sensor_response import LeakSensorResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.api.base_response import RestResponse
from utilities.logger import Logger


class CHCLeakSensorDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.chc_leak_sensor_url = urljoin(base_url, "/api/separation/cm/leaksensor/configuration")
        self.chc_leak_sensor_status_url = urljoin(base_url, "/api/separation/cm/leaksensor/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_chc_leak_sensor_configuration(self, payload: LeakSensorConfig) -> RestResponse[None]:
        self.logger.debug(f"Put Request Method dataset: \n{payload}")
        return self._request.put_request(self.chc_leak_sensor_url, payload)

    def get_chc_leak_sensor_configuration(self) -> RestResponse[LeakSensorResponse]:
        return self._request.get_request(self.chc_leak_sensor_status_url, LeakSensorResponse)
