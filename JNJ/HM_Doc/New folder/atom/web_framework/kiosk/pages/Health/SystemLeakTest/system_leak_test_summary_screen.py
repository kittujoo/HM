"""
File_Name: system_leak_test_summary_screen.py
Desc: This file contains specific user action on all the screen in the dynamic leak test summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022
__modified = "Tyler Prada"added pressure unit function- 6/22/23
__modified = "Supreet Sethi "Renaming pressure unit function based on review comments- 12/11/23
"""
import re
import time

from web_framework.kiosk.pages.Health.Models.leak_test_summary import LeakTestSummaryDetails
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.system_leak_test_constant import SystemLeakTestConstant
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import SystemLeakTestWorkFlowSummaryLocators
from web_framework.kiosk.pages.base_page import BasePage


class SystemLeakTestSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.leak_test_summary = None

    def validate_summary_screen(self):
        locator = SystemLeakTestWorkFlowSummaryLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary Screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_details(self):
        self.validate_summary_screen()
        time.sleep(1)
        current_solvent = self.get_solvent_line(SystemLeakTestWorkFlowSummaryLocators.SOLVENT_INFO_LABEL)
        current_accum_target_pressure = self.get_target_pressure(
            SystemLeakTestWorkFlowSummaryLocators.ACCUMULATOR_TARGET_INFO_LABEL)
        current_primary_target_function = self.get_target_pressure(
            SystemLeakTestWorkFlowSummaryLocators.PRIMARY_TARGET_INFO_LABEL)

        current_end_point = self.get_text(SystemLeakTestWorkFlowSummaryLocators.ENDPOINT_INFO_LABEL)
        current_prime_option = self.get_prime_option_text(SystemLeakTestWorkFlowSummaryLocators.PRIME_OPTION_LABEL)
        self.logger.info(f"solvent_current_prime_option======>>>>>>{current_prime_option}")

        leak_test_summary_details = LeakTestSummaryDetails(current_solvent, current_accum_target_pressure,
                                                           current_primary_target_function,
                                                           current_end_point, current_prime_option)
        return leak_test_summary_details

    def get_solvent_line(self, locator):
        solvent_line_text = self.get_text(locator)
        self.logger.info(f"solvent_line_text======>>>>>>{solvent_line_text}")
        solvent_line = solvent_line_text[8]
        return solvent_line

    def get_target_pressure(self, locators):

        try:
            pressure_text = self.get_text(locators)
            self.logger.info(f"locators==>> {locators}")
            pressure = pressure_text.split()
            target_pressure = pressure[0]

            current_target_pressure = int(target_pressure)
            return current_target_pressure

        except:
            self.logger.info(f" Exception block")
            return ''

    def get_prime_option_text(self, locator):
        prime_option_text = self.get_text(locator)
        if prime_option_text == "Not selected":
            prime_option_label = "Don't prime"
        else:
            prime_option_label = "Prime"

        return prime_option_label

    def expected_summary_details_for_standard_test(self, solvent_line, expected_accum_pressure,
                                                   expected_primary_pressure):
        """

        :param solvent_line:
        :param expected_accum_pressure:
        :param expected_primary_pressure:
        :return:
        """
        expected_solvent = solvent_line
        expected_accum_target_pressure = int(expected_accum_pressure)
        expected_primary_target_pressure = int(expected_primary_pressure)
        expected_end_point = SystemLeakTestConstant.DefaultEndPoint
        expected_prime_option = SystemLeakTestConstant.DefaultPrimeOption
        expected_test_fail_option = SystemLeakTestConstant.DefaultTestFailOption
        expected_estimate_time = SystemLeakTestConstant.DefaultEstimatedTime

        leak_test_summary_details = LeakTestSummaryDetails(expected_solvent, expected_accum_target_pressure,
                                                           expected_primary_target_pressure,
                                                           expected_end_point, expected_prime_option,
                                                           expected_test_fail_option,
                                                           expected_estimate_time)
        return leak_test_summary_details

    def get_accumulator_target_pressure_unit(self):
        accumulator_text = self.get_text(SystemLeakTestWorkFlowSummaryLocators.ACCUMULATOR_TARGET_INFO_LABEL)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", accumulator_text)
        return pressure_unit[1]

    def get_primary_target_pressure_unit(self):
        primary_text = self.get_text(SystemLeakTestWorkFlowSummaryLocators.PRIMARY_TARGET_INFO_LABEL)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", primary_text)
        return pressure_unit[1]
