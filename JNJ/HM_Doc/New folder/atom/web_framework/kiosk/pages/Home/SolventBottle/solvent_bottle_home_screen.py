from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.Home.SolventBottle.solvent_bottle_home_screen import SolventBottleScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SolventBottleHomeScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_mobile_phase_home_screen(self):
        locator = SolventBottleScreenLocators.SOLVENT_BOTTLE_A
        screen_name = "solvent Bottle screen"
        self.validate_screen(locator, screen_name, self.wait_time)
