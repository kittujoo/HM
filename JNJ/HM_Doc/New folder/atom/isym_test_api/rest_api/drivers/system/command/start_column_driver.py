"""
Desc: This file contains the payload that needs to be sent with a start column request
"""
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.system.start_column_request import StartColumnRequest
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class StartColumnDriver:

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.start_column_url = urljoin(base_url, "api/datasystem/acquisition/conditioncolumn")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def set_start_column(self, payload: StartColumnRequest) -> RestResponse[None]:
        return self._request.post_request(self.start_column_url, payload)
