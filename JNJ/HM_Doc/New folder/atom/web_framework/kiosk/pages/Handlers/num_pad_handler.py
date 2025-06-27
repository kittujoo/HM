"""
File_Name: num_pad_handler.py
Desc: This file contains the common shared code related to numpad actions across all the pages
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in - 06/11/2020
"""
import time

from utilities.logger import Logger
from web_framework.kiosk.pages.Handlers.web_elements_handler import WebElementsHandler
from web_framework.kiosk.pages.Handlers.touch_actions_handler import TouchActionsHandler
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators


class NumPadHandler:
    """
        Num pad handler class that contains
            common shared code across all the pages
    """

    number_pad_dictionary = {
        "1": BasePageLocators.NUM_PAD_1_BUTTON,
        "2": BasePageLocators.NUM_PAD_2_BUTTON,
        "3": BasePageLocators.NUM_PAD_3_BUTTON,
        "4": BasePageLocators.NUM_PAD_4_BUTTON,
        "5": BasePageLocators.NUM_PAD_5_BUTTON,
        "6": BasePageLocators.NUM_PAD_6_BUTTON,
        "7": BasePageLocators.NUM_PAD_7_BUTTON,
        "8": BasePageLocators.NUM_PAD_8_BUTTON,
        "9": BasePageLocators.NUM_PAD_9_BUTTON,
        "0": BasePageLocators.NUM_PAD_0_BUTTON,
        ".": BasePageLocators.NUM_PAD_DECIMAL}

    def __init__(self, driver):
        super().__init__()
        self.logger = Logger(self.__class__.__name__)
        self._driver = driver

    def enter_value(self, number):
        """
        THis functions allows the user to enter any number in the numpad entry field
        :param number:
        :return:
        """
        if number is None:
            return

        index = 0
        while index < len(number):
            if number[index] in NumPadHandler.number_pad_dictionary:
                locator = NumPadHandler.number_pad_dictionary[number[index]]
                self.logger.info(f"Locator value => {locator}")
                TouchActionsHandler.tap(self._driver, locator)
            index += 1

    def tap_delete_button(self, no_of_times):
        """
        Tap delete button for a given number of times.
        :param no_of_times:
        :return: void
        """
        index = 0
        locator = BasePageLocators.NUM_PAD_DELETE_BUTTON
        while index < no_of_times:
            time.sleep(.1)
            TouchActionsHandler.tap_text_field(self._driver, locator)
            index += 1

    def clear_num_pad_entries(self, text_field_locator):
        """
        This function clears the content in the numpad entry field
        :param text_field_locator:
        :return:
        """
        entries = WebElementsHandler.get_element(self._driver, text_field_locator)
        entries = entries.get_attribute("ng-reflect-value")
        self.logger.info(f"*********************************entries  ====> {entries}")
        entries_count = len(entries)
        self.logger.info(f"**************************entries count ====> {entries_count}")
        self.tap_delete_button(entries_count)
