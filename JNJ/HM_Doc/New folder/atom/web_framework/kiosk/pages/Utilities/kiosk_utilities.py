"""
File_Name: kiosk_utilities.py
Desc: This file contains the common methods shared between classses
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in - 11/1/2021
"""

from utilities.logger import Logger


class KioskUtilities:

    def __init__(self, driver):
        super().__init__()
        self.logger = Logger(self.__class__.__name__)
        self._driver = driver

    def add_xpath_to_locator(self, locator, xpath_addition):
        """
        This method takes base xpath locator, appends more xpath, and returns a new element locator
        @param locator: an xpath locator | ex: //ics-input-stepper
        @param xpath_addition: a string of xpath to be added to the locator | ex: //div[@id='input-plus']
        @return: new locator which combines base locator to the additional xpath | ex: //ics-input-stepper//div[@id='input-plus']
        """
        locator_list = list(locator)
        locator_list[1] = locator_list[1] + xpath_addition
        new_locator = tuple(locator_list)
        return new_locator