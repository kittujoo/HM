from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage


class DataChannelsPage(MethodEditorBasePage):
    AMBIENT_TEMPERATURE_TOGGLE = (By.XPATH, "//Text[@Name='Ambient Laboratory Temperature (°C)']/following-sibling::Button")
    SYSTEM_PRESSURE_TOGGLE = (By.XPATH, "//Text[@Name='System Pressure']/following-sibling::Button")
    FLOW_RATE_TOGGLE = (By.XPATH, "//Text[@Name='System flow rate (mL/min)']/following-sibling::Button")
    SOLVENT_A_TOGGLE_LOCATOR = (By.XPATH, "//Text[@Name='Percent composition of solvent A']/following-sibling::Button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def toggle_ambient_temperature(self):
        self.set_toggle_state(self.AMBIENT_TEMPERATURE_TOGGLE, True)

    def toggle_system_pressure(self):
        self.set_toggle_state(self.SYSTEM_PRESSURE_TOGGLE, True)

    def toggle_flow_rate(self):
        self.set_toggle_state(self.FLOW_RATE_TOGGLE, True)

    def toggle_percent_solvent_a(self):
        self.set_toggle_state(self.SOLVENT_A_TOGGLE_LOCATOR, True)
