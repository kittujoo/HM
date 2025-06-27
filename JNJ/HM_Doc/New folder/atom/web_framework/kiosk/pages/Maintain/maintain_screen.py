"""
File_Name: maintain_screen.py
Desc: This file contains specific user action on the web elements in the maintain screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/2/2021
"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.base_page import BasePage

logger = Logger("commands_screen_page")


class MaintainScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def validate_maintain_screen(self):
        locator = MaintainScreenPageLocators.MAINTAIN_HEADER
        screen_name = "Maintain screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_panel(self, navigation_panel):
        panel_text_dictionary = {
            "replace": MaintainScreenPageLocators.REPLACE_PANEL,
            "calibrate": MaintainScreenPageLocators.CALIBRATE_PANEL,
            "service": MaintainScreenPageLocators.SERVICE_PANEL}

        if navigation_panel in panel_text_dictionary:
            locator = panel_text_dictionary[navigation_panel]
            self.tap(locator)
            return

        assert False, (f"Unexpected navigation panel => {navigation_panel}")

    def tap_calibrate_wavelength_tab(self):
        self.tap(MaintainScreenPageLocators.CALIBRATE_DETECTOR)

    def tap_replace_components(self):
        self.tap(MaintainScreenPageLocators.REPLACE_PANEL)
