"""
file_Name: pump_module_configuration_screen.py
Desc: This file contains specific user actions on the elements in the system screen which includes
      solvent manager module
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/3/2021
__modified__ = Tyler Prada" refactoring for pump module 1/4/23
"""

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.SolventManager.pump_module_configuration_screen import PumpModuleConfigurationScreenlocators
from web_framework.kiosk.pages.base_page import BasePage


class PumpModuleConfigurationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_pump_module_configuration_screen(self):
        locator = PumpModuleConfigurationScreenlocators.SOLVENT_MANAGER_CONFIGURATION_MENU
        screen_name = "Solvent manager configuration screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_fluidic_light_chamber_panel(self):
        self.tap(PumpModuleConfigurationScreenlocators.FLUIDIC_CHAMBER_LIGHT_PANEL)

    def tap_leak_detection_panel(self):
        self.tap(PumpModuleConfigurationScreenlocators.LEAK_DETECTION_PANEL)

    def tap_noflow_shutdown_panel(self):
        self.tap(PumpModuleConfigurationScreenlocators.NOFLOW_SHUTDOWN_PANEL)
