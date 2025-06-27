from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.logger import Logger
from utilities.string_utility import str_to_float
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class SampleTemperaturePage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    _setpoint_editbox_locator = (By.XPATH, "//Text[@Name='Temperature Setpoint (°C)']/following::Spinner")
    _setpoint_toggle_locator = (By.XPATH, "//Text[contains(@Name, 'Enable to control')]/following::Button")
    _tolerance_editbox_locator = (By.XPATH, "//Text[@Name='Tolerance (±°C)']/following::Spinner")
    _tolerance_toggle_locator = (By.XPATH, "//Text[contains(@Name, 'Enable to hold next injections until')]/following::Button")
    _sample_temperature_title_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Temperature')]")
    _group_title_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/Text[@Name='Sample Temperature']")
    _sample_temperature_sub_menu_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/List/ListItem[Text[@Name='Sample Temperature']]")
    _sample_temperature_sub_menu_sub_titles_locator = (
        By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/List/ListItem[Text[@Name='Sample Temperature']]/Text[position() > 1]")
    _sample_temperature_sub_menu_text_locator = (By.XPATH, "//Document[@Name='AllianceiSMethodEditor']/List/ListItem/Text[@Name='Sample Temperature']")
    _set_temperature_title_locator = (By.XPATH, "//Text[contains(@Name, 'Set Compartment Temperature')]")
    _set_temperature_subtitle_locator = (By.XPATH, "//Text[contains(@Name, 'Enable to')]")
    _set_settings_title_locator = (By.XPATH, "//Text[contains(@Name, 'Setpoint (°C)')]")
    _setpoint_hint_locator = (By.XPATH, "//Text[contains(@Name, '40.0 °C')]")
    _tolerance_settings_title_locator = (By.XPATH, "//Text[contains(@Name, 'Tolerance')]")
    _tolerance_input_title_locator = (By.XPATH, "//Text[contains(@Name, '(±°C)')]")
    _tolerance_setting_subtitle_locator = (By.XPATH, "//Text[contains(@Name, 'injections')]")
    _favorite_icon_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Temperature')]/following::Button")
    _tolerance_setting_title_locator = (By.XPATH, "//Text[contains(@Name, '(±°C)')]")
    _tolerance_hint_text_locator = (By.XPATH, "//Text[contains(@Name, '0.5 to 10.0')]")

    def set_compartment_toggle(self, state: bool):
        self.set_toggle_state(self._setpoint_toggle_locator, state)

    def set_temperature_setpoint(self, temperature: float):
        self.set_text(self._setpoint_editbox_locator, str(temperature))
        actual_value = self.get_element_value_attribute(self._setpoint_editbox_locator)
        assert float(actual_value) == temperature, "Failed to set Temperature Setpoint value"

    def set_tolerance_toggle(self, state: bool):
        self.set_toggle_state(self._tolerance_toggle_locator, state)

    def set_temperature_tolerance(self, temperature: float):
        self.set_text(self._tolerance_editbox_locator, str(temperature))
        actual_value = self.get_element_value_attribute(self._tolerance_editbox_locator)
        assert float(actual_value) == temperature, "Failed to set Temperature Tolerance value"

    def get_sample_temperature_title(self):
        return self.get_text(self._sample_temperature_title_locator)

    def get_settings_group_title(self):
        return self.get_text(self._group_title_locator)

    def get_set_temperature_title(self):
        return self.get_text(self._set_temperature_title_locator)

    def get_compartment_temperature_subtitle(self):
        return self.get_text(self._set_temperature_subtitle_locator)

    def get_setpoint_setting_title(self):
        return self.get_text(self._set_settings_title_locator)

    def get_setpoint_hint_message(self):
        return self.get_text(self._setpoint_hint_locator)

    def get_tolerance_input_title(self):
        return self.get_text(self._tolerance_input_title_locator)

    def get_tolerance_setting_subtitle(self):
        return self.get_text(self._tolerance_setting_subtitle_locator)

    def get_tolerance_settings_title(self):
        return self.get_text(self._tolerance_settings_title_locator)

    def set_favorite(self):
        self.click_on_element(self._favorite_icon_locator)

    def get_sample_temperature_subtitle(self):
        elements = self.find_elements(self._sample_temperature_sub_menu_sub_titles_locator)
        result = " ".join(element.get_attribute("Name") for element in elements)
        return result

    def validate_setpoint_temperature(self, expected_value):
        actual_value = self.get_text(self._setpoint_editbox_locator)
        actual_value = str_to_float(actual_value)
        assert actual_value == expected_value, f"The 'temperature setpoint' is incorrect. actual_value = {actual_value}, expected_value = {expected_value}"

    def validate_tolerance_temperature(self, expected_value):
        actual_value = self.get_text(self._tolerance_editbox_locator)
        actual_value = str_to_float(actual_value)
        assert actual_value == expected_value, f"The 'tolerance temperature' is incorrect. actual_value = {actual_value}, expected_value = {expected_value}"

    def validate_compartment_temperature_toggle_state(self, expected_toggle_state):
        self._validate_toggle_state(self._setpoint_toggle_locator, expected_toggle_state, 'Compartment Temperature')

    def validate_temperature_tolerance_toggle_state(self, expected_toggle_state):
        self._validate_toggle_state(self._tolerance_toggle_locator, expected_toggle_state, 'Temperature Tolerance')

    def get_tolerance_hint_text(self):
        return self.get_text(self._tolerance_hint_text_locator)

    def set_tolerance(self, temperature_tolerance: float):
        self.set_text(self._tolerance_editbox_locator, str(temperature_tolerance))
        actual_value = self.get_element_value_attribute(self._tolerance_editbox_locator)
        assert float(actual_value) == temperature_tolerance, "Failed to set Tolerance value"

    def is_sample_temperature_displayed(self):
        return self.is_displayed_with_timeout(5, self._group_title_locator)

    def toggle_sample_temperature(self, state: bool):
        self.set_toggle_state(self._setpoint_toggle_locator, state)

    def set_setpoint(self, state: str):
        self.set_text(self._setpoint_editbox_locator, state)
