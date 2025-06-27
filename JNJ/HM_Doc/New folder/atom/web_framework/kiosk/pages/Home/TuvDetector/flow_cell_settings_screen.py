"""
File_Name: flow_cell_configuration_screen.py
Desc: This file contains specific user action on the web elements in the flow cell screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22
"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.TuvDetector.flow_cell_condition_card_locators import FlowCellConditionCardLocators
from web_framework.kiosk.pages.base_page import BasePage


class FlowCellSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def validate_flow_cell_settings_screen(self):
        locator = FlowCellConditionCardLocators.HEADER
        wait_time = self.wait_time
        screen_name = "UV lamp configuration screen"
        self.validate_screen(locator, screen_name, wait_time)
