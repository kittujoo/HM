"""
File_Name: wavelength_settings_screen.py
Desc: This file contains specific user action on the web elements in the tuv wavelength setting screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/20/2021

"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.TuvDetector.channel_common_condition_card import ChannelSettingScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class ChannelSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Channel settings screen"

    def enter_wavelength(self, number):
        self.enter_value(number)

    def is_wavelength_setting_screen_exist(self):
        return self.is_displayed(ChannelSettingScreenLocators.HEADER)

    def validate_wavelength_setting_screen(self):
        locator = ChannelSettingScreenLocators.HEADER
        wait_time = self.wait_time
        screen_name = "wavelength setting screen"
        self.validate_screen(locator, screen_name, wait_time)

    def tap_dual_mode_selector_component(self):
        self.tap(ChannelSettingScreenLocators.WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT)

    def tap_single_mode_selector_component(self):
        self.tap(ChannelSettingScreenLocators.WAVE_LENGTH_MODE_SINGLE_SELECTOR_COMPONENT)

    def get_wavelength_mode(self):
        wavelength_mode = self.get_text(ChannelSettingScreenLocators.WAVE_LENGTH_MODE_READ_BACK)
        return wavelength_mode

    def enter_first_wavelength(self, wavelength):

        self.tap_text_field(ChannelSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD)
        self.clear_num_pad_entries(ChannelSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD)
        self.enter_wavelength(wavelength)

    def enter_second_wavelength(self, wavelength):
        self.tap_text_field(ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD)
        self.clear_num_pad_entries(ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD)
        self.enter_wavelength(wavelength)

    def is_dual_mode_enabled(self):
        wave_length_mode = self.get_element(
            ChannelSettingScreenLocators.WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT)
        is_dual_mode_selected = wave_length_mode.get_attribute("class")
        if is_dual_mode_selected == "ng-star-inserted active":
            self.logger.info(f"is the dual mode enabled =>{is_dual_mode_selected}")
            return True
        else:
            return False

    def validate_dual_wave_length_mode_enabled(self):
        is_dual_wave_length_header_displayed = self.is_displayed(
            ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER)
        self.logger.info(f"THE dual header is {is_dual_wave_length_header_displayed}")
        assert is_dual_wave_length_header_displayed is True, "The dual wave length mode is not enabled"

    def validate_single_wave_length_mode_enabled(self):
        is_single_wave_length_header_displayed = self.is_displayed(
            ChannelSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER)

        assert is_single_wave_length_header_displayed is True, "The single wave length mode is not enabled"

    def validate_first_wavelength(self, actual_first_wave_length):
        time.sleep(1)  # will be removed once the scroll component wiggle issue fixed
        expected_first_wave_length = self.get_text(ChannelSettingScreenLocators.WAVE_LENGTH_1_READ_BACK_VALUE)
        expected_first_wave_length_value = expected_first_wave_length.strip()
        expected_first_wave_length_value = expected_first_wave_length_value[0:3]
        self.logger.info(f"expected_first_wave_length_value==>>>{expected_first_wave_length_value} ")
        self.logger.info(f"actual_first_wave_length==>>>{actual_first_wave_length} ")
        assert actual_first_wave_length == expected_first_wave_length_value, f"The wavelength does not match"

    def validate_second_wavelength(self, actual_second_wave_length):
        time.sleep(1)  # will be removed once the scroll component wiggle issue fixed
        expected_second_wave_length = self.get_text(ChannelSettingScreenLocators.WAVE_LENGTH_2_READ_BACK_VALUE)
        expected_first_wave_length = expected_second_wave_length.strip()
        expected_first_wave_length_value = expected_first_wave_length[0:3]
        self.logger.info(f"expected_second_wave_length_value==>>>{expected_first_wave_length_value} ")
        self.logger.info(f"actual_second_wave_length==>>>{actual_second_wave_length} ")
        assert actual_second_wave_length == expected_first_wave_length_value, f"The wavelength does not match"
