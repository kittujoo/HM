"""
File_Name: sample_temperature_test_workflow.py
Desc: This file contains specific user actions on screens within the sample temperature test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/22
__modified__ = "Tyler Prada" Post-FCS update 7/19/23
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_temperature_test_constants import SampleTemperatureTestConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_temperature_test_workflow_locators import SampleTemperatureTestLocators
from web_framework.kiosk.pages.base_page import BasePage


class SampleTemperatureTestSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_welcome_screen(self):
        locator = SampleTemperatureTestLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the sample temperature test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_screen(self):
        locator = SampleTemperatureTestLocators.PRECONDITIONS_PAGE_BANNER
        screen_name = "Preconditions screen for the sample temperature test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_summary_screen(self):
        locator = SampleTemperatureTestLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary screen for the sample temperature test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_text(self):
        return [
            self.get_text(SampleTemperatureTestLocators.WELCOME_PARA_ONE),
            self.get_text(SampleTemperatureTestLocators.WELCOME_PARA_TWO),
            self.get_text(SampleTemperatureTestLocators.WELCOME_PARA_THREE)
        ]

    def validate_preconditions(self):
        assert self.is_condition_met(SampleTemperatureTestLocators.AMBIENT_TEMPERATURE_STATE), f"The ambient temperature state is in a failure condition"
        assert self.is_condition_met(
            SampleTemperatureTestLocators.COMPARTMENT_TEMPERATURE_STATE), f"The compartment temperature state is in a failure condition"
        assert self.is_condition_met(SampleTemperatureTestLocators.COMPARTMENT_DOOR_STATE), f"The compartment door state is in a failure condition"
        assert self.is_condition_met(SampleTemperatureTestLocators.SAMPLE_TRAY_STATE), f"The sample tray state is in a failure condition"

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            SampleTemperatureTestLocators.STATUS_BANNER,
            SampleTemperatureTestConstants.StatusValidateText, WaitTimeConstants.SmallWait)

    def wait_for_test_end(self, starting_element, target_element, timeout=WaitTimeConstants.SampleTemperatureTest):
        self.wait_for_element_visibility(self.long_wait_time, starting_element)
        assert self.is_displayed(starting_element)
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_displayed(target_element):
                return
            elif self.is_displayed(SampleTemperatureTestLocators.WORKFLOW_STOPPED_BANNER):
                assert False, "Sample Temperature Test got interrupted"
        assert False, "Sample Temperature Test did not finish in the allotted time"
