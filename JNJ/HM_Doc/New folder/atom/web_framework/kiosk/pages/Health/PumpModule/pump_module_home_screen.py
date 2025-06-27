"""
File_Name: pump_module_home_screen.py
Desc: This file contains specific user action on the instrument diagnostic screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022

"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.instrument_diagnostic_locators import InstrumentDiagnosticLocators
from web_framework.kiosk.pages.base_page import BasePage


class PumpModuleHomeScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Health home screen"

    def validate_instrument_diagnostic_screen(self):
        locator = InstrumentDiagnosticLocators.HEADER
        screen_name = "Instrument Diagnostic  screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def tap_pump_module(self):
        self.tap(InstrumentDiagnosticLocators.SOLVENT_MANAGER_ICON)
