"""
File_Name: prime_solvents_workflow.py
Desc: This file contains specific user action on the prime solvents workflow setup screens
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/25/23
"""
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.prime_solvents_workflow_constants import \
    PrimeSolventsWorkflowConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Setup.prime_solvents_workflow_locators import PrimeSolventsWorkflowLocators, \
    PrimeSolventsWelcomeScreenLocators, SolventLinesOptionLocators, PrimeSummaryLocators, CompositionOptionLocators, FinalOptionsLocators
from web_framework.kiosk.pages.base_page import BasePage


class PrimeMultiSolventWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Prime Solvents Setup Screen"

    def validate_setup_selection_screen(self):
        locator = PrimeSolventsWorkflowLocators.START_PANEL
        screen_name = "setup selection screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_welcome_screen(self):
        locator = PrimeSolventsWorkflowLocators.WELCOME_PAGE_BANNER
        screen_name = "welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_caution_screen(self):
        locator = PrimeSolventsWorkflowLocators.CAUTIONS_PAGE_BANNER
        screen_name = "cautions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_order_screen(self):
        locator = PrimeSolventsWorkflowLocators.PRIME_SOLVENT_ORDER_BANNER
        screen_name = "solvent order screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_prime_by_line_composition_screen(self):
        locator = SolventLinesOptionLocators.SOLVENT_LINE_TOGGLE
        screen_name = "prime by line composition screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_final_flow_screen(self):
        locator = PrimeSolventsWorkflowLocators.FINAL_FLOW_BANNER
        screen_name = "final flow screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_final_comp_screen(self):
        locator = PrimeSolventsWorkflowLocators.FINAL_COMP_BANNER
        screen_name = "final composition screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_LIST_PARAGRAPH),
                self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_PARAGRAPH_TWO)]

    def get_welcome_list_text(self):
        return [self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_LIST_FIRST_POINT),
                self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_LIST_SECOND_POINT),
                self.get_text(PrimeSolventsWelcomeScreenLocators.WELCOME_LIST_THIRD_POINT)]

    def get_caution_list_text(self):
        return [self.get_text(PrimeSolventsWelcomeScreenLocators.FIRST_CAUTION_TEXT),
                self.get_text(PrimeSolventsWelcomeScreenLocators.SECOND_CAUTION_TEXT)]

    def select_prime_solvent_lines(self, solvent_lines):
        # this if tree is kinda weird, wanna find a better way to do this
        if solvent_lines.find('A') != -1:
            current_state = self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_A)
            self.logger.info(f"current_state====>>>{current_state}")
            if not self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_A):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_A)
        else:
            if self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_A):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_A)

        if solvent_lines.find('B') != -1:
            if not self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_B):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_B)
        else:
            if self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_B):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_B)

        if solvent_lines.find('C') != -1:
            if not self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_C):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_C)
        else:
            if self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_C):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_C)

        if solvent_lines.find('D') != -1:
            if not self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_D):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_D)
        else:
            if self.is_checkbox_checked(SolventLinesOptionLocators.SOLVENT_LINE_D):
                self.tap(SolventLinesOptionLocators.SOLVENT_LINE_D)

    def validate_line_selection_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSolventsWorkflowLocators.PRIME_SOLVENT_SELECTION_BANNER,
            PrimeSolventsWorkflowConstants.prime_by_solvent_header, WaitTimeConstants.SmallWait)

    def validate_comp_selection_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSolventsWorkflowLocators.PRIME_COMP_SELECTION_BANNER,
            PrimeSolventsWorkflowConstants.prime_by_composition_header, WaitTimeConstants.SmallWait)

    def validate_prime_by_line_duration_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSolventsWorkflowLocators.PRIME_SOLVENT_DURATION_BANNER,
            PrimeSolventsWorkflowConstants.prime_by_solvent_duration, WaitTimeConstants.SmallWait)

    def validate_prime_by_comp_duration_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSolventsWorkflowLocators.PRIME_COMP_DURATION_BANNER,
            PrimeSolventsWorkflowConstants.prime_by_composition_duration, WaitTimeConstants.SmallWait)

    def validate_prime_summary_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSummaryLocators.PRIME_SUMMARY_HEADER,
            PrimeSolventsWorkflowConstants.prime_summary_header, WaitTimeConstants.SmallWait)

    def validate_stepper_button_appeared(self):
        self.wait_for_element_visibility(self.wait_time, PrimeSolventsWorkflowLocators.STEPPER_BUTTON_PLUS)

    def validate_time_edit_field_appeared(self):
        self.wait_for_element_load(CompositionOptionLocators.TIME_EDIT_FIELD, self.wait_time)

    def validate_flow_rate_edit_field_appeared(self):
        self.wait_for_element_visibility(self.wait_time, FinalOptionsLocators.FLOW_RATE_FIELD)

    def validate_eq_duration_edit_field_appeared(self):
        self.wait_for_element_visibility(self.wait_time, FinalOptionsLocators.EQ_FIELD)
