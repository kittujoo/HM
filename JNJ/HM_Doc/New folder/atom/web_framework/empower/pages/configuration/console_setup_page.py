from selenium.webdriver.common.by import By

from web_framework.empower.pages.configuration.console_page import ConsoleBasePage


class ConsoleSetupPage(ConsoleBasePage):
    SHUTDOWN_BUTTON_LOCATOR = (By.XPATH, "//Image[@Name='ics-img-play.svg'][1]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_shutdown(self):
        self.click_on_element(self.SHUTDOWN_BUTTON_LOCATOR)
