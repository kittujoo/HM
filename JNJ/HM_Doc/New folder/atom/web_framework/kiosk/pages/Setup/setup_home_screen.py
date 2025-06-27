from web_framework.kiosk.pages.Locators.Setup.setup_screen_locators import SetupScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SetupHomeScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

    def validate_setup_screen(self):
        locator = SetupScreenLocators.SETUP_HEADER
        screen_name = "setup screen"
        self.validate_screen(locator, screen_name, self.wait_time)
