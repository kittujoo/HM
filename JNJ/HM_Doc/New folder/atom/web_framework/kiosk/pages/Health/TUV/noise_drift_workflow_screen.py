"""
File_Name: noise_drift_workflow.py
Desc: This file contains specific user actions on screens within the noise & drift workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/20/22
__modified__ = "Sharmila Vairamani" updates the locators - 6/13/2022
"""
import time

from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Health.Models.noise_drift_summary import (NoiseDriftSolventDetails, NoiseDriftWavelengthDetails,
                                                                         NoiseDriftDataFrequencyDetails)
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.Health.TUV.noise_drift_workflow_locators import (NoiseDriftSetupLocators, NoiseDriftWelcomeLocators,
                                                                                         NoiseDriftWorkflowLocators)
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import SolventCompositionTabScreen as solcomp
from web_framework.kiosk.pages.base_page import BasePage


class NoiseDriftWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_solvent_details = None
        self.selected_wavelength_details = None
        self.selected_frequency_rate_details = None

    def validate_flow_rate_screen(self):
        locator = NoiseDriftSetupLocators.SETUP_FLOW_BANNER
        screen_name = "flow screen for noise & drift test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_wavelength_screen(self):
        locator = NoiseDriftSetupLocators.SETUP_WAVELENGTH_BANNER
        screen_name = "wavelength screen for noise & drift test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_data_rate_screen(self):
        locator = NoiseDriftSetupLocators.SETUP_DATA_RATE_BANNER
        screen_name = "data rate screen for noise & drift test"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(NoiseDriftWelcomeLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(NoiseDriftWelcomeLocators.WELCOME_PARAGRAPH_TWO),
                self.get_text(NoiseDriftWelcomeLocators.WELCOME_PARAGRAPH_THREE)]

    def get_caution_paragraph_text(self):
        return [self.get_text(NoiseDriftSetupLocators.CAUTION_PARAGRAPH_ONE),
                self.get_text(NoiseDriftSetupLocators.CAUTION_PARAGRAPH_TWO),
                self.get_text(NoiseDriftSetupLocators.CAUTION_PARAGRAPH_THREE)]

    def tap_wavelength_option(self, wavelength_option):
        wavelength_option_dictionary = {
            "single": NoiseDriftSetupLocators.SINGLE_CHANNEL_OPTION,
            "dual": NoiseDriftSetupLocators.DUAL_CHANNEL_OPTION
        }

        if wavelength_option in wavelength_option_dictionary:
            self.tap(wavelength_option_dictionary[wavelength_option])
            return

        assert False, f"Unexpected wavelength channel option => {wavelength_option}"

    def tap_filter_constant_option(self, filter_time_constant):
        filter_constant_option_dictionary = {
            "Slow": NoiseDriftSetupLocators.SLOW_FILTER_OPTION,
            "Normal": NoiseDriftSetupLocators.NORMAL_FILTER_OPTION,
            "Fast": NoiseDriftSetupLocators.FAST_FILTER_OPTION
        }

        if filter_time_constant in filter_constant_option_dictionary:
            self.tap(filter_constant_option_dictionary[filter_time_constant])
            return

        assert False, f"Unexpected filter time option => {filter_time_constant}"

    def reset_composition(self):
        reset_composition_element = self.get_element(NoiseDriftSetupLocators.RESET_COMPOSITION_BUTTON)
        reset_composition_button_disable = reset_composition_element.get_attribute("ng-reflect-disabled")
        reset_composition_button_disable = TypeConverter.to_bool(reset_composition_button_disable)
        self.logger.info(f"reset_composition_button_disable ====>>>>{reset_composition_button_disable}")
        if not reset_composition_button_disable:
            self.wait_element_to_be_clickable(NoiseDriftSetupLocators.RESET_COMPOSITION_BUTTON, self.wait_time)
            self.tap(NoiseDriftSetupLocators.RESET_COMPOSITION_BUTTON)
        else:
            self.logger.info(" The solvent composition button is disabled")
        if self.selected_solvent_details:
            self.selected_solvent_details.solvent_a = "100.0"
            self.selected_solvent_details.solvent_b = "0.0"
            self.selected_solvent_details.solvent_c = "0.0"
            self.selected_solvent_details.solvent_d = "0"
            self.set_selected_solvent_details(self.selected_solvent_details)

    def selected_and_get_solvent_details(self, flow_rate, line_1, line_2, line_3, line_4):
        self.reset_composition()
        solvent_line_1 = SolventLine.parse(line_1)
        solvent_line_2 = SolventLine.parse(line_2)
        solvent_line_3 = SolventLine.parse(line_3)
        solvent_line_4 = SolventLine.parse(line_4)
        solvent_composition = self.build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3,
                                                             solvent_line_4)
        self.logger.info(f"solvent_composition====>>>{solvent_composition}")
        self.enter_composition(solvent_composition)
        entered_solvent_a = self.get_composition(
            NoiseDriftSetupLocators.SOLVENT_A_EDIT_FIELD)
        entered_solvent_b = self.get_composition(
            NoiseDriftSetupLocators.SOLVENT_B_EDIT_FIELD)
        entered_solvent_c = self.get_composition(
            NoiseDriftSetupLocators.SOLVENT_C_EDIT_FIELD)
        entered_solvent_d = self.get_composition(
            NoiseDriftSetupLocators.SOLVENT_D_EDIT_FIELD)

        noise_drifts_solvent_details = NoiseDriftSolventDetails(flow_rate, entered_solvent_a,
                                                                entered_solvent_b,
                                                                entered_solvent_c, entered_solvent_d)
        return noise_drifts_solvent_details

    def build_solvent_composition(self, solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4):
        """
        This function builds solvent composition for the given solvent line
        :param solvent_line_1: parsed data from the feature file
        :param solvent_line_2: parsed data from the feature file
        :param solvent_line_3: parsed data from the feature file
        :param solvent_line_4: parsed data from the feature file
        :return: solvent_composition
        """
        solvent_composition = SolventComposition()
        solvent_composition.add(solvent_line_1)
        solvent_composition.add(solvent_line_2)
        solvent_composition.add(solvent_line_3)
        solvent_composition.add(solvent_line_4)
        return solvent_composition

    def enter_composition(self, solvent_composition):

        solvent_list = solvent_composition.get_solvent_lines()
        lock_icon_locator = ""
        edit_field_locator = ""
        for solvent in solvent_list:
            if solvent.line_id == "A":
                self.logger.info(f"The solvent composition for A is entered")
                edit_field_locator = solcomp.SOLVENT_A_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_A_LOCK_ICON
                # hint_locator = solcomp.SOLVENT_A_HINT_LOCATOR

            if solvent.line_id == "B":
                self.logger.info(f"The solvent composition for B is entered")
                edit_field_locator = solcomp.SOLVENT_B_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_B_LOCK_ICON
                # hint_locator = solcomp.SOLVENT_B_HINT_LOCATOR

            if solvent.line_id == "C":
                edit_field_locator = solcomp.SOLVENT_C_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_C_LOCK_ICON

            if solvent.line_id == "D":
                edit_field_locator = solcomp.SOLVENT_D_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_D_LOCK_ICON

            self.set_composition_and_edit_field_lock(edit_field_locator,
                                                     solvent.percentage_value)

    def get_solvent_line(self, line_id, percentage_value, line_locked):
        """
        This function constructs solvent line with the given input data
        :param line_id: The line id
        :param percentage_value: composition value
        :param line_locked: locked or not
        :return:
        """
        solvent_line = SolventLine(line_id, percentage_value)
        solvent_line.line_id = line_id
        solvent_line.percentage_value = percentage_value
        solvent_line.locked = line_locked
        return solvent_line

    def set_composition_and_edit_field_lock(self, locator, composition):
        self.set_composition(composition, locator)

    def set_composition(self, composition, locator):

        self.logger.info("The lock is already unlocked")
        self.tap(locator)
        self.enter_value_for_specific_module(locator, composition)

    def set_edit_field_lock(self, lock_state, lock_locator):
        self.logger.info(f"lock state ++++++>>>>>>>> {lock_state}")
        lock_state = TypeConverter.to_bool(lock_state)
        currently_locked = self.is_edit_field_locked(lock_locator)
        self.logger.info(f"lock currently_locked ++++++>>>>>>>> {currently_locked}")
        self.toggle_switch("Leak sensor monitor", lock_locator,
                           currently_locked, lock_state)

    def is_edit_field_locked(self, lock_locator):
        edit_field_lock = self.get_element(lock_locator)
        lock_icon_class_string = edit_field_lock.get_attribute("ng-reflect-svg-icon")
        self.logger.info(f"The lock icon class attribute  {lock_icon_class_string}")
        lock_icon_value = "unlocked"

        if lock_icon_value in lock_icon_class_string:
            return False
        else:
            return True

    def get_composition(self, locator):
        return self.get_user_input_text(locator)

    def set_selected_solvent_details(self, noise_drifts_solvent_details):
        self.selected_solvent_details = noise_drifts_solvent_details

    def get_selected_solvent_details(self):
        return self.selected_solvent_details

    def select_and_get_dual_wavelength(self, channel_a_value, channel_b_value):
        if channel_a_value == "":
            self.logger.info("When the wavelength is channel B")

            self.tap(NoiseDriftSetupLocators.CHANNEL_B_PANEL)
            self.set_spinner_value(NoiseDriftSetupLocators.WAVELENGTH_PICKER, channel_b_value)
            noise_drift_wavelength_details = NoiseDriftWavelengthDetails(channel_a_value, channel_b_value)

        elif channel_b_value == "":
            self.logger.info("When the wavelength is channel A")
            self.tap(NoiseDriftSetupLocators.CHANNEL_A_PANEL)
            self.set_spinner_value(NoiseDriftSetupLocators.WAVELENGTH_PICKER, channel_a_value)
            noise_drift_wavelength_details = NoiseDriftWavelengthDetails(channel_a_value, channel_b_value)


        else:
            self.logger.info("When the wavelngth is channel B and A")
            self.logger.info(f"When the wavelngth is channel B ==={channel_a_value}, channel_b_value ==>>{channel_b_value}")
            self.tap(NoiseDriftSetupLocators.CHANNEL_A_PANEL)
            self.set_spinner_value(NoiseDriftSetupLocators.WAVELENGTH_PICKER, channel_a_value)

            self.tap(NoiseDriftSetupLocators.CHANNEL_B_PANEL)
            self.set_spinner_value(NoiseDriftSetupLocators.WAVELENGTH_PICKER, channel_b_value)
            noise_drift_wavelength_details = NoiseDriftWavelengthDetails(channel_a_value, channel_b_value)

        return noise_drift_wavelength_details

    def set_selected_wavelength_details(self, noise_drifts_wavelength_details):
        self.selected_wavelength_details = noise_drifts_wavelength_details

    def get_selected_wavelength_details(self):
        return self.selected_wavelength_details

    def select_and_get_data_rate(self, data_rate_value, filter_time_constant):
        self.validate_data_rate_screen()
        self.tap(NoiseDriftSetupLocators.DATA_RATE)
        self.wait_for_element_visibility(self.wait_time, NoiseDriftSetupLocators.DATA_RATE_HZ_BANNER)

        self.set_spinner_value(NoiseDriftSetupLocators.DATA_RATE_PICKER, data_rate_value)
        if not self.is_toggle_component_enabled(NoiseDriftSetupLocators.FILTER_TOGGLE):
            self.tap(NoiseDriftSetupLocators.FILTER_TOGGLE)
        self.tap_filter_constant_option(filter_time_constant)

        noise_drift_data_frequency_details = NoiseDriftDataFrequencyDetails(data_rate_value, filter_time_constant)
        return noise_drift_data_frequency_details

    def set_selected_frequency_rate_details(self, noise_drifts_frequency_rate_details):
        self.selected_frequency_rate_details = noise_drifts_frequency_rate_details

    def get_selected_frequency_details(self):
        return self.selected_frequency_rate_details

    def validate_tuv_detector_screen(self):
        locator = NoiseDriftWorkflowLocators.TUV_DETECTOR_BANNER
        screen_name = "TUV Detector"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_noise_and_drift_test_button(self):
        locator = NoiseDriftWorkflowLocators.NOISE_AND_DRIFT_TEST_BUTTON
        self.tap(locator)

    def validate_welcome_screen(self):
        locator = NoiseDriftWelcomeLocators.WELCOME_HEADER
        screen_name = "Welcome"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_start_button(self):
        locator = NoiseDriftWorkflowLocators.START_BUTTON
        self.tap(locator)

    def tap_done_button(self):
        locator = NoiseDriftWorkflowLocators.DONE_BUTTON
        self.tap(locator)

    def tap_back_button(self):
        locator = NoiseDriftWorkflowLocators.BACK_BUTTON
        self.tap(locator)
