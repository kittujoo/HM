import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_page_locator_lookup import UserSettingsPageLocatorLookup
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen

logger = Logger(__name__)

if __name__ == Path(__file__).stem:
    scenarios('../../features/UserSettingsScreen/picker_component_loading.feature')

@given('User navigates to the user preferences screen')
def user_profile_screen(dash_board_screen_page: DashBoardScreen):
    logger.info("The user profile settings screen test begins *************")
    dash_board_screen_page.validate_dashboard_screen()
    dash_board_screen_page.tap_user_settings_icon()


@when('User taps the Date and Time format tab')
def tap_date_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.DATE_AND_TIME_TAB)
    
    
@then('User validates the time zone picker is displayed')
def validate_time_zone_picker(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.TIME_ZONE_TAB)
    try:
        assert user_profile_settings_screen_page.is_picker_displayed(UserSettingsScreenPageLocators.TIME_ZONE_PICKER)

    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@then('User validates the date picker is displayed')
def validate_date_picker(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DATE_FORMAT_PANEL)
    try:
        assert user_profile_settings_screen_page.is_picker_displayed(UserSettingsScreenPageLocators.DATE_FORMAT_PICKER)

    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@when('User confirms the user profile settings')
def tap_done_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap_done_button()


@when(cfparse('User selects the date format as "{date_format}"'))
def select_date_format(user_profile_settings_screen_page: UserProfileSettingsScreen, date_format):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    datetime_format_dictionary = UserSettingsPageLocatorLookup.datetime_format_dictionary
    user_profile_settings_screen_page.select_spinner_options(date_format, datetime_format_dictionary)


@when('User taps the Date and Time format tab in the settings screen')
def navigate_to_date_settings(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DATETIME_SETTINGS_TAB)
