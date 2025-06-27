"""
file_Name: sm_configuration_screen.py
Desc: This file contains specific user actions on the elements in the system screen which includes
      sample manager module
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/11/2020
__modified__ = "Sharmila Vairamani" Added validation function - 01/26/2021

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_screen import SMConfigurationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SMConfigurationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def tap_volume_settings(self):
        self.tap(SMConfigurationScreenLocators.VOLUMES_TAB)

    def tap_light_preference_settings(self):
        self.tap(SMConfigurationScreenLocators.COMPARTMENT_LIGHT_TAB)

    def tap_options(self):
        self.tap(SMConfigurationScreenLocators.OPTIONS_TAB)

    def tap_notifications(self):
        self.tap(SMConfigurationScreenLocators.PREFERENCES_TAB)

    def validate_sm_configuration_screen(self):
        locator = SMConfigurationScreenLocators.HEADER
        screen_name = "SM configure screen"
        self.validate_screen(locator, screen_name, self.wait_time)
