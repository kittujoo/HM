import os.path
from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus
from isym_test_api.rest_api.api.behavior.needle_seal_readiness.needle_seal_readiness_request import NeedleSealReadinessRequest
from isym_test_api.rest_api.api.behavior.needle_seal_readiness.needle_seal_readiness_results_response import NeedleSealReadinessResultResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver


class NeedleSealReadinessDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.needle_seal_readiness_url = urljoin(base_url, "/api/system/behavior/routine/needlesealreadiness")
        self.needle_seal_readiness_result_url = urljoin(base_url, "/api/system/behavior/routine/needlesealreadiness/result")
        self.needle_seal_readiness_status_url = urljoin(base_url, "/api/system/behavior/routine/needlesealreadiness/status")
        self._request = rest_api_driver

    def start_test(self, payload) -> NeedleSealReadinessRequest:
        return self._request.put_request(self.needle_seal_readiness_url, payload)

    def get_result(self) -> NeedleSealReadinessResultResponse:
        received_data = self._request.get_request(self.needle_seal_readiness_result_url, NeedleSealReadinessResultResponse).data
        return received_data

    def get_status(self) -> BehaviorStatus:
        received_data = self._request.get_request(self.needle_seal_readiness_status_url, BehaviorStatus).data
        return received_data
