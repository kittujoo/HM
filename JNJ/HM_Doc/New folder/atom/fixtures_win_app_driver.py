import os
import threading
from typing import Tuple

import pytest
from selenium.common.exceptions import NoSuchWindowException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utilities.logger import Logger
from web_framework.empower.pages.configuration.instrument_method_creation_page import InstrumentMethodCreationPage

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def win_app_driver_url(settings):
    host = settings.empower_hostname
    port = settings.empower_port
    return f"http://{host}:{port}"


@pytest.fixture(scope='function')
def win_app_root_driver(win_app_driver_url) -> WebDriver:
    desired_caps = {"platformName": "Windows",
                    "app": "Root",
                    "deviceName": "WindowsPC"}

    driver = WebDriver(
        command_executor=win_app_driver_url,
        desired_capabilities=desired_caps)
    current_thread = threading.current_thread()
    setattr(current_thread, 'win_app_driver', driver)
    yield driver
    delattr(current_thread, 'win_app_driver')
    driver.close()


class WinAppDriverHandler:

    def __init__(self, win_app_root_driver: WebDriver, win_app_driver_url: str, implicit_wait_time: int = 5):
        self.win_app_root_driver: WebDriver = win_app_root_driver
        self._win_app_driver_url: str = win_app_driver_url
        self.driver_storage = []
        self.implicit_wait_time: int = implicit_wait_time

    def _get_window_handle(self, locator, wait_time_sec=30):

        try:
            wait = WebDriverWait(self.win_app_root_driver, wait_time_sec)
            # locator = (By.XPATH, f"//Window[contains(@Name, '{window_name}')]")
            element = wait.until(
                EC.visibility_of_element_located(locator))

            if not element:
                return None

            if handle := element.get_attribute("NativeWindowHandle"):
                return hex(int(handle))

            raise ValueError(f"Window with locator {locator} had empty NativeWindowHandle attribute")
        except TimeoutException:
            logger.debug(f"Failed to get native handler of [{locator}]")
            raise ValueError(f"Failed to locate Window with locator {locator}")

    def attach_to_running_application_by_locator(self, locator: Tuple[By, str], wait_time_sec):
        handle = self._get_window_handle(locator, wait_time_sec)
        driver = WebDriver(
            command_executor=self._win_app_driver_url,
            desired_capabilities={"platformName": "Windows",
                                  "appTopLevelWindow": handle})
        driver.implicitly_wait(self.implicit_wait_time)
        try:
            driver.maximize_window()
        except WebDriverException:
            logger.debug(f"Failed to maximize window located by {locator}, seems current application doesnt support maximizing of the main window")
        self.driver_storage.append(driver)
        return driver

    def attach_to_running_application(self, window_name, wait_time_sec=30) -> WebDriver:
        return self.attach_to_running_application_by_locator((By.XPATH, f"//Window[contains(@Name, '{window_name}')]"), wait_time_sec)

    def attach_to_running_application_by_xpath(self, xpath, wait_time_sec=30) -> WebDriver:
        return self.attach_to_running_application_by_locator((By.XPATH, xpath), wait_time_sec)

    def start_application(self, exec_path, extra_capabilities=None) -> WebDriver:
        desired_caps = {"app": exec_path,
                        "ms:experimental-webdriver": True}
        if extra_capabilities:
            desired_caps = {**desired_caps, **extra_capabilities}
        driver = WebDriver(
            command_executor=self._win_app_driver_url,
            desired_capabilities=desired_caps)
        driver.implicitly_wait(self.implicit_wait_time)
        try:
            driver.maximize_window()
        except WebDriverException:
            logger.debug(f"Failed to maximize window located by {exec_path}, seems current application doesnt support maximizing of the main window")
        self.driver_storage.append(driver)
        return driver

    def stop(self):
        for drv in self.driver_storage:
            try:
                for item in drv.find_elements_by_xpath("//Button[@Name='Close']"):
                    item.click()
                instrument_page = InstrumentMethodCreationPage(drv)
                if instrument_page.is_save_dialog_displayed():
                    instrument_page.close_unsaved_changes_dialog()
                drv.quit()
            except NoSuchWindowException:
                pass


@pytest.fixture(scope='function')
def win_app_driver_handler(win_app_root_driver: WebDriver, win_app_driver_url: str) -> WinAppDriverHandler:
    handler = WinAppDriverHandler(win_app_root_driver, win_app_driver_url)
    yield handler
    handler.stop()
