from typing import Optional
from urllib.parse import urljoin

from isym_test_api.rest_api.api.base_response import RestResponse
from isym_test_api.rest_api.api.column_manager.temperature_control_request import ChcThermalControlState, ThermalControlState
from isym_test_api.rest_api.api.column_manager.temperature_control_response import ColumnTemperatureControlResponse
from isym_test_api.rest_api.api.column_manager.temperature_request import ColumnTemperatureW
from isym_test_api.rest_api.api.column_manager.temperature_response import ColumnTemperatureResponse
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger


class ColumnManagerTemperatureDriver(object):

    def __init__(self, rest_api_driver: RestAPIDriver, base_url, assert_timeout: AssertTimeout):
        self.temperature_url = urljoin(base_url, "/api/separation/cm/chamber1/temperature")
        self.temperature_control_url = urljoin(base_url, "/api/separation/cm/chamber1/temperaturecontrol")
        self._request = rest_api_driver
        self._assert_timeout = assert_timeout

        self.logger = Logger(self.__class__.__name__)

    def set_temperature_control(self, state: ThermalControlState) -> Optional[RestResponse[None]]:
        if self.get_temperature_control() != state:
            set_temperature_request = ChcThermalControlState(state)
            return self._request.put_request(self.temperature_control_url, set_temperature_request)
        else:
            self.logger.debug(f"Already in the expected state {state}")
            return None

    def get_temperature_control(self) -> RestResponse[ColumnTemperatureControlResponse]:
        return self._request.get_request(self.temperature_control_url, ColumnTemperatureControlResponse)

    def cleanup(self):
        self.set_temperature_control(ThermalControlState.ThermalControlState_OFF)
        self._assert_timeout.are_equal(lambda: self.get_thermal_control_state(), ThermalControlState.ThermalControlState_OFF.name,
                                       "Column Manager temperature control is not off")

    def set_temperature(self, set_temperature_request: ColumnTemperatureW) -> RestResponse[None]:
        return self._request.put_request(self.temperature_url, set_temperature_request)

    def get_temperature(self) -> RestResponse[ColumnTemperatureResponse]:
        return self._request.get_request(self.temperature_url, ColumnTemperatureResponse)

    def get_current_temperature(self) -> float:
        return self.get_temperature().data.currentTemperatureDegC

    def get_target_temperature(self) -> float:
        return self.get_temperature().data.targetTemperatureDegC

    def get_thermal_control_state(self) -> str:
        return self.get_temperature_control().data.thermalControlState
