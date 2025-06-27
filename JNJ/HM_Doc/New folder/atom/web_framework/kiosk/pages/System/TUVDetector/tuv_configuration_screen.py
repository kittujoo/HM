"""
File_Name: tuv_configuration_screen.py
Desc: This file contains specific user actions on the elements in the TUV configuration screen page
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/23/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 02/04/2021
_modified__ = "Sharmila Vairamani" Changed the locator name - 03/19/2021
__modified__ = "Tyler Prada" changed locators within methods 8/9/21

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_screen import (
    SMConfigurationScreenLocators,
)
from web_framework.kiosk.pages.Locators.System.TUVDetector.tuv_configuration_screen import (
    TUVConfigurationScreenLocators,
)
from web_framework.kiosk.pages.System.Models.tuv_configuration_settings import (
    TUVConfigurationSettings,
)
from web_framework.kiosk.pages.base_page import BasePage


class TUVConfigurationScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.previous_tuv_configuration_settings = None

    def tap_preferences_tab(self):
        self.tap(TUVConfigurationScreenLocators.PREFERENCES_TAB)

    def get_optics_temperature_settings_read_back_value(self):
        current_temperature = self.get_text(
            TUVConfigurationScreenLocators.TEMPERATURE_SETTINGS_READ_BACK
        )
        return current_temperature

    def get_operation_settings_read_back_value(self):
        current_operation = self.get_text(
            TUVConfigurationScreenLocators.OPERATION_SETTINGS_READ_BACK
        )
        return current_operation

    def tap_close_shutter_preference_settings(self):
        self.tap(TUVConfigurationScreenLocators.CLOSE_SHUTTER_PREFERENCE_TAB)

    def tap_options_tab(self):
        self.tap(TUVConfigurationScreenLocators.OPTIONS_TAB)

    def get_shutter_preference_settings_read_back_value(self):
        current_shutter_settings = self.get_text(
            TUVConfigurationScreenLocators.SHUTTER_PREFERENCE_SETTINGS_READ_BACK
        )
        return current_shutter_settings

    def get_options_settings_read_back_value(self):
        current_options = self.get_text(
            TUVConfigurationScreenLocators.OPTIONS_SETTINGS_READ_BACK
        )
        return current_options

    def is_tuv_icon_selected(self):
        return self.is_enabled(TUVConfigurationScreenLocators.TUV_ICON)

    def validate_tuv_settings_screen(self):
        locator = TUVConfigurationScreenLocators.TUV_HEADER
        screen_name = "TUV settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_tuv_configuration_settings_value(self):
        current_leak_sensor_options = self.get_text(
            TUVConfigurationScreenLocators.OPTIONS_SETTINGS_READ_BACK
        )
        current_close_shutter_preference = self.get_text(
            TUVConfigurationScreenLocators.SHUTTER_PREFERENCE_SETTINGS_READ_BACK
        )
        tuv_configuration_settings = TUVConfigurationSettings(
            current_close_shutter_preference,
            current_leak_sensor_options
        )
        return tuv_configuration_settings

    def set_previous_tuv_configuration_settings(self, tuv_configuration_settings):
        self.previous_tuv_configuration_settings = tuv_configuration_settings

    def get_previous_tuv_configuration_settings(self):
        return self.previous_tuv_configuration_settings

    def validate_settings_screen(self):
        locator = TUVConfigurationScreenLocators.HEADER
        screen_name = "SystemSettings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_sm_icon(self):
        self.tap(SMConfigurationScreenLocators.SAMPLE_MANAGER_ICON)
