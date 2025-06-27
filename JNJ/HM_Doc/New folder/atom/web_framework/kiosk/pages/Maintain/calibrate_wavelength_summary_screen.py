"""
File_Name: calibrate_wavelength_summary_screen.py
Desc: This file contains specific user actions on screens within the calibrate wavelength workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila" Initial Check-in 02/22/2022
__modified__ = "Tyler Prada" added summary details functions 7/18/22
"""

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.calibrate_wavelength_constant import CalibrateWavelengthConstant
from web_framework.kiosk.pages.Locators.Maintain.calibrate_wavelength_locators import CalibrateWavelengthSummaryLocators
from web_framework.kiosk.pages.Maintain.Models.calibrate_wavelength_summary import CalibrateWavelengthSummaryDetails
from web_framework.kiosk.pages.base_page import BasePage


class CalibrateWavelengthSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = CalibrateWavelengthSummaryLocators.SUMMARY_HEADER
        screen_name = "Summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_screen_details(self, flush_toggle_status):
        current_flush = self.get_text(CalibrateWavelengthSummaryLocators.FLUSH_INFO_LABEL)
        if not flush_toggle_status:
            current_pre_flush = None
        else:
            current_pre_flush = self.get_text(CalibrateWavelengthSummaryLocators.PRE_FLUSH_INFO_LABEL)
        current_flow_cell = self.get_text(CalibrateWavelengthSummaryLocators.FLOW_CELL_INFO_LABEL)
        current_lamp_state = self.get_text(CalibrateWavelengthSummaryLocators.LAMP_INFO_LABEL)

        calibrate_wavelength_summary_details = CalibrateWavelengthSummaryDetails(current_flush,
                                                                                 current_pre_flush,
                                                                                 current_flow_cell,
                                                                                 current_lamp_state)

        return calibrate_wavelength_summary_details

    def get_flowrate(self):
        current_flow_rate_string = self.get_text(
            CalibrateWavelengthSummaryLocators.FLOW_INFO_LABEL)
        current_flow_rate_info = current_flow_rate_string[:-6]
        self.logger.info(current_flow_rate_info)
        return current_flow_rate_info
