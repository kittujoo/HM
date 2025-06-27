from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/UserSettingsScreen/sign_out.feature')

logger = Logger(__name__)


@given('User navigates to the user profile screen')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.wait_element_to_be_clickable(DashBoardsScreenPageLocators.USER_SETTINGS, session_dash_board_screen_page.wait_time)
    session_dash_board_screen_page.tap_user_settings_icon()


@when('User taps the lock button')
def tap_lock(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SIGN_OUT_BUTTON)


@when('User taps the confirm button')
def tap_confirm(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.wait_element_to_be_clickable(UserProfileHubPageLocators.SIGN_OUT_CONFIRM, user_profile_hub_screen_page.wait_time)
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SIGN_OUT_CONFIRM)


@when('User taps the cancel button')
def tap_cancel(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SIGN_OUT_CANCEL)


@then(cfparse('User is redirected to dashboard screen after {wait_time: d} seconds'))
def validate_timeout(user_profile_hub_screen_page: UserProfileHubScreen, dashboard_screen_page: DashBoardScreen, wait_time):
    try:
        assert user_profile_hub_screen_page.is_displayed(UserProfileHubPageLocators.SIGN_OUT_CANCEL), "The cancel button was not displayed"
        assert user_profile_hub_screen_page.is_displayed(UserProfileHubPageLocators.SIGN_OUT_CONFIRM), "The sign out button was not displayed"
    finally:
        user_profile_hub_screen_page.wait_sign_out_timer(wait_time)
        dashboard_screen_page.validate_dashboard_screen()


@then('User is redirected to dashboard screen')
def validate_dashboard_screen(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()


@then('User stays in the user setting screen')
def validate_user_setting_screen(user_profile_hub_screen_page: UserProfileHubScreen, dashboard_screen_page: DashBoardScreen):
    try:
        user_profile_hub_screen_page.validate_user_hub_screen()
    finally:
        user_profile_hub_screen_page.wait_element_to_be_clickable(BasePageLocators.DONE_BUTTON, user_profile_hub_screen_page.wait_time)
        user_profile_hub_screen_page.tap_done_button()
        dashboard_screen_page.validate_dashboard_screen()
