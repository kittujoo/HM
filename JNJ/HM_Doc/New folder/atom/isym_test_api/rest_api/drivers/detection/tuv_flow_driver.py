"""
    Filename: tuv_flow_driver.py
    Driver to create TUV flow API requests
"""
from urllib.parse import urljoin

from isym_test_api.rest_api.api.detection.leak_sensor_response import LeakSensorResponse
from isym_test_api.rest_api.api.detection.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.api.base_response import RestResponse
from utilities.logger import Logger


class TUVFlowDriver(object):
    """
    Defines TUV Flow API driver, inheriting from RestAPIDriver
    """

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.tuv_leak_sensor_config_url = urljoin(base_url, "api/detection/tuv/leaksensor/configuration")
        self.tuv_leak_sensor_config_status_url = urljoin(base_url, "api/detection/tuv/leaksensor/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_tuv_leak_sensor_configuration(self, payload: LeakSensorConfig) -> RestResponse:
        self.logger.debug(f"Put Request URL: \n{payload}")
        return self._request.put_request(self.tuv_leak_sensor_config_url, payload)

    def get_tuv_leak_sensor_configuration(self) -> LeakSensorResponse:
        return self._request.get_request(self.tuv_leak_sensor_config_status_url, LeakSensorResponse).data
