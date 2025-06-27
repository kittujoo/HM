"""
File_Name: replace_components_screen.py
Desc: This file contains specific user action on all the screen in the calibrate wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/13/2022

"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Maintain.replace_components_locators import ReplaceComponentsScreenPageLocators
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceComponentsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def tap_replace_seal_tab(self):
        self.tap(ReplaceComponentsScreenPageLocators.REPLACE_SEAL)

    def tap_replace_needle_tab(self):
        self.tap(ReplaceComponentsScreenPageLocators.REPLACE_NEEDLE)
