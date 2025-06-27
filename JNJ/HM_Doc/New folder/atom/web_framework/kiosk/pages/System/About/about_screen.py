from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.System.system_about_screen_locators import AboutScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class AboutScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_about_screen(self):
        locator = AboutScreenLocators.HEADER
        screen_name = "About screen"
        self.validate_screen(locator, screen_name, self.wait_time)
