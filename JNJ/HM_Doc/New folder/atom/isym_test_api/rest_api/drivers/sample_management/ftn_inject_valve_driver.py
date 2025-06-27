from urllib.parse import urljoin

from isym_test_api.rest_api.api.sample_management.inject_valve_request import FtnInjectValveRequest
from isym_test_api.rest_api.api.sample_management.inject_valve_response import FtnInjectValveR
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class FtnInjectValveDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.inject_valve_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/injectvalve")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_inject_valve(self, payload: FtnInjectValveRequest):
        self.logger.debug(f"Inject Valve payload: \n{payload}")
        return self._request.put_request(self.inject_valve_url, payload)

    def get_inject_valve(self) -> FtnInjectValveR:
        received_data = self._request.get_request(self.inject_valve_url, FtnInjectValveR).data
        self.logger.debug(f"Inject Valve response: \n{received_data}")
        return received_data
