from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.assert_timeout import AssertTimeout
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from web_framework.method_editor.pages.sample_manager.sample_manager_advanced_page import SampleManagerAdvancedPage
from web_framework.method_editor.pages.sample_manager.data_channels_page import DataChannelsSampleManagerPage
from web_framework.method_editor.pages.sample_manager.sample_temperature_page import SampleTemperaturePage
from web_framework.method_editor.pages.sample_manager.wash_solvents_page import WashSolventsPage
from web_framework.method_editor.pages.sample_manager.wash_time_page import WashTimePage


class SampleManagerMenu(MethodEditorBasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._assert_timeout: AssertTimeout = AssertTimeout(10, 1)

    _submenus_names = ["Sample Temperature", "Wash Solvents", "Wash Time", "Data Channels: Sample Manager", "Sample Manager Advanced"]
    _submenus_names_locator = (By.XPATH, "//ListItem/Text[1]")

    _sample_temperature_locator = (By.XPATH, "//Text[@Name='Sample Temperature']")
    _sample_temperature_state_locator = (By.XPATH, "//Text[@Name='Sample Temperature']/following::Text")

    _wash_solvents_locator = (By.XPATH, "//Text[@Name='Wash Solvents']")
    _wash_solvents_state_locator = (By.XPATH, "//Text[@Name='Wash Solvents']/following::Text")

    _wash_time_locator = (By.XPATH, "//Text[@Name='Wash Time']")
    _wash_time_state_locator = (By.XPATH, "//Text[@Name='Wash Time']/following::Text[contains(@Name, ' s')]")

    _data_channels_locator = (By.XPATH, "//Text[@Name='Data Channels: Sample Manager']")

    _advanced_locator = (By.XPATH, "//Text[@Name='Sample Manager Advanced']")
    _advanced_state_locator = (By.XPATH, "//Text[@Name='Sample Manager Advanced']/following::Text")

    def validate_opened(self):
        def get_submenus_names():
            sub_menus = [element.get_attribute("Name") for element in self.find_elements(self._submenus_names_locator)]
            return sub_menus

        self._assert_timeout.is_true(lambda: get_submenus_names() == self._submenus_names,
                                     "Failed to validate Sample manager menu, seems driver is on another location")

    def open_sample_temperature(self) -> SampleTemperaturePage:
        self.click_on_element(self._sample_temperature_locator)
        return SampleTemperaturePage(self._driver)

    def get_sample_temperature_state(self) -> str:
        state = self.get_element_name_attribute(self._sample_temperature_state_locator)
        return state

    def open_wash_solvents(self) -> WashSolventsPage:
        self.click_on_element(self._wash_solvents_locator)
        return WashSolventsPage(self._driver)

    def get_wash_solvents_state(self) -> str:
        state = self.get_element_name_attribute(self._wash_solvents_state_locator)
        return state

    def open_wash_time(self) -> WashTimePage:
        self.click_on_element(self._wash_time_locator)
        return WashTimePage(self._driver)

    def get_wash_time_state(self) -> str:
        state = self.get_element_name_attribute(self._wash_time_state_locator)
        return state

    def open_data_channels_sample_manager(self) -> DataChannelsSampleManagerPage:
        self.click_on_element(self._data_channels_locator)
        return DataChannelsSampleManagerPage(self._driver)

    def is_data_channels_sample_manager_displayed(self) -> bool:
        return self.is_displayed_with_timeout(5, self._data_channels_locator)

    def open_advanced(self) -> SampleManagerAdvancedPage:
        self.click_on_element(self._advanced_locator)
        return SampleManagerAdvancedPage(self._driver)

    def get_advanced_state(self) -> str:
        state = self.get_element_name_attribute(self._advanced_state_locator)
        return state
