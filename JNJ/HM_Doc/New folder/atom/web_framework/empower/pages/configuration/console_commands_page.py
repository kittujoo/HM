from selenium.webdriver.common.by import By

from web_framework.empower.pages.configuration.console_page import ConsoleBasePage


class ConsoleCommandsPage(ConsoleBasePage):
    FLOW_RATE_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@Name, "ics-img-play.svg") or contains(@Name, "ics-img-pause.svg")]')
    LAMP_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@Name, "ics-img-lamp-off-cp.svg") or contains(@Name, "ics-img-lamp-on-cp.svg")]')
    RESET_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@Name, "ics-img-reset.svg")]')
    FLOW_STATE_TEXT_LOCATOR = (By.XPATH, '//*[contains(@Name, "Flow On") or contains(@Name, "Flow Off")]')
    LAMP_OFF_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@Name, "ics-img-lamp-off-cp.svg")]')
    LAMP_ON_BUTTON_LOCATOR = (By.XPATH, '//*[contains(@Name, "ics-img-lamp-on-cp.svg")]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_flow_rate_button(self):
        self.click_on_element(self.FLOW_RATE_BUTTON_LOCATOR)

    def click_on_lamp_button(self):
        self.click_on_element(self.LAMP_BUTTON_LOCATOR)

    def system_reset_command(self):
        self.click_on_element(self.RESET_BUTTON_LOCATOR)

    def get_control_flow_state_text(self) -> str:
        return self.get_text(self.FLOW_STATE_TEXT_LOCATOR)

    def is_lamp_off(self) -> str:
        return self.is_displayed(self.LAMP_OFF_BUTTON_LOCATOR)

    def get_control_lamp_state(self) -> bool:
        return self.is_displayed(self.LAMP_ON_BUTTON_LOCATOR)
