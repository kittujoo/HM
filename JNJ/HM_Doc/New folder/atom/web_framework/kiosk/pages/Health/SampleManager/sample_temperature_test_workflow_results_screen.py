"""
File_Name: sample_temperature_test_workflow_results_screen.py
Desc: This file contains specific user actions on screens within the sample temperature test workflow results screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 7/19/23
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_temperature_test_constants import SampleTemperatureTestConstants
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_temperature_test_workflow_locators import SampleTemperatureTestLocators
from web_framework.kiosk.pages.base_page import BasePage


class SampleTemperatureTestResultsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_results_screen(self):
        locator = SampleTemperatureTestLocators.RESULTS_PAGE_BANNER
        screen_name = "Results screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_results_value(self):
        # measured change needs to be +/- the amount of the target change
        # ex: If target is 2C then the measured needs to be AT LEAST 2C below or above
        # time for values to populate in the drop menu
        time.sleep(1)
        test_status = self.get_text(SampleTemperatureTestLocators.RESULTS_STATUS)
        target_change = float(self.get_text(SampleTemperatureTestLocators.TARGET_CHANGE).strip())
        measured_change = abs(float(self.get_text(SampleTemperatureTestLocators.MEASURED_CHANGE).strip()))
        assert measured_change >= target_change, f"The measured change was less than what was targeted. Target: {target_change} | Measured: {measured_change}"
        assert test_status == SampleTemperatureTestConstants.PassMessage, f"The test was displayed as failed"

    def validate_measured_change(self, temperature):
        test_status = self.get_text(SampleTemperatureTestLocators.RESULTS_STATUS)
        measured_change = float(self.get_text(SampleTemperatureTestLocators.MEASURED_CHANGE).strip())
        assert measured_change >= temperature, f"The measured change was not greater than {temperature} degrees Celsius. Actual Measured Change: \
                                                {measured_change}"
        assert test_status == SampleTemperatureTestConstants.PassMessage, "The test was displayed as failed"
