"""
file_Name: solvent_configuration_screen.py
Desc: This file contains specific user actions on the elements in the system screen which includes
      solvent configuration
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 12/15/2021

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.SolventManager.mobile_phase_configuration_settings_locators import MobilePhaseConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.Home.SolventManager.solvent_configuration_locators import SolventConfigurationsScreenLocators
from selenium.webdriver.support.color import Color
from web_framework.kiosk.pages.base_page import BasePage


class SolventConfigurationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_solvent_configuration_screen(self):
        locator = SolventConfigurationsScreenLocators.NEEDLE_WASH_TAB
        screen_name = "Solvent configuration settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_solvent_phase_tab(self, solvent):
        solvent_phase_text_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_TAB,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_TAB}

        locator = solvent_phase_text_dictionary[solvent]
        self.tap(locator)

    def set_toggle_status(self, wash_solvent, toggle_status):
        toggle_dict = {'Needle_Wash': SolventConfigurationsScreenLocators.NEEDLE_WASH_TOGGLE,
                       'Seal_Wash': SolventConfigurationsScreenLocators.SEAL_WASH_TOGGLE
                       }
        self.wait_for_element_visibility(self.wait_time, toggle_dict[wash_solvent])
        self.set_toggle_button(toggle_dict[wash_solvent], toggle_status)
        self.logger.info(f"Successfully Set The {wash_solvent} Toggle Value As {toggle_status}")

    def select_bottle_volume(self, wash_solvent, bottle_volume):
        bottle_volume_text_dictionary = {
            "2L": MobilePhaseConfigurationSettingsScreenLocators.SOLVENT_BOTTLE_2L_OPTION,
            "4L": MobilePhaseConfigurationSettingsScreenLocators.SOLVENT_BOTTLE_4L_OPTION,
            "5L": MobilePhaseConfigurationSettingsScreenLocators.SOLVENT_BOTTLE_5L_OPTION}
        mobile_phase_volume_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_VOLUME,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_VOLUME}

        self.tap(mobile_phase_volume_dictionary[wash_solvent])
        bottle_volume_locator = bottle_volume_text_dictionary[bottle_volume]
        self.scroll_to_view(bottle_volume_locator)
        self.tap(bottle_volume_locator)

    def select_line_color(self, wash_solvent, line_color):
        line_color_text_dictionary = {
            "blue": MobilePhaseConfigurationSettingsScreenLocators.LINE_COLOR_BLUE,
            "red": MobilePhaseConfigurationSettingsScreenLocators.LINE_COLOR_RED,
            "green": MobilePhaseConfigurationSettingsScreenLocators.LINK_COLOR_GREEN,
            "pink": MobilePhaseConfigurationSettingsScreenLocators.LINE_COLOR_PINK}
        line_color_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_COLOR,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_COLOR}

        self.wait_element_to_be_clickable(line_color_dictionary[wash_solvent], self.wait_time)
        self.tap(line_color_dictionary[wash_solvent])
        line_color_locator = line_color_text_dictionary[line_color]
        self.tap(line_color_locator)

    def get_volume(self, wash_solvent):
        mobile_phase_text_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_VOLUME_TAG,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_VOLUME_TAG}
        return self.get_text(mobile_phase_text_dictionary[wash_solvent])

    def get_line_color(self, wash_solvent):
        mobile_phase_text_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_LINE_COLOR,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_LINE_COLOR}
        actual_color = Color.from_string(self.find_element(mobile_phase_text_dictionary[wash_solvent]).value_of_css_property('background-color'))
        return actual_color

    def get_toggle_status(self, wash_solvent):
        toggle_dict = {'Needle_Wash': SolventConfigurationsScreenLocators.NEEDLE_WASH_TOGGLE,
                       'Seal_Wash': SolventConfigurationsScreenLocators.SEAL_WASH_TOGGLE
                       }
        self.wait_for_element_visibility(self.wait_time, toggle_dict[wash_solvent])
        return self.is_toggle_component_enabled(toggle_dict[wash_solvent])

    def set_default_color(self, wash_solvent):
        line_color_dictionary = {
            "Needle_Wash": SolventConfigurationsScreenLocators.NEEDLE_WASH_COLOR,
            "Seal_Wash": SolventConfigurationsScreenLocators.SEAL_WASH_COLOR}
        self.wait_element_to_be_clickable(line_color_dictionary[wash_solvent], self.wait_time)
        self.tap(line_color_dictionary[wash_solvent])
        self.tap(SolventConfigurationsScreenLocators.SET_DEFAULT)

    def set_color_for_wash_solvent(self, wash_solvent, color):
        self.tap_solvent_phase_tab(wash_solvent)
        self.set_toggle_status(wash_solvent, "true")
        self.select_line_color(wash_solvent, color)
