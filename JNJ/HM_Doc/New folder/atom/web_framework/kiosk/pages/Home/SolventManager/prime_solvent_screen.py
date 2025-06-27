"""
file_Name: prime_solvent.py
Desc: This file contains specific user actions on the elements in the prime solvent workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/16/22
"""
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.condition_card_constants import MobilePhaseSolventConditionCard
from web_framework.kiosk.pages.Locators.Home.SolventManager.mobile_phase_configuration_settings_locators import PrimeSolventLocators
from web_framework.kiosk.pages.base_page import BasePage


class PrimeSolventSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_priming_options_screen(self):
        locator = PrimeSolventLocators.PRIMING_OPTIONS_BANNER
        screen_name = "Priming options screen "
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_priming_progress_screen(self):
        locator = PrimeSolventLocators.PRIMING_PROGRESS_BANNER
        screen_name = "Priming progress screen "
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_stop_info(self):
        expected_text_line_1 = MobilePhaseSolventConditionCard.StopPrimeInfo1
        actual_text_line_1 = self.get_text(PrimeSolventLocators.STOP_INFO_LINE_1)
        self.validate_text(actual_text_line_1, expected_text_line_1)

        expected_text_line_2 = MobilePhaseSolventConditionCard.StopPrimeInfo2
        actual_text_line_2 = self.get_text(PrimeSolventLocators.STOP_INFO_LINE_2)
        self.validate_text(actual_text_line_2, expected_text_line_2)
