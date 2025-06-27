"""
File_Name: instrument_configuration_screen.py
Desc: This file contains specific user actions on the elements in the instrument configuration screen page
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 02/02/2021
__modified__ = "Tyler Prada" added column manager 12/15/21
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.Locators.System.instrument_configuration_screen import InstrumentConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.base_page import BasePage


class InstrumentConfigurationScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_instrument_configuration_screen(self):
        locator = InstrumentConfigurationScreenLocators.HEADER
        screen_name = "System Settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def wait_for_settings_save(self):
        self.wait_for_element_visibility(WaitTimeConstants.MidWait, InstrumentConfigurationScreenLocators.OPTIONS_PANEL)
        # even when visible, taking a second to be able to click properly afterwards
        self.wait_till_element_is_invisible(BasePageLocators.DONE_BUTTON, self.wait_time)

    def tap_tuv_icon(self):
        self.tap(InstrumentConfigurationScreenLocators.TUV_ICON)

    def tap_sm_icon(self):
        self.tap(InstrumentConfigurationScreenLocators.SAMPLE_MANAGER_ICON)

    def tap_solvent_manager_icon(self):
        self.tap(InstrumentConfigurationScreenLocators.SOLVENT_MANAGER_ICON)

    def tap_column_manager_icon(self):
        self.tap(InstrumentConfigurationScreenLocators.COLUMN_MANAGER_ICON)

    def tap_bottle_icon(self):
        self.tap(InstrumentConfigurationScreenLocators.BOTTLE_ICON)
