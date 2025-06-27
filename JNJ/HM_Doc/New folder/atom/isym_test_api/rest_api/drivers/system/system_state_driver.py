from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.about_response import AboutResponse
from isym_test_api.rest_api.api.system.system_state_response import SystemStateResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class SystemStateDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.system_state_url = urljoin(base_url, "api/system/state")
        self.system_about_url = urljoin(base_url, "api/system/about")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_system_state(self) -> SystemStateResponse:
        return self._request.get_request(self.system_state_url, SystemStateResponse).data

    def get_about_info(self) -> RestResponse[AboutResponse]:
        return self._request.get_request(self.system_about_url, AboutResponse)
