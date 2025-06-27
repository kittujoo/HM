from urllib.parse import urljoin
from isym_test_api.rest_api.api.behavior.dynamic_leak.dynamic_leak_request import SystemLeakTest
from isym_test_api.rest_api.api.behavior.dynamic_leak.dynamic_leak_result_response import DynamicLeakResultResponse
from isym_test_api.rest_api.api.behavior.dynamic_leak.dynamic_leak_status_response import DynamicLeakStatusResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class DynamicLeakDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.dynamic_leak_url = urljoin(base_url, "/api/system/behavior/routine/dynamicleak")
        self.dynamic_leak_result_url = urljoin(base_url, "/api/system/behavior/routine/dynamicleak/result")
        self.dynamic_leak_status_url = urljoin(base_url, "/api/system/behavior/routine/dynamicleak/status")
        self._request = rest_api_driver

        self.logger = Logger(self.__class__.__name__)

    def start_leak_test(self, payload: SystemLeakTest):
        return self._request.put_request(self.dynamic_leak_url, payload)

    def get_result(self):
        return self._request.get_request(self.dynamic_leak_result_url, DynamicLeakResultResponse).data

    def get_status(self):
        return self._request.get_request(self.dynamic_leak_status_url, DynamicLeakStatusResponse).data.state
