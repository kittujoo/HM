"""
File_Name: shutdown_workflow.py
Desc: This file contains specific user actions on screens within the shutdown workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/13/2022

"""

import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import SolventCompositionConditionCardConstants
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import (SolventCompositionTabScreen as solcomp, SolventCompositionTabScreen)
from web_framework.kiosk.pages.Locators.Setup.shutdown_workflow_locators import ShutdownWorkflowLocators
from web_framework.kiosk.pages.base_page import BasePage


class ShutdownWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.selected_solvent_summary_details = None

    def enter_flow_rate(self, flow_rate):
        self.enter_value(flow_rate)

    def set_composition(self, composition, locator):

        self.logger.info("The lock is already unlocked")
        self.tap(locator)
        self.enter_value_for_specific_module(locator, composition)

    def get_composition(self, locator):
        return self.get_user_input_text(locator)

    def reset_composition(self):
        reset_composition_element = self.get_element(SolventCompositionTabScreen.RESET_COMPOSITION_BUTTON)
        reset_composition_button_disable = reset_composition_element.get_attribute("ng-reflect-disabled")
        reset_composition_button_disable = TypeConverter.to_bool(reset_composition_button_disable)
        self.logger.info(f"reset_composition_button_disable ====>>>>{reset_composition_button_disable}")

        if not reset_composition_button_disable:
            self.tap(SolventCompositionTabScreen.RESET_COMPOSITION_BUTTON)
        else:
            self.logger.info(" The solvent composition"
                             " button is disabled")

    def set_composition_and_edit_field_lock(self, locator, composition):
        self.set_composition(composition, locator)

    def enter_composition(self, solvent_composition):

        solvent_list = solvent_composition.get_solvent_lines()
        lock_icon_locator = ""
        edit_field_locator = ""
        for solvent in solvent_list:
            if solvent.line_id == "A":
                self.logger.info(f"The solvent composition for A is entered")
                edit_field_locator = solcomp.SOLVENT_A_EDIT_FIELD

            if solvent.line_id == "B":
                self.logger.info(f"The solvent composition for B is entered")
                edit_field_locator = solcomp.SOLVENT_B_EDIT_FIELD

            if solvent.line_id == "C":
                edit_field_locator = solcomp.SOLVENT_C_EDIT_FIELD

            if solvent.line_id == "D":
                edit_field_locator = solcomp.SOLVENT_D_EDIT_FIELD

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
                edit_field_locator = solcomp.SOLVENT_A_EDIT_FIELD
                hint_locator = solcomp.SOLVENT_A_HINT_LOCATOR

            if solvent.line_id == "B":
                self.logger.info(f"The solvent composition for B is entered")
                edit_field_locator = solcomp.SOLVENT_B_EDIT_FIELD
                hint_locator = solcomp.SOLVENT_B_HINT_LOCATOR

            if solvent.line_id == "C":
                edit_field_locator = solcomp.SOLVENT_C_EDIT_FIELD
                hint_locator = solcomp.SOLVENT_C_HINT_LOCATOR

            if solvent.line_id == "D":
                edit_field_locator = solcomp.SOLVENT_D_EDIT_FIELD
                hint_locator = solcomp.SOLVENT_D_HINT_LOCATOR

            self.set_composition(solvent.percentage_value, edit_field_locator)
            time.sleep(1)
            self.validate_hint_message(hint_locator, expected_hint_message)

    def set_selected_solvent_details(self, solvent_summary_details):
        self.selected_solvent_summary_details = solvent_summary_details

    def get_selected_solvent_summary_details(self):
        return self.selected_solvent_summary_details

    def validate_welcome_screen(self):
        locator = ShutdownWorkflowLocators.WELCOME_HEADER
        screen_name = "shutdown workflow welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_column_temperature_screen(self):
        locator = ShutdownWorkflowLocators.COLUMN_TEMPERATURE_HEADER
        screen_name = "shutdown workflow column temperature screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_sample_temperature_screen(self):
        locator = ShutdownWorkflowLocators.SAMPLE_TEMPERATURE_HEADER
        screen_name = "shutdown workflow sample temperature screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_lamp_screen(self):
        locator = ShutdownWorkflowLocators.LAMP_HEADER
        screen_name = "shutdown workflow lamp screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_rate_screen(self):
        locator = ShutdownWorkflowLocators.FLOW_RATE_HEADER
        screen_name = "shutdown workflow flowrate screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_screen(self):
        locator = ShutdownWorkflowLocators.SOLVENT_HEADER
        screen_name = "shutdown workflow solvent screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(ShutdownWorkflowLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(ShutdownWorkflowLocators.WELCOME_PARAGRAPH_TWO),
                self.get_text(ShutdownWorkflowLocators.WELCOME_PARAGRAPH_THREE)]
