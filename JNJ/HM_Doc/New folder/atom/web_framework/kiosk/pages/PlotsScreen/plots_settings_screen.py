"""
File_Name: plots_screen.py
Desc: This file contains specific user actions on the elements in the plots screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/03/2021

"""
import time

from utilities.logger import Logger
from utilities.string_utility import remove_substring
from web_framework.kiosk.pages.Locators.Plots.plots_screen_locators import (PlotsSettingsScreenLocators as pssl, PlotsSettingsScreenLocators)
from web_framework.kiosk.pages.PlotsScreen.plots_settings_screen_locators_lookup import PlotsSettingsLookup
from web_framework.kiosk.pages.base_page import BasePage


class PlotsSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.previous_plots_selected = []
        self.previous_plots_color_selected = []

    def add_previous_plot(self, current_plot):
        self.previous_plots_selected += [current_plot]
        self.logger.info(f"previous_plots_selected=={self.previous_plots_selected}")

    def add_previous_plot_color(self, current_plot_color):
        self.previous_plots_color_selected += [current_plot_color]

    def validate_plot_settings_screen(self):
        locator = pssl.TIME_WINDOW_HEADER
        screen_name = "plots settings screen"
        self.wait_for_element_load(locator, self.wait_time)
        self.validate_screen(locator, screen_name, self.wait_time)

    def select_time_window(self, time):

        time_window_text_dictionary = PlotsSettingsLookup.time_window_text_dictionary
        if time in time_window_text_dictionary:
            locator = time_window_text_dictionary[time]
            self.tap(locator)
            return

        assert False, f"Unexpected flow path => {time}"

    def is_time_wheel_visible(self):
        return self.is_displayed(pssl.TIME_WINDOW_COMPONENT)

    def select_more_action_icons(self, number):
        action_icons_text_dictionary = PlotsSettingsLookup.action_icons_text_dictionary

        if number in action_icons_text_dictionary:
            locator = action_icons_text_dictionary[number]
            is_menus_visible = self.is_menus_visible(locator)
            if not is_menus_visible:
                self.tap(locator)
            return

        assert False, f"Unexpected flow path => {number}"

    def tap_plots_settings_icons(self, icon_number):
        settings_icons_text_dictionary = PlotsSettingsLookup.settings_icons_text_dictionary

        if icon_number in settings_icons_text_dictionary:
            locator = settings_icons_text_dictionary[icon_number]
            self.tap(locator)
            return

        assert False, f"Unexpected flow path => {icon_number}"

    def is_menus_visible(self, locator):
        option_state_element = self.get_element(locator)
        option_selected_state = option_state_element.get_attribute("class")
        self.logger.info(f"The element   {option_state_element} is enable is class {option_selected_state}")

        option_selected_state = option_selected_state.find("active")

        if option_selected_state == -1:
            return False
        return True

    def select_plot_options(self, plot_option):
        plots_color_dictionary = PlotsSettingsLookup.plots_options_dictionary
        locator = plots_color_dictionary[plot_option]
        self.wait_for_element_load(locator, self.wait_time)
        self.tap(locator)

    def validate_more_action_icon_extended(self, number):
        action_icons_text_dictionary = PlotsSettingsLookup.action_icons_text_dictionary
        for plots in action_icons_text_dictionary:
            locator = action_icons_text_dictionary[plots]

            if plots == number:
                assert self.is_menus_visible(locator)
                self.logger.info(f"inside the if function")

            else:
                self.logger.info(f"inside the else function")
                assert self.is_menus_visible(locator) is False

    def validate_action_icons_retracted(self):
        action_icons_text_dictionary = PlotsSettingsLookup.action_icons_text_dictionary
        for plots in action_icons_text_dictionary:
            locator = action_icons_text_dictionary[plots]
            self.logger.info(f"For {plots} the icon visibility is {self.is_menus_visible(locator)}")
            assert self.is_menus_visible(locator) is False

    def is_play_button_displayed(self):
        plots_text_element = self.get_element(PlotsSettingsScreenLocators.CENTER_PLAY_PAUSE_ELEMENT)
        button_image_displayed = plots_text_element.get_attribute("ng-reflect-svg-icon")

        if button_image_displayed == "ics-img-pause":
            return False
        else:
            return True

    def get_selected_time_window_options(self):
        actual_time = self.get_text(PlotsSettingsScreenLocators.CUSTOM_TIME_WINDOW)
        string_to_remove = "\nCustom"
        current_time_selected = remove_substring(actual_time, string_to_remove)
        return current_time_selected

    def tap_toggle_button_on(self, locator):
        is_toggle_button_turn_on = self.is_toggle_button_enabled(locator)

        if not is_toggle_button_turn_on:
            self.logger.info("*** Toggle button is not enabled")
            self.tap_toggle_button(locator)

        else:
            self.logger.info("*** Toggle button is enabled")
            time.sleep(1)
        assert self.is_toggle_button_enabled(locator), 'Toggle button is switched off'

    def tap_toggle_button_off(self, locator):
        is_toggle_button_turn_on = self.is_toggle_button_enabled(locator)

        if is_toggle_button_turn_on:
            self.logger.info("*** Toggle button is not enabled")
            self.tap_toggle_button(locator)

        else:
            self.logger.info("*** Toggle button is enabled")
            time.sleep(1)
        assert not self.is_toggle_button_enabled(locator), 'Toggle button is switched off'

    def tap_toggle_button(self, locator):
        self.tap(locator)

    def select_plot_color(self, color):
        color_dictionary = PlotsSettingsLookup.plots_color_dictionary
        self.scroll_to_spinner_options(color, color_dictionary)

    def turn_off_plots(self):
        self.tap(PlotsSettingsScreenLocators.PLOT_ONE_TAB)
        self.tap_toggle_button_off(PlotsSettingsScreenLocators.PLOT_ONE_TOGGLE_BUTTON)
        self.tap(PlotsSettingsScreenLocators.PLOT_TWO_TAB)
        self.tap_toggle_button_off(PlotsSettingsScreenLocators.PLOT_TWO_TOGGLE_BUTTON)
        self.tap(PlotsSettingsScreenLocators.PLOT_THREE_TAB)
        self.tap_toggle_button_off(PlotsSettingsScreenLocators.PLOT_THREE_TOGGLE_BUTTON)
        self.tap(PlotsSettingsScreenLocators.PLOT_FOUR_TAB)
        self.tap_toggle_button_off(PlotsSettingsScreenLocators.PLOT_FOUR_TOGGLE_BUTTON)

    def set_default_hour(self):
        current_state = self.is_default_value_button_disabled(PlotsSettingsScreenLocators.DEFAULT_TIME_BUTTON)
        self.logger.info(f"current_state ==>> {current_state}")

        if not current_state:
            self.tap(PlotsSettingsScreenLocators.DEFAULT_TIME_BUTTON)
        custom_time = self.get_selected_time_window_options()
        self.logger.info(f"custom_time ==>>{custom_time}")
        assert custom_time == "1 h", f"custom_time ===>>{custom_time} "
