from typing import Tuple

from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.constants.wait_time_constants import WaitTimeConstants
from web_framework.web_driver_common.constants import DEFAULT_WAIT_TIME


def is_element_visible(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def is_element_present(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        return True
    except TimeoutException:
        return False


def validate_element_not_present(driver: WebDriver, locator: Tuple[By, str], timeout: int = 1, message: str = None):
    message = message or f"Element described by locator: {locator} was found on the page"
    is_visible = is_element_visible(driver, locator, timeout)
    assert not is_visible, message


def is_displayed(driver: WebDriver, locator: Tuple[str, str]):
    """
    Returns whether the locator is visible to user
    :param driver: Instance of WebDriver
    :param locator: Tuple with By type and search value
    :return: Boolean
    """
    try:
        return driver.find_element(*locator).is_displayed()
    except NoSuchElementException:
        return False


def get_text(driver: WebDriver, locator: Tuple[str, str]):
    """
    Returns the text of the given web locator
    :param locator: desired locator for getting text
    :param driver: instance of WebDriver
    :return: text of the web locator
    """
    try:
        ignored_exceptions = (StaleElementReferenceException,)
        your_element = WebDriverWait(driver, DEFAULT_WAIT_TIME, ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located(locator))
        return your_element.text.strip()
    except TimeoutException:
        assert False, f"The click action on locator {locator} is not complete within {DEFAULT_WAIT_TIME} seconds."
    except NoSuchElementException:
        assert False, f"The locator {locator} not found to perform get_text action"


def assert_element_visible(driver, locator, element_description, timeout=WaitTimeConstants.SmallWait):
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))
    except Exception as e:
        assert False, f"WinAppDriver failed to find {element_description}, by locator: {locator}, with error: [{e}]"


def is_displayed_with_timeout(driver: WebDriver, locator: Tuple[str, str], wait_time: int = 5):
    """
    An expectation for checking that all elements are present on the DOM of a
    page and visible. Visibility means that the elements are not only displayed
    but also has a height and width that is greater than 0.h
    :param driver:
    :param wait_time:
    :param locator:
    :return:
    """
    try:
        WebDriverWait(driver, wait_time).until(EC.visibility_of_all_elements_located(locator))
        return True
    except TimeoutException:
        return False
    except NoSuchWindowException:
        return False
