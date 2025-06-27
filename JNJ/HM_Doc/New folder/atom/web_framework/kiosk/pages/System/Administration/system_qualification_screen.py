"""
File_Name: system_qualification_screen.py
Desc: This file contains specific user actions within administration screen and system qualification screen
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
"""
import re

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.Administration.system_qualification_screen_locators import SystemQualificationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage

logger = Logger("test_system_qualification")


class SystemQualificationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_system_qualification_screen(self):
        locator = SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_MENU
        screen_name = "System Qualification Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_system_qualification_toggle_status(self, current_toggle_state):
        self.wait_time_to_load_value(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_MENU)
        if current_toggle_state != self.is_toggle_component_enabled(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE):
            self.set_toggle_button(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE, current_toggle_state)

    def validate_system_qualification_toggle_state(self, expected_toggle_state):
        self.wait_time_to_load_value(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_MENU)
        actual_toggle_state = self.is_toggle_component_enabled(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE)
        assert actual_toggle_state == expected_toggle_state, (f"The system qualification on system qualification screen was unexpected. "
                                                              f"Expected: {expected_toggle_state} ,Actual: {actual_toggle_state}")

    def get_selected_expiry_system_qualification(self) -> str:
        actual_month = self.get_text(SystemQualificationScreenLocators.QUALIFICATION_EXPIRES_LABEL)
        string_to_remove = re.search(r'\d+', actual_month)
        current_month_selected = string_to_remove.group()
        return current_month_selected

    def enable_system_qualification(self):
        if not self.is_toggle_component_enabled(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE):
            self.tap(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE)
        else:
            self.logger.debug("System qualification toggle is already enabled")
