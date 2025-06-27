from urllib.parse import urljoin

from isym_test_api.rest_api.api.system.exclusive_mode_request import ExclusiveModeRequest
from isym_test_api.rest_api.api.system.exclusive_mode_response import ExclusiveModeResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class ExclusiveModeDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.exclusive_mode_url = urljoin(base_url, "api/datasystem/acquisition/exclusivemode")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def get_exclusive_mode(self) -> ExclusiveModeResponse:
        received_data = self._request.get_request(self.exclusive_mode_url, ExclusiveModeResponse).data
        self.logger.debug(f"Get exclusive mode response: {received_data}")
        return received_data

    def set_exclusive_mode(self, exclusive_mode: bool, requestor: str):
        exclusive_mode_request = ExclusiveModeRequest(exclusiveMode=exclusive_mode, requestor=requestor)
        self.logger.debug(f"Exclusive mode was set to: {exclusive_mode_request}")
        self._request.put_request(self.exclusive_mode_url, exclusive_mode_request)
