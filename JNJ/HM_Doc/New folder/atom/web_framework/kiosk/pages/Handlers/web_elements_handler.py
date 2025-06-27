"""
File_Name: web_elements_handler.py
Desc: This file contains the common shared code related to web elements across all the pages
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in - 06/11/2020
__modified__ = "sharmila Vairamani" Added new function - 06/16/2020
__modified__ = "Sharmila Vairamani" refactored get_container_text function - 09/28/2020
__modified__ = "Sharmila Vairamani" change the logger to reflect the correct class name - 11/04/2020
__modified__ = "Sharmila Vairamani" Refactor get_container_text function - 05/27/2021
__modified__ = "Tyler Prada" Added get_input_value method 10/8/21
__modified__ = "Tyler Prada" Added get_elements method 11/1/21
"""
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from utilities.logger import Logger
from web_framework.web_driver_common.element import get_text

logger = Logger(__name__)


class WebElementsHandler:
    wait_time = 5

    @staticmethod
    def get_container_text(driver, locator):
        """
        Returns the text of the locator from the div/span tags
        :param locator: locator of the text to be retrieved from div/span tags
        :param driver: driver
        :return: text of the web locator

        """
        try:
            time.sleep(1)
            return get_text(driver, locator)
        except StaleElementReferenceException as st_exception:
            logger.warning(
                f"Caught StaleElementReferenceException, try to locate after sleep for locator {locator} ")
            time.sleep(1)
            try:
                none_count = 0
                while none_count < WebElementsHandler.wait_time:
                    container_text = driver.find_element(*locator).text
                    if container_text is None:
                        logger.warning(f"After getting None for  container text {container_text}")
                        time.sleep(1)
                        none_count += 1
                    else:
                        logger.info(f"After Caught StaleElementReferenceException, container text ->{container_text}<-")
                        logger.info(f"the locator of the container_test ==={locator}")
                        return container_text
            except NoSuchElementException as exception:
                assert False, f"The locator {locator} not found to perform get text action"

    @staticmethod
    def get_entered_value(driver, locator):
        """
        This function returns the value entered by the user in the text box
        @param driver: driver
        @param locator: locator that houses the value to be retrieved
        :param locator: locator of the edit field
        :return: value entered by the user
        """
        try:
            return driver.find_element(*locator).get_attribute("ng-reflect-value")
        except NoSuchElementException as exception:
            assert False, f"The locator {locator} not found to perform get input value action"

    @staticmethod
    def get_element(driver, locator):
        """
        This function returns the element of the given locator. This method is used mainly when we need to
        manipulate data/user actions from the given locator of the webelement.
        :param driver:
        :param locator:
        :return: element
        """
        try:
            return driver.find_element(*locator)
        except StaleElementReferenceException as st_exception:
            logger.warning(
                f"Caught StaleElementReferenceException, try to locate after sleep for locator {locator} ")
            time.sleep(1)
            try:
                none_count = 0
                while none_count < WebElementsHandler.wait_time:
                    element = driver.find_element(*locator)
                    if element is None:
                        logger.warning(f"After getting None for  container text {element}")
                        time.sleep(1)
                        none_count += 1
                    else:
                        logger.info(f"After Caught StaleElementReferenceException, container text ->{element}<-")
                        logger.info(f"the locator of the container_test ==={locator}")
                        return element
            except NoSuchElementException as exception:
                assert False, f"The locator {locator} not found to perform get text action"

    @staticmethod
    def get_elements(driver, locator):
        """
        This function returns an element list of the given locator.
        :param driver:
        :param locator:
        :return: element list
        """
        try:
            return driver.find_elements(*locator)
        except NoSuchElementException as exception:
            assert False, f"The locator {locator} not found to perform get elements action"

    @staticmethod
    def is_selected(driver, locator):
        """
        Returns whether the locator is selected
        Can be used to check if a checkbox or radio button is selected.
        :param locator:
        :return: Boolean
        """
        try:
            return driver.find_element(locator).is_selected()
        except NoSuchElementException as exception:
            return False

    @staticmethod
    def is_enabled(driver, locator):
        """
        Returns whether the locator is enabled to user
        :param locator:
        :return: Boolean
        """
        try:
            return driver.find_element(*locator).is_enabled()
        except NoSuchElementException as exception:
            return False
