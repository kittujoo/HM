"""
File_Name:tuv_detector_home_screen.py
Desc: This file contains specific user action on the tuv detector home screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__modified__ = "Sharmila Vairamani" Renamed home locators to TUVHomeScreenLocators
__modified__ = "Sharmila Vairamani" Addedchannel A abd B specific functions - 05/15/2021


"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.TuvDetector.tuv_home_screen import TUVHomeScreenLocators as hsl
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class TUVDetectorHomeScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def tap_wavelength_setting_icon(self):
        self.tap(hsl.WAVELENGTH_CONDITIONAL_CARD)

    def get_first_wavelength(self):
        self.logger.info("Inside the get first wavelength")
        first_wavelength_value = self.get_container_text(hsl.WAVE_LENGTH_1_READ_BACK_VALUE)
        first_wavelength_unit = self.get_container_text(hsl.WAVE_LENGTH_1_READ_BACK_UNITS)
        self.logger.info(f"first_wavelength_value===>>>>>  {first_wavelength_value}")
        self.logger.info(f"first_wavelength_unit===>>>>>  {first_wavelength_unit}")
        first_wavelength = str(first_wavelength_value) + ' ' + first_wavelength_unit
        first_wavelength = first_wavelength.strip()
        return first_wavelength

    def get_second_wavelength(self):
        second_wavelength_value = self.get_container_text(hsl.WAVE_LENGTH_2_READ_BACK_VALUE)
        second_wavelength_unit = self.get_container_text(hsl.WAVE_LENGTH_2_READ_BACK_UNITS)
        second_wavelength = str(second_wavelength_value) + ' ' + second_wavelength_unit
        second_wavelength = second_wavelength.strip()
        return second_wavelength

    def validate_tuv_detector_home_screen(self):
        locator = hsl.CHANNEL_A_CONDITION_CARD
        screen_name = "home screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_channel_a_condition_card(self):
        self.tap(hsl.CHANNEL_A_CONDITION_CARD)

    def get_channel_a_absorbance_value(self):
        return self.get_condition_card_value(hsl.CHANNEL_A_ABSORBANCE_VALUE_BEFORE_DECIMAL,
                                             hsl.CHANNEL_A_ABSORBANCE_VALUE_AFTER_DECIMAL)

    def get_channel_b_absorbance_value(self):
        return self.get_condition_card_value(hsl.CHANNEL_B_ABSORBANCE_VALUE_BEFORE_DECIMAL,
                                             hsl.CHANNEL_B_ABSORBANCE_VALUE_AFTER_DECIMAL)

    def tap_channel_b_condition_card(self):
        self.tap(hsl.CHANNEL_B_CONDITION_CARD)

    def get_channel_a_status(self):
        status = self.get_container_text(hsl.CHANNEL_A_READ_BACK_STATUS)
        read_back_status = status.strip()
        return read_back_status

    def get_channel_b_status(self):
        status = self.get_container_text(hsl.CHANNEL_B_READ_BACK_STATUS)
        read_back_status = status.strip()
        return read_back_status

    def get_absorbance_units(self):
        return self.get_container_text(hsl.CHANNEL_A_ABSORBANCE_UNITS)

    def tap_tuv_schematic_icon(self):
        self.tap(TopLevelDashBoardScreenLocators.TUV_ICON)
        self._logger.debug(' The column manager read back card was tapped')
