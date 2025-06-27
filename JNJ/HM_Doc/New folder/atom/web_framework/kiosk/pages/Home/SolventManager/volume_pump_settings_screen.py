"""
File_Name: volume_pumped_settings_screen.py
Desc: This file contains specific user action on the elements in the volume pumped settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/07/2022

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.SolventManager.volume_pumped_condition_card_locators import VolumePumpSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class PumpVolumeSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def validate_volume_settings_screen(self):
        locator = VolumePumpSettingsScreenLocators.FLOW_TOGGLE_BUTTON
        screen_name = "System pressure settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)
