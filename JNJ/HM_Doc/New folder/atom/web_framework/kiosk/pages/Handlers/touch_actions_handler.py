"""
File_Name: touch_actions_handler.py
Desc: This file contains the common shared code related to touch actions across all the pages
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in - 06/11/2020
__modified__ = "sharmila Vairamani" Added new function - 06/16/2020
__modified__ = "Sharmila Vairamani" removed not needed logger info - 11/04/2020
__modified__="Sharmila Vairamani" Refactor tap function to handle stale element exception - 05/27/2020
__modified__ "Tyler Prada" Added the release function to work in tandem with tap-and-hold 7/2/21
__modified__ "Tyler Prada" Added scroll_from_element 8/20/21
"""
import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import TouchActions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logger import Logger
from web_framework.kiosk.pages.Handlers.web_elements_handler import WebElementsHandler

logger = Logger("TouchActionsHandler")


class TouchActionsHandler:

    @staticmethod
    def tap(driver: WebDriver, locator):
        """
        Taps on a given locator.
        :param locator:
        :param driver:
        :return: void

        """

        start_time = time.time()
        while time.time() - start_time <= WebElementsHandler.wait_time:
            try:
                WebDriverWait(driver, WebElementsHandler.wait_time) \
                    .until(expected_conditions.element_to_be_clickable(locator))
                is_element_visible = driver.find_element(*locator).is_displayed()
                if is_element_visible:
                    target_element = driver.find_element(*locator)
                    action = TouchActions(driver)
                    action.tap(target_element).perform()
                    return
            except NoSuchElementException as exception:
                logger.warning(
                    f"Caught NoSuchElementException, try to locate after sleep for locator {locator} ")
            except StaleElementReferenceException as st_exception:
                logger.warning(
                    f"Caught StaleElementReferenceException, try to locate after sleep for locator {locator} ")
            time.sleep(1)

        assert False, f"Expected locator {locator} is not found"

    @staticmethod
    def tap_text_field(driver, locator):
        """
        Taps on a given text input field. This function should be used when the user wants to tap on the text/
        text input field
        :param locator of any text input field
        :param driver:
        :return: void

        """
        try:
            target_element = WebDriverWait(driver, WebElementsHandler.wait_time) \
                .until(expected_conditions.visibility_of_element_located(locator))
            action = TouchActions(driver)
            action.tap(target_element).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {locator} is not found"

    @staticmethod
    def long_press(driver, locator):
        """
        Taps on a given locator.
        :param locator:
        :param driver:
        :return: void

        """
        try:
            target_element = driver.find_element(*locator)
            action = TouchActions(driver)
            action.long_press(target_element).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {locator} is not found"

    @staticmethod
    def tap_and_hold(driver, xcord, ycord):
        """
        Taps on a given locator.
        :param locator:
        :param driver:
        :return: void

        """
        try:

            action = TouchActions(driver)
            action.tap_and_hold(xcord, ycord).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {xcord} {ycord} is not found"

    @staticmethod
    def release(driver, xcord, ycord):
        """
        Releases the hold from the tap_and_hold method
        :param locator:
        :param driver:
        :return: void

        """
        try:

            action = TouchActions(driver)
            action.release(xcord, ycord).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {xcord} {ycord} was not found"

    @staticmethod
    def scroll_from_element(driver, locator, xoffset, yoffset):

        try:
            target_element = driver.find_element(*locator)
            action = TouchActions(driver)
            action.scroll_from_element(target_element, xoffset, yoffset).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {locator} was not found"

    @staticmethod
    def scroll(driver, xoffset, yoffset):
        try:

            action = TouchActions(driver)
            action.scroll(xoffset, yoffset).perform()
        except NoSuchElementException as exception:
            assert False, f"Expected locator {xoffset} {yoffset} was not found"
