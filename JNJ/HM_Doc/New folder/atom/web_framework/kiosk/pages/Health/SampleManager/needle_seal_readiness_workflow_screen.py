"""
File_Name: needle_seal_readiness_workflow.py
Desc: This file contains specific user actions on screens within the needle seal readiness test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/17/22
__modified = "Tyler Prada" added screen validation 6/22/23
"""

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.needle_seal_readiness_constants import \
    NeedleSealReadinessConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import \
    (NeedleSealReadinessLocators, NeedleSealReadinessWelcomeLocators, NeedleSealReadinessSetupLocators)
from web_framework.kiosk.pages.base_page import BasePage


class NeedleSealReadinessSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_welcome_screen(self):
        locator = NeedleSealReadinessLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_setup_screen(self):
        locator = NeedleSealReadinessSetupLocators.SETUP_BANNER
        screen_name = "Setup screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_composition_screen(self):
        locator = NeedleSealReadinessSetupLocators.COMPOSITION_BANNER
        screen_name = "Composition screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        self.wait_time_to_load_value(NeedleSealReadinessWelcomeLocators.WELCOME_PARAGRAPH_ONE)
        return [
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_PARAGRAPH_ONE),
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_PARAGRAPH_TWO),
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_PARAGRAPH_THREE)
        ]

    def get_instruction_text(self):
        self.wait_time_to_load_value(NeedleSealReadinessWelcomeLocators.WELCOME_LIST_PARAGRAPH)
        return [
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_LIST_PARAGRAPH),
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_LIST_ITEM_ONE),
            self.get_text(NeedleSealReadinessWelcomeLocators.WELCOME_LIST_ITEM_TWO)
        ]

    def get_setup_text(self):
        self.wait_time_to_load_value(NeedleSealReadinessSetupLocators.SETUP_LINE_ONE)
        return [
            self.get_text(NeedleSealReadinessSetupLocators.SETUP_LINE_ONE),
            self.get_text(NeedleSealReadinessSetupLocators.SETUP_LINE_TWO)
        ]

    def get_comp_setup_text(self):
        self.wait_time_to_load_value(NeedleSealReadinessSetupLocators.COMP_TEXT_ONE)
        return [
            self.get_text(NeedleSealReadinessSetupLocators.COMP_TEXT_ONE),
            self.get_text(NeedleSealReadinessSetupLocators.COMP_TEXT_TWO)
        ]

    def validate_flow_settings_screen(self):
        self.validate_simple_text_wait_condition(
            NeedleSealReadinessSetupLocators.SETUP_BANNER,
            NeedleSealReadinessConstants.SetupHeader, WaitTimeConstants.SmallWait)

    def validate_flow_default_value(self):
        locator = NeedleSealReadinessSetupLocators.FlOW_HINT_FIELD
        expected_hint_message = NeedleSealReadinessConstants.FlowHintMessage
        self.validate_hint_message(locator, expected_hint_message)

    def validate_comp_default_value(self):
        locator = NeedleSealReadinessSetupLocators.COMP_HINT_FIELD
        expected_hint_message = NeedleSealReadinessConstants.CompHintMessage
        self.validate_hint_message(locator, expected_hint_message)
