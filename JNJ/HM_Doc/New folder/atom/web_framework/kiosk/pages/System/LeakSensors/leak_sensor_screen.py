"""
File_Name: leak_sensor_screen.py
Desc: This file contains specific user actions within leak sensor screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.system_leak_sensor_screen_locators import LeakSensorScreenLocators
from web_framework.kiosk.pages.base_page import BasePage

logger = Logger("test_leak_sensor_screen")

state_dict = {True: "No Leak", False: "Disabled"}


class LeakSensorScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_leak_sensor_configuration_screen(self):
        locator = LeakSensorScreenLocators.LEAK_SENSOR_CONFIGURATION_MENU
        screen_name = "Leak Sensor Screen"
        self.validate_screen(locator, screen_name, self.wait_time)
        self.wait_time_to_load_value(LeakSensorScreenLocators.QSM_LEAK_STATUS)

    def get_leak_sensor_switch_state(self):
        locator = LeakSensorScreenLocators.QSM_LEAK_SENSOR
        return self.is_toggle_component_enabled(locator)

    def switch_pump_leak_sensor_toggle(self, toggle_state):
        locator = LeakSensorScreenLocators.QSM_LEAK_SENSOR

        current_toggle_status = self.is_toggle_component_enabled(locator)
        self.wait_till_condition_met(locator=LeakSensorScreenLocators.QSM_LEAK_STATUS, expected_condition=state_dict[current_toggle_status],
                                     wait_time=self.wait_time,
                                     error_message="Expected state not received")
        self.toggle_switch("Solvent configuration screen toggle", locator, current_toggle_status, toggle_state)
        self.wait_till_condition_met(locator=LeakSensorScreenLocators.QSM_LEAK_STATUS, expected_condition=state_dict[toggle_state], wait_time=self.wait_time,
                                     error_message="Expected state not received")

    def switch_leak_sensor_toggle(self, toggle_state, sensor_name_locator, status_locator):
        current_toggle_status = self.is_toggle_component_enabled(sensor_name_locator)
        self.wait_till_condition_met(locator=status_locator, expected_condition=state_dict[current_toggle_status],
                                     wait_time=self.wait_time,
                                     error_message="Expected state not received")
        if current_toggle_status != toggle_state:
            self.toggle_switch("Leak Sensor toggle", sensor_name_locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=status_locator, expected_condition=state_dict[toggle_state], wait_time=self.wait_time,
                                         error_message="Expected state not received")

    def validate_leak_sensor_status(self, status_locator, expected_text):
        actual_text = self.get_text(status_locator)
        assert self.get_text(status_locator) == state_dict[
            expected_text], f"The leak sensor toggle is not as expected. Actual: {actual_text}, Expected: {expected_text}"

    def switch_sm_leak_sensor_toggle(self, toggle_state):
        locator = LeakSensorScreenLocators.SM_LEAK_SENSOR

        current_toggle_status = self.is_toggle_component_enabled(locator)
        self.wait_till_condition_met(locator=LeakSensorScreenLocators.SM_LEAK_STATUS, expected_condition=state_dict[current_toggle_status],
                                     wait_time=self.wait_time,
                                     error_message="Expected condition not met for SM leak sensor toggle status")
        self.toggle_switch("SM configuration screen toggle", locator, current_toggle_status, toggle_state)
        self.wait_till_condition_met(locator=LeakSensorScreenLocators.SM_LEAK_STATUS, expected_condition=state_dict[toggle_state], wait_time=self.wait_time,
                                     error_message="Expected condition not met for SM leak sensor toggle status")

    def switch_tuv_leak_sensor_toggle(self, toggle_state):
        locator = LeakSensorScreenLocators.TUV_LEAK_SENSOR
        current_toggle_status = self.get_leak_sensor_toggle_state(locator)
        if current_toggle_status != toggle_state:
            self.toggle_switch("TUV configuration screen toggle", locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=LeakSensorScreenLocators.TUV_LEAK_STATUS, expected_condition=state_dict[toggle_state],
                                         wait_time=self.wait_time,
                                         error_message="TUV Expected state not received")

    def get_leak_sensor_toggle_state(self, locator):
        self.wait_time_to_load_value(LeakSensorScreenLocators.TUV_LEAK_STATUS)
        value = self.is_toggle_component_enabled(locator)
        return value

    def switch_chc_leak_sensor_toggle(self, toggle_state):
        locator = LeakSensorScreenLocators.CHC_LEAK_SENSOR_TOGGLE
        self.wait_time_to_load_value(LeakSensorScreenLocators.CHC_LEAK_SENSOR_STATUS)
        current_toggle_status = self.is_toggle_component_enabled(locator)
        if current_toggle_status != toggle_state:
            self.toggle_switch("CHC configuration screen toggle", locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=LeakSensorScreenLocators.CHC_LEAK_SENSOR_STATUS, expected_condition=state_dict[toggle_state],
                                         wait_time=self.wait_time,
                                         error_message="CHC Expected state not received")

    def get_chc_sensor_toggle_state(self, locator) -> bool:
        self.wait_time_to_load_value(LeakSensorScreenLocators.CHC_LEAK_SENSOR_STATUS)
        value = self.is_toggle_component_enabled(locator)
        return value
