from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class ControlPanel(WinAppBasePage):

    def __init__(self, driver, assert_timeout: AssertTimeout):
        super().__init__(driver)
        self._assert_timeout = assert_timeout

    def _get_text_value(self, index: int) -> str:
        """
            Due to lack of automation IDs we need to load controls based on position.
            This should be a temporary solution until the ids and supporting structure are added to the apps.
        """
        return self.get_text((By.XPATH, f"(//Document//Text)[{index}]"))

    def get_instrument_state(self) -> str:
        return self._get_text_value(1)

    def get_flow_rate_value(self) -> str:
        return self._get_text_value(2)

    def get_flow_rate_unit(self) -> str:
        return self._get_text_value(3)

    def get_instrument_type(self) -> str:
        return self._get_text_value(4)

    def get_lamp_state(self) -> str:
        return self._get_text_value(8)

    def get_sample_temperature_value(self) -> str:
        return self._get_text_value(10)

    def get_sample_temperature_unit(self) -> str:
        return self._get_text_value(11)

    def get_column_temperature_value(self) -> str:
        return self._get_text_value(13)

    def get_column_temperature_unit(self) -> str:
        return self._get_text_value(14)

    def get_system_pressure_value(self) -> str:
        return self._get_text_value(16)

    def get_system_pressure_unit(self) -> str:
        return self._get_text_value(17)

    def open_console(self):
        """
        Console ca be opened from the Control Panel's header, but only by clicking on the left or right sides of the header.
        The below approach will identify the State banner and will attempt to click somewhere on it's left side
        """
        state_element = self.find_element((By.XPATH, "//Document//Group[@LocalizedControlType='banner']"))
        ActionChains(self._driver).move_to_element_with_offset(state_element, -25, 5).click().perform()

    def validate_system_state(self, expected_state: str):
        self._assert_timeout.are_equal(lambda: self.get_instrument_state(), expected_state, "Unexpected Control Panel system state",
                                       timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)
