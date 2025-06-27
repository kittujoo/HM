"""
file_Name: column_manager_configuration_settings_screen.py
Desc:This file contains specific user action on the elements in the column manager configuration settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/2021

"""

import time
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.System.ColumnManager.column_manager_configuration_settings_screen_locators import (
    ColumnManagerConfigurationSettingsScreenLocators)
from web_framework.kiosk.pages.base_page import BasePage
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import state_dict


class ColumnManagerConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_column_manager_configuration_settings_screen(self):
        locator = ColumnManagerConfigurationSettingsScreenLocators.COLUMN_MANAGER_SETTINGS_HEADER
        screen_name = "Column manager configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_chc_configuration_switch_state(self) -> bool:
        self.wait_time_to_load_value(ColumnManagerConfigurationSettingsScreenLocators.LEAK_DETECTION_STATE)
        value = self.is_toggle_component_enabled(ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE)
        return value

    def switch_chc_leak_sensor_toggle_to_state(self, toggle_state):
        locator = ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE
        self.wait_time_to_load_value(ColumnManagerConfigurationSettingsScreenLocators.LEAK_DETECTION_STATE)
        current_toggle_status = self.is_toggle_component_enabled(locator)
        if current_toggle_status != toggle_state:
            self.toggle_switch("CHC configuration screen toggle", locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=ColumnManagerConfigurationSettingsScreenLocators.LEAK_DETECTION_STATE,
                                         expected_condition=state_dict[toggle_state],
                                         wait_time=self.wait_time,
                                         error_message="CHC Expected state not received")
            
    def set_leak_sensor_toggle_status(self, desired_toggle_state):
        # Time for toggle initialization from ISYM
        time.sleep(3)
        if desired_toggle_state:
            if not self.is_toggle_component_enabled(
                    ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE):
                self.set_toggle_button(ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE,
                                                                               desired_toggle_state)
        if not desired_toggle_state:
            if self.is_toggle_component_enabled(ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE):
                self.set_toggle_button(ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE,
                                                                               desired_toggle_state)

    def validate_leak_sensor_toggle_status(self, expected_toggle_status):
        # Time for toggle initialization from ISYM
        time.sleep(3)
        assert self.is_toggle_component_enabled(
            ColumnManagerConfigurationSettingsScreenLocators.LEAK_SENSOR_ALARM_TOGGLE) == expected_toggle_status
