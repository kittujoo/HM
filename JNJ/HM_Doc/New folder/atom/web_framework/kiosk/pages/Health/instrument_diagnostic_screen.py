"""
File_Name: instrument_screen.py
Desc: This file contains specific user action on the instrument diagnostic screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/2021
__modified__ = "Tyler Prada" Adjustments for leak test moving to health screen 2/21/22
"""
from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.instrument_diagnostic_locators import InstrumentDiagnosticLocators
from web_framework.kiosk.pages.base_page import BasePage


@dataclass
class IssueListItem:
    issue_type: str
    border_color: Color
    title: str
    subtitle: str


class InstrumentDiagnosticScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Health home screen"

    def validate_instrument_diagnostic_screen(self):
        locator = InstrumentDiagnosticLocators.HEADER
        screen_name = "Instrument Diagnostic screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_pump_module(self):
        self.tap(InstrumentDiagnosticLocators.SOLVENT_MANAGER_ICON)

    def get_first_active_error_element(self):
        element = self.find_element(InstrumentDiagnosticLocators.FIRST_ACTIVE_ERROR_ISSUE)
        return element

    # TODO split to header and title
    def get_first_active_error_text(self):
        text = self.get_text(InstrumentDiagnosticLocators.FIRST_ACTIVE_ERROR_ISSUE)
        return text

    def get_issue_title_by_index(self, index: int) -> str:
        title = self.get_text((By.XPATH,
                               f"//ics-info-list-item[@ng-reflect-inline='true'][{index}]//div[contains(@class, 'info-list-item-title')]"))
        return title

    def get_issue_subtitle_by_index(self, index: int) -> str:
        subtitle = self.get_text((By.XPATH,
                                  f"//ics-info-list-item[@ng-reflect-inline='true'][{index}]//div[contains(@class, 'info-list-item-subtitle')]"))
        return subtitle

    def get_issue_type_by_index(self, index: int) -> str:
        element = self.find_element((By.XPATH,
                                     f"//ics-info-list-item[@ng-reflect-inline='true'][{index}]//div[contains(@class, 'info-list-item-indicator')]"))
        issue_type = element.get_attribute("ng-reflect-ng-class")
        return issue_type

    def get_issue_border_color_by_index(self, index: int) -> Color:
        color_str = self.find_element((By.XPATH,
                                       f"//ics-info-list-item[@ng-reflect-inline='true'][{index}]//div[contains(@class, 'info-list-item-indicator')]")).value_of_css_property(
            "border-left-color")

        return Color.from_string(color_str)

    def get_issue_items(self, limit: int = 3):
        elements_count = len(self.find_elements(InstrumentDiagnosticLocators.ISSUE_ITEMS))
        issues = []
        for index in range(1, min(limit, elements_count + 1)):
            issue_type = self.get_issue_type_by_index(index)
            border_color = self.get_issue_border_color_by_index(index)
            title = self.get_issue_title_by_index(index)
            subtitle = self.get_issue_subtitle_by_index(index)
            issues.append(
                IssueListItem(issue_type=issue_type, border_color=border_color, title=title, subtitle=subtitle))
        return issues
