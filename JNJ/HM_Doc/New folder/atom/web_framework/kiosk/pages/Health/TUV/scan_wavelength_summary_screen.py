"""
File_Name: scan_wavelength_summary_screen.py
Desc: This file contains specific user actions on screens within the scan wavelength test workflow summary screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila" Initial Check-in 11/28/22
"""
import re

from web_framework.kiosk.pages.Health.Models.scan_wavelength_summary import ScanWavelengthSummaryDetails
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import NeedleSealReadinessSummaryLocators
from web_framework.kiosk.pages.Locators.Health.TUV.scan_wavelength_workflow_locators import ScanWavelengthSummaryScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class ScanWavelengthSummaryScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_summary_screen(self):
        locator = ScanWavelengthSummaryScreenLocators.SUMMARY_PAGE_BANNER
        screen_name = "Summary Screen for the scan wavelength workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_summary_details(self):
        self.validate_summary_screen()
        current_wavelength_text = self.get_text(ScanWavelengthSummaryScreenLocators.MIN_WAVE_INFO)
        wavelength_rates = re.search(r'(\d{1,3})[\s[a-z]*]*(\d{1,3})', current_wavelength_text)
        min_wavlength = wavelength_rates[1]
        max_wavlength = wavelength_rates[2]

        current_scan_rate_text = self.get_text(ScanWavelengthSummaryScreenLocators.SCAN_RATE_INFO)
        current_scan_rate_text = current_scan_rate_text.replace("nm/min", "")
        current_scan_rate_text = current_scan_rate_text.strip()
        self.logger.info(f" current scan rate =={current_scan_rate_text}")
        current_summary_details = ScanWavelengthSummaryDetails(min_wavlength, max_wavlength, current_scan_rate_text)
        return current_summary_details

    def expected_summary_details(self, min_wavelength, maxi_wavelength, date_rate):
        expected_min_wavelength = min_wavelength
        expected_maxi_wavelength = maxi_wavelength
        expected_date_rate = date_rate

        expected_summary_details = ScanWavelengthSummaryDetails(expected_min_wavelength,
                                                                expected_maxi_wavelength,
                                                                expected_date_rate)
        return expected_summary_details

    def get_summary_text(self):
        return [
            self.get_text(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_ONE),
            self.get_text(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_TWO),
            self.get_text(NeedleSealReadinessSummaryLocators.SUMMARY_LINE_THREE)
        ]
