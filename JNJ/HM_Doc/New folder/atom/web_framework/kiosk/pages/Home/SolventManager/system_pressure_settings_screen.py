"""
File_Name: system_pressure_settings_screen.py
Desc: This file contains specific user action on the elements in the system pressure settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/29/2021
__modified__"Tyler Prada" Removed select and is_active methods | moved to a base class - 04/5/2021
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Common.pressure_settings_screen_base import PressureSettingsScreenBase
from web_framework.kiosk.pages.Locators.Home.SolventManager.system_pressure_condition_card import SystemPressureSettingsScreenLocators


class SystemPressureSettingsScreen(PressureSettingsScreenBase):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.locators_class = SystemPressureSettingsScreenLocators
        self.wait_time = 5

    def validate_system_pressure_settings_screen(self):
        locator = SystemPressureSettingsScreenLocators.PRESSURE_SETTINGS_OPTION_LIST
        screen_name = "System pressure settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)
