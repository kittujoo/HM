"""
File_Name: wavelength_settings_screen.py
Desc: This file contains specific user action on the web elements in the tuv wavelength setting screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/05/2020
__modified__ = "Sharmila Vairamani" refactor common function- 05/07/2020
__modified__ = "Sharmila Vairamani" Added wavelength condition card user action
__modified__ = "Sharmila Vairamani" Refactor the common function - 06/11/2020
__modified__ = "sharmila Vairamani" Added validation - 06/16/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Sharmila Vairamani" Renamed the locator class name - 03/24/2021


"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.TuvDetector.wavelength_condition_card import WavelengthSettingScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class WavelengthSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def enter_wavelength(self, number):
        self.enter_value(number)

    def is_wavelength_setting_screen_exist(self):
        return self.is_displayed(WavelengthSettingScreenLocators.HEADER)

    def validate_wavelength_setting_screen(self):
        locator = WavelengthSettingScreenLocators.HEADER
        wait_time = self.wait_time
        screen_name = "wavelength setting screen"
        self.validate_screen(locator, screen_name, wait_time)

    def tap_dual_selector_component(self):
        return self.tap(WavelengthSettingScreenLocators.WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT)

    def get_first_wavelength(self):
        first_wavelength_value = self.get_text(WavelengthSettingScreenLocators.WAVE_LENGTH_1_READ_BACK_VALUE)
        first_wavelength_unit = self.get_text(WavelengthSettingScreenLocators.WAVE_LENGTH_1_READ_BACK_UNITS)
        first_wavelength = str(first_wavelength_value) + ' ' + first_wavelength_unit
        first_wavelength = first_wavelength.strip()
        return first_wavelength

    def get_second_wavelength(self):
        second_wavelength_value = self.get_text(WavelengthSettingScreenLocators.WAVE_LENGTH_2_READ_BACK_VALUE)
        second_wavelength_unit = self.get_text(WavelengthSettingScreenLocators.WAVE_LENGTH_2_READ_BACK_UNITS)
        second_wavelength = str(second_wavelength_value) + ' ' + second_wavelength_unit
        second_wavelength = second_wavelength.strip()
        return second_wavelength

    def get_wavelength_mode(self):
        wavelength_mode = self.get_text(WavelengthSettingScreenLocators.WAVE_LENGTH_MODE_READ_BACK)
        return wavelength_mode

    def enter_first_wavelength(self, wavelength):

        self.tap_text_field(WavelengthSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD)
        self.clear_num_pad_entries(WavelengthSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD)
        self.enter_wavelength(wavelength)

    def enter_second_wavelength(self, wavelength):
        self.tap_text_field(WavelengthSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD)
        self.clear_num_pad_entries(WavelengthSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD)
        self.enter_wavelength(wavelength)

    def is_dual_mode_enabled(self):
        wave_length_mode = self.get_element(
            WavelengthSettingScreenLocators.WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT)
        is_dual_mode_selected = wave_length_mode.get_attribute("class")
        if is_dual_mode_selected == "ng-star-inserted active":
            self.logger.info(f"is the dual mode enabled =>{is_dual_mode_selected}")
            return True
        else:
            return False

    def validate_dual_wave_length_mode_enabled(self):
        is_dual_wave_length_header_displayed = self.is_displayed(
            WavelengthSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER)
        self.logger.info(f"THE dual header is {is_dual_wave_length_header_displayed}")
        is_dual_wave_length_label_displayed = self.is_displayed(
            WavelengthSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD_LABEL)
        self.logger.info(f"THE SINGLE WAVELENGTH HEADER {is_dual_wave_length_label_displayed}")
        assert is_dual_wave_length_header_displayed and is_dual_wave_length_label_displayed is True, "The dual wave length mode is not enabled"

    def validate_single_wave_length_mode_enabled(self):
        is_single_wave_length_header_displayed = self.is_displayed(
            WavelengthSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER)
        is_single_wave_length_label_displayed = self.is_displayed(
            WavelengthSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD_LABEL)
        assert is_single_wave_length_label_displayed and is_single_wave_length_header_displayed is True, "The single wave length mode is not enabled"
