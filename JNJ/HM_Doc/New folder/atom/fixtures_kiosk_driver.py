"""
File_Name: fixtures_function_scope.py
Desc:
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__ = "Sharmila Vairamani" Changed the logging implementation - 04/27/2020
__modified__ = "Sharmila Vairamani" implemented thread storage to capture screenshots - 10/30/2020
__modified__ = "Sharmila Vairamani" removed autouse in the function browser - 11/04/2020

"""
import os
import threading
from typing import Type, TypeVar, Callable

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures_configurations import BrowserConfiguration
from utilities.assert_timeout import AssertTimeout
from utilities.configuration_models import EnvironmentType
from utilities.logger import Logger
from web_framework.kiosk.common.Browsers.browser_factory import BrowserFactory
from web_framework.kiosk.common.Browsers.chrome_browser_factory import BrowserDriverFactory
from web_framework.kiosk.common.Browsers.remote_browser_factory import RemoteBrowserFactory
from web_framework.kiosk.pages.base_page import BasePage

logger = Logger(os.path.basename(__file__))

default_chrome_executable = "chromedriver"

PageBaseTypeGeneric = TypeVar("PageBaseTypeGeneric", bound=BasePage)

PageCreator = Callable[[Type[PageBaseTypeGeneric]], PageBaseTypeGeneric]


@pytest.fixture(scope='session')
def browser_factory(settings, environment_type: EnvironmentType, browser_config: BrowserConfiguration, run_on_local: bool) -> BrowserFactory:
    if run_on_local:
        executable_path = ChromeDriverManager().install().replace("/", "\\")
        return BrowserDriverFactory(browser_config.headless, browser_config.results_folder, executable_path)
    elif environment_type == EnvironmentType.CDS:
        executable_path = ChromeDriverManager().install().replace("/", "\\")
        return RemoteBrowserFactory(settings.host, settings.host_username, settings.host_password, browser_config.headless, executable_path)
    elif environment_type == EnvironmentType.SIMULATION or environment_type == EnvironmentType.REAL:
        return BrowserDriverFactory(browser_config.headless, browser_config.results_folder, default_chrome_executable)
    else:
        raise ValueError(f"Unsupported platform to start chrome driver: [{environment_type}]")


@pytest.fixture(scope='session')
def session_browser(browser_factory) -> WebDriver:
    """
    Session scope fixture to  return the currently configured web driver, which will
    be used by all function scope related test script fixtures.  These test scripts must
    be designed to handle each scenario in a separate browser instance.`
    :return: WebDriver
    """
    web_driver = browser_factory.create_web_driver()
    logger.debug("From browser, before yielding web driver in function_browser fixture")
    yield web_driver
    web_driver.quit()
    browser_factory.stop()


@pytest.fixture
def browser(session_browser: WebDriver, kiosk_base_url):
    """
    Function scope fixture to  return the currently configured web driver, which will
    be used by all function scope related test script fixtures.  These test scripts must
    be designed to handle each scenario in a separate browser instance.`
    :return: WebDriver
    """
    session_browser.get(kiosk_base_url)
    current_thread = threading.current_thread()
    setattr(current_thread, 'web_driver', session_browser)
    yield session_browser
    delattr(current_thread, 'web_driver')
    # session_browser.close()


@pytest.fixture
def page_builder(browser, kiosk_base_url, assert_timeout: AssertTimeout) -> PageCreator:
    """
    Function scope fixture to return function handler, that builds/constructs
    the page for a given page type.
    :param kiosk_base_url:
    :param browser:
    :param assert_timeout:
    :return: function
    """

    def get_page(page_type: Type[PageBaseTypeGeneric]):
        logger.debug(f"Creating instance of [{page_type}] page")
        page = page_type(driver=browser, base_url=kiosk_base_url, assert_timeout=assert_timeout)
        logger.debug(f"Browser page [{page_type}] created successfully")

        return page

    return get_page
