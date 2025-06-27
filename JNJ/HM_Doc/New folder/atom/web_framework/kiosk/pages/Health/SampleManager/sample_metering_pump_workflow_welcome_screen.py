from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import (SampleMeteringPumpLocators,
                                                                                                            SampleMeteringPumpWelcomeLocators)
from web_framework.kiosk.pages.base_page import BasePage


class SampleMeteringPumpWelcomeScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_welcome_screen(self):
        locator = SampleMeteringPumpLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the sample metering pump leak test workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self):
        return [
            self.get_text(SampleMeteringPumpWelcomeLocators.WELCOME_PARAGRAPH_ONE),
            self.get_text(SampleMeteringPumpWelcomeLocators.WELCOME_PARAGRAPH_TWO)
        ]
