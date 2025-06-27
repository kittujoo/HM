"""
File_Name: plots_screen.py
Desc: This file contains specific user actions on the elements in the plots screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/08/2021
__modified__  = "Sharmila Vairamani" Added validation function and is_play_button_displayed 05/16/2021
__modified__  = "Sharmila Vairamani" Added is_play_button_displayed 05/16/2021

"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.plots import PlotsConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Plots.plots_screen_locators import (PlotScreenLocators as psl, PlotScreenLocators)
from web_framework.kiosk.pages.base_page import BasePage


class PlotsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.current_plots_selected = []
        self.current_plots_color_selected = []

        self.time_window_text_dictionary = {
            "Five": psl.FIVE_MINUTE_TIME_WINDOW,
            "Fifteen": psl.FIFTEEN_MINUTE_TIME_WINDOW,
            "Custom": psl.CUSTOM_TIME_WINDOW
        }

        self.color_code_dictionary = {
            "Red": PlotsConstants.Red,
            "Blue": PlotsConstants.Blue,
            "Orange": PlotsConstants.Orange,
            "Pink": PlotsConstants.Pink,
            "Yellow": PlotsConstants.Yellow,
            "Green": PlotsConstants.Green

        }

    def add_current_plots_selected(self, current_plot):
        self.current_plots_selected += [current_plot]
        self.logger.info(f"current_plots_selected=={self.current_plots_selected}")

    def add_current_plot_color(self, current_plot_color):
        self.current_plots_color_selected += [current_plot_color]

    def get_current_plots(self):
        return self.current_plots_selected

    def get_current_plots_color(self):
        return self.current_plots_color_selected

    def get_previous_plots(self, page_type):
        return page_type.previous_plots_selected

    def get_previous_plots_color(self, page_type):
        return page_type.previous_plots_color_selected

    def clear_plots_list(self, page_type):
        page_type.previous_plots_selected.clear()

    def clear_plots_color_list(self, page_type):
        page_type.previous_plots_color_selected.clear()

    def tap_settings_icon(self):
        self.tap(psl.SETTINGS_ICON)

    def tap_play_pause_icon(self):
        self.tap(psl.PLAY_PAUSE_BUTTON)

    def select_time_window(self, time):
        if time in self.time_window_text_dictionary:
            locator = self.time_window_text_dictionary[time]
            self.tap(locator)
            return

        assert False, f"Unexpected flow path => {time}"

    def get_start_time_window_value(self):
        return self.get_temperature(psl.TIME_BEFORE_DECIMAL, psl.TIME_AFTER_DECIMAL)

    def get_end_time_window_value(self):
        return self.get_text(psl.TIME_NOW_VALUE)

    def play_plots(self):
        is_plots_playing = self.is_plot_playing()

        if is_plots_playing:
            self.logger.info("***The plots are already in playing state")

        else:
            self.logger.info("***User taps the play pause button")
            self.tap_play_pause_icon()

    def is_plot_playing(self):
        plots_text = self.get_text(psl.PLAY_PAUSE_ELEMENT)
        if plots_text == "PAUSE":
            return True

    def pause_plots(self):
        # time.sleep(1)
        is_plots_playing = self.is_plot_playing()

        if is_plots_playing:
            self.tap_play_pause_icon()
        else:
            self.logger.info("The plots is already in paused state")

    def is_option_selected(self, locator):
        option_state_element = self.get_element(locator)
        option_selected_state = option_state_element.get_attribute("class")
        self.logger.info(f"The element   {option_state_element} is enable is class {option_selected_state}")

        option_selected_state = option_selected_state.find("active")

        if option_selected_state == -1:
            return False
        return True

    def validate_time_option_selected(self, expected_time_window):

        for actual_time_window in self.time_window_text_dictionary:
            locator = self.time_window_text_dictionary[actual_time_window]
            is_time_window_enabled = self.is_option_selected(locator)
            if is_time_window_enabled:
                assert actual_time_window == expected_time_window, f"The time window option is not as expected. \
                                                                        Expected Time Window: {expected_time_window}. Actual Time Window: {actual_time_window}"
            else:
                self.logger.debug(f"The {actual_time_window} is not enabled.")

    def validate_plot_screen(self):
        locator = PlotScreenLocators.SETTINGS_ICON
        screen_name = "plots screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_plot_graph_screen(self):
        locator = PlotScreenLocators.PLOTS_GRAPH
        screen_name = "plots screen"
        self.validate_screen(locator, screen_name, WaitTimeConstants.PlotsTestWait)

    def validate_time_window_component(self):
        locator = PlotScreenLocators.TIME_WINDOW_COMPONENT
        screen_name = "plots screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def is_play_button_displayed(self):
        plots_text_element = self.get_element(psl.PLAY_PAUSE_ELEMENT)
        button_image_displayed = plots_text_element.get_attribute("ng-reflect-text")

        if button_image_displayed == PlotsConstants.PauseButtonText:
            return False
        else:
            return True

    def validate_color(self, actual_plots_color, expected_colour):

        for actual_colour, expected_colour in zip(actual_plots_color, expected_colour):

            if actual_colour in self.color_code_dictionary:
                color_code = self.color_code_dictionary[actual_colour]
                self.logger.info(f"inside the validate_color====={expected_colour}")
                assert color_code == expected_colour, f"The actual color is {color_code}, The expected =={expected_colour}"
            else:
                assert False, f"The given color is not in the list=={actual_colour}"

    def get_color_code_list(self, locator):
        links = []
        no_of_plots = self.find_elements(locator)
        self.logger.info(f'no_of_elements==={len(no_of_plots)}')
        plots = int(len(no_of_plots))
        assert plots != 0, f"The plots are not displayed, no_of_graphs==>>{plots}"

        for plot in no_of_plots:
            link = plot.value_of_css_property('fill')
            self.logger.info(f"color_link_text ==={link}")
            actual_color = TypeConverter.to_str(link)
            actual_color = actual_color[4::]
            actual_color = actual_color.rstrip(")")
            actual_color = TypeConverter.to_str(actual_color)
            links.append(actual_color)
        return links

    def validate_graph(self, locator):
        expected_graphs = self.find_elements(locator)
        no_of_expected_graphs = len(expected_graphs)
        self.logger.info(f'no_of_expected_graphs==={no_of_expected_graphs}')

        assert no_of_expected_graphs != 0, f"The plots are not displayed, no_of_graphs==>>{expected_graphs}"
        no_of_actual_graphs = 0
        start_time = time.time()
        while time.time() - start_time < 30:
            try:
                actual_graphs = self.find_elements(PlotScreenLocators.GRAPH_STATE)
                no_of_actual_graphs = len(actual_graphs)
                self.logger.info(f'no_of_actual_graphs==={no_of_actual_graphs}')
                if no_of_expected_graphs == no_of_actual_graphs:
                    break
            except:
                self.logger.info(f'Inside the exception')
                time.sleep(5)
        assert no_of_actual_graphs != 0, f" The graph is not visible"

        assert no_of_actual_graphs == no_of_expected_graphs, f" Expected graphs =>{no_of_expected_graphs} acutal {no_of_actual_graphs}"
