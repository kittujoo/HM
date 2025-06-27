"""
File_Name: flow_path_settings_screen.py
Desc: This file contains specific user action on the elements in the flow path settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/16/2021
__modified__ = "Tyler Prada" changed select_flow_path to have one mixer option 3/1/22
__modified__ = "Tyler Prada" Reworked functions for card changes 4/28/22
"""
from utilities.logger import Logger

from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_path_condition_card import FlowPathSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class FlowPathSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def validate_flow_path_settings_screen(self):
        locator = FlowPathSettingsScreenLocators.FLOW_PATH_OPTION_LIST
        screen_name = "Flow path settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_flow_path(self, flow_path):
        flow_path_text_dictionary = {
            "Blocked": FlowPathSettingsScreenLocators.BLOCKED_OPTION,
            "Vent": FlowPathSettingsScreenLocators.VENT_OPTION,
            "Mixer": FlowPathSettingsScreenLocators.MIXER_OPTION}

        if flow_path in flow_path_text_dictionary:
            locator = flow_path_text_dictionary[flow_path]
            self.tap(locator)
            return

        assert False, (f"Unexpected flow path => {flow_path}")
