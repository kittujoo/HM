"""
File_Name: heater_cooler_workflow.py
Desc: This file contains specific user actions on screens within the heater/cooler workflow
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 1/14/2021
__modified__ = "Tyler Prada" added get text method 1/20/22
__modified__ = "Tyler Prada" Adjustments due to workflow changes 7/22/22
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Health.Models.heater_cooler_summary import HeaterCoolerSummaryDetails
from web_framework.kiosk.pages.Locators.Health.ColumnModule.heater_cooler_workflow_locators import (HeaterCoolerWorkflowLocators,
                                                                                                    HeaterCoolerPreconditionLocators,
                                                                                                    HeaterCoolerWelcomeLocators)
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.base_page import BasePage


class HeaterCoolerWorkflowSetupScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.heater_cooler_summary_details = None

    def set_heater_cooler_details(self, heater_cooler_summary_details):
        self.heater_cooler_summary_details = heater_cooler_summary_details

    def get_selected_summary_details(self):
        return self.heater_cooler_summary_details

    def validate_welcome_screen(self):
        locator = HeaterCoolerWorkflowLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the heater/cooler workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_precondition_screen(self):
        locator = HeaterCoolerPreconditionLocators.PRECONDITION_PAGE_BANNER
        screen_name = "Pre-condition Screen for the heater/cooler workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_next_button_inactive(self):
        next_button = self.get_element(BasePageLocators.NEXT_BUTTON_LABEL)
        next_button_state = next_button.get_attribute("ng-reflect-available")
        active_element_state = next_button_state.find("false")
        self.logger.info(f"The next_button_state==>>{next_button_state} ")

        if active_element_state != -1:
            return True
        return False

    def get_welcome_paragraph_text(self):
        return [
            self.get_text(HeaterCoolerWelcomeLocators.WELCOME_PARAGRAPH_ONE),
            self.get_text(HeaterCoolerWelcomeLocators.WELCOME_PARAGRAPH_TWO)
        ]

    def get_summary_details(self):
        ambient_temperature_string = self.get_text(HeaterCoolerPreconditionLocators.AMBIENT_TEMPERATURE_INFO_LABEL)
        self.logger.info(f" ambient_temperature_string ======  {ambient_temperature_string}")
        ambient_temperature = ambient_temperature_string[-2:]

        column_temperature_string = self.get_text(HeaterCoolerPreconditionLocators.COLUMN_TEMPERATURE_INFO_LABEL)
        column_temperature = column_temperature_string[-2:]
        column_door_state = self.get_text(HeaterCoolerPreconditionLocators.COLUMN_DOOR_INFO_LABEL)

        heater_cooler_summary_details = HeaterCoolerSummaryDetails(ambient_temperature,
                                                                   column_temperature,
                                                                   column_door_state)
        self.logger.info(f"heater_cooler_summary_details===>>>{heater_cooler_summary_details}")
        return heater_cooler_summary_details
