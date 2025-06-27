from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class SampleManagerAdvancedPage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    _sample_manager_advanced_title_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Manager Advanced')]")
    _sample_manager_advanced_values_locator = (By.XPATH, "//Text[contains(@Name, 'Values')]")
    _sample_manager_advanced_summary_locator = (By.XPATH, "//Text[contains(@Name, 'Values')]/following::Text")
    _sample_manager_advanced_setting_group_title_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Manager Advanced')]")

    _sample_manager_advanced_default_locator = (By.XPATH, "//Text[contains(@Name, 'Waters recommends using default values for all settings')]/following::Text")
    _sample_manager_advanced_custom_locator = (By.XPATH, "//Text[contains(@Name, 'Custom')]")

    _vial_bottom_title_locator = (By.XPATH, "//Text[contains(@Name, 'Automatic Vial Bottom Detection')]")
    _vial_bottom_button_locator = (By.XPATH, "//Text[contains(@Name, 'Automatic Vial Bottom Detection')]/following::Button")

    _needle_placement_title_locator = (By.XPATH, "//Text[contains(@Name, 'Needle Placement from Bottom (mm)')]")
    _needle_placement_summary_locator = (By.XPATH, "//Text[contains(@Name, 'Needle Placement from Bottom (mm)')]/following::Text")
    _needle_placement_editbox_locator = (
        By.XPATH, "//Text[contains(@Name, 'The distance from the tip of the needle to the bottom of the sample container')]/following::Spinner")
    _needle_placement_hint_locator = (
        By.XPATH, "//Text[contains(@Name, 'The distance from the tip of the needle to the bottom of the sample container')]/following::Spinner/following::Text")

    _syringe_title_locator = (By.XPATH, "//Text[contains(@Name, 'Syringe Draw Rate (μL/min)')]")
    _syringe_editbox_locator = (By.XPATH, "//Text[contains(@Name, 'Syringe Draw Rate (μL/min)')]/following::Spinner")
    _syringe_hint_locator = (By.XPATH, "//Text[contains(@Name, 'Syringe Draw Rate (μL/min)')]/following::Spinner/following::Text")

    def get_sample_manager_advanced_title(self):
        return self.get_text(self._sample_manager_advanced_title_locator)

    def get_sample_manager_advanced_values(self):
        return self.get_text(self._sample_manager_advanced_values_locator)

    def get_sample_manager_advanced_summary(self):
        return self.get_text(self._sample_manager_advanced_summary_locator)

    def get_sample_manager_advanced_setting_group_title(self):
        return self.get_text(self._sample_manager_advanced_setting_group_title_locator)

    def get_sample_manager_advanced_default(self):
        return self.get_text(self._sample_manager_advanced_default_locator)

    def get_sample_manager_advanced_custom(self):
        return self.get_text(self._sample_manager_advanced_custom_locator)

    def get_vial_bottom_title(self):
        return self.get_text(self._vial_bottom_title_locator)

    def get_vial_bottom_button(self):
        return self.get_text(self._vial_bottom_button_locator)

    def get_needle_placement_title(self):
        return self.get_text(self._needle_placement_title_locator)

    def get_needle_placement_summary(self):
        return self.get_text(self._needle_placement_summary_locator)

    def get_needle_placement_editbox(self):
        return self.get_text(self._needle_placement_editbox_locator)

    def get_needle_placement_hint(self):
        return self.get_text(self._needle_placement_hint_locator)

    def get_syringe_title(self):
        return self.get_text(self._syringe_title_locator)

    def get_syringe_editbox(self):
        return self.get_text(self._syringe_editbox_locator)

    def get_syringe_hint(self):
        return self.get_text(self._syringe_hint_locator)

    def set_default(self):
        self.click_on_element(self._sample_manager_advanced_default_locator)

    def set_custom(self):
        self.click_on_element(self._sample_manager_advanced_custom_locator)

    def is_sample_manager_advanced_displayed(self) -> bool:
        return self.is_displayed_with_timeout(5, self._sample_manager_advanced_setting_group_title_locator)

    def validate_automatic_vial_bottom_detection_toggle_state(self, expected_toggle_state):
        self._validate_toggle_state(self._vial_bottom_button_locator, expected_toggle_state, 'Automatic Vial Bottom Detection')

    def validate_automatic_vial_bottom_detection_toggle_is_enabled(self, expected_is_enabled_state):
        self._validate_element_is_enabled(self._vial_bottom_button_locator, expected_is_enabled_state, 'Automatic Vial Bottom Detection')

    def validate_needle_placement_editbox_is_enabled(self, expected_is_enabled_state):
        self._validate_element_is_enabled(self._needle_placement_editbox_locator, expected_is_enabled_state, 'Needle Placement from Bottom')

    def validate_syringe_editbox_is_enabled(self, expected_is_enabled_state):
        self._validate_element_is_enabled(self._syringe_editbox_locator, expected_is_enabled_state, 'Syringe Draw Rate')

    def set_needle_placement_editbox(self, needle_placement: str):
        self.set_text(self._needle_placement_editbox_locator, str(needle_placement))

    def set_syringe_editbox(self, syringe: str):
        self.set_text(self._syringe_editbox_locator, str(syringe))

    def set_automatic_vial_bottom_detection_toggle(self, state: bool):
        self.set_toggle_state(self._vial_bottom_button_locator, state)
