"""
File_Name: sample_metering_pump_workflow_summary_screen.py
Desc: This file contains specific user actions on screens within the sample metering pump leak test workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/10/22
__modified__ = "Tyler Prada" adjusted summary validation 12/5/22
__modified__ = "Tyler Prada" Post FCS adjustments 6/13/23
__modified = "Tyler Prada" added pressure unit function for validation 6/22/23
"""
import re

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_metering_pump_constants import SampleMeteringPumpConstants
from web_framework.kiosk.pages.Health.Models.sample_metering_pump_summary import SampleMeteringPumpSummaryDetails
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import SampleMeteringPumpSummaryLocators
from web_framework.kiosk.pages.base_page import BasePage


class SampleMeteringPumpSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = SampleMeteringPumpSummaryLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_details(self, toggle_position):
        prime_pump = TypeConverter.to_bool(toggle_position)

        if prime_pump:
            self.wait_time_to_load_value(SampleMeteringPumpSummaryLocators.PRIMING_OPTION_INFO_LABEL, "")
            current_priming_option = self.get_text(SampleMeteringPumpSummaryLocators.PRIMING_OPTION_INFO_LABEL)
        else:
            current_priming_option = None

        sample_metering_pump_summary_details = SampleMeteringPumpSummaryDetails(current_priming_option)

        return sample_metering_pump_summary_details

    def get_expected_summary_details(self, toggle_position):
        prime_pump = TypeConverter.to_bool(toggle_position)

        if prime_pump:
            expected_priming_option = SampleMeteringPumpConstants.DefaultPrimingOption
        else:
            expected_priming_option = None

        sample_metering_pump_summary_details = SampleMeteringPumpSummaryDetails(expected_priming_option)
        return sample_metering_pump_summary_details

    def get_target_pressure_unit(self):
        primary_text = self.get_text(SampleMeteringPumpSummaryLocators.TARGET_PRESSURE_INFO_LABEL)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", primary_text)
        return pressure_unit[1]
