"""
File_Name: replace_needle_status_screen.py
Desc: This file contains specific user action on all the screen in the calibrate wavelength workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/13/2022

"""
import time

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.replace_needle_constants import ReplaceNeedleConstant
from web_framework.kiosk.pages.Locators.Maintain.replace_needle_workflow_locators import StatusAndTestsScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class ReplaceNeedleStatusScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_progress_bar(self):

        start_time = time.time()
        current_progress_value = None
        while time.time() - start_time < 600:
            current_progress_value = self.get_progress_value()
            self.logger.info(f"current_progress_value===>>>>{current_progress_value}")

            if current_progress_value == 95.0:
                break
            time.sleep(1)

        assert current_progress_value == 95.0, f"The progress bar does not function"

    def get_progress_value(self):
        progress_bar_element = self.get_element(StatusAndTestsScreenLocators.PROGRESS_BAR)
        progress_bar_element_value = progress_bar_element.get_attribute("ng-reflect-value")

        progress_bar_element_value = TypeConverter.to_float(progress_bar_element_value)

        return progress_bar_element_value

    def get_procedure_text(self):
        self.logger.info(
            "The replace needle workflow begins workflow++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return [self.get_text(StatusAndTestsScreenLocators.REPLACE_NEEDLE_TEST_PARA_ONE),
                self.get_text(StatusAndTestsScreenLocators.REPLACE_NEEDLE_TEST_PARA_TWO),
                self.get_text(StatusAndTestsScreenLocators.REPLACE_NEEDLE_TEST_PARA_THREE)]

    def validate_tests_running_text(self):
        actual_paragraph_text = self.get_tests_text()
        self.logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")

        expected_paragraph_text = ReplaceNeedleConstant.expected_test_text
        self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"

    def get_tests_text(self):
        return [self.get_text(StatusAndTestsScreenLocators.TEST_ONE),
                self.get_text(StatusAndTestsScreenLocators.TEST_TWO),
                self.get_text(StatusAndTestsScreenLocators.TEST_THREE)]

    def validate_information_text(self):
        time.sleep(3)
        actual_paragraph_text1 = self.get_text(StatusAndTestsScreenLocators.INFORMATION_TEXT)
        self.logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text1}")

        expected_paragraph_text = ReplaceNeedleConstant.information_text
        self.logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
        assert actual_paragraph_text1 == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text1}"
    #
    # def get_information_text(self):
    #     time.sleep(1)
    #     actual_text1 =
    #     self.logger.info(f"actual_text43643547547547=====>>>>{actual_text1}")
    #     return actual_text1
