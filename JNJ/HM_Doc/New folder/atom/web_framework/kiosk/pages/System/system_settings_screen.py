"""
File_Name: system_settings_screen.py
Desc: This file contains specific user actions on general settings related to the system.
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 02/02/2021

"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SystemSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_settings_screen(self):
        locator = SystemSettingsScreenLocators.HEADER
        screen_name = "System Settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_configuration_tab(self):
        self.tap(SystemSettingsScreenLocators.CONFIGURATION_TAB)

    def tap_module_configuration_tab(self):
        self.tap(SystemSettingsScreenLocators.CONFIGURATION_TAB)

    def tap_leak_sensor_tab(self):
        self.tap(SystemSettingsScreenLocators.LEAK_SENSOR_TAB)

    def tap_administration_tab(self):
        self.tap(SystemSettingsScreenLocators.ADMINISTRATION_TAB)
    def tap_performance_counters_tab(self):
        self.tap(SystemSettingsScreenLocators.PERFORMANCE_COUNTERS_TAB)
