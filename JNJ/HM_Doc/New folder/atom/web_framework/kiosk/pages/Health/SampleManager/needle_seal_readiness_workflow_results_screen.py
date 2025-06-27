"""
File_Name: needle_seal_readiness_results_screen.py
Desc: This file contains specific user actions on screens within the needle seal readiness test workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/17/22
"""

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.needle_seal_readiness_constants import \
    NeedleSealReadinessConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import \
    NeedleSealReadinessResultsLocators
from web_framework.kiosk.pages.base_page import BasePage


class NeedleSealReadinessResultsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_results_screen(self):
        locator = NeedleSealReadinessResultsLocators.RESULTS_BANNER
        screen_name = "Summary Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            NeedleSealReadinessResultsLocators.STATUS_BANNER,
            NeedleSealReadinessConstants.StatusHeader, WaitTimeConstants.SmallWait)

    def get_results_info(self):
        self.wait_time_to_load_value(NeedleSealReadinessResultsLocators.RESULTS_LINE_ONE)
        return [
            self.get_text(NeedleSealReadinessResultsLocators.RESULTS_LINE_ONE),
            self.get_text(NeedleSealReadinessResultsLocators.RESULTS_LINE_TWO)]

    def validate_results_table(self):
        locator = NeedleSealReadinessResultsLocators.PRESSURE_DIFFERENCE_LABEL
        screen_name = "Summary Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_status_info(self):
        self.wait_time_to_load_value(NeedleSealReadinessResultsLocators.STATUS_LINE_ONE)
        return [
            self.get_text(NeedleSealReadinessResultsLocators.STATUS_LINE_ONE),
            self.get_text(NeedleSealReadinessResultsLocators.STATUS_LINE_TWO)]
