"""
File_Name: calibrate_axes_workflow.py
Desc: This file contains specific user actions on screens within the calibrate axes workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/9/2022
__modified__ = "Tyler Prada" added platter power off screen validation function 5/3/22
__modified__ = "Tyler Prada" moved summary screen to respective summary script 6/17/22
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.calibrate_axes_locators import CalibrateAxesWorkflowLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.base_page import BasePage


class CalibrateAxesWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_power_off_screen(self):
        locator = CalibrateAxesWorkflowLocators.POWEROFF_INFO_BANNER
        screen_name = "Power off info screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_setup_screen(self):
        locator = CalibrateAxesWorkflowLocators.SETUP_PAGE_BANNER
        screen_name = "Setup Screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_next_button_inactive(self):
        next_button = self.get_element(BasePageLocators.NEXT_BUTTON_LABEL)
        next_button_state = next_button.get_attribute("ng-reflect-available")
        active_element_state = next_button_state.find("false")
        self.logger.info(f"The next_button_state==>>{next_button_state} ")

        if active_element_state != -1:
            return True
        return False

    def choose_calibration_path(self, calibration_path):
        path_text_dictionary = {
            "Z-Axis": CalibrateAxesWorkflowLocators.ZAXIS_PATH,
            "Zp-Axis": CalibrateAxesWorkflowLocators.ZPAXIS_PATH,
            "Platter": CalibrateAxesWorkflowLocators.PLATTER_PATH,
            "B-0-Axes": CalibrateAxesWorkflowLocators.B0_PATH,
            "Hard-Stop": CalibrateAxesWorkflowLocators.HARD_STOP_PATH
        }

        if calibration_path in path_text_dictionary:
            locator = path_text_dictionary[calibration_path]
            self.tap(locator)
            return

        assert False, f"Unexpected calibration path => {calibration_path}"

    def validate_cautions_banner(self):
        locator = CalibrateAxesWorkflowLocators.CAUTIONS_PAGE_BANNER
        screen_name = "Cautions Screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_functions_banner(self):
        locator = CalibrateAxesWorkflowLocators.FUNCTIONS_PAGE_BANNER
        screen_name = "Functions screen for the calibrate axes workflow"
        self.validate_screen(locator, screen_name, self.wait_time)
