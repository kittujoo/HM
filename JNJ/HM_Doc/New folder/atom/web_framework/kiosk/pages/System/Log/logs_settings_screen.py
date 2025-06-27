"""
File_Name: system_logs_screen.py
Desc: This file contains specific user actions within system logs screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22
__modified__ = "Sharmila Vairmani" Added test definition - 03/11/2023

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class LogSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_system_logs_screen(self):
        locator = SystemLogsScreenLocators.HEADER
        screen_name = "System logs screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def select_content_filter(self, simple_filter_option):
        simple_filter_text_dictionary = {
            "Errors": SystemLogsScreenLocators.ERROR_OPTION,
            "Warnings": SystemLogsScreenLocators.WARNINGS_OPTION,
            "All": SystemLogsScreenLocators.ALL_OPTION,
            "Information": SystemLogsScreenLocators.INFORMATION_OPTION,
        }

        if simple_filter_option in simple_filter_text_dictionary:
            locator = simple_filter_text_dictionary[simple_filter_option]
            self.scroll_to_view(locator)
            return

        assert False, f"Unexpected content filter option => {simple_filter_option}"

    def select_date_range_filter(self, simple_filter_option):
        simple_filter_text_dictionary = {

            "1 Month": SystemLogsScreenLocators.MONTH_FILTER_BUTTON,
            "1 Week": SystemLogsScreenLocators.WEEK_FILTER_BUTTON,
            "All": SystemLogsScreenLocators.ALL_FILTER_BUTTON}

        if simple_filter_option in simple_filter_text_dictionary:
            locator = simple_filter_text_dictionary[simple_filter_option]
            self.scroll_to_view(locator)
            return

        assert False, f"Unexpected data range filter option => {simple_filter_option}"

    def validate_add_log_entry_screen(self):
        locator = SystemLogsScreenLocators.ADD_ENTRY_HEADER
        screen_name = "Add log entry screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def add_new_log_entry(self, log_note):
        self.clear_text_area(SystemLogsScreenLocators.ADD_ENTRY_TEXT_AREA)
        self.enter_string(log_note)
