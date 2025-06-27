import os.path
from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.system_noise_and_drift.system_noise_and_drift_request import SystemTuvNoiseAndDriftRequest
from isym_test_api.rest_api.api.behavior.system_noise_and_drift.system_noise_and_drift_result_response import SystemNoiseAndDriftResultResponse
from isym_test_api.rest_api.api.behavior.system_noise_and_drift.system_noise_and_drift_status_response import SystemNoiseAndDriftStatusResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class SystemNoiseAndDriftDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.system_noise_and_drift_url = urljoin(base_url, "/api/system/behavior/routine/noisedrift")
        self.system_noise_and_drift_result_url = urljoin(base_url, "/api/system/behavior/routine/noisedrift/result")
        self.system_noise_and_drift_status_url = urljoin(base_url, "/api/system/behavior/routine/noisedrift/status")
        self._request = rest_api_driver

        self.logger = Logger(self.__class__.__name__)

    def start_test(self, payload: SystemTuvNoiseAndDriftRequest):
        self.logger.debug(f"Put Request Method dataset: \n{payload}")
        return self._request.put_request(self.system_noise_and_drift_url, payload)

    def get_result(self) -> SystemNoiseAndDriftResultResponse:
        received_data = self._request.get_request(self.system_noise_and_drift_result_url, SystemNoiseAndDriftResultResponse).data
        self.logger.debug(f"Get Results: \n{received_data}")
        return received_data

    def get_status(self) -> SystemNoiseAndDriftStatusResponse:
        received_data = self._request.get_request(self.system_noise_and_drift_status_url, SystemNoiseAndDriftStatusResponse).data
        self.logger.debug(f"Get Status: \n{received_data}")
        return received_data
