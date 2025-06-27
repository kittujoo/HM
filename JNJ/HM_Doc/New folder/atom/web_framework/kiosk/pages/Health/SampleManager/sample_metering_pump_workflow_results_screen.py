"""
File_Name: sample_metering_pump_workflow_results_screen.py
Desc: This file contains specific user actions on screens within the sample metering pump leak test workflow results screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 6/27/22
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import SampleMeteringPumpResultsLocators
from web_framework.kiosk.pages.base_page import BasePage


class SampleMeteringPumpResultsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_results_screen(self):
        locator = SampleMeteringPumpResultsLocators.RESULTS_PAGE_BANNER
        screen_name = "results screen for sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_current_leak_rate(self):
        return self.get_text(SampleMeteringPumpResultsLocators.LEAK_RATE_INFO_LABEL)
