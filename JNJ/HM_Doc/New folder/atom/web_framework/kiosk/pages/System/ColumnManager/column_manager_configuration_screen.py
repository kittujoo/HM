"""
file_Name: column_manager_configuration_screen.py
Desc: This file contains specific user actions on the elements in the system screen which includes
      column manager module
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/2021


"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.ColumnManager.column_manager_configuration_screen_locators import ColumnManagerConfigurationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class ColumnManagerConfigurationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_column_manager_configuration_screen(self):
        locator = ColumnManagerConfigurationScreenLocators.COLUMN_MANAGER_CONFIGURATION_MENU
        screen_name = "Column manager configuration screen"
        self.validate_screen(locator, screen_name, self.wait_time)
