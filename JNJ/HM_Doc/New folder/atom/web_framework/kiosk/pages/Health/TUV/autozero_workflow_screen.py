"""
File_Name: autozero_workflow.py
Desc: This file contains specific user actions on screens within the autozero workflow
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/1/23
"""
import time
import re

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Health.TUV.autozero_workflow_locators import AutozeroWorkflowLocators
from web_framework.kiosk.pages.base_page import BasePage


class AutozeroWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_autozero_screen(self):
        locator = AutozeroWorkflowLocators.PAGE_BANNER
        screen_name = "Autozero screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_channel_reset_values(self):
        start_time = time.time()
        while time.time() - start_time < WaitTimeConstants.AutoZeroTest:
            current_text = self.get_text(AutozeroWorkflowLocators.CHANNEL_A_OFFSET)
            self.logger.info(f"current_text===>>>{current_text}")

            if current_text == "0.0000 AU":
                break
            time.sleep(1)
        channel_a = re.search(r'(\d\.\d{4})',self.get_text(AutozeroWorkflowLocators.CHANNEL_A_OFFSET))
        channel_b = re.search(r'(\d\.\d{4})',self.get_text(AutozeroWorkflowLocators.CHANNEL_B_OFFSET))
        channel_a_value = float(channel_a[1])
        channel_b_value = float(channel_b[1])
        assert channel_a_value == 0.0000 and channel_b_value == 0.0000, f"Values were not reset. Channel A: {channel_a_value}, Channel B: {channel_b_value}"

    def validate_channel_autozero_values(self):
        start_time = time.time()
        while time.time() - start_time < WaitTimeConstants.AutoZeroTest:
            current_text = self.get_text(AutozeroWorkflowLocators.CHANNEL_A_OFFSET)
            self.logger.info(f"current_text===>>>{current_text}")

            if current_text != "0.0000" and current_text != "--":
                break
            time.sleep(1)
        channel_a = re.search(r'(\d\.\d{4})', self.get_text(AutozeroWorkflowLocators.CHANNEL_A_OFFSET))
        channel_b = re.search(r'(\d\.\d{4})', self.get_text(AutozeroWorkflowLocators.CHANNEL_B_OFFSET))
        channel_a_value = float(channel_a[1])
        channel_b_value = float(channel_b[1])
        assert channel_a_value != 0.0000 and channel_b_value != 0.0000, f"Values were not updated from autozero process. Channel A: {channel_a_value}, Channel B: {channel_b_value}"

