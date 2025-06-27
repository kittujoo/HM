"""
File_Name: uv_lamp_configuration_screen.py
Desc: This file contains specific user action on the web elements in the uv lamp configuration screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22
"""
import re

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.TuvDetector.uv_lamp_condition_card_locators import UVLampConditionCardLocators, UVLampConditionCardSettingsLocators
from web_framework.kiosk.pages.base_page import BasePage


class UVLampSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5
        self.lamp_hours_info = None

    def validate_uv_lamp_settings_screen(self):
        locator = UVLampConditionCardLocators.HEADER
        wait_time = self.wait_time
        screen_name = "UV lamp configuration screen"
        self.validate_screen(locator, screen_name, wait_time)

    def validate_lamp_hours_count(self):
        lamp_hours_text = self.get_text(UVLampConditionCardSettingsLocators.LAMP_HOURS_INFO_LABEL)
        capture = re.search(r'(\d+).of.(\d+)', lamp_hours_text)
        current_lamp_hours = capture[1]
        lamp_hours_max = capture[2]
        if not current_lamp_hours <= lamp_hours_max:
            return False
        return True

    def validate_good_ignition_count(self):
        lamp_ignitions_text = self.get_text(UVLampConditionCardSettingsLocators.LAMP_IGNITIONS_INFO_LABEL)
        capture = re.search(r'(\d+).of.(\d+)', lamp_ignitions_text)
        current_lamp_ignitions = capture[1]
        lamp_ignitions_max = capture[2]
        if not current_lamp_ignitions <= lamp_ignitions_max:
            return False
        return True

    def get_hours(self):
        actual_hours_info = self.get_container_text(UVLampConditionCardSettingsLocators.LAMP_HOURS_INFO_LABEL)
        self.logger.info(f"actual_hours_info ===>>> {actual_hours_info}")
        actual_hours_info = actual_hours_info[-10:]
        self.logger.info(f"actual_hours_info ===>>> {actual_hours_info}")

    def set_lamp_hours_info(self, lamp_hours_info):
        self.lamp_hours_info = lamp_hours_info

    def get_lamp_hours_info(self):
        return self.lamp_hours_info

    def get_lamp_used_hours(self):
        actual_lamp_hours_info = self.get_lamp_hours_info()
        expected_lamp_used_hours = actual_lamp_hours_info[:-14]
        lamp_used_hours = expected_lamp_used_hours.strip()
        return lamp_used_hours

    def get_lamp_total_hours(self):
        actual_lamp_hours_info = self.get_lamp_hours_info()
        split_lamp_hours_info = actual_lamp_hours_info.split("of")
        lamp_total_hours = split_lamp_hours_info[1].strip()
        lamp_total_hours = lamp_total_hours[:-6].strip()
        return lamp_total_hours
