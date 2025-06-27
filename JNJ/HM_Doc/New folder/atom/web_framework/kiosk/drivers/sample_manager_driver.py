"""
    Filename: sample_manager_driver.py
    Driver to control Sample Manager screen actions
"""
from utilities.logger import Logger

from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_pressure_settings_screen import SamplePressureSettingsScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_temperature_settings_screen import SampleTemperatureSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.sample_temperature_condition_card import (
    SampleTemperatureSettingScreenLocators)
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators


class SampleManagerDriver(object):
    """
    Class to control Sample Manager screen actions
    """

    def __init__(self, page_builder):
        self.sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen = page_builder(SampleTemperatureSettingsScreen)
        self.sample_manager_home_screen_page: SampleManagerHomeScreen = page_builder(SampleManagerHomeScreen)
        self.sample_pressure_setting_screen_page: SamplePressureSettingsScreen = page_builder(SamplePressureSettingsScreen)
        self.logger = Logger(self.__class__.__name__)

    def set_temperature(self, temperature):
        """
        Driver to set sample temperature.
        :param temperature: Sample temperature value
        """
        self.sample_manager_home_screen_page.tap_sample_temperature_condition_card()
        is_toggle_button_enabled = self.sample_temperature_settings_screen_page.is_toggle_button_enabled()
        if not is_toggle_button_enabled:
            self.sample_temperature_settings_screen_page.tap_toggle_button()
        self.sample_temperature_settings_screen_page.set_spinner_value(
            SampleTemperatureSettingScreenLocators.SAMPLE_TEMPERATURE_LIST, str(temperature))
        self.sample_temperature_settings_screen_page.tap_done_button()

    def set_unit(self, unit):
        """
        Driver to set sample pressure unit.
        :param unit: Sample pressure unit value
        """
        self.sample_manager_home_screen_page.tap_sample_pressure_condition_card()
        self.sample_pressure_setting_screen_page.validate_sample_pressure_settings_screen()
        self.sample_pressure_setting_screen_page.select_unit_option(unit)
        self.sample_pressure_setting_screen_page.tap_done_button()

    def check_unit(self):
        """
        Driver to check sample pressure unit.
        :return: Sample pressure unit value
        """
        self.sample_manager_home_screen_page.wait_for_element_load(
            SampleManagerHomeScreenLocators.SAMPLE_PRESSURE_UNIT,
            WaitTimeConstants.SmallWait)
        return self.sample_manager_home_screen_page.get_text(SampleManagerHomeScreenLocators.SAMPLE_PRESSURE_UNIT)
