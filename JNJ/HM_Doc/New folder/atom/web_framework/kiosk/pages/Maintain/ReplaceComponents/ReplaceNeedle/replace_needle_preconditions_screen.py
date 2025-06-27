"""
File_Name: replace_needle_precondition_screen.py
Desc: This file contains specific user action on all the screen in the calibrate wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/13/2022

"""

from utilities.logger import Logger

from web_framework.kiosk.pages.base_page import BasePage


class ReplaceNeedlePreconditionsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

        self.logger = Logger(self.__class__.__name__)
