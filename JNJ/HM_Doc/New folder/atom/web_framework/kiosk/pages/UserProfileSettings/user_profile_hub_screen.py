"""
File_Name: user_profile_hub_screen.py
Desc: This file contains specific user action on the web elements in the user profile hub screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/18/2021

"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.base_page import BasePage


class UserProfileHubScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_user_hub_screen(self):
        locator = UserProfileHubPageLocators.INSTRUMENT_NAME
        screen_name = "user settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def wait_sign_out_timer(self, wait_time):
        while wait_time >= 0:
            if not int(self.find_element(UserProfileHubPageLocators.SIGN_OUT_TIMER).get_attribute("style").split(" ")[2].strip("s")):
                return True
        assert False, f"The timer did not end within the given {wait_time} seconds"
