import os.path
import time
import traceback
from typing import Tuple
from uuid import uuid4

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.atom.constants import RESULTS_FOLDER
from utilities.logger import Logger
from utilities.win_app_driver_utilities import set_element_text
from web_framework.web_driver_common.constants import WIN_APP_BY
from web_framework.web_driver_common.element import is_displayed, get_text, is_displayed_with_timeout


class WinAppBasePage:

    def __init__(self, driver: WebDriver):
        self._logger = Logger(self.__class__.__name__)
        self._driver: WebDriver = driver
        self.wait_time = 5

    def validate_opened(self):
        """Method that should validate that driver located on current page"""
        pass

    def validate_setup_screen(self):
        pass
        # next code left as an example:
        # locator = SetupScreenLocators.SETUP_HEADER
        # screen_name = "setup screen"
        # self.validate_screen(locator, screen_name, self.wait_time)

    def validate_screen(self, locator, screen_name, wait_time):
        """
        This function is to validate any given screen before execution of the test scripts
        """
        screen_exists = False
        try:
            self.wait_for_element_visibility(locator, wait_time)
            screen_exists = self.is_displayed(locator)
        except Exception:
            time.sleep(wait_time)
            try:
                self.wait_for_element_visibility(locator, wait_time)
                screen_exists = self.is_displayed(locator)
            except Exception as generic_exception:
                traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
        self._logger.info(f"The {screen_name} is displayed => {screen_exists}")
        assert screen_exists, f"Failed to move to {screen_name} "

    def wait_for_element_visibility(self, locator, wait_time):
        """
        An expectation for checking that all elements are present on the DOM of a
        page and visible. Visibility means that the element is not only displayed,
        but also has a height and width that is greater than 0.h
        :param wait_time:
        :param locator:
        :return:
        """
        try:
            return WebDriverWait(self._driver, wait_time).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            assert False, f"The control for locator '{locator}' was not visible in the given time {wait_time}."

    def is_displayed_with_timeout(self, wait_time, locator):
        """
        An expectation for checking that all elements are present on the DOM of a
        page and visible. Visibility means that the elements are not only displayed
        but also has a height and width that is greater than 0.h
        :param wait_time:
        :param locator:
        :return:
        """
        return is_displayed_with_timeout(self._driver, locator, wait_time)

    def is_displayed(self, locator):
        """
        Returns whether the locator is visible to user
        :param locator:
        :return: Boolean
        """
        return is_displayed(self._driver, locator)

    def press_ok(self):
        ok_button = self._driver.find_element(WIN_APP_BY, '1')
        ok_button.click()

    def press_yes_by_name(self):
        ok_button = self._driver.find_element_by_name('Yes')
        ok_button.click()

    def press_ok_by_name(self):
        ok_button = self._driver.find_element_by_name('OK')
        ok_button.click()

    def press_continue_by_name(self):
        continue_button = self._driver.find_element_by_name('Continue')
        continue_button.click()

    def press_save(self):
        save_button = self._driver.find_element_by_name("Save")
        save_button.click()

    def find_element(self, locator: Tuple[str, str]):
        element = self._driver.find_element(*locator)
        return element

    def find_elements(self, locator: Tuple[str, str]):
        elements = self._driver.find_elements(*locator)
        return elements

    def click_on_element(self, locator: Tuple[str, str]) -> None:
        element = self.find_element(locator)
        element.click()

    def get_element_attribute(self, locator: Tuple[str, str], attribute: str):
        element = self.find_element(locator)
        attribute_value = element.get_attribute(attribute)
        return attribute_value

    def get_element_name_attribute(self, locator: Tuple[str, str]):
        name = self.get_element_attribute(locator, "Name")
        return name

    def set_text(self, locator: Tuple[str, str], text: str):
        element = self.find_element(locator)
        set_element_text(element, str(text))

    def clear_and_set_text(self, locator: Tuple[str, str], text: str):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Returns the text of the given web locator
        :param locator: desired locator for getting text
        :return: text of the web locator
        """
        return get_text(self._driver, locator)

    def double_click(self, locator: Tuple[str, str]):
        element = self.find_element(locator)
        ActionChains(self._driver).double_click(on_element=element).perform()

    def save_page_source(self, file_path=RESULTS_FOLDER):
        source = self._driver.page_source
        file_name = os.path.join(file_path, f"page_source-{uuid4()}.xml")
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(source)
