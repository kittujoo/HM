"""
File_Name: logs_screen.py
Desc: This file contains specific user actions within system logs screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22

"""
from typing import List, Dict

from utilities.logger import Logger
from web_framework.kiosk.common.Utilities.table import get_table_data
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class LogsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_system_logs_screen(self):
        locator = SystemLogsScreenLocators.HEADER
        screen_name = "System logs screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_table_entries(self) -> List[Dict[str, str]]:
        table = get_table_data(self.get_driver(), table_locator=SystemLogsScreenLocators.LOG_TABLE)
        assert table, "Table data was empty"
        return table

    def tap_row_element(self, sub_text):
        locator = SystemLogsScreenLocators.LOG_TABLE_ROW
        self.wait_for_element_load(locator, self.wait_time)
        no_of_elements = self.find_elements(locator)
        for element in no_of_elements:
            text_web_ele = element.find_elements_by_tag_name('li')
            for ele in text_web_ele:
                if ele.text == sub_text:
                    element.click()
                    return