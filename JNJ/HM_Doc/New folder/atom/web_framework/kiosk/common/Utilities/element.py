from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_element_visibility(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10, proceed_on_absence: bool = False):
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException as e:
        if not proceed_on_absence:
            raise e from None
        return None
    return element


def wait_for_element_invisibility(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10):
    element = WebDriverWait(driver, timeout).until(EC.invisibility_of_element(locator))
    return element
