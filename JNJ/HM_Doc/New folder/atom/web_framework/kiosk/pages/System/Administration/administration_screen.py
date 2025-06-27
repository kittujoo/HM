"""
File_Name: administration_screen.py
Desc: This file contains specific user actions within administration screen and system qualification screen
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
"""

from web_framework.kiosk.pages.Locators.System.Administration.administration_configuration_screen_locators import AdministrationConfigurationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class AdministrationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

    def validate_administration_configuration_screen(self):
        locator = AdministrationConfigurationScreenLocators.ADMINISTRATION_CONFIGURATION_MENU
        screen_name = "Administration Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_acquisition_checks_tab(self):
        self.tap(AdministrationConfigurationScreenLocators.ACQUISITION_CHECKS_TAB)

    def validate_acquisition_checks_screen(self):
        locator = AdministrationConfigurationScreenLocators.ACQUISITION_CHECKS_TAB
        screen_name = "Acquisition Checks Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_run_time_checks_tab(self):
        self.tap(AdministrationConfigurationScreenLocators.RUN_TIME_CHECKS_TAB)

    def tap_pre_run_checks_tab(self):
        self.tap(AdministrationConfigurationScreenLocators.PRE_RUN_CHECKS_TAB)
