"""
File_Name: user_profile_settings_screen.py
Desc: This file contains specific user action on the web elements in the user profile settings screen
__copyright__ = "Copyright (c) 2019 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/15/2020
__modified__ = "Sharmila Vairamani" Added user action functions for the test - 12/09/2020
__modified__ = "Sharmila Vairamani" Changed the class name - 12/11/2020
__modified__ = "Tyler Prada" added methods related to screen saver and datetime test script 06/30/2021
__modified__ = "Sharmila Vairamani" Added selection and validation method 09/06/2021
__modified__ = "Sharmila Vairamani" Added validate time zone option - 10/20/2021
__modified__ = "Tyler Prada" Update to date&time related functions. Edits for fixed defects, other general tweaks due to UI changes 6/8/22
__modified__ = "Tyler Prada" added validation function for instrument name page 9/28/22
__modified__ = "Tyler Prada" Date & time function adjustments 9/19/23
"""
import time

from selenium.webdriver.common.by import By

from utilities.logger import Logger
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_page_locator_lookup import UserSettingsPageLocatorLookup
from web_framework.kiosk.pages.base_page import BasePage


class UserProfileSettingsScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)

    def validate_user_settings_screen(self):
        locator = UserSettingsScreenPageLocators.USER_SETTINGS_HEADER
        screen_name = "user settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_instrument_name_screen(self):
        locator = UserSettingsScreenPageLocators.INSTRUMENT_NAME_TEXT_AREA
        screen_name = "Instrument name screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_volume(self, volume_settings):
        volume_settings_dictionary = UserSettingsPageLocatorLookup.volume_settings_dictionary
        if volume_settings in volume_settings_dictionary:
            locator = volume_settings_dictionary[volume_settings]
            self.tap(locator)
            return

        assert False, f"Unexpected volume settings => {volume_settings}"

    def select_screen_lock_period(self, screen_lock_period):
        screen_lock_period_dictionary = UserSettingsPageLocatorLookup.screen_lock_period_dictionary
        if screen_lock_period in screen_lock_period_dictionary:
            locator = screen_lock_period_dictionary[screen_lock_period]
            self.tap_text_field(locator)
            return

        assert False, f"Unexpected screen lock period => {screen_lock_period}"

    def navigate_screen_lock_page(self):
        self.tap(UserSettingsScreenPageLocators.SCREEN_LOCK_TAB)

    def navigate_theme_settings_page(self):
        self.tap(UserSettingsScreenPageLocators.THEME_SETTINGS_TAB)

    def select_theme_settings(self, theme_settings):
        theme_settings_dictionary = UserSettingsPageLocatorLookup.theme_settings_dictionary
        if theme_settings in theme_settings_dictionary:
            locator = theme_settings_dictionary[theme_settings]
            self.tap_text_field(locator)
            return

        assert False, f"Unexpected theme settings => {theme_settings}"

    def get_current_date_format(self):
        element_text = self.get_container_text(UserSettingsScreenPageLocators.EXAMPLE_DATE_LABEL)
        return element_text

    def get_displayed_time_format(self):
        element_text = self.get_container_text(UserSettingsScreenPageLocators.EXAMPLE_TIME_LABEL)
        self.logger.info(f"element_text=====>>>>>>>{element_text} ")
        return element_text[len("Example: "):]

    def get_screen_lock_duration(self):
        return self.get_text(UserSettingsScreenPageLocators.LOCK_SCREEN_DURATION)

    def get_system_name(self):
        return self.get_text(UserSettingsScreenPageLocators.SYSTEM_NAME_DISPLAY_LABEL)

    def get_system_name_comment_card_string(self):
        return self.get_text(UserSettingsScreenPageLocators.SYSTEM_NAME_COMMENT_CARD)

    def navigate_datetime_settings_page(self):
        self.tap(UserSettingsScreenPageLocators.DATETIME_SETTINGS_TAB)

    def navigate_volume_settings_page(self):
        self.tap(UserSettingsScreenPageLocators.SOUND_PREFERENCE_SETTINGS_TAB)

    def is_picker_displayed(self, locator):
        picker_display_status = self.is_displayed(locator)
        return picker_display_status

    def validate_time_format(self, time_format):
        datetime_format_dictionary = UserSettingsPageLocatorLookup.datetime_format_dictionary
        if time_format in datetime_format_dictionary:
            locator = datetime_format_dictionary[time_format]
            return self.is_active(locator)

        assert False, f"Unexpected time format => {time_format}"

    def validate_volume_settings_screen(self):
        locator = UserSettingsScreenPageLocators.SOUND_PREFERENCE_SETTINGS_HEADER
        screen_name = "user settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_datetime_settings_screen(self):
        locator = UserSettingsScreenPageLocators.DATE_TIME_HEADER
        screen_name = "Date and time settings screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def select_and_validate_time_zone_options(self):

        try:

            self.select_and_validate_spinner_range(reversed(range(4, 13)),
                                                   UserSettingsScreenPageLocators.TIME_ZONE_OPTIONS,
                                                   UserSettingsScreenPageLocators.SELECTED_TIME_ZONE_LABEL)
            self.select_and_validate_spinner_range(range(5, 9),
                                                   UserSettingsScreenPageLocators.TIME_ZONE_OPTIONS,
                                                   UserSettingsScreenPageLocators.SELECTED_TIME_ZONE_LABEL)


        finally:
            self.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
            self.tap_done_button()

    def select_and_validate_date_format_options(self):

        try:

            for x in range(2, 8):
                date_format_locator = (By.XPATH, f"{UserSettingsScreenPageLocators.DATE_FORMAT_OPTIONS}li[{x}]")
                self.logger.info(f"The list of locators ===>>>{date_format_locator}")

                self.wait_for_element_visibility(5, date_format_locator)
                self.tap(date_format_locator)
                time.sleep(1)
                assert self.is_option_selected(date_format_locator), f"The {date_format_locator} is not selected"
                actual_text = self.get_text(date_format_locator)
                time.sleep(1)
                expected_text = self.get_current_date_format()
                self.validate_text(actual_text, expected_text)

        finally:
            self.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
            self.tap_done_button()

    def validate_time_zone_option(self, expected_text):
        actual_text = self.get_text(UserSettingsScreenPageLocators.SELECTED_TIME_ZONE_LABEL)
        time.sleep(1)
        self.validate_text(actual_text, expected_text)

    def set_date_and_time_format(self, date_format='02/29/2020', time_zone_option='UTC'):
        self.tap(UserSettingsScreenPageLocators.DATE_FORMAT_PANEL)
        date_format_style_dictionary = UserSettingsPageLocatorLookup.datetime_format_dictionary
        self.scroll_to_spinner_options(date_format, date_format_style_dictionary)
        if not self.is_toggle_component_enabled(UserSettingsScreenPageLocators.TIME_TOGGLE):
            self.tap(UserSettingsScreenPageLocators.TIME_TOGGLE)
        self.tap(UserSettingsScreenPageLocators.TIME_ZONE_TAB)
        timezone_style_dictionary = UserSettingsPageLocatorLookup.time_zone_dictionary
        self.scroll_to_spinner_options(time_zone_option, timezone_style_dictionary)

