from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.column_compartment.column_temperature_page import ColumnTemperaturePage
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class ColumnCompartmentMenu(MethodEditorBasePage):
    _column_temperature_locator = (By.XPATH, "//Text[@Name='Column Temperature']")
    _column_temperature_state_locator = (By.XPATH, "//Text[@Name='Column Temperature']/following::Text")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_column_temperature(self) -> ColumnTemperaturePage:
        self.click_on_element(self._column_temperature_locator)
        return ColumnTemperaturePage(self._driver)
