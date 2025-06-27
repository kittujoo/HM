from typing import Tuple, Union

from selenium.webdriver.common.by import By

from utilities.logger import Logger
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY


class SingleInjectionTab(WinAppBasePage):
    SAMPLE_NAME_INPUT_LOCATOR = (WIN_APP_BY, '20311')
    FUNCTION_DROPDOWN_LOCATOR = (WIN_APP_BY, '20485')
    METHOD_DROPDOWN_LOCATOR = (WIN_APP_BY, '20503')
    PLATE_WELL_INPUT_LOCATOR = (WIN_APP_BY, '20495')
    INJECTION_VOLUME_INPUT_LOCATOR = (WIN_APP_BY, '20502')
    RUN_TIME_INPUT_LOCATOR = (WIN_APP_BY, '20489')
    DEVELOP_METHOD_BUTTON_LOCATOR = (WIN_APP_BY, '20504')
    PREPARE_BUTTON_LOCATOR = (WIN_APP_BY, '20500')
    INJECT_BUTTON_LOCATOR = (WIN_APP_BY, '20501')

    @staticmethod
    def _get_function_dropdown_item_locator(function_name: str) -> Tuple[str, str]:
        return By.XPATH, f"//ListItem[@Name='{function_name}']"

    @staticmethod
    def _get_method_dropdown_item_locator(method_set_name: str) -> Tuple[str, str]:
        return By.XPATH, f"//ListItem[@Name='{method_set_name}']"

    def __init__(self, driver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    def set_sample_name(self, sample_name: str):
        element = self._driver.find_element(*self.SAMPLE_NAME_INPUT_LOCATOR)
        element.clear()
        self.set_text(self.SAMPLE_NAME_INPUT_LOCATOR, sample_name)

    def select_function(self, function_name: str):
        self.click_on_element(self.FUNCTION_DROPDOWN_LOCATOR)
        self.click_on_element(self._get_function_dropdown_item_locator(function_name))

    def select_method(self, method_set: str):
        self.click_on_element(self.METHOD_DROPDOWN_LOCATOR)
        self.click_on_element(self._get_method_dropdown_item_locator(method_set))

    def set_plate(self, plate: str):
        self.set_text(self.PLATE_WELL_INPUT_LOCATOR, plate)

    def set_injection_volume(self, injection_volume: Union[int, float]):
        self.set_text(self.INJECTION_VOLUME_INPUT_LOCATOR, str(injection_volume))

    def set_run_time(self, run_time: Union[int, float]):
        self.set_text(self.RUN_TIME_INPUT_LOCATOR, str(run_time))

    def click_develop_methods_button(self):
        self.click_on_element(self.DEVELOP_METHOD_BUTTON_LOCATOR)

    def click_prepare_button(self):
        self.click_on_element(self.PREPARE_BUTTON_LOCATOR)

    def click_inject_button(self):
        self.click_on_element(self.INJECT_BUTTON_LOCATOR)
