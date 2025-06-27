# """
# File_Name: lock_screen.py
# Desc: This file contains specific user action on the web elements in the lock screen
# __copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
# __author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
# __modified__= "Sharmila Vairamani" Added validate_lock_screen method - 10/16/2020
# __modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
import allure

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.lock_screen_locators import LockScreenPageLocators
from web_framework.kiosk.pages.base_page import BasePage


class LockScreen(BasePage):
    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def swipe_to_unlock_component_exists(self):
        return self.is_displayed(LockScreenPageLocators.swipe_up_component)

    def validate_lock_screen(self):
        locator = LockScreenPageLocators.swipe_to_unlock_component
        screen_name = "lock screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    @allure.step("Swipe to unlock")
    def swipe_to_unlock(self):
        self.press_esc_key()
