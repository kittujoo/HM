import os
from pytest_bdd import given, when
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen

logger = Logger(os.path.basename(__file__))


# region Given

@given('User sets pre-required date and time format')
def set_date_time_setting(session_dash_board_screen_page: DashBoardScreen, user_profile_hub_screen_page: UserProfileHubScreen,
                          user_profile_settings_screen_page: UserProfileSettingsScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_user_settings_icon()
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.DATE_AND_TIME_TAB)
    user_profile_settings_screen_page.set_date_and_time_format()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
    user_profile_hub_screen_page.tap_done_button()
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.validate_dashboard_screen()

# endregion Given


# region When

@when('User enters the log screen')
def navigate_log_screen(dashboard_screen_page: DashBoardScreen, system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap(SystemSettingsScreenLocators.LOGS_TAB)

# endregion When
