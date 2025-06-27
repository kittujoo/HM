"""
File_Name: tuv_configuration_settings_screen.py
Desc: This file contains specific user action on the elements in the TUV configuration settings screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/23/2020
__modified__    = "Sharmila Vairamani" Initial Check-in 11/20/2020
_modified__ = "Sharmila Vairamani" Changed the locator name - 03/19/2021
__Modified__ = "Tyler Prada" Added a few new validate methods 8/9/21
__modified__ = "Tyler Prada" Close shutter preference toggle conversion changes 11/17/21
"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.System.TUVDetector.tuv_configuration_settings_screen import TUVConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import state_dict


class TUVConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def set_temperature_stabilization_settings(self, temperature):
        temperature_text_dictionary = {
            "normal": TUVConfigurationSettingsScreenLocators.NORMAL_TEMPERATURE_SETTINGS,
            "higher": TUVConfigurationSettingsScreenLocators.HIGHER_TEMPERATURE_SETTINGS,
            "much_higher": TUVConfigurationSettingsScreenLocators.MUCH_HIGHER_TEMPERATURE
        }
        self.tap_for_dictionary_value(temperature, temperature_text_dictionary, "Unexpected temperature")

    def is_leak_sensor_enabled(self):
        return self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON)

    def is_lamp_with_resident_id_enabled(self):
        return self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.LAMP_WITH_RESIDENT_ID_TOGGLE_BUTTON)

    def is_flow_cell_with_resident_id_enabled(self):
        return self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.FLOW_CELL_WITH_RESIDENT_ID_TOGGLE_BUTTON)

    # NOTE: This function should be removed when the isym response time does not take so long
    def wait_for_isym_toggle(self):
        time.sleep(5)

    def tap_close_shutter_preference_settings(self):
        self.tap(TUVConfigurationSettingsScreenLocators.CLOSE_SHUTTER_PREFERENCE_TAB)

    def validate_options_screen(self):
        locator = TUVConfigurationSettingsScreenLocators.OPTIONS_CONTAINER
        screen_name = "Options Screen in the TUV settings configuration"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_leak_sensor_monitor_mode(self, leak_sensor_enabled):
        leak_sensor_enabled = TypeConverter.to_bool(leak_sensor_enabled)
        self.logger.info(f"leak_sensor_enabled => {leak_sensor_enabled}")
        currently_enabled = self.is_leak_sensor_enabled()
        self.logger.info(f"currently enabled => {currently_enabled}")
        self.toggle_switch("Leak sensor monitor", TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON,
                           currently_enabled, leak_sensor_enabled)

    def tap_options_tab(self):
        self.tap(TUVConfigurationSettingsScreenLocators.OPTIONS_TAB)

    def validate_tuv_configuration_settings_screen(self):
        locator = TUVConfigurationSettingsScreenLocators.TUV_CONFIGURATION_SETTINGS_HEADER
        screen_name = "TUV configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_lamp_with_resident_id_mode(self, lamp_resident_id_enabled):
        lamp_resident_id_enabled = TypeConverter.to_bool(lamp_resident_id_enabled)
        currently_enabled = self.is_lamp_with_resident_id_enabled()
        self.toggle_switch("Lamp with resident ID", TUVConfigurationSettingsScreenLocators.LAMP_WITH_RESIDENT_ID_TOGGLE_BUTTON,
                           currently_enabled, lamp_resident_id_enabled)

    def set_flow_cell_with_resident_id_mode(self, flow_cell_resident_id_enabled):
        flow_cell_resident_id_enabled = TypeConverter.to_bool(flow_cell_resident_id_enabled)
        currently_enabled = self.is_flow_cell_with_resident_id_enabled()
        self.toggle_switch("Lamp with resident ID", TUVConfigurationSettingsScreenLocators.FLOW_CELL_WITH_RESIDENT_ID_TOGGLE_BUTTON,
                           currently_enabled, flow_cell_resident_id_enabled)

    def tap_preferences_tab(self):
        self.tap(TUVConfigurationSettingsScreenLocators.PREFERENCES_TAB)

    def validate_optics_temperature(self, expected_temperature):
        temperature_text_dictionary = {
            "Normal room temperature": TUVConfigurationSettingsScreenLocators.NORMAL_TEMPERATURE_SETTINGS,
            "High room temperature": TUVConfigurationSettingsScreenLocators.HIGHER_TEMPERATURE_SETTINGS,
            "Very high room temperature": TUVConfigurationSettingsScreenLocators.MUCH_HIGHER_TEMPERATURE
        }

        if expected_temperature in temperature_text_dictionary:
            locator = temperature_text_dictionary[expected_temperature]
            return self.is_active(locator)

        assert False, f"Unexpected optics temperature => {expected_temperature}"

    def validate_leak_sensor(self, leak_toggle):
        leak_sensor_text_dictionary = {
            "Leak sensor enabled": True,
            "Leak sensor disabled": False
        }

        if leak_toggle in leak_sensor_text_dictionary:
            toggle_status = leak_sensor_text_dictionary[leak_toggle]

            if toggle_status:
                return self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON)

            if not toggle_status:
                return not self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON)

    def get_tuv_configuration_switch_state(self):
        self.wait_time_to_load_value(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_STATE)
        value = self.is_toggle_component_enabled(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON)
        return value

    def switch_tuv_leak_sensor_toggle_to_state(self, toggle_state):
        locator = TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON
        self.wait_time_to_load_value(TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_STATE)
        current_toggle_status = self.is_toggle_component_enabled(locator)
        if current_toggle_status != toggle_state:
            self.toggle_switch("TUV configuration screen toggle", locator, current_toggle_status, toggle_state)
            self.wait_till_condition_met(locator=TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_STATE,
                                         expected_condition=state_dict[toggle_state],
                                         wait_time=self.wait_time,
                                         error_message="TUV Expected state not received")
