from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class DataChannelsSampleManagerPage(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    _data_channels_title_locator = (By.XPATH, "//Text[contains(@Name, 'Data Channels: Sample Manager')]")
    _temperature_title_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Temperature')]")
    _temperature_subtitle_locator = (By.XPATH, "//Text[contains(@Name, 'Compartment temperature')]")
    _temperature_toggle_locator = (By.XPATH, "//Text[contains(@Name, 'Compartment temperature')]/following::Button")
    _pressure_title_locator = (By.XPATH, "//Text[contains(@Name, 'Sample Pressure')]")
    _pressure_subtitle_locator = (By.XPATH, "//Text[contains(@Name, 'Sample pressure')]")
    _pressure_toggle_locator = (By.XPATH, "//Text[contains(@Name, 'Sample pressure')]/following::Button")
    _favorite_icon_locator = (By.XPATH, "//Text[contains(@Name, 'Data Channels: Sample Manager')]/following::Button")

    def get_data_channels_title(self):
        return self.get_text(self._data_channels_title_locator)

    def get_temperature_title(self):
        return self.get_text(self._temperature_title_locator)

    def get_temperature_subtitle(self):
        return self.get_text(self._temperature_subtitle_locator)

    def get_temperature_toggle(self):
        return self.get_element_toggle_attribute(self._temperature_toggle_locator)

    def set_temperature_toggle(self, state: bool):
        self.set_toggle_state(self._temperature_toggle_locator, state)

    def get_pressure_title(self):
        return self.get_text(self._pressure_title_locator)

    def get_pressure_subtitle(self):
        return self.get_text(self._pressure_subtitle_locator)

    def get_pressure_toggle(self):
        return self.get_element_toggle_attribute(self._pressure_toggle_locator)

    def set_pressure_toggle(self, state: bool):
        self.set_toggle_state(self._pressure_toggle_locator, state)

    def set_favorite(self):
        self.click_on_element(self._favorite_icon_locator)