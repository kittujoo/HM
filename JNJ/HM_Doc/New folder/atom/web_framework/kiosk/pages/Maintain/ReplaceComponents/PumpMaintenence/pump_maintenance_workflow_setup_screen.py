"""
File_Name: pump_maintenance_workflow_setup_screen.py
Desc: This file contains specific user action on all the screen in the pump maintenance workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/3/22

"""
import re

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.pump_maintenance_workflow_locators import (PumpMaintenanceWorkflowLocators,
                                                                                            PumpMaintenanceWorkflowWelcomeLocators,
                                                                                            PumpMaintenanceWorkflowCautionLocators,
                                                                                            PumpMaintenanceWorkflowProcedureLocators,
                                                                                            PumpMaintenanceSummaryLocators)
from web_framework.kiosk.pages.base_page import BasePage


class PumpMaintenanceWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)
        self.text_visibility_wait = 1

    def validate_welcome_screen(self):
        locator = PumpMaintenanceWorkflowLocators.WELCOME_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_cautions_screen(self):
        locator = PumpMaintenanceWorkflowLocators.CAUTIONS_BANNER
        screen_name = "Cautions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_procedure_screen(self):
        locator = PumpMaintenanceWorkflowLocators.PROCEDURE_BANNER
        screen_name = "Procedure screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flush_options_screen(self):
        locator = PumpMaintenanceWorkflowLocators.FLUSH_OPTIONS_BANNER
        screen_name = "Flush options screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_options_screen(self):
        locator = PumpMaintenanceWorkflowLocators.FLUSH_SOLVENT_OPTIONS_BANNER
        screen_name = "Solvent selection screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_summary_screen(self):
        locator = PumpMaintenanceWorkflowLocators.SUMMARY_BANNER
        screen_name = "Summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_status_screen(self):
        locator = PumpMaintenanceWorkflowLocators.STATUS_BANNER
        screen_name = "Status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, PumpMaintenanceWorkflowWelcomeLocators.WELCOME_PARAGRAPH)
        return [self.get_text(PumpMaintenanceWorkflowWelcomeLocators.WELCOME_PARAGRAPH),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_ONE),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_TWO),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_THREE),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_FOUR),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_FIVE),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.LEFT_LIST_ITEM_SIX),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.RIGHT_LIST_ITEM_ONE),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.RIGHT_LIST_ITEM_TWO),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.RIGHT_LIST_ITEM_THREE),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.RIGHT_LIST_ITEM_FOUR),
                self.get_text(PumpMaintenanceWorkflowWelcomeLocators.RIGHT_LIST_ITEM_FIVE)]

    def get_caution_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, PumpMaintenanceWorkflowCautionLocators.FIRST_CAUTION_TEXT)
        return [self.get_text(PumpMaintenanceWorkflowCautionLocators.FIRST_CAUTION_TEXT),
                self.get_text(PumpMaintenanceWorkflowCautionLocators.SECOND_CAUTION_TEXT)]

    def get_procedure_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_TOP_PARAGRAPH)
        return [self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_TOP_PARAGRAPH),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_ONE),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_TWO),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_THREE),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_FOUR),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_FIVE),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_SIX),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_SEVEN),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_STEP_EIGHT),
                self.get_text(PumpMaintenanceWorkflowProcedureLocators.PROCEDURE_BOTTOM_PARAGRAPH)]

    def validate_flush_parameters(self, flush_duration):
        flush_params_text = self.get_text(PumpMaintenanceSummaryLocators.FLUSH_PARAMS_INFO_LABEL)
        capture = re.search(r'(\d+\.\d+)', flush_params_text)
        flush_minutes = capture[1]
        if not flush_minutes == flush_duration:
            return False
        return True
