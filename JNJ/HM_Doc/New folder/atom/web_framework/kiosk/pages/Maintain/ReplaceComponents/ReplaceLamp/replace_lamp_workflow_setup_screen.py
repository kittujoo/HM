"""
File_Name: replace_lamp_workflow_setup_screen.py
Desc: This file contains specific user action on all the screen in the replace lamp workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/24/22

"""
import re

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.replace_lamp_workflow_locators import (ReplaceLampWorkflowLocators,
                                                                                        ReplaceLampWorkflowWelcomeLocators, ReplaceLampWorkflowCautionLocators,
                                                                                        ReplaceLampWorkflowPreconditionsLocators,
                                                                                        ReplaceLampWorkflowRemovalLocators,
                                                                                        ReplaceLampWorkflowFirstInstallationLocators,
                                                                                        ReplaceLampWorkflowSecondInstallationLocators,
                                                                                        ReplaceLampWorkflowFinishLocators)
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceLampWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)
        self.text_visibility_wait = 1

    def validate_welcome_screen(self):
        locator = ReplaceLampWorkflowLocators.WELCOME_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_cautions_screen(self):
        locator = ReplaceLampWorkflowLocators.CAUTIONS_BANNER
        screen_name = "Cautions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_screen(self):
        locator = ReplaceLampWorkflowLocators.PRECONDITIONS_BANNER
        screen_name = "Preconditions screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_removal_screen(self):
        locator = ReplaceLampWorkflowLocators.REMOVAL_BANNER
        screen_name = "Removal screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_first_installation_screen(self):
        locator = ReplaceLampWorkflowLocators.FIRST_INSTALL_BANNER
        screen_name = "First installation screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_second_installation_screen(self):
        locator = ReplaceLampWorkflowLocators.SECOND_INSTALL_BANNER
        screen_name = "Second installation screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_finish_screen(self):
        locator = ReplaceLampWorkflowLocators.FINISH_BANNER
        screen_name = "Finish screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(ReplaceLampWorkflowWelcomeLocators.WELCOME_PARA_ONE),
                self.get_text(ReplaceLampWorkflowWelcomeLocators.WELCOME_PARA_TWO),
                self.get_text(ReplaceLampWorkflowWelcomeLocators.WELCOME_PARA_THREE)]

    def get_caution_text(self):
        return [self.get_text(ReplaceLampWorkflowCautionLocators.BURN_CAUTION_TEXT),
                self.get_text(ReplaceLampWorkflowCautionLocators.GENERAL_CAUTION_TEXT),
                self.get_text(ReplaceLampWorkflowCautionLocators.GENERAL_CAUTION_BULLET_ONE),
                self.get_text(ReplaceLampWorkflowCautionLocators.GENERAL_CAUTION_BULLET_TWO)]

    def validate_precondition_states(self):
        if not self.is_condition_met(ReplaceLampWorkflowPreconditionsLocators.LAMP_STATE_STATUS):
            return False
        if not self.is_condition_met(ReplaceLampWorkflowPreconditionsLocators.FLOW_STATE_STATUS):
            return False
        if not self.is_condition_met(ReplaceLampWorkflowPreconditionsLocators.POWER_STATE_STATUS):
            return False

        return True

    def get_preconditions_text(self):
        return [self.get_text(ReplaceLampWorkflowPreconditionsLocators.WARNING_PARA_ONE),
                self.get_text(ReplaceLampWorkflowPreconditionsLocators.WARNING_PARA_TWO),
                self.get_text(ReplaceLampWorkflowPreconditionsLocators.WARNING_PARA_THREE)]

    def get_removal_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, ReplaceLampWorkflowRemovalLocators.REMOVAL_STEP_ONE)
        return [self.get_text(ReplaceLampWorkflowRemovalLocators.REMOVAL_STEP_ONE),
                self.get_text(ReplaceLampWorkflowRemovalLocators.REMOVAL_STEP_TWO),
                self.get_text(ReplaceLampWorkflowRemovalLocators.REMOVAL_STEP_THREE),
                self.get_text(ReplaceLampWorkflowRemovalLocators.REMOVAL_STEP_FOUR),
                self.get_text(ReplaceLampWorkflowRemovalLocators.WARNING_TEXT),
                self.get_text(ReplaceLampWorkflowRemovalLocators.CAUTION_PARA_ONE),
                self.get_text(ReplaceLampWorkflowRemovalLocators.CAUTION_PARA_TWO),
                self.get_text(ReplaceLampWorkflowRemovalLocators.CAUTION_PARA_THREE)]

    def get_first_installation_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, ReplaceLampWorkflowFirstInstallationLocators.INSTALLATION_STEP_ONE)
        return [self.get_text(ReplaceLampWorkflowFirstInstallationLocators.INSTALLATION_STEP_ONE),
                self.get_text(ReplaceLampWorkflowFirstInstallationLocators.INSTALLATION_STEP_TWO),
                self.get_text(ReplaceLampWorkflowFirstInstallationLocators.INSTALLATION_STEP_THREE),
                self.get_text(ReplaceLampWorkflowFirstInstallationLocators.INSTALLATION_STEP_FOUR),
                self.get_text(ReplaceLampWorkflowFirstInstallationLocators.CAUTION_TEXT)]

    def get_second_installation_text(self):
        self.wait_for_element_visibility(self.text_visibility_wait, ReplaceLampWorkflowSecondInstallationLocators.INSTALLATION_STEP_FIVE)
        return [self.get_text(ReplaceLampWorkflowSecondInstallationLocators.INSTALLATION_STEP_FIVE),
                self.get_text(ReplaceLampWorkflowSecondInstallationLocators.INSTALLATION_STEP_SIX),
                self.get_text(ReplaceLampWorkflowSecondInstallationLocators.INSTALLATION_STEP_SEVEN),
                self.get_text(ReplaceLampWorkflowSecondInstallationLocators.CAUTION_TEXT)]

    def validate_lamp_hours_range(self):
        lamp_hours_text = self.get_text(ReplaceLampWorkflowFinishLocators.LAMP_HOURS)
        capture = re.search(r'(\d*).of.(\d*)', lamp_hours_text)
        current_lamp_hours = capture[1]
        lamp_hours_max = capture[2]
        if not current_lamp_hours <= lamp_hours_max:
            return False
        return True
