"""
File_Name: flow_settings_screen.py
Desc: This file contains specific user action on the elements in the flow setting screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 06/23/2020
__modified__ = "Sharmila Vairamani"  Added enter composition and  is edit field locked function 11/06/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Sharmila Vairamani" Added page specific functions - 02/15/2020
__modified__ = "Sharmila Vairamani" Added get_flow_rate and is_flow_edit_field_in_error_state functions - 02/24/2021
__modified__ = "Sharmila Vairamani" Added reset_composition method - 02/25/2021
__modified__ = "Sharmila Vairamani" Added tap_solvent_composition_tab  - 03/23/2021
__modified__= "sharmila Vairmani " Refactored tap_solvent_composition_tab - 04/08/2021
__modified__= "Sharmila Vairamani " Changed the locator value - 06/29/2021
__modified__ = "Tyler Prada" Added field focus method - 11/15/21
__modified__ = "Tyler Prada" Adjustment on validate flow screen 12/7/21
__modified__ = "Sharmila Vairamani" Added hint messages test steps 01/19/2022
__modified__ "Sharmila Vairamani" Added tap_toggle_button_on 02/28/2022
__modified__ "Martin Yanev" Modify get_field_focus_state 12/04/2022

"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import SolventCompositionConditionCardConstants
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import (FlowControlTabScreen, SolventCompositionTabScreen,
                                                                                        FlowSettingsScreenLocator)
from web_framework.kiosk.pages.base_page import BasePage


class FlowSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.wait_time = 5

    def select_flow(self, flow):
        flow_text_dictionary = {
            "Off": FlowControlTabScreen.OFF_FLOW_OPTION,
            "Low": FlowControlTabScreen.LOW_FLOW_OPTION,
            "Custom": FlowControlTabScreen.CUSTOM_FLOW_OPTION
        }

        if flow in flow_text_dictionary:
            locator = flow_text_dictionary[flow]
            self.tap(locator)
            return

        assert False, f"Unexpected flow option => {flow}"

    def validate_composition_settings_screen(self):
        locator = SolventCompositionTabScreen.SOLVENT_D_EDIT_FIELD
        screen_name = "flow settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_settings_screen(self):
        locator = FlowSettingsScreenLocator.HEADER
        screen_name = "flow settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_flow_info(self):
        flow_info = self.get_container_text(FlowControlTabScreen.FLOW_INFO)
        return flow_info

    def tap_flow_tab(self):
        self.tap(FlowControlTabScreen.FLOW_TAB)

    def tap_solvent_composition_tab(self):
        start_time = time.time()
        while time.time() - start_time < 10:
            self.tap(SolventCompositionTabScreen.SOLVENT_COMPOSITION_TAB)
            if self.is_displayed(SolventCompositionTabScreen.SOLVENT_D_EDIT_FIELD):
                break
            time.sleep(1)

        assert self.is_displayed(SolventCompositionTabScreen.SOLVENT_D_EDIT_FIELD), f"The edit field is not hidden"

    def enter_flow_rate(self, flow_rate):
        self.enter_value(flow_rate)

    def enter_time(self, time):
        self.tap(FlowControlTabScreen.TIME_EDIT_FIELD)
        self.enter_value(time)

    def is_edit_field_locked(self, lock_locator):
        edit_field_lock = self.get_element(lock_locator)
        lock_icon_class_string = edit_field_lock.get_attribute("ng-reflect-svg-icon")
        self.logger.info(f"The lock icon class attribute  {lock_icon_class_string}")
        lock_icon_value = "unlocked"

        if lock_icon_value in lock_icon_class_string:
            return False
        else:
            return True

    def set_edit_field_lock(self, lock_state, lock_locator):
        self.logger.info(f"lock state ++++++>>>>>>>> {lock_state}")
        lock_state = TypeConverter.to_bool(lock_state)
        currently_locked = self.is_edit_field_locked(lock_locator)
        self.logger.info(f"lock currently_locked ++++++>>>>>>>> {currently_locked}")
        self.toggle_switch("Leak sensor monitor", lock_locator,
                           currently_locked, lock_state)

    def set_composition(self, composition, locator):

        self.logger.info("The lock is already unlocked")
        self.tap(locator)
        self.enter_value_for_specific_module(locator, composition)

    def set_composition_and_edit_field_lock(self, locator, composition):
        self.set_composition(composition, locator)

    def get_composition(self, locator):
        return self.get_user_input_text(locator)

    def enter_composition(self, solvent_composition):

        solvent_list = solvent_composition.get_solvent_lines()
        lock_icon_locator = ""
        edit_field_locator = ""
        for solvent in solvent_list:
            if solvent.line_id == "A":
                self.logger.info(f"The solvent composition for A is entered")
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_A_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_A_LOCK_ICON
                # hint_locator = solcomp.SOLVENT_A_HINT_LOCATOR

            if solvent.line_id == "B":
                self.logger.info(f"The solvent composition for B is entered")
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_B_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_B_LOCK_ICON
                # hint_locator = solcomp.SOLVENT_B_HINT_LOCATOR

            if solvent.line_id == "C":
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_C_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_C_LOCK_ICON

            if solvent.line_id == "D":
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_D_EDIT_FIELD
                # lock_icon_locator = solcomp.SOLVENT_D_LOCK_ICON

            self.set_composition_and_edit_field_lock(edit_field_locator,
                                                     solvent.percentage_value)

    def validate_hint_field(self, solvent_composition):
        solvent_list = solvent_composition.get_solvent_lines()
        edit_field_locator = ""
        expected_hint_message = SolventCompositionConditionCardConstants.SolventHintMessage
        hint_locator = None
        for solvent in solvent_list:
            if solvent.line_id == "A":
                self.logger.info(f"The solvent composition for A is entered")
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_A_EDIT_FIELD
                hint_locator = SolventCompositionTabScreen.SOLVENT_A_HINT_LOCATOR

            if solvent.line_id == "B":
                self.logger.info(f"The solvent composition for B is entered")
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_B_EDIT_FIELD
                hint_locator = SolventCompositionTabScreen.SOLVENT_B_HINT_LOCATOR

            if solvent.line_id == "C":
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_C_EDIT_FIELD
                hint_locator = SolventCompositionTabScreen.SOLVENT_C_HINT_LOCATOR

            if solvent.line_id == "D":
                edit_field_locator = SolventCompositionTabScreen.SOLVENT_D_EDIT_FIELD
                hint_locator = SolventCompositionTabScreen.SOLVENT_D_HINT_LOCATOR

            self.set_composition(solvent.percentage_value, edit_field_locator)
            time.sleep(1)
            self.validate_hint_message(hint_locator, expected_hint_message)

    def get_solvent_line_id(self, locator):
        solvent_id = self.get_text(locator)
        self.logger.info(f"solvent_id_string=>>{solvent_id}")

        return solvent_id

    def get_flow_rate(self):
        current_flow_rate = self.get_user_input_text(FlowControlTabScreen.FLOW_RATE_EDIT_FIELD)
        return current_flow_rate

    def is_flow_edit_field_in_error_state(self):
        return self.is_edit_field_in_error_state(FlowControlTabScreen.FLOW_EDIT_FIELD_STATE)

    def reset_composition(self):
        reset_composition_element = self.get_element(SolventCompositionTabScreen.RESET_COMPOSITION_BUTTON)
        reset_composition_button_disable = reset_composition_element.get_attribute("ng-reflect-disabled")
        reset_composition_button_disable = TypeConverter.to_bool(reset_composition_button_disable)
        self.logger.info(f"reset_composition_button_disable ====>>>>{reset_composition_button_disable}")

        if not reset_composition_button_disable:
            self.tap(SolventCompositionTabScreen.RESET_COMPOSITION_BUTTON)
        else:
            self.logger.info(" The solvent composition button is disabled")

    def get_field_focus_state(self, focused_field):
        field_focus_text_dictionary = {
            "A": SolventCompositionTabScreen.SOLVENT_A_FIELD_FOCUS,
            "B": SolventCompositionTabScreen.SOLVENT_B_FIELD_FOCUS,
            "C": SolventCompositionTabScreen.SOLVENT_C_FIELD_FOCUS,
            "D": SolventCompositionTabScreen.SOLVENT_D_FIELD_FOCUS,
        }

        if focused_field in field_focus_text_dictionary:
            locator = field_focus_text_dictionary[focused_field]

            # check for focus in the singular field
            field_element = self.get_element(locator)
            field_focus_state = field_element.get_attribute("class")
            self.logger.info(f"field_focus_state ===={field_focus_state}")
            field_focus_state = field_focus_state.find("inactive")
            self.logger.info(f"field_focus_state ===={field_focus_state}")

            # if the field is focused on then true condition
            if field_focus_state != -1:
                return False
            return True

    def tap_toggle_button(self):
        self.tap(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)

    def validate_hint_message(self, locator, expected_hint_message):
        actual_hint_message = self.get_text(locator)
        self.logger.info(f"actual_hint_message====>>>>{actual_hint_message}")
        self.logger.info(f"expected_hint_message====>>>>{expected_hint_message}")
        assert actual_hint_message == expected_hint_message, f"actual_hint_message====>>>>{actual_hint_message}, expected_hint_message====>>>>{expected_hint_message}"

    def tap_flow_rate_button_on(self):
        self.wait_time_to_load_value(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
        super().tap_toggle_button_on(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)

    def tap_flow_rate_button_off(self):
        self.wait_time_to_load_value(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
        super().tap_toggle_button_off(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
