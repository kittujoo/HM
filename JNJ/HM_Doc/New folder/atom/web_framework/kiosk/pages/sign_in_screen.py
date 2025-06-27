"""
File_Name: sign_in_screen.py
Desc: This file contains specific user action on the web elements in the sign-in screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 11/15/19
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Tyler Prada" added delete_pin_entries, removed clear methods - 10/20/21
"""
from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Locators.lock_screen_locators import LockScreenPageLocators
from web_framework.kiosk.pages.Locators.sign_in_screen_locators import SignInScreenLocators
from web_framework.kiosk.pages.base_page import BasePage


class SignInScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def enter_pin(self, pin):
        self.logger.info(f"enter pin {pin}")

        number_pad_dictionary = {
            "1": SignInScreenLocators.NUM_PAD_1,
            "2": SignInScreenLocators.NUM_PAD_2,
            "3": SignInScreenLocators.NUM_PAD_3,
            "4": SignInScreenLocators.NUM_PAD_4,
            "5": SignInScreenLocators.NUM_PAD_5,
            "6": SignInScreenLocators.NUM_PAD_6,
            "7": SignInScreenLocators.NUM_PAD_7,
            "8": SignInScreenLocators.NUM_PAD_8,
            "9": SignInScreenLocators.NUM_PAD_9,
            "0": SignInScreenLocators.NUM_PAD_0}

        index = 0
        while index < len(pin):
            if pin[index] in number_pad_dictionary:
                locator = number_pad_dictionary[pin[index]]
                self.tap(locator)
            index += 1

    def tap_show_password_icon(self):
        self.tap(SignInScreenLocators.SHOW_PASSWORD_ICON)

    def display_error_message(self):
        error_display = self.get_text(SignInScreenLocators.PIN_DISPLAY)
        return error_display

    def get_pin_entered(self):
        pin_entry = self.get_element(SignInScreenLocators.PIN_TEXT_BOX)
        pin_entered = pin_entry.get_attribute("value")
        return pin_entered

    def tap_unlock_button(self):
        self.tap(SignInScreenLocators.UNLOCK_BUTTON)

    def delete_pin_entries(self):
        pin_length = len(self.get_pin_entered())
        for _ in range(pin_length):
            self.tap(SignInScreenLocators.DELETE_BUTTON)

    def tap_back_button(self):
        self.tap(SignInScreenLocators.BACK_BUTTON)

    def is_system_ready_image_exists(self):
        return self.is_displayed(LockScreenPageLocators.SYSTEM_READY_COMPONENT)

    def is_home_icon_displayed(self):
        return self.is_displayed(DashBoardsScreenPageLocators.HOME)

    def validate_sign_in_screen(self):
        locator = SignInScreenLocators.PIN_TEXT_BOX
        wait_time = 10
        screen_name = "sign in screen"
        self.validate_screen(locator, screen_name, wait_time)

    def unlock_with_pin(self, pin):
        self.tap(SignInScreenLocators.PIN_TEXT_BOX)
        self.enter_pin(pin)
        self.tap_unlock_button()
