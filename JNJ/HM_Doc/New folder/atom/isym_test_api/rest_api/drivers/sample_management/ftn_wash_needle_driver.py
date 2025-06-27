from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.sample_management.wash_needle_request import FTNWashNeedleRequest
from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus
from isym_test_api.rest_api.api.sample_management.wash_needle_store import FTNWashNeedleStore
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class FtnWashNeedleDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.wash_needle_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/behavior/washneedle")
        self.wash_needle_status_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/behavior/washneedle/status")
        self.needle_wash_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/behavior/needlewash")
        self.needle_wash_status_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/behavior/needlewash/status")
        self.wash_needle_store_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/behavior/washneedle/store")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def send_wash_needle_request(self, payload: FTNWashNeedleRequest) -> RestResponse[None]:
        return self._request.put_request(self.wash_needle_url, payload)

    def send_needle_wash_request(self, payload: FTNWashNeedleRequest) -> RestResponse[None]:
        return self._request.put_request(self.needle_wash_url, payload)

    def get_wash_needle_status(self) -> RestResponse[BehaviorStatus]:
        return self._request.get_request(self.wash_needle_status_url, BehaviorStatus)

    def get_needle_wash_status(self) -> RestResponse[BehaviorStatus]:
        return self._request.get_request(self.needle_wash_status_url, BehaviorStatus)

    def get_wash_needle_store(self) -> RestResponse[FTNWashNeedleStore]:
        return self._request.get_request(self.wash_needle_store_url, FTNWashNeedleStore)
