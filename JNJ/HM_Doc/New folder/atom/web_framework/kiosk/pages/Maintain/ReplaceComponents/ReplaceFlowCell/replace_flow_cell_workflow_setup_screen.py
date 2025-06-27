"""
File_Name: replace_flow_cell_workflow_setup_screen.py
Desc: This file contains specific user action on all the screen in the replace flow cell workflow
__copyright__ = "Copyright (c) 2022 by Waters Corpora22on, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/14/22

"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.Locators.Maintain.replace_flow_cell_workflow_locators import (ReplaceFlowCellWorkflowLocators,
                                                                                             ReplaceFlowCellWelcomeScreenLocators,
                                                                                             ReplaceFlowCellCautionScreenLocators,
                                                                                             ReplaceFlowCellRemoveScreenLocators,
                                                                                             ReplaceFlowCellInstallScreenLocators,
                                                                                             ReplaceFlowCellPreconditionsScreenLocators)
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceFlowCellWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)

    def validate_welcome_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.WELCOME_BANNER
        screen_name = "Welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_caution_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.CAUTION_BANNER
        screen_name = "Caution screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_summary_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.PRECONDITIONS_SUMMARY_BANNER
        screen_name = "Preconditions summary screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_preconditions_status_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.PRECONDITIONS_STATUS_BANNER
        screen_name = "preconditions status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_removal_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.REMOVAL_BANNER
        screen_name = "Removal screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_first_installation_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.FIRST_INSTALLATION_BANNER
        screen_name = "First installation screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_second_installation_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.SECOND_INSTALLATION_BANNER
        screen_name = "Second installation screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_flow_conditioning_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.FLOW_CONDITIONING_BANNER
        screen_name = "Flow conditioning screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_solvent_conditioning_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.SOLVENT_CONDITIONING_BANNER
        screen_name = "Solvent conditioning screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_status_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.STATUS_BANNER
        screen_name = "Status screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_finish_screen(self):
        locator = ReplaceFlowCellWorkflowLocators.FINISH_BANNER
        screen_name = "Finish screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [self.get_text(ReplaceFlowCellWelcomeScreenLocators.WELCOME_PARA_ONE),
                self.get_text(ReplaceFlowCellWelcomeScreenLocators.WELCOME_PARA_TWO),
                self.get_text(ReplaceFlowCellWelcomeScreenLocators.WELCOME_PARA_THREE)]

    def get_caution_paragraph_text(self):
        return [self.get_text(ReplaceFlowCellCautionScreenLocators.HOT_SURFACE_TEXT),
                self.get_text(ReplaceFlowCellCautionScreenLocators.GENERAL_CAUTION_TEXT)]

    def get_removal_text(self):
        return [self.get_text(ReplaceFlowCellRemoveScreenLocators.REPLACE_STEP_ONE),
                self.get_text(ReplaceFlowCellRemoveScreenLocators.REPLACE_STEP_TWO),
                self.get_text(ReplaceFlowCellRemoveScreenLocators.REPLACE_STEP_THREE),
                self.get_text(ReplaceFlowCellRemoveScreenLocators.REPLACE_STEP_FOUR)]

    def get_first_installation_text(self):
        return [self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_FIVE),
                self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_SIX),
                self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_SEVEN),
                self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_EIGHT)]

    def get_second_installation_text(self):
        return [self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_NINE),
                self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_TEN),
                self.get_text(ReplaceFlowCellInstallScreenLocators.INSTALL_STEP_ELEVEN)]

    def precondition_status(self):
        if self.is_displayed(ReplaceFlowCellPreconditionsScreenLocators.LAMP_STATE_CHECK_STATUS) and self.is_displayed(
                ReplaceFlowCellPreconditionsScreenLocators.FLOW_STATE_CHECK_STATUS) and self.is_displayed(
            ReplaceFlowCellPreconditionsScreenLocators.POWER_STATE_CHECK_STATUS):
            return True
        else:
            return False

    def validate_preconditions_process(self, max_wait_time):
        start_time = time.time()
        while time.time() - start_time < max_wait_time:

            if self.precondition_status():
                break
            time.sleep(1)
        assert self.precondition_status(), f"One or more of the precondition statuses was not met"

    def validate_next_button_inactive(self):
        button_status = self.get_element(BasePageLocators.NEXT_BUTTON_LABEL)
        is_button_inactive = button_status.get_attribute("ng-reflect-available")
        self.logger.info(f"is_button_inactive==>>>{is_button_inactive}")
        is_button_inactive = TypeConverter.to_bool(is_button_inactive)

        assert is_button_inactive is False, f"The next button is in an active state when it should not be"
