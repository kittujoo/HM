"""
File_Name: noise_drift_workflow_results_screen.py
Desc: This file contains specific user actions on screens within the noise & drift workflow results screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairmani" Initial Check-in 06/13/2022
"""

import re

from web_framework.kiosk.pages.Health.Models.noise_drift_results import NoiseDriftConditionDetails
from web_framework.kiosk.pages.Health.Models.noise_drift_summary import NoiseDriftSolventDetails
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.TUV.noise_drift_workflow_locators import NoiseDriftResultsLocators
from web_framework.kiosk.pages.base_page import BasePage


class NoiseDriftWorkflowResultsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_results_screen(self):
        locator = NoiseDriftResultsLocators.RESULTS_BANNER
        screen_name = "results screen for noise & drift test"
        self.validate_screen(locator, screen_name, wait_time=10)

    def validate_results_data_table(self):
        locator = NoiseDriftResultsLocators.FLOW_RATE_INFO
        screen_name = "Noise and drift result data"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_condition_details(self):
        current_flow_rate = self.get_text(NoiseDriftResultsLocators.FLOW_RATE_INFO)
        current_composition = self.get_text(NoiseDriftResultsLocators.COMPOSITION_INFO)
        current_flow_cell = self.get_text(NoiseDriftResultsLocators.FLOW_CELL_TYPE_INFO)
        current_ambient_temperature = self.get_text(NoiseDriftResultsLocators.AMBIENT_TEMPERATURE_INFO)

        noise_drift_summary_details = NoiseDriftConditionDetails(current_flow_rate, current_composition,
                                                                 current_flow_cell, current_ambient_temperature)
        return noise_drift_summary_details

    def get_solvent_details(self):
        flow_rate = self.get_text(NoiseDriftResultsLocators.FLOW_RATE_INFO)
        self.logger.info(f"flow_rate=====>>>>>>>{flow_rate}")
        current_flow_rate = flow_rate.strip()
        current_composition = self.get_text(NoiseDriftResultsLocators.COMPOSITION_INFO)
        current_composition = current_composition.replace(" ", "")
        solvent_composition_values = current_composition.split("%:")
        self.logger.info(f"solvent_composition_information+++++++>>>>>>>>>{current_composition}")
        self.logger.info(f"solvent_composition_values+++++++>>>>>>>>>{solvent_composition_values}")
        solvent_a = re.sub(r"\D", "", solvent_composition_values[0]) + ".0"
        solvent_b = re.sub(r"\D", "", solvent_composition_values[1]) + ".0"
        solvent_c = re.sub(r"\D", "", solvent_composition_values[2]) + ".0"
        solvent_d = re.sub(r"\D", "", solvent_composition_values[3])

        noise_drift_summary_details = NoiseDriftSolventDetails(current_flow_rate, solvent_a, solvent_b, solvent_c, solvent_d)
        return noise_drift_summary_details
