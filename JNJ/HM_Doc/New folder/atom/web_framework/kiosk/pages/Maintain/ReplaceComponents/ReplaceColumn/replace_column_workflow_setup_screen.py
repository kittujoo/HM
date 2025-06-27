"""
File_Name: replace_column_workflow_setup_screen.py
Desc: This file contains specific user action on all the screen in the replace column workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 0/0/00

"""
import re

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import SolventCompositionTabScreen as solcomp
from web_framework.kiosk.pages.Locators.Maintain.replace_column_workflow_locators import (ReplaceColumnWorkflowLocators, ReplaceColumnWelcomeScreenLocators,
                                                                                          ReplaceColumnCautionScreenLocators)
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceColumnWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)

    def validate_welcome_screen(self):
        locator = ReplaceColumnWorkflowLocators.WELCOME_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_caution_screen(self):
        locator = ReplaceColumnWorkflowLocators.CAUTION_BANNER
        screen_name = "Caution screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_column_screen(self):
        locator = ReplaceColumnWorkflowLocators.FLUSH_COLUMN_BANNER
        screen_name = "Flush column screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_column_composition_screen(self):
        locator = ReplaceColumnWorkflowLocators.FLUSH_COLUMN_COMPOSITION_BANNER
        screen_name = "Flush column composition screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_column_summary_screen(self):
        locator = ReplaceColumnWorkflowLocators.FLUSH_COLUMN_SUMMARY_BANNER
        screen_name = "Flush column summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_column_status_screen(self):
        locator = ReplaceColumnWorkflowLocators.FLUSH_COLUMN_STATUS_BANNER
        screen_name = "Flush column status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_screen(self):
        locator = ReplaceColumnWorkflowLocators.PRECONDITIONS_BANNER
        screen_name = "Preconditions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_removal_screen(self):
        locator = ReplaceColumnWorkflowLocators.REMOVE_BANNER
        screen_name = "Removal screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_installation_screen(self):
        locator = ReplaceColumnWorkflowLocators.INSTALL_BANNER
        screen_name = "Installation screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_new_column_screen(self):
        locator = ReplaceColumnWorkflowLocators.NEW_COLUMN_BANNER
        screen_name = "New column screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_new_column_options_screen(self):
        locator = ReplaceColumnWorkflowLocators.NEW_COLUMN_OPTIONS_BANNER
        screen_name = "New column options screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    # Prime Instrument Screens?

    def validate_condition_column_screen(self):
        locator = ReplaceColumnWorkflowLocators.CONDITION_COLUMN_BANNER
        screen_name = "Condition column screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_condition_solvents_column_screen(self):
        locator = ReplaceColumnWorkflowLocators.CONDITION_SOLVENTS_COLUMN_BANNER
        screen_name = "Condition solvents column screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_condition_duration_column_screen(self):
        locator = ReplaceColumnWorkflowLocators.CONDITION_DURATION_COLUMN_BANNER
        screen_name = "Condition duration column screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_column_summary_screen(self):
        locator = ReplaceColumnWorkflowLocators.COLUMN_SUMMARY_BANNER
        screen_name = "Column summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_column_status_screen(self):
        locator = ReplaceColumnWorkflowLocators.COLUMN_STATUS_BANNER
        screen_name = "Column status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_column_results_screen(self):
        locator = ReplaceColumnWorkflowLocators.COLUMN_RESULTS_BANNER
        screen_name = "Column results screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(ReplaceColumnWelcomeScreenLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(ReplaceColumnWelcomeScreenLocators.WELCOME_PARAGRAPH_TWO),
                self.get_text(ReplaceColumnWelcomeScreenLocators.WELCOME_LIST_ITEM_ONE),
                self.get_text(ReplaceColumnWelcomeScreenLocators.WELCOME_LIST_ITEM_TWO),
                self.get_text(ReplaceColumnWelcomeScreenLocators.WELCOME_LIST_ITEM_THREE)]

    def get_caution_paragraph_text(self):
        return [self.get_text(ReplaceColumnCautionScreenLocators.HOT_SURFACE_PARAGRAPH),
                self.get_text(ReplaceColumnCautionScreenLocators.CORROSIVE_MATERIALS_PARAGRAPH),
                self.get_text(ReplaceColumnCautionScreenLocators.CAUTION_PARAGRAPH)]

    def enter_composition(self, solvent_composition):

        solvent_list = solvent_composition.get_solvent_lines()
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

    def set_composition(self, composition, locator):
        self.tap(locator)
        self.enter_value_for_specific_module(locator, composition)

    def set_composition_and_edit_field_lock(self, locator, composition):
        self.set_composition(composition, locator)

    def validate_summary_composition(self, flow_rate, line_1, line_2, line_3, line_4):
        text = self.get_text(ReplaceColumnWorkflowLocators.FLUSH_COLUMN_COMPOSITION_LABEL)

        regex_object = re.search(r"(\d+\.\d+).*\s(\d+)%\s\w,\s(\d+)%\s\w,\s(\d+)%\s\w\sand\s(\d+)", text)
        self.logger.info(regex_object.groups())

        assert regex_object.group(1) == flow_rate, f"Entered and summary flow rates do not match | Entered: {flow_rate} | Summary: {regex_object.group(1)}"
        assert regex_object.group(2) == line_1, f"Entered and summary line 1 composition do not match | Entered: {line_1} | Summary: {regex_object.group(2)}"
        assert regex_object.group(3) == line_2, f"Entered and summary line 2 composition do not match | Entered: {line_2} | Summary: {regex_object.group(3)}"
        assert regex_object.group(4) == line_3, f"Entered and summary line 3 composition do not match | Entered: {line_3} | Summary: {regex_object.group(4)}"
        assert regex_object.group(5) == line_4, f"Entered and summary line 4 composition do not match | Entered: {line_4} | Summary: {regex_object.group(5)}"
