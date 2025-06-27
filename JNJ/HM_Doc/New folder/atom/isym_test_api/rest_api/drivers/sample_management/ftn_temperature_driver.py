from typing import Optional
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.sample_management.temperature_control_request import FtnThermalControlState, ThermalControlState
from isym_test_api.rest_api.api.sample_management.temperature_control_response import FTNTemperatureControlResponse
from isym_test_api.rest_api.api.sample_management.temperature_request import FtnSampleTemperatureW
from isym_test_api.rest_api.api.sample_management.temperature_response import FTNTemperatureResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger


class FTNTemperatureDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url, assert_timeout: AssertTimeout):
        self.temperature_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/temperature")
        self.temperature_control_url = urljoin(base_url, "/api/samplemanagement/sm-ftn/temperaturecontrol")
        self._request = rest_api_driver
        self._assert_timeout = assert_timeout

        self.logger = Logger(self.__class__.__name__)

    def set_temperature_control(self, state: ThermalControlState) -> Optional[RestResponse[None]]:
        if self.get_temperature_control() != state:
            set_temperature_request = FtnThermalControlState(state)
            return self._request.put_request(self.temperature_control_url, set_temperature_request)
        else:
            self.logger.debug(f"Already in the expected state {state}")
            return None

    def get_temperature_control(self) -> RestResponse[FTNTemperatureControlResponse]:
        return self._request.get_request(self.temperature_control_url, FTNTemperatureControlResponse)

    def cleanup(self):
        self.set_temperature_control(ThermalControlState.ThermalControlState_OFF)
        self._assert_timeout.are_equal(lambda: self.get_thermal_control_state(), ThermalControlState.ThermalControlState_OFF.name,
                                       "Sample Manager temperature control is not off")

    def set_temperature(self, set_temperature_request: FtnSampleTemperatureW) -> RestResponse[None]:
        return self._request.put_request(self.temperature_url, set_temperature_request)

    def get_temperature(self) -> RestResponse[FTNTemperatureResponse]:
        return self._request.get_request(self.temperature_url, FTNTemperatureResponse)

    def get_current_temperature(self) -> float:
        return self.get_temperature().data.currentTemperatureDegC

    def get_target_temperature(self) -> float:
        return self.get_temperature().data.targetTemperatureDegC

    def get_thermal_control_state(self) -> str:
        return self.get_temperature_control().data.thermalControlState
