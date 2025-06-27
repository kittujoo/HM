"""
    File_Name: startup_workflow_driver.py
    Desc: This file contains driver specific actions on control startup workflow.
    __copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
    __author__    = "Imran Abbas Satti" Initial Check-in 01/20/2023

"""
from utilities.logger import Logger

from web_framework.kiosk.common.Constants.UI.WorkflowConstants.startup_constants import StartupConstants
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Locators.Setup.setup_screen_locators import SetupScreenLocators
from web_framework.kiosk.pages.Locators.Setup.startup_workflow_locators import (StartupSummaryLocators, StartupWorkflowLocators)
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Setup.setup_home_screen import SetupHomeScreen
from web_framework.kiosk.pages.Setup.startup_workflow_screen import StartupWorkflowSetupScreen
from web_framework.kiosk.pages.Setup.startup_workflow_summary_screen import StartupWorkflowSummaryScreen


class StartUpWorkFlowDriver(object):
    """
    Class to control startup workflow actions
    """

    def __init__(self, page_builder):
        self.setup_screen_page: SetupHomeScreen = page_builder(SetupHomeScreen)
        self.startup_workflow_setup_page: StartupWorkflowSetupScreen = page_builder(StartupWorkflowSetupScreen)
        self.startup_workflow_summary_screen: StartupWorkflowSummaryScreen = page_builder(StartupWorkflowSummaryScreen)
        self.flow_setting_screen_page: FlowSettingsScreen = page_builder(FlowSettingsScreen)
        self.logger = Logger(self.__class__.__name__)

    def validate_startup_welcome_screen(self):
        """
        Driver to validate the welcome screen after hitting startup button
        :return: None
        """
        self.setup_screen_page.validate_setup_screen()
        self.setup_screen_page.tap(SetupScreenLocators.STARTUP_INS_ACQUISITION)
        self.startup_workflow_setup_page.validate_welcome_screen()

    def validate_default_flow_upto_startbtn(self):
        """
        Driver to validate the startup flow with default values
        :return: None
        """
        self.startup_workflow_setup_page.wait_for_element_visibility(5, BasePageLocators.NEXT_BUTTON_LABEL)
        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_prime_solvent_screen()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_seal_wash()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_needle_wash()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_sample_metering_pump_duration()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_sample_metering_pump_composition()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_temperature_control_screen()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_detector_screen()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.validate_equilibration_screen()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_summary_screen.validate_startup_summary_screen()

        self.startup_workflow_setup_page.tap_next_button()
        self.startup_workflow_setup_page.wait_for_element_load(
            StartupWorkflowLocators.START_BUTTON,
            StartupConstants.DefaultTestTime)
        self.startup_workflow_setup_page.tap(StartupWorkflowLocators.START_BUTTON)

    def validate_instrument_startup_status(self):
        """
        Driver to validate startupflow. Returns true in case of workflow is not completed
        :return: Bool
        """
        self.startup_workflow_setup_page.wait_for_element_load(
            StartupSummaryLocators.STARTUP_PROGRESS_BANNER,
            StartupConstants.DefaultTestTime)
        self.startup_workflow_setup_page.validate_element_wait_condition(
            StartupSummaryLocators.STARTUP_PROGRESS_BANNER,
            StartupSummaryLocators.STARTUP_COMPLETE_BANNER,
            StartupConstants.DefaultTestTime)
        self.flow_setting_screen_page.tap_done_button()
        return self.startup_workflow_setup_page.is_displayed(
            StartupSummaryLocators.WORKFLOW_STOPPED_UNEXPECTEDLY)
