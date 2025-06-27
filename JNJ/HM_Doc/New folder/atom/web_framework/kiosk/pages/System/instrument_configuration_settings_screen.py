"""
File_Name: instrument_configuration_settings_screen.py
Desc: This file contains specific user actions on the elements in the instrument configuration settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/20/2021
__modified__ = "Sharmila vairamani" Added scroll_to_option 09/20/2021
__modified__ = "Tyler Prada" New validation function 10/19/23
"""

import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.instrument_configuration_settings_screen import InstrumentConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class InstrumentConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_instrument_configuration_settings_screen(self):
        locator = InstrumentConfigurationSettingsScreenLocators.INSTRUMENT_CONFIG_HEADER
        screen_name = "Instrument Configuration Settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)
        # time for selector animation
        time.sleep(2)

    def select_pressure_unit(self, pressure_unit):
        pressure_unit_text_dictionary = {
            "MPa": InstrumentConfigurationSettingsScreenLocators.MPA_PRESSURE_UNIT,
            "kPa": InstrumentConfigurationSettingsScreenLocators.KPA_PRESSURE_UNIT,
            "bar": InstrumentConfigurationSettingsScreenLocators.BAR_PRESSURE_UNIT,
            "psi": InstrumentConfigurationSettingsScreenLocators.PSI_PRESSURE_UNIT}

        locator = pressure_unit_text_dictionary[pressure_unit]
        self.tap(locator)

    def validate_pressure_unit_selection(self, pressure_unit):
        pressure_unit_text_dictionary = {
            "MPa": InstrumentConfigurationSettingsScreenLocators.MPA_PRESSURE_UNIT,
            "kPa": InstrumentConfigurationSettingsScreenLocators.KPA_PRESSURE_UNIT,
            "bar": InstrumentConfigurationSettingsScreenLocators.BAR_PRESSURE_UNIT,
            "psi": InstrumentConfigurationSettingsScreenLocators.PSI_PRESSURE_UNIT}

        locator = pressure_unit_text_dictionary[pressure_unit]
        return self.is_active(locator)

    def get_tubing_kit_option(self, option):
        tubing_kit_text_dictionary = {
            "standard": InstrumentConfigurationSettingsScreenLocators.STANDARD_TUBING_KIT,
            "high flow": InstrumentConfigurationSettingsScreenLocators.HIGH_FLOW_TUBING_KIT,
            "high ph": InstrumentConfigurationSettingsScreenLocators.HIGH_PH_TUBING_KIT}

        locator = tubing_kit_text_dictionary.get(option, None)
        return locator

    def select_tubing_kit_option(self, tubing_kit_option):
        locator = self.get_tubing_kit_option(tubing_kit_option)
        self.wait_element_to_be_clickable(locator, self.wait_time)
        self.tap(locator)
        # time for selector animation
        time.sleep(2)

    def validate_tubing_kit_option(self, selection):
        locator = self.get_tubing_kit_option(selection)
        return self.is_active(locator)

    def tap_cancel(self):
        self.wait_element_to_be_clickable(InstrumentConfigurationSettingsScreenLocators.CANCEL_BUTTON, self.wait_time)
        self.tap(InstrumentConfigurationSettingsScreenLocators.CANCEL_BUTTON)
