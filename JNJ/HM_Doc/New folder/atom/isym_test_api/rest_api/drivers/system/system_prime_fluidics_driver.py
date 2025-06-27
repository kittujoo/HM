from urllib.parse import urljoin

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus
from isym_test_api.rest_api.api.behavior.prime_fluidics.system_prime_fluidics_request import SystemPrimeFluidicsRequest
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class PrimeFluidicsDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.prime_fluidics_url = urljoin(base_url, "api/system/behavior/setup/primefluidics")
        self.prime_fluidics_status_url = urljoin(base_url, "api/system/behavior/setup/primefluidics/status")
        self._request = rest_api_driver
        self.logger = Logger(self.__class__.__name__)

    def prime_fluidics_test_setup(self, payload: SystemPrimeFluidicsRequest):
        self.logger.debug(f"Setup Prime Fluidics payload: \n{payload}")
        self._request.put_request(self.prime_fluidics_url, payload)

    def get_prime_fluidics_test_status(self) -> BehaviorStatus:
        received_data = self._request.get_request(self.prime_fluidics_status_url, BehaviorStatus).data
        self.logger.debug(f"Get prime fluidics status response: \n{received_data}")
        return received_data
