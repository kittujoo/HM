from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class ColumnTemperaturePage(MethodEditorBasePage):
    COLUMN_TEMPERATURE_TOGGLE_LOCATOR = (By.XPATH, "//Text[@Name='Enable to control the compartment temperature']/following-sibling::Button")
    SETPOINT_EDITBOX_LOCATOR = (By.XPATH, "//Text[@Name='Temperature Setpoint (°C)']/following::Spinner")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def toggle_column_temperature(self, state: bool):
        self.set_toggle_state(self.COLUMN_TEMPERATURE_TOGGLE_LOCATOR, state)

    def set_setpoint(self, state: str):
        self.set_text(self.SETPOINT_EDITBOX_LOCATOR, state)
