"""
File_Name: replace_seal_workflow_setup_screen.py
Desc: This file contains specific user action on all the screen in the replace seal workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/27/22

"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.replace_seal_workflow_locators import (ReplaceSealWorkflowLocators, ReplaceSealWorkflowWelcomeLocators,
                                                                                        ReplaceSealWorkflowProcedureOneLocators)
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceSealWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)
        self.text_visibility_wait = 1

    def validate_welcome_screen(self):
        locator = ReplaceSealWorkflowLocators.WELCOME_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_cautions_screen(self):
        locator = ReplaceSealWorkflowLocators.CAUTIONS_BANNER
        screen_name = "Cautions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_screen(self):
        locator = ReplaceSealWorkflowLocators.PRECONDITIONS_BANNER
        screen_name = "Preconditions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_carriage_status_screen(self):
        locator = ReplaceSealWorkflowLocators.CARRIAGE_STATUS_BANNER
        screen_name = "Carriage status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_procedure_one_screen(self):
        locator = ReplaceSealWorkflowLocators.PROCEDURE_ONE_BANNER
        screen_name = "First procedure screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_procedure_two_screen(self):
        locator = ReplaceSealWorkflowLocators.PROCEDURE_TWO_BANNER
        screen_name = "Second procedure screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_seal_test_status_screen(self):
        locator = ReplaceSealWorkflowLocators.SEAL_TEST_STATUS_BANNER
        screen_name = "Seal test status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, ReplaceSealWorkflowWelcomeLocators.WELCOME_PARA_ONE)
        return [self.get_text(ReplaceSealWorkflowWelcomeLocators.WELCOME_PARA_ONE),
                self.get_text(ReplaceSealWorkflowWelcomeLocators.WELCOME_PARA_TWO),
                self.get_text(ReplaceSealWorkflowWelcomeLocators.WELCOME_PARA_THREE)]

    def get_procedure_one_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, ReplaceSealWorkflowProcedureOneLocators.PROC_ONE_PARA_ONE)
        return [self.get_text(ReplaceSealWorkflowProcedureOneLocators.PROC_ONE_PARA_ONE),
                self.get_text(ReplaceSealWorkflowProcedureOneLocators.PROC_ONE_PARA_TWO),
                self.get_text(ReplaceSealWorkflowProcedureOneLocators.PROC_ONE_PARA_THREE)]
