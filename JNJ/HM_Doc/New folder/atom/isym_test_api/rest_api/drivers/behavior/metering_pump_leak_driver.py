from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_request import SystemMeteringPumpLeakTest
from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_result_response import MeteringPumpLeakResultResponse
from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_status_response import MeteringPumpLeakStatusResponse
from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_store_response import MeteringPumpLeakStoreResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.logger import Logger


class MeteringPumpLeakDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url):
        self.metering_pump_leak_url = urljoin(base_url, "/api/system/behavior/routine/meteringpumpleak")
        self.metering_pump_leak_result_url = urljoin(base_url, "/api/system/behavior/routine/meteringpumpleak/result")
        self.metering_pump_leak_status_url = urljoin(base_url, "/api/system/behavior/routine/meteringpumpleak/status")
        self.metering_pump_leak_store_url = urljoin(base_url, "/api/system/behavior/routine/meteringpumpleak/store")
        self._request = rest_api_driver

        self.logger = Logger(self.__class__.__name__)

    def start_test(self, payload: SystemMeteringPumpLeakTest) -> RestResponse[SystemMeteringPumpLeakTest]:
        return self._request.put_request(self.metering_pump_leak_url, payload, SystemMeteringPumpLeakTest)

    def get_result(self) -> RestResponse[MeteringPumpLeakResultResponse]:
        return self._request.get_request(self.metering_pump_leak_result_url, MeteringPumpLeakResultResponse)

    def get_status(self) -> RestResponse[MeteringPumpLeakStatusResponse]:
        return self._request.get_request(self.metering_pump_leak_status_url, MeteringPumpLeakStatusResponse)

    def get_store(self) -> RestResponse[MeteringPumpLeakStoreResponse]:
        return self._request.get_request(self.metering_pump_leak_store_url, MeteringPumpLeakStoreResponse)
