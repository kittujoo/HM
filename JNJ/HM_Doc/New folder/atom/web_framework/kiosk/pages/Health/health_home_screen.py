"""
File_Name: health_home_screen.py
Desc: This file contains specific user action on the health screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/2021
__modified__ = "Tyler Prada" Adjustments for leak test moving to health screen 2/21/22
"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class HealthHomeScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Health home screen"

    def validate_health_screen(self):
        locator = HealthScreenLocators.HEALTH_TITLE
        screen_name = "health screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_leak_test_panel(self):
        self.tap(HealthScreenLocators.LEAK_TEST_PANEL)

    def tap_trouble_shoot_panel(self):
        self.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)

    def tap_issue_resolution_panel(self):
        self.tap(HealthScreenLocators.ISSUE_RESOLUTION_PANEL)
