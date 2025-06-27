"""
File_Name: sample_pressure_settings_screen.py
Desc: This file contains specific user action on the elements in the sample pressure settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/5/2021
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Common.pressure_settings_screen_base import PressureSettingsScreenBase
from web_framework.kiosk.pages.Locators.Home.SampleManager.sample_pressure_condition_card import SamplePressureSettingsScreenLocators


class SamplePressureSettingsScreen(PressureSettingsScreenBase):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = SamplePressureSettingsScreenLocators
        self.wait_time = 5

    def validate_sample_pressure_settings_screen(self):
        locator = SamplePressureSettingsScreenLocators.SAMPLE_PRESSURE_SETTINGS_OPTION_LIST
        screen_name = "System pressure settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)
