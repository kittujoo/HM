"""
File_Name: replace_needle_screen.py
Desc: This file contains specific user action on all the screen in the replace needle screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 09/19/2022

"""
import time

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_needle_constants import ReplaceNeedleConstant
from web_framework.kiosk.pages.Locators.Maintain.replace_needle_workflow_locators import (ReplaceNeedleWelcomeScreenLocators,
                                                                                          ReplaceNeedlePreconditionsScreenLocators)
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceNeedleScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def get_welcome_paragraph_text(self):
        self.logger.info(
            "The replace needle workflow begins workflow++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return [self.get_text(ReplaceNeedleWelcomeScreenLocators.WELCOME_PARA_ONE),
                self.get_text(ReplaceNeedleWelcomeScreenLocators.WELCOME_PARA_TWO),
                self.get_text(ReplaceNeedleWelcomeScreenLocators.WELCOME_PARA_THREE)]

    def get_customs_text(self):
        time.sleep(1)
        actual_text = self.get_text(ReplaceNeedleWelcomeScreenLocators.CAUTION_TEXT)
        self.logger.info(f"actual_text=====>>>>{actual_text}")
        return actual_text

    def validate_warning_text(self):
        actual_paragraph_text = self.get_warning_text()
        self.logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ReplaceNeedleConstant.warning_text
        self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    def get_warning_text(self):
        time.sleep(1)
        actual_text = self.get_text(ReplaceNeedlePreconditionsScreenLocators.WARNING_TEXT)
        self.logger.info(f"actual_text=====>>>>{actual_text}")
        return actual_text
