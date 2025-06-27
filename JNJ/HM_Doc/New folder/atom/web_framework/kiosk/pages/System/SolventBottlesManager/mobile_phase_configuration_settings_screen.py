"""
file_Name: solvent_configuration_settings_screen.py
Desc: This file contains specific user actions on the elements in the system screen which includes
      solvent configuration
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 12/15/2021
__modified__ = "Tyler Prada" Added mobile phase settings screen functions 8/8/22
__modified__ = "Tyler Prada" Added another default color 12/6/22
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.SolventManager.mobile_phase_configuration_settings_locators import (
    MobilePhaseConfigurationSettingsScreenLocators as MobileLocators, MobilePhaseConfigurationSettingsScreenLocators)
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.mobile_phase_configuration_settings_screen_locators import \
    MobilePhaseConfigurationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from selenium.webdriver.support.color import Color


class MobilePhaseConfigurationSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_mobile_phase_selection_screen(self):
        locator = MobileLocators.REPLACE_SOLVENT_PANEL
        screen_name = "Mobile Phase options screen "
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_mobile_phase_settings_screen(self):
        locator = MobileLocators.MOBILE_PHASE_A_TAB
        screen_name = "Mobile Phase configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_mobile_phase_tab(self, mobile_phase):
        mobile_phase_text_dictionary = {
            "A": MobileLocators.MOBILE_PHASE_A_TAB,
            "B": MobileLocators.MOBILE_PHASE_B_TAB,
            "C": MobileLocators.MOBILE_PHASE_C_TAB,
            "D": MobileLocators.MOBILE_PHASE_D_TAB}

        locator = mobile_phase_text_dictionary[mobile_phase]
        self.tap(locator)

    def get_volume(self, mobile_phase):
        mobile_phase_text_dictionary = {
            "A": MobilePhaseConfigurationScreenLocators.SOLVENT_VOLUME_A_READ_BACK_VALUE,
            "B": MobilePhaseConfigurationScreenLocators.SOLVENT_VOLUME_B_READ_BACK_VALUE,
            "C": MobilePhaseConfigurationScreenLocators.SOLVENT_VOLUME_C_READ_BACK_VALUE,
            "D": MobilePhaseConfigurationScreenLocators.SOLVENT_VOLUME_D_READ_BACK_VALUE}
        return self.get_text(mobile_phase_text_dictionary[mobile_phase])

    def get_line_color(self, mobile_phase):
        mobile_phase_text_dictionary = {
            "A": MobilePhaseConfigurationScreenLocators.SOLVENT_A_LINE_COLOR_ICON,
            "B": MobilePhaseConfigurationScreenLocators.SOLVENT_B_LINE_COLOR_ICON,
            "C": MobilePhaseConfigurationScreenLocators.SOLVENT_C_LINE_COLOR_ICON,
            "D": MobilePhaseConfigurationScreenLocators.SOLVENT_D_LINE_COLOR_ICON}
        actual_color = Color.from_string(self.find_element(mobile_phase_text_dictionary[mobile_phase]).value_of_css_property('background-color'))
        return actual_color

    def select_bottle_volume(self, mobile_phase, bottle_volume):
        bottle_volume_text_dictionary = {
            "2L": MobileLocators.SOLVENT_BOTTLE_2L_OPTION,
            "4L": MobileLocators.SOLVENT_BOTTLE_4L_OPTION,
            "5L": MobileLocators.SOLVENT_BOTTLE_5L_OPTION}
        mobile_phase_volume_dictionary = {
            "A": MobileLocators.SOLVENT_BADGE_A,
            "B": MobileLocators.SOLVENT_BADGE_B,
            "C": MobileLocators.SOLVENT_BADGE_C,
            "D": MobileLocators.SOLVENT_BADGE_D}

        self.tap(mobile_phase_volume_dictionary[mobile_phase])
        bottle_volume_locator = bottle_volume_text_dictionary[bottle_volume]
        self.scroll_to_view(bottle_volume_locator)
        self.tap(bottle_volume_locator)

    def select_line_color(self, mobile_phase, line_color):
        line_color_text_dictionary = {
            "blue": MobileLocators.LINE_COLOR_BLUE,
            "red": MobileLocators.LINE_COLOR_RED,
            "green": MobileLocators.LINK_COLOR_GREEN,
            "pink": MobileLocators.LINE_COLOR_PINK}
        mobile_phase_color_dictionary = {
            "A": MobileLocators.LINE_COLOR_INFO_LABEL_A,
            "B": MobileLocators.LINE_COLOR_INFO_LABEL_B,
            "C": MobileLocators.LINE_COLOR_INFO_LABEL_C,
            "D": MobileLocators.LINE_COLOR_INFO_LABEL_D}
        self.wait_element_to_be_clickable(mobile_phase_color_dictionary[mobile_phase], self.wait_time)
        self.tap(mobile_phase_color_dictionary[mobile_phase])
        line_color_locator = line_color_text_dictionary[line_color]
        self.wait_element_to_be_clickable(line_color_locator, self.wait_time)
        self.tap(line_color_locator)

    def set_default_color(self, mobile_phase):
        mobile_phase_volume_dictionary = {
            "A": MobileLocators.LINE_COLOR_INFO_LABEL_A,
            "B": MobileLocators.LINE_COLOR_INFO_LABEL_B,
            "C": MobileLocators.LINE_COLOR_INFO_LABEL_C,
            "D": MobileLocators.LINE_COLOR_INFO_LABEL_D}
        self.wait_element_to_be_clickable(mobile_phase_volume_dictionary[mobile_phase], self.wait_time)
        self.tap(mobile_phase_volume_dictionary[mobile_phase])
        self.tap(MobileLocators.SET_DEFAULT)

    def set_toggle_status(self, wash_solvent, toggle_status):
        toggle_dict = {'A': MobileLocators.BOTTLE_TOGGLE_A,
                       'B': MobileLocators.BOTTLE_TOGGLE_B,
                       'C': MobileLocators.BOTTLE_TOGGLE_C,
                       'D': MobileLocators.BOTTLE_TOGGLE_D,
                       }
        self.wait_for_element_visibility(self.wait_time, toggle_dict[wash_solvent])
        self.set_toggle_button(toggle_dict[wash_solvent], toggle_status)
        self.logger.info(f"Successfully Set The {wash_solvent} Toggle Value As {toggle_status}")

    def get_toggle_status(self, mobile_phase):
        toggle_dict = {'A': MobileLocators.BOTTLE_TOGGLE_A,
                       'B': MobileLocators.BOTTLE_TOGGLE_B,
                       'C': MobileLocators.BOTTLE_TOGGLE_C,
                       'D': MobileLocators.BOTTLE_TOGGLE_D,
                       }
        self.wait_for_element_visibility(self.wait_time, toggle_dict[mobile_phase])
        return self.is_toggle_component_enabled(toggle_dict[mobile_phase])

    def cancel_reset(self):
        self.tap(MobileLocators.CANCEL_RESET)

    def set_color_for_mobile_phase(self, mobile_phase, color):
        self.tap_mobile_phase_tab(mobile_phase)
        self.set_toggle_status(mobile_phase, "true")
        self.select_line_color(mobile_phase, color)

    def tap_reset_button(self):
        self.wait_element_to_be_clickable(MobilePhaseConfigurationSettingsScreenLocators.RESET,
                                          self.wait_time)
        self.tap(MobilePhaseConfigurationSettingsScreenLocators.RESET)
