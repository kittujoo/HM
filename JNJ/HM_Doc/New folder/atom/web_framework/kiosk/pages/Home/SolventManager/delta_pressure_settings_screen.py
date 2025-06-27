"""
File_Name: delta_pressure_settings_screen.py
Desc: This file contains specific user action on the elements in the flow path settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 7/26/2021
"""

from utilities.logger import Logger

from web_framework.kiosk.pages.Locators.Home.SolventManager.delta_pressure_condition_card import DeltaPressureSettingsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class DeltaPressureSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def validate_delta_pressure_settings_screen(self):
        locator = DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_HEADER_LABEL
        screen_name = "Delta pressure settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def switch_on_pressure_monitor(self):
        current_toggle_status = self.is_toggle_component_enabled(DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_TOGGLE)
        if not current_toggle_status:
            self.toggle_switch("Delta pressure toggle", DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_TOGGLE, current_toggle_status, True)

    def switch_off_pressure_monitor(self):
        current_toggle_status = self.is_toggle_component_enabled(
            DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_TOGGLE)
        if current_toggle_status:
            self.toggle_switch("Delta pressure toggle", DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_TOGGLE,
                               current_toggle_status, False)
    #
    # def switch_on_pressure_notifications(self):
    #     current_toggle_status = self.is_toggle_component_enabled(DeltaPressureSettingsScreenLocators.NOTIFICATIONS_TOGGLE)
    #     if not current_toggle_status:
    #         self.toggle_switch("Notifications toggle", DeltaPressureSettingsScreenLocators.NOTIFICATIONS_TOGGLE, current_toggle_status, True)
