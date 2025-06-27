"""
File_Name: needle_seal_readiness_workflow_summary_screen.py
Desc: This file contains specific user actions on screens within the needle seal readiness test workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/17/22
__modified = "Tyler Prada" Added pressure unit function 6/22/23
"""
import re

from utilities.logger import Logger
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Health.Models.needle_seal_readiness_summary import NeedleSealReadinessSummaryDetails
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import \
    NeedleSealReadinessSummaryLocators
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import \
    SampleMeteringPumpSummaryLocators
from web_framework.kiosk.pages.base_page import BasePage


class NeedleSealReadinessSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = NeedleSealReadinessSummaryLocators.FLOW_RATE_INFO_LABEL
        screen_name = "Summary Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_details(self):
        self.validate_summary_screen()
        current_flow_rate = self.get_text(NeedleSealReadinessSummaryLocators.FLOW_RATE_INFO_LABEL)
        self.logger.info(f" current_flow_rate =={current_flow_rate}")
        current_composition = self.get_text(NeedleSealReadinessSummaryLocators.COMPOSITION_LABEL)
        self.logger.info(f" current_composition =={current_composition}")
        current_system_pressure = self.get_text(NeedleSealReadinessSummaryLocators.SYSTEM_PRESSURE_INFO_LABEL)
        self.logger.info(f" current_system_pressure =={current_system_pressure}")

        needle_seal_readiness_summary_details = NeedleSealReadinessSummaryDetails(current_flow_rate,
                                                                                  current_composition,
                                                                                  current_system_pressure)

        return needle_seal_readiness_summary_details

    def get_expected_solvent_composition(self, line_1, line_2, line_3, line_4):
        composition_data_list = [line_1, line_2, line_3, line_4]
        composition_list = []

        for i in range(len(composition_data_list)):
            composition = SolventLine.get_percentage_value(composition_data_list[i])
            composition_list.append(composition)
        return composition_list

    def get_summary_text(self):
        self.wait_time_to_load_value(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_ONE)
        return [
            self.get_text(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_ONE),
            self.get_text(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_TWO)
        ]

    def get_target_pressure_unit(self):
        primary_text = self.get_text(SampleMeteringPumpSummaryLocators.TARGET_PRESSURE_INFO_LABEL)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", primary_text)
        return pressure_unit[1]
