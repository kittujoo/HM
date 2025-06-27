"""
File_Name: system_leak_test_setup_screen.py
Desc: This file contains specific user action on all the screen in the leak test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022
__author__ = "Sharmila Vairamani" Changed the scripts to fcs changes - 06/09/2023
__modified = "Tyler Prada" Added pressure unit functions 6/22/23
__modified = "Supreet Sethi" Added accumulator target pressure unit hint function 12/07/2023
"""
import re
import time

from web_framework.kiosk.pages.Health.Models.leak_test_summary import LeakTestSummaryDetails
from utilities.logger import Logger
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_flow_locators_lookup import SystemLeakTestSettingsLookup
from web_framework.kiosk.pages.Locators.Health.leak_test_workflow_locators import LeakTestWorkflowLocators
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import (SystemLeakTestWorkflowSetupLocators,
                                                                                 SystemLeakTestWorkflowLocators)
from web_framework.kiosk.pages.base_page import BasePage


class SystemLeakTestSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_summary_details = None

    def tap_back_icon(self):
        self.tap(LeakTestWorkflowLocators.BACK_BUTTON)

    def validate_welcome_screen(self):
        locator = LeakTestWorkflowLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_selection_screen(self):
        locator = SystemLeakTestWorkflowSetupLocators.SETUP_SOLVENT_LINE_BANNER
        screen_name = "Solvent line selection screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_test_selection_screen(self):
        locator = SystemLeakTestWorkflowSetupLocators.SETUP_TEST_OPTIONS_BANNER
        screen_name = "Test type selection screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_pressure_setup_screen(self):
        locator = SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_HEADER
        screen_name = "pressure setup screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_custom_options_screen(self):
        locator = SystemLeakTestWorkflowSetupLocators.SETUP_CUSTOM_OPTIONS_BANNER
        screen_name = "Custom options selection screen for the leak test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def select_leak_test_solvent_line(self, solvent_line: str):
        if solvent_line in SystemLeakTestSettingsLookup.solvent_line_dictionary:
            locator = SystemLeakTestSettingsLookup.solvent_line_dictionary[solvent_line]
            self.tap(locator)
            return
        assert False, f"Invalid solvent => {solvent_line}"

    def select_standard_test_mode(self):
        self.tap(SystemLeakTestWorkflowSetupLocators.STANDARD_TEST_PANEL)

    def select_custom_test_mode(self):
        self.tap(SystemLeakTestWorkflowSetupLocators.CUSTOM_TEST_PANEL)

    def select_leak_test_settings(self, settings_value, settings_locator_lookup_dict):
        settings_locator_lookup_dictionary = settings_locator_lookup_dict

        if settings_value in settings_locator_lookup_dictionary:
            locator = settings_locator_lookup_dictionary[settings_value]
            self.tap(locator)
            return

        assert False, f"Unexpected settings_value => {settings_value}"

    def get_selected_solvent_line(self):
        for items in SystemLeakTestSettingsLookup.solvent_line_dictionary:
            locator = SystemLeakTestSettingsLookup.solvent_line_dictionary[items]
            self.logger.info(f"%%%%%%%%%%%%%locator{locator}")
            if self.is_radio_button_selected(locator):
                active_button_element = self.get_element(locator)
                line_selected = active_button_element.get_attribute("ng-reflect-value")
                self.logger.info(f"line_selected ===>> {line_selected}")
                line_selected = line_selected[12]
                return line_selected

    def get_selected_options(self, dict):

        self.logger.info(f"%%%%%%%%%%%%%inside the loop ")
        for items in dict:
            locator = dict[items]
            if self.is_active(locator):
                selected_option = self.get_text(locator)
                self.logger.info(f"%%%%%%%%%%%%%inside the loop {selected_option}")
                return selected_option

    def get_accumulator_target_pressure_unit(self):
        accumulator_text = self.get_text(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_HEADER)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", accumulator_text)
        return pressure_unit[1]

    def get_accumulator_target_pressure_hint_unit(self):
        target_hint_text = self.get_text(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_PRESSURE_HINT)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", target_hint_text)
        return pressure_unit[1]

    def get_primary_target_pressure_unit(self):
        primary_text = self.get_text(SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_HEADER)
        pressure_unit = re.search("(bar|psi|MPa|kPa)", primary_text)
        return pressure_unit[1]

    def get_leak_test_selected_summary_details(self, solvent_line, acc_pressure, end_point, prime_option):

        self.select_leak_test_solvent_line(solvent_line)
        time.sleep(2)  # time for the animation to complete
        selected_solvent = self.get_selected_solvent_line()
        self.tap_next_button()

        selected_accum_target_pressure, selected_primary_target_pressure = self.add_accumulator_pressure(
            acc_pressure)

        self.tap_next_button()
        self.logger.info("User selects the end point option")
        time.sleep(2)  # time for the animation to complete
        self.select_leak_test_settings(end_point, SystemLeakTestSettingsLookup.end_point_text_dictionary)
        selected_end_point_option = self.get_selected_options(SystemLeakTestSettingsLookup.end_point_text_dictionary)
        self.logger.info("User selects the prime option")
        time.sleep(2)  # time for the animation to complete
        self.select_leak_test_settings(prime_option, SystemLeakTestSettingsLookup.prime_options_text_dictionary)
        selected_prime_option = self.get_selected_options(SystemLeakTestSettingsLookup.prime_options_text_dictionary)
        self.logger.info("User selects the retry option ")
        time.sleep(2)  # time for the animation to complete
        self.tap_next_button()

        leak_test_summary_details = LeakTestSummaryDetails(selected_solvent, selected_accum_target_pressure,
                                                           selected_primary_target_pressure,
                                                           selected_end_point_option, selected_prime_option)
        return leak_test_summary_details

    def add_primary_and_accum_pressure(self, acc_pressure, primary_pressure):
        self.logger.info("When the primary pressure  and accumulator is added")
        self.select_check_box(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_CHECKBOX)
        self.enter_value_for_specific_module(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD,
                                             acc_pressure)
        self.select_check_box(SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_CHECKBOX)
        self.enter_value_for_specific_module(SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_FIELD,
                                             primary_pressure)
        selected_primary_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_FIELD)
        selected_primary_target_pressure = int(selected_primary_target_pressure)
        selected_accum_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD)
        selected_accum_target_pressure = int(selected_accum_target_pressure)
        return selected_accum_target_pressure, selected_primary_target_pressure

    def add_primary_pressure(self, primary_pressure):
        self.logger.info("When the accumulator pressure is not added")
        self.select_check_box(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_CHECKBOX)
        self.clear_num_pad_entries(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD)
        self.deselect_check_box(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_CHECKBOX)
        self.logger.info("When the primary pressure is  added")
        self.select_check_box(SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_CHECKBOX)
        self.enter_value_for_specific_module(SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_FIELD,
                                             primary_pressure)
        selected_primary_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_FIELD)
        selected_primary_target_pressure = int(selected_primary_target_pressure)
        selected_accum_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD)
        return selected_accum_target_pressure, selected_primary_target_pressure

    def add_accumulator_pressure(self, acc_pressure):
        self.clear_num_pad_entries(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD)
        self.enter_value_for_specific_module(SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD,
                                             acc_pressure)
        selected_primary_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.PRIMARY_TARGET_FIELD)
        selected_accum_target_pressure = self.get_entered_value(
            SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD)
        selected_accum_target_pressure = int(selected_accum_target_pressure)
        selected_primary_target_pressure = int(selected_primary_target_pressure)
        return selected_accum_target_pressure, selected_primary_target_pressure

    def set_selected_summary_details(self, leak_test_summary_details):
        self.selected_summary_details = leak_test_summary_details

    def get_selected_summary_details(self):
        return self.selected_summary_details

    def get_welcome_paragraph_text(self):
        return [self.get_text(SystemLeakTestWorkflowLocators.WELCOME_PARA_ONE),
                self.get_text(SystemLeakTestWorkflowLocators.WELCOME_PARA_TWO),
                self.get_text(SystemLeakTestWorkflowLocators.WELCOME_PARA_THREE)]

    def get_better_results_text(self):
        return [self.get_text(SystemLeakTestWorkflowLocators.POINT_ONE_FOR_BETTER_RESULTS_TEXT),
                self.get_text(SystemLeakTestWorkflowLocators.POINT_TWO_FOR_BETTER_RESULTS_TEXT),
                self.get_text(SystemLeakTestWorkflowLocators.POINT_THREE_FOR_BETTER_RESULTS_TEXT)]
