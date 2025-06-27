"""
File_Name: heater_cooler_workflow_summary_screen.py
Desc: This file contains specific user actions on screens within the heater/cooler workflow summary screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 1/14/2021
__modified__ = "Tyler Prada" Added summary and result screen details methods 2/15/22
__modified__ = "Tyler Prada" Adjustments due to workflow changes & results rework 7/22/22
__modified__ = "Sharmila Vairmani" update the  validate_summary_screen function 12/16/22

"""

import time

from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.heater_cooler_constants import HeaterCoolerConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Health.Models.heater_cooler_summary import HeaterCoolerSummaryDetails
from web_framework.kiosk.pages.Locators.Health.ColumnModule.heater_cooler_workflow_locators import (HeaterCoolerSummaryLocators, HeaterCoolerResultsLocators)
from web_framework.kiosk.pages.base_page import BasePage


class HeaterCoolerWorkflowSummaryScreen(BasePage):

    def __init__(self, driver, base_url, assert_timeout: AssertTimeout, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.assert_time_out = assert_timeout

    def validate_summary_screen(self):
        locator = HeaterCoolerSummaryLocators.COLUMN_DOOR_INFO_LABEL
        screen_name = "Summary Screen for the heater/cooler workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_heater_cooler_test_screen(self):
        locator = HeaterCoolerSummaryLocators.PROGRESS_BANNER
        screen_name = "Progress cycle screen for the heater/cooler workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_results_screen(self):
        locator = HeaterCoolerResultsLocators.RESULTS_PAGE_BANNER
        screen_name = "Results screen for the heater/cooler workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_details(self):
        current_ambient_temperature_string = self.get_container_text(HeaterCoolerSummaryLocators.AMBIENT_TEMPERATURE_INFO_LABEL)
        current_ambient_temperature = current_ambient_temperature_string[-2:]
        current_column_temperature_string = self.get_container_text(HeaterCoolerSummaryLocators.COLUMN_TEMPERATURE_INFO_LABEL)
        current_column_temperature = current_column_temperature_string[-2:]
        current_column_door = self.get_container_text(HeaterCoolerSummaryLocators.COLUMN_DOOR_INFO_LABEL)

        heater_cooler_summary_details = HeaterCoolerSummaryDetails(current_ambient_temperature,
                                                                   current_column_temperature,
                                                                   current_column_door)

        return heater_cooler_summary_details

    def validate_results_values(self):
        # time is for the data table opening animation
        time.sleep(2)
        test_status = self.get_container_text(HeaterCoolerResultsLocators.RESULTS_STATUS)
        current_ambient_temperature = float(self.get_container_text(HeaterCoolerResultsLocators.AMBIENT_TEMPERATURE_INFO_LABEL))
        target_change = float(self.get_container_text(HeaterCoolerResultsLocators.TARGET_RATE_INFO_LABEL))
        measured_change = abs(float(self.get_container_text(HeaterCoolerResultsLocators.MEASURED_RATE_INFO_LABEL)))

        assert current_ambient_temperature >= HeaterCoolerConstants.AmbientTemperatureMin and current_ambient_temperature <= HeaterCoolerConstants.AmbientTemperatureMax, f"Ambient Temp is out of range: {current_ambient_temperature}"
        assert measured_change >= target_change, f"The measured change was less than what was targeted. Target: {target_change} | Measured: {measured_change}"
        assert test_status == HeaterCoolerConstants.PassMessage, "The test was displayed as failed"

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            HeaterCoolerSummaryLocators.STATUS_BANNER,
            HeaterCoolerConstants.StatusValidateText, WaitTimeConstants.SmallWait)

    def validate_column_temp_page_banners(self) -> bool:
        if self.is_displayed(HeaterCoolerResultsLocators.RESULTS_PAGE_BANNER):
            return True
        elif self.is_displayed(HeaterCoolerSummaryLocators.WORKFLOW_STOPPED_BANNER):
            return False
        else:
            return False

    def wait_for_column_test_end(self, timeout=HeaterCoolerConstants.MaxTimeTocompleteheaterCooler):
        starting_element = HeaterCoolerSummaryLocators.PROGRESS_BANNER
        self.wait_for_element_visibility(self.long_wait_time, starting_element)
        assert self.is_displayed(starting_element)
        result = self.assert_time_out.wait_for_condition(lambda: self.validate_column_temp_page_banners(),
                                                         timeout_in_seconds=timeout, polling_period_in_seconds=2)
        assert result, "Column Compartment Temperature Test did not finish in the allotted time or got interrupted"

    def validate_measured_change(self, temperature):
        test_status = self.get_text(HeaterCoolerResultsLocators.RESULTS_STATUS)
        measured_change = float(self.get_text(HeaterCoolerResultsLocators.MEASURED_RATE_INFO_LABEL).strip())
        assert measured_change >= temperature, f"The measured change was not greater than {temperature} degrees Celsius. Actual Measured Change: \
                                                    {measured_change}"
        assert test_status == HeaterCoolerConstants.PassMessage, "The test was displayed as failed"
