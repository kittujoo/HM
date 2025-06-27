"""
File_Name: sample_metering_pump_workflow.py
Desc: This file contains specific user actions on screens within the sample metering pump leak test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 0/0/00
__modified__ = "Tyler Prada" adjusted summary validation 12/5/22
__modified = "Tyler Prada" added pressure unit function for validation 6/22/23
"""
import re
import time
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_metering_pump_constants import SampleMeteringPumpConstants
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_temperature_test_constants import SampleTemperatureTestConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import (SampleMeteringPumpLocators,
                                                                                                            SampleMeteringPumpSetupLocators,
                                                                                                            SampleMeteringPumpWelcomeLocators,
                                                                                                            SampleMeteringPumpResultsLocators)
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_temperature_test_workflow_locators import SampleTemperatureTestLocators
from web_framework.kiosk.pages.Utilities.solvent_composition_utility import SolventCompositionUtilities


class SampleMeteringPumpSetupScreen(SolventCompositionUtilities):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_solvent_option = None
        self.selected_prime_option = None

    def validate_welcome_screen(self):
        locator = SampleMeteringPumpLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_setup_screen(self):
        locator = SampleMeteringPumpSetupLocators.SOLVENT_SETUP_BANNER
        screen_name = "Solvent setup for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_priming_setup_screen(self):
        locator = SampleMeteringPumpSetupLocators.PRIME_SETUP_BANNER
        screen_name = "Priming setup for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_selected_prime_option(self, prime_option):
        self.selected_prime_option = prime_option

    def get_expected_prime_option(self):
        prime_pump = TypeConverter.to_bool(self.selected_prime_option)

        if prime_pump:
            return SampleMeteringPumpConstants.DefaultPrimingOption
        else:
            return None

    def get_target_pressure_unit(self):
        primary_text = self.get_text(SampleMeteringPumpSetupLocators.TARGET_PRESSURE_HEADER)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", primary_text)
        return pressure_unit[1]

    def get_welcome_paragraph_text(self):
        return [
            self.get_text(SampleMeteringPumpWelcomeLocators.WELCOME_PARAGRAPH_ONE),
            self.get_text(SampleMeteringPumpWelcomeLocators.WELCOME_PARAGRAPH_TWO)
        ]

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            SampleTemperatureTestLocators.STATUS_BANNER,
            SampleTemperatureTestConstants.StatusValidateText, WaitTimeConstants.SmallWait)

    def wait_for_test_end(self, timeout=SampleMeteringPumpConstants.SampleMeteringPumpDefaultWaitTime):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_displayed(SampleMeteringPumpResultsLocators.RESULTS_PAGE_BANNER):
                return
            elif self.is_displayed(SampleMeteringPumpResultsLocators.WORKFLOW_STOPPED_BANNER):
                assert False, "Test got interrupted"
        assert False, "Test did not finish in the allotted time"

    def get_target_pressure_hint_unit(self):
        target_hint_text = self.get_text(SampleMeteringPumpSetupLocators.TARGET_PRESSURE_HINT)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", target_hint_text)
        return pressure_unit[1]
