"""
File_Name: noise_drift_workflow_summary_screen.py
Desc: This file contains specific user actions on screens within the noise & drift workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/20/22
__modified__ = "Sharmila Vairamani" added summary details function - 6/13/2022

"""

import time
import re

from web_framework.kiosk.common.Constants.UI.WorkflowConstants.noise_and_drift_constants import NoiseAndDriftConstants
from web_framework.kiosk.pages.Health.Models.noise_drift_summary import (NoiseDriftSolventDetails, NoiseDriftWavelengthDetails,
                                                                              NoiseDriftDataFrequencyDetails)
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.TUV.noise_drift_workflow_locators import NoiseDriftSummaryLocators, NoiseDriftResultsLocators
from web_framework.kiosk.pages.base_page import BasePage


class NoiseDriftWorkflowSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = NoiseDriftSummaryLocators.SUMMARY_BANNER
        screen_name = "wavelength screen for noise & drift test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_solvent_details(self):
        self.wait_time_to_load_value(NoiseDriftSummaryLocators.FLOW_RATE_INFO_LABEL)
        current_flow_rate = self.get_text(NoiseDriftSummaryLocators.FLOW_RATE_INFO_LABEL)
        current_flow_rate = current_flow_rate[:-6]
        current_flow_rate = current_flow_rate.strip()
        solvent_composition_information = self.get_text(NoiseDriftSummaryLocators.COMPOSITION_INFO_LABEL)
        solvent_composition_information = solvent_composition_information.replace(" ", "")
        solvent_composition_values = solvent_composition_information.split("%,")
        self.logger.info(f"solvent_composition_information+++++++>>>>>>>>>{solvent_composition_information}")
        self.logger.info(f"solvent_composition_values+++++++>>>>>>>>>{solvent_composition_values}")
        current_solvent_a = re.sub(r"\D", "", solvent_composition_values[0]) + ".0"
        current_solvent_b = re.sub(r"\D", "", solvent_composition_values[1]) + ".0"
        current_solvent_c = re.sub(r"\D", "", solvent_composition_values[2]) + ".0"
        current_solvent_d = re.sub(r"\D", "", solvent_composition_values[3])
        noise_drift_solvent_details = NoiseDriftSolventDetails(current_flow_rate, current_solvent_a, current_solvent_b,
                                                               current_solvent_c, current_solvent_d)
        return noise_drift_solvent_details

    def get_wavelength_details(self, wavelength_mode):

        if wavelength_mode == "single":
            current_wavelength_a = self.get_text(NoiseDriftSummaryLocators.WAVELENGTH_A_INFO_LABEL)
            current_wavelength_a = current_wavelength_a[0:3]
            current_wavelength_b = ""

        else:
            current_wavelength_a = self.get_text(NoiseDriftSummaryLocators.WAVELENGTH_A_INFO_LABEL)
            current_wavelength_a = current_wavelength_a[0:3]
            current_wavelength_b = self.get_text(NoiseDriftSummaryLocators.WAVELENGTH_B_INFO_LABEL)
            current_wavelength_b = current_wavelength_b[0:3]

        noise_drift_wavelength_details = NoiseDriftWavelengthDetails(current_wavelength_a, current_wavelength_b)
        return noise_drift_wavelength_details

    def get_data_rate_details(self):
        current_data_rate_text = self.get_text(NoiseDriftSummaryLocators.DATA_RATE_INFO_LABEL)
        current_data_rate = current_data_rate_text[:2]
        current_data_rate = current_data_rate.strip()

        current_filter_text = self.get_text(NoiseDriftSummaryLocators.FILTER_INFO_LABEL)
        current_filter = current_filter_text[:-8]
        current_filter = current_filter.strip()

        noise_drift_data_frequency_details = NoiseDriftDataFrequencyDetails(current_data_rate, current_filter)
        return noise_drift_data_frequency_details

    def validate_noise_drift_cycle(self):
        max_cycle_wait = 1200  # 20min
        assert self.is_displayed(NoiseDriftSummaryLocators.STATUS_BANNER)

        start_time = time.time()
        while time.time() - start_time < max_cycle_wait:
            if self.is_displayed(NoiseDriftSummaryLocators.RESULTS_BANNER):
                break
            time.sleep(1)
        assert self.is_displayed(NoiseDriftSummaryLocators.RESULTS_BANNER), f"Noise & Drift cycle was not completed"

    def wait_for_test_end(self, timeout=NoiseAndDriftConstants.NoiseDriftTestWait):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.is_displayed(NoiseDriftResultsLocators.RESULTS_BANNER):
                return
            elif self.is_displayed(NoiseDriftResultsLocators.WORKFLOW_STOPPED_BANNER):
                self.tap_done_button()
                assert False, "Workflow got interrupted"
        assert False, "Workflow did not finish in the allotted time"
