from time import sleep
from typing import Tuple, Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class MethodEditorBasePage(WinAppBasePage):
    DELETE_BUTTON_LOCATOR = (By.NAME, 'Delete')
    SAVE_BUTTON_LOCATOR = (By.NAME, 'Save')
    OPEN_BUTTON_LOCATOR = (By.NAME, 'Open')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_element_value_attribute(self, locator: Tuple[str, str]):
        name = self.get_element_attribute(locator, "Value.Value")
        return name

    def get_element_toggle_attribute(self, locator: Tuple[str, str]) -> Optional[bool]:
        raw_state = self.get_element_attribute(locator, "Toggle.ToggleState")
        if raw_state is None:
            return None
        state = bool(int(raw_state))
        return state

    def set_toggle_state(self, locator: Tuple[str, str], state: bool):
        current_state = self.get_element_toggle_attribute(locator)
        if current_state == state:
            return

        self.click_on_element(locator)
        sleep(0.5)
        actual_state = self.get_element_toggle_attribute(locator)
        assert actual_state == state, f'Failed to switch {"On" if state else "Off"} the toggle located by {locator}'

    def get_toggle_state(self, locator: Tuple[str, str]):
        return self.get_element_toggle_attribute(locator)

    def _validate_toggle_state(self, toggle_locator: Tuple[str, str], expected_toggle_state: bool, toggle_name: str):
        actual_toggle_state = self.get_toggle_state(toggle_locator)
        assert actual_toggle_state == expected_toggle_state, \
            f"The '{toggle_name}' toggle state is incorrect. actual_toggle_state: {actual_toggle_state}, expected_toggle_state: {expected_toggle_state}"

    def click_delete_toolbar_button(self):
        self.click_on_element(self.DELETE_BUTTON_LOCATOR)

    def click_save_toolbar_button(self):
        self.click_on_element(self.SAVE_BUTTON_LOCATOR)

    def click_open_toolbar_button(self):
        self.click_on_element(self.OPEN_BUTTON_LOCATOR)

    def is_save_method_button_enabled(self):
        return self.find_element(self.SAVE_BUTTON_LOCATOR).is_enabled()

    def get_element_is_enabled_attribute(self, locator: Tuple[str, str]) -> Optional[bool]:
        raw_state = self.get_element_attribute(locator, "IsEnabled")
        if raw_state is None:
            return None
        state = True if raw_state.lower() == "true" else False

        return state

    def get_is_enabled_state(self, locator: Tuple[str, str]):
        return self.get_element_is_enabled_attribute(locator)

    def _validate_element_is_enabled(self, element_locator: Tuple[str, str], expected_is_enabled_state: bool, element_name: str):
        actual_is_enabled_state = self.get_is_enabled_state(element_locator)
        assert actual_is_enabled_state == expected_is_enabled_state, \
            f"The '{element_name}' isEnabled attribute is incorrect. actual_is_enabled_state: {actual_is_enabled_state}, expected_is_enabled_state: {expected_is_enabled_state}"
