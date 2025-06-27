"""
File_Name: system_leak_test_results_screen.py
Desc: This file contains specific user action on all the screen in the leak test workflow results screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022

"""


from web_framework.kiosk.pages.Health.Models.dynamic_leak_test_results import (PrimaryResultsDetails, AccumulatorResultsDetails)
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.system_leak_test_constant import SystemLeakTestConstant
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import (SystemLeakTestWorkflowResultsLocators, SystemLeakTestSinglePressureLocators)
from web_framework.kiosk.pages.base_page import BasePage


class SystemLeakTestResultsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_summary_details = None

    def validate_results_screen(self):
        locator = SystemLeakTestWorkflowResultsLocators.RESULTS_HEADER
        screen_name = "Results Screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_arrow_status(self):
        current_arrow = self.get_element(SystemLeakTestWorkflowResultsLocators.ARROW_STATUS)
        current_arrow_state = current_arrow.get_attribute("ng-reflect-icon")
        self.logger.info(f"current_arrow_state===>{current_arrow_state}")
        assert current_arrow_state == "ics-img-arrow-down", "The results were not hidden"

    def get_expected_primary_results(self, expected_primary_pressure):
        expected_result_state = SystemLeakTestConstant.PrimaryResultState
        expected_primary_pressure = int(expected_primary_pressure)
        expected_leak_rate = SystemLeakTestConstant.PrimaryLeakRate
        expected_final_stroke = SystemLeakTestConstant.PrimaryFinalStroke
        expected_compression_attempts = SystemLeakTestConstant.PrimaryCompressionAttempts
        expected_primary_results_details = PrimaryResultsDetails(expected_result_state, expected_primary_pressure,
                                                                 expected_leak_rate, expected_final_stroke,
                                                                 expected_compression_attempts)
        return expected_primary_results_details

    def get_expected_accumulator_results(self, expected_accum_pressure):
        expected_result_state = SystemLeakTestConstant.AccumulatorResultState
        expected_accum_pressure = int(expected_accum_pressure)
        expected_leak_rate = SystemLeakTestConstant.AccumulatorLeakRate
        expected_final_stroke = SystemLeakTestConstant.AccumulatorFinalStroke
        expected_compression_attempts = SystemLeakTestConstant.AccumulatorCompressionAttempts
        expected_primary_results_details = AccumulatorResultsDetails(expected_result_state, expected_accum_pressure,
                                                                     expected_leak_rate, expected_final_stroke,
                                                                     expected_compression_attempts)
        return expected_primary_results_details

    def get_current_primary_results(self):
        current_result_state = self.get_text(SystemLeakTestWorkflowResultsLocators.PRIMARY_RESULT_STATE)
        current_primary_pressure = self.get_text(SystemLeakTestWorkflowResultsLocators.PRIMARY_MAX_PRESSURE)
        current_leak_rate = float(self.get_text(SystemLeakTestWorkflowResultsLocators.PRIMARY_LEAK_RATE))
        current_final_stroke = float(self.get_text(SystemLeakTestWorkflowResultsLocators.PRIMARY_STROKE_PERCENT))
        current_compression_attempts = self.get_text(SystemLeakTestWorkflowResultsLocators.PRIMARY_ATTEMPTS)
        primary_results_details = PrimaryResultsDetails(current_result_state, current_primary_pressure,
                                                        current_leak_rate, current_final_stroke,
                                                        current_compression_attempts)
        return primary_results_details

    def get_current_accumulator_results(self):
        current_result_state = self.get_text(SystemLeakTestWorkflowResultsLocators.ACCUMULATOR_RESULT_STATE)
        current_primary_pressure = self.get_text(SystemLeakTestWorkflowResultsLocators.ACCUMULATOR_MAX_PRESSURE)
        current_leak_rate = float(self.get_text(SystemLeakTestWorkflowResultsLocators.ACCUMULATOR_LEAK_RATE))
        current_final_stroke = float(self.get_text(SystemLeakTestWorkflowResultsLocators.ACCUMULATOR_STROKE_PERCENT))
        current_compression_attempts = self.get_text(SystemLeakTestWorkflowResultsLocators.ACCUMULATOR_ATTEMPTS)
        accumulator_results_details = AccumulatorResultsDetails(current_result_state, current_primary_pressure,
                                                                current_leak_rate, current_final_stroke,
                                                                current_compression_attempts)
        return accumulator_results_details

    def get_single_primary_results(self):
        current_result_state = self.get_text(SystemLeakTestSinglePressureLocators.PRIMARY_RESULT_STATE)
        current_primary_pressure = self.get_text(SystemLeakTestSinglePressureLocators.PRIMARY_MAX_PRESSURE)
        current_leak_rate = self.get_text(SystemLeakTestSinglePressureLocators.PRIMARY_LEAK_RATE)
        current_final_stroke = self.get_text(SystemLeakTestSinglePressureLocators.PRIMARY_STROKE_PERCENT)
        current_compression_attempts = self.get_text(SystemLeakTestSinglePressureLocators.PRIMARY_ATTEMPTS)
        primary_results_details = PrimaryResultsDetails(current_result_state, current_primary_pressure,
                                                        current_leak_rate, current_final_stroke,
                                                        current_compression_attempts)
        return primary_results_details
