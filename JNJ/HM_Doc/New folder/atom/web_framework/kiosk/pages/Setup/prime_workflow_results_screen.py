"""
File_Name: prime_results_screen.py
Desc: This file contains specific user action on the prime solvents workflow setup screens
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/25/23
"""
from utilities.logger import Logger
from web_framework.kiosk.pages.base_page import BasePage


class PrimeResultScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Prime Solvents results Screen"
