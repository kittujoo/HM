"""
File_Name: shutdown_workflow_summary_screen.py
Desc: This file contains specific user actions on screens within the shutdown workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/12/2022

"""

from web_framework.kiosk.common.Constants.UI.WorkflowConstants.shutdown_constants import ShutdownConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.Setup.shutdown_workflow_locators import ShutdownWorkflowLocators
from web_framework.kiosk.pages.Setup.Models.summary_workflow import (TemperatureSummaryDetails, SolventSummaryDetails)
from web_framework.kiosk.pages.base_page import BasePage
import re


class ShutdownWorkflowSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_solvent_summary_details = None

    def get_current_temperature_details(self):
        current_sample_temperature_text = self.get_text(ShutdownWorkflowLocators.SAMPLE_TEMPERATURE_INFO)
        current_sample_temperature = None
        current_column_temperature = None
        for text in current_sample_temperature_text.split():
            try:
                current_sample_temperature = float(text)
                break
            except:
                continue

        current_column_temperature_text = self.get_text(ShutdownWorkflowLocators.COLUMN_TEMPERATURE_INFO)
        for text in current_column_temperature_text.split():
            try:
                current_column_temperature = float(text)
                break
            except:
                continue

        temperature_summary_details = TemperatureSummaryDetails(current_sample_temperature, current_column_temperature)
        return temperature_summary_details

    def get_expected_temperature_details(self, sample_temperature, column_temperature):
        expected_sample_temperature = sample_temperature
        expected_column_temperature = column_temperature
        startup_temperature_details = TemperatureSummaryDetails(expected_sample_temperature,
                                                                expected_column_temperature)
        return startup_temperature_details

    def get_solvent_details(self):
        current_solvent_info = self.get_text(ShutdownWorkflowLocators.SOLVENT_INFO)
        self.logger.info(f"current_solvent_info ==>> {current_solvent_info}")
        current_flow_rate_info = self.get_text(ShutdownWorkflowLocators.FLOW_RATE_INFO)
        self.logger.info(f"current_flow_rate_info ==>> {current_flow_rate_info}")
        current_solvent_info_list = re.findall(r"[^,\s]+", current_solvent_info)
        self.logger.info(f"current_solvent_info_list ==>> {current_solvent_info_list}")
        current_flow_rate_info_list = current_flow_rate_info.split()
        current_flow_rate = current_flow_rate_info_list[2]
        current_flow_rate = TypeConverter.to_float(current_flow_rate)

        # > 85% A, 5% B, 5% C, 5% D
        #  current_solvent_info_list ==>> ['85%', 'A,', '5%', 'B,', '5%', 'C,', '5%', 'D']
        solvent_checklist = ['A', 'B', 'C', 'D']

        for solvent in solvent_checklist:
            index = solvent_checklist.index(solvent)
            if solvent not in current_solvent_info_list:
                new_index = index + index
                current_solvent_info_list[new_index:new_index] = ['0%', solvent + ',']
                self.logger.info(f"current_solvent_info_list ==>> {current_solvent_info_list}")

        current_solvent_a = current_solvent_info_list[0][:-1]
        current_solvent_b = current_solvent_info_list[2][:-1]
        current_solvent_c = current_solvent_info_list[4][:-1]
        current_solvent_d = current_solvent_info_list[6][:-1]
        current_solvent_a = TypeConverter.to_float(current_solvent_a)
        current_solvent_b = TypeConverter.to_float(current_solvent_b)
        current_solvent_c = TypeConverter.to_float(current_solvent_c)
        current_solvent_d = TypeConverter.to_float(current_solvent_d)

        solvent_summary_details = SolventSummaryDetails(current_flow_rate, current_solvent_a, current_solvent_b,
                                                        current_solvent_c, current_solvent_d)
        self.logger.info(f"solvent_summary_details ==>> {solvent_summary_details}")
        return solvent_summary_details

    def validate_summary_screen(self):
        locator = ShutdownWorkflowLocators.SUMMARY_HEADER
        screen_name = "shutdown workflow summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            ShutdownWorkflowLocators.STATUS_HEADER,
            ShutdownConstants.StatusValidateText, WaitTimeConstants.SmallWait)
