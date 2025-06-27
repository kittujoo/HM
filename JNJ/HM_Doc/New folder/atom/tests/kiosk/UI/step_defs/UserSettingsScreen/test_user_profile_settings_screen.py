import re
import time
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.Locators.lock_screen_locators import LockScreenPageLocators
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_page_locator_lookup import UserSettingsPageLocatorLookup
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen
from web_framework.kiosk.pages.lock_screen import LockScreen
from web_framework.kiosk.pages.sign_in_screen import SignInScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/UserSettingsScreen/user_profile_settings.feature')

logger = Logger(__name__)


###########################
# - General / HUB steps - #
###########################


@given('User navigates to the user profile screen')
def user_profile_screen(session_dash_board_screen_page: DashBoardScreen):
    logger.info("The user profile settings screen test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_user_settings_icon()


@given('User navigates to the kiosk settings')
def kiosk_settings(session_dash_board_screen_page: DashBoardScreen,
                   user_profile_settings_screen_page: UserProfileSettingsScreen):
    logger.info("The kiosk settings test begins *************")
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_system()
    session_dash_board_screen_page.tap(SystemSettingsScreenLocators.KIOSK_SETTINGS_TAB)
    user_profile_settings_screen_page.validate_user_settings_screen()


@then('User navigates to the user settings hub')
def navigate_back_screen_saver_tab(dashboard_screen_page: DashBoardScreen,
                                   user_profile_hub_screen_page: UserProfileHubScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_user_settings_icon()
    user_profile_hub_screen_page.validate_user_hub_screen()


@then('User confirms the user profile settings through kiosk settings')
def tap_done_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@then('User returns to the dashboard')
def navigate_return_dashboard(user_profile_hub_screen_page: UserProfileHubScreen,
                              dashboard_screen_page: DashBoardScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap_done_button()
    dashboard_screen_page.tap_home()
    dashboard_screen_page.validate_dashboard_screen()


@then('User signs back into KIOSK')
def sign_into_kiosk(signin_screen_page: SignInScreen):
    signin_screen_page.press_esc_key()
    signin_screen_page.validate_sign_in_screen()
    signin_screen_page.enter_pin("1234")
    signin_screen_page.tap_unlock_button()


@then('User applies the user profile settings')
def tap_apply_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap_apply_button()


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@when('User cancels the user profile settings')
@then('User cancels the user profile settings')
def tap_cancel_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.CANCEL_BUTTON)


@then('User cancels the user profile settings through kiosk screen')
def tap_cancel_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap_cancel_button()


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@when('User confirms the user profile settings')
@then('User confirms the user profile settings')
def tap_done_button(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@when('User signs out of the KIOSK')
def sign_out_from_user_hub(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SIGN_OUT_BUTTON)
    # sleep time for the modal to appear
    time.sleep(1)
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SIGN_OUT_CONFIRM)


#########################
# -- Sounds Settings -- #
#########################


@when('User taps the sound tab')
def tap_sound_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SOUND_TAB)


@when(cfparse('User sets the volume as "{volume_settings}"'))
def set_sound_settings(user_profile_settings_screen_page: UserProfileSettingsScreen, volume_settings):
    # user_profile_settings_screen_page.navigate_volume_settings_page()
    user_profile_settings_screen_page.validate_volume_settings_screen()
    user_profile_settings_screen_page.set_volume(volume_settings)


################################
# -- Date and Time Settings -- #
################################

# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then('User taps the Date and Time format tab')
@when('User taps the Date and Time format tab')
def tap_date_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.DATE_AND_TIME_TAB)


@when('User navigates to the date and time tab')
def navigate_datetime_tab(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_user_settings_screen()
    user_profile_settings_screen_page.navigate_datetime_settings_page()


@when('User taps the time zone tab')
def tap_time_zone_tab(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.TIME_ZONE_TAB)


@when(cfparse('User scrolls to an "{time_zone_option}" in the time zone'))
def scroll_to_time_zone_option(user_profile_settings_screen_page: UserProfileSettingsScreen, time_zone_option):
    date_format_style_dictionary = UserSettingsPageLocatorLookup.time_zone_dictionary
    user_profile_settings_screen_page.scroll_to_spinner_options(time_zone_option, date_format_style_dictionary)


@when(cfparse('User scrolls to select the date format as "{date_format}"'))
def scroll_to_select_date_format(user_profile_settings_screen_page: UserProfileSettingsScreen, date_format):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DATE_FORMAT_PANEL)
    date_format_style_dictionary = UserSettingsPageLocatorLookup.datetime_format_dictionary
    user_profile_settings_screen_page.scroll_to_spinner_options(date_format, date_format_style_dictionary)


@then(cfparse('Validate the time zone option "{expected_text}"'))
def validate_time_zone_option(user_profile_settings_screen_page: UserProfileSettingsScreen, expected_text, dashboard_screen_page: DashBoardScreen):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    try:
        user_profile_settings_screen_page.validate_time_zone_option(expected_text)
    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
        user_profile_settings_screen_page.tap_done_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.validate_dashboard_screen()


@when(cfparse('User selects the time format as "{time_format}"'))
def select_time_format(user_profile_settings_screen_page: UserProfileSettingsScreen, time_format):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    if time_format == "24 Hour":
        if not user_profile_settings_screen_page.is_toggle_component_enabled(UserSettingsScreenPageLocators.TIME_TOGGLE):
            user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.TIME_TOGGLE)
    else:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.TIME_TOGGLE)


@when(cfparse('User selects the date format as "{date_format}"'))
def select_date_format(user_profile_settings_screen_page: UserProfileSettingsScreen, date_format):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DATE_FORMAT_PANEL)
    user_profile_settings_screen_page.select_spinner_text(UserSettingsScreenPageLocators.DATE_FORMAT_LIST, date_format)


@when(cfparse('User sets the date as "{month}" "{day}" "{year}"'))
def set_date(user_profile_settings_screen_page: UserProfileSettingsScreen, month, day, year):
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.SELECT_DATE_PANEL)
    user_profile_settings_screen_page.select_spinner_text(UserSettingsScreenPageLocators.SELECT_MONTH_SPINNER, month)
    user_profile_settings_screen_page.set_spinner_value(UserSettingsScreenPageLocators.SELECT_DAY_SPINNER, day)
    user_profile_settings_screen_page.set_spinner_value(UserSettingsScreenPageLocators.SELECT_YEAR_SPINNER, year)


@then('User navigates back to the date and time tab')
def navigate_back_datetime_tab(dashboard_screen_page: DashBoardScreen,
                               user_profile_hub_screen_page: UserProfileHubScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_user_settings_icon()
    user_profile_hub_screen_page.validate_user_hub_screen()


@then(cfparse('User verifies the "{time_format}" and the "{displayed_time_format}" were saved'))
def validate_time_format_saved(user_profile_settings_screen_page: UserProfileSettingsScreen,
                               time_format, displayed_time_format):
    try:
        user_profile_settings_screen_page.validate_datetime_settings_screen()
        if time_format == "24 Hour":
            assert user_profile_settings_screen_page.is_toggle_component_enabled(
                UserSettingsScreenPageLocators.TIME_TOGGLE), f"The time format: {time_format}, was not saved"
        else:
            assert not user_profile_settings_screen_page.is_toggle_component_enabled(
                UserSettingsScreenPageLocators.TIME_TOGGLE), f"The time format: {time_format}, was not saved"
        assert displayed_time_format == user_profile_settings_screen_page.get_displayed_time_format(), f"The time format: {displayed_time_format}, is incorrect from expected"
    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
        user_profile_settings_screen_page.tap_done_button()


@then(cfparse('User verifies the "{date_format}" was saved'))
def validate_date_format_saved(user_profile_settings_screen_page: UserProfileSettingsScreen, date_format, dashboard_screen_page: DashBoardScreen):
    try:
        user_profile_settings_screen_page.validate_datetime_settings_screen()
        assert date_format == user_profile_settings_screen_page.get_current_date_format(), f"The date format: {date_format}, was not saved"
    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)
        user_profile_settings_screen_page.tap_done_button()
        dashboard_screen_page.tap_home()
        dashboard_screen_page.validate_dashboard_screen()


@then('User selects and validates the time zone option')
def select_time_zone_option(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.TIME_ZONE_PANEL)
    user_profile_settings_screen_page.select_and_validate_time_zone_options()


@then('User selects and validates the date format option')
def select_and_validate_date_format(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_datetime_settings_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DATE_FORMAT_PANEL)
    user_profile_settings_screen_page.select_and_validate_date_format_options()


@then(cfparse('User verifies the date format in logs is "{date_format}"'))
def validate_system_logs_screen(system_settings_screen: SystemSettingsScreen, date_format, dashboard_screen_page: DashBoardScreen):
    try:
        dashboard_screen_page.tap_system()
        system_settings_screen.tap(SystemSettingsScreenLocators.LOGS_TAB)
        log_list_text: list = system_settings_screen.get_text_from_table(SystemLogsScreenLocators.LOG_TABLE_COLUMN)
        log_date = log_list_text[0]
        date_format_pattern = UserSettingsPageLocatorLookup.date_time_format_pattern
        assert re.findall(date_format_pattern[date_format], log_date), f"The Date format is not as expected. Expected format: {date_format}"
    finally:
        system_settings_screen.tap(SystemLogsScreenLocators.BACK_BUTTON)
        dashboard_screen_page.tap_home()
        dashboard_screen_page.validate_dashboard_screen()


@then(cfparse('User verifies "{displayed_time_format}" is reflected in logs'))
def validate_time_in_system_logs_screen(dashboard_screen_page: DashBoardScreen, system_settings_screen: SystemSettingsScreen, displayed_time_format):
    try:
        dashboard_screen_page.tap_system()
        system_settings_screen.tap(SystemSettingsScreenLocators.LOGS_TAB)
        log_list_text: list = system_settings_screen.get_text_from_table(SystemLogsScreenLocators.LOG_TABLE_COLUMN)
        log_time = log_list_text[0]
        time_format_pattern = UserSettingsPageLocatorLookup.date_time_format_pattern
        assert re.findall(time_format_pattern[displayed_time_format], log_time), f"The Time format is not as expected. Expected format: {displayed_time_format}"
    finally:
        system_settings_screen.tap(SystemLogsScreenLocators.BACK_BUTTON)
        dashboard_screen_page.tap_home()
        dashboard_screen_page.validate_dashboard_screen()


#####################################
# -- Display and Themes Settings -- #
#####################################
# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then('User taps the display tab')
@when('User taps the display tab')
def tap_display_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.DISPLAY)


@when(cfparse('User selects the theme settings as "{theme_settings}"'))
def select_them_settings(user_profile_settings_screen_page: UserProfileSettingsScreen, theme_settings):
    user_profile_settings_screen_page.validate_user_settings_screen()
    user_profile_settings_screen_page.select_theme_settings(theme_settings)


###############################
# -- Screen Saver Settings -- #
###############################

# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then('User taps the screen saver tab')
@when('User taps the screen saver tab')
def tap_screen_saver_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.SCREEN_SAVER)


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then('User navigates to the screen saver tab')
@when('User navigates to the screen saver tab')
def navigate_screen_saver_tab(user_profile_settings_screen_page: UserProfileSettingsScreen):
    user_profile_settings_screen_page.validate_user_settings_screen()
    user_profile_settings_screen_page.navigate_screen_saver_settings_page()


@when(cfparse('User selects the screen saver settings period as "{screen_saver_period}"'))
def select_screen_saver_period(user_profile_settings_screen_page: UserProfileSettingsScreen, screen_saver_period):
    user_profile_settings_screen_page.select_screen_saver_period(screen_saver_period)


@then(cfparse('Validate the screen saver picker is displayed "{expected_screen_saver_picker_display_status}"'))
def validate_screen_saver_picker(user_profile_settings_screen_page: UserProfileSettingsScreen,
                                 expected_screen_saver_picker_display_status):
    logger.info("***************The user profile settings screen test ends *************")

    try:
        is_screen_saver_picker_displayed = user_profile_settings_screen_page.is_screen_saver_displayed()
        expected_screen_saver_picker_display_status = TypeConverter.to_bool(expected_screen_saver_picker_display_status)
        assert is_screen_saver_picker_displayed == expected_screen_saver_picker_display_status, f"The actual screen saver is displayed {is_screen_saver_picker_displayed} "

    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.CANCEL_BUTTON)
        user_profile_settings_screen_page.tap_cancel_button()


@when(cfparse('User selects the screen saver style as "{screen_saver_style}"'))
def select_screen_saver_style(user_profile_settings_screen_page: UserProfileSettingsScreen, screen_saver_style):
    user_profile_settings_screen_page.validate_screen_saver_settings_screen()
    user_profile_settings_screen_page.select_spinner_text(UserSettingsScreenPageLocators.SCREEN_SAVER_LIST,
                                                          screen_saver_style)


@when(cfparse('User scrolls to select the style as "{screen_saver_style}"'))
def scroll_to(user_profile_settings_screen_page: UserProfileSettingsScreen, screen_saver_style):
    screen_saver_style_dictionary = UserSettingsPageLocatorLookup.screen_saver_style_dictionary
    user_profile_settings_screen_page.scroll_to_spinner_options(screen_saver_style, screen_saver_style_dictionary)


@then(cfparse('User verifies that the "{screen_saver_style}" was saved'))
def validate_screen_saver_style_saved(user_profile_settings_screen_page: UserProfileSettingsScreen, screen_saver_style):
    try:
        user_profile_settings_screen_page.validate_screen_saver_settings_screen()
        assert screen_saver_style == user_profile_settings_screen_page.get_container_text(
            UserSettingsScreenPageLocators.SCREEN_SAVER_PREVIEW_WINDOW), f"The screen saver style: {screen_saver_style}, was not saved"
    finally:

        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.CANCEL_BUTTON)
        user_profile_settings_screen_page.tap_cancel_button()


@then(cfparse('User verifies that the "{screen_saver_style}" was not saved'))
def validate_screen_saver_style_not_saved(user_profile_settings_screen_page: UserProfileSettingsScreen,
                                          screen_saver_style):
    try:
        user_profile_settings_screen_page.validate_screen_saver_settings_screen()
        assert not screen_saver_style == user_profile_settings_screen_page.get_container_text(
            UserSettingsScreenPageLocators.SCREEN_SAVER_PREVIEW_WINDOW), f"The screen saver style: {screen_saver_style}, was saved when it should not have"
    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.CANCEL_BUTTON)
        user_profile_settings_screen_page.tap_cancel_button()


@then('User selects and validates the screen saver options')
def select_and_validate_screen_saver(user_profile_settings_screen_page):
    user_profile_settings_screen_page.select_and_validate_screen_saver_options()


@then(cfparse('User validates the screen saver option displayed is "{is_displayed}"'))
def is_screen_saver_displayed(user_profile_settings_screen_page: UserProfileSettingsScreen,
                              user_profile_hub_screen_page: UserProfileHubScreen, is_displayed):
    try:
        actual_screen_saver_option_state = user_profile_settings_screen_page.is_screen_saver_displayed()
        actual_screen_saver_option_state = TypeConverter.to_bool(actual_screen_saver_option_state)
        expected_screen_saver_option_state = TypeConverter.to_bool(is_displayed)
        assert actual_screen_saver_option_state == expected_screen_saver_option_state, \
            f"expected_screen_saver_option_state=> {expected_screen_saver_option_state}"

    finally:
        user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.CANCEL_BUTTON)
        user_profile_hub_screen_page.tap_cancel_button()


##################################
# -- Instrument Name Settings -- #
##################################

# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then('User taps the system name tab')
@when('User taps the system name tab')
def tap_instrument_name_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.INSTRUMENT_NAME)


@when(cfparse('User enters the "{system_name}"'))
def enter_system_name(user_profile_settings_screen_page: UserProfileSettingsScreen, system_name):
    user_profile_settings_screen_page.validate_instrument_name_screen()
    user_profile_settings_screen_page.clear_text_area(UserSettingsScreenPageLocators.INSTRUMENT_NAME_TEXT_AREA)
    user_profile_settings_screen_page.enter_string(system_name)
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@when(cfparse('User erases {length:d} characters from system name'))
def erase_system_name(user_profile_settings_screen_page: UserProfileSettingsScreen, length: int):
    user_profile_settings_screen_page.validate_user_settings_screen()
    user_profile_settings_screen_page.tap(UserProfileHubPageLocators.INSTRUMENT_NAME)
    user_profile_settings_screen_page.validate_instrument_name_screen()
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.INSTRUMENT_NAME_TEXT_AREA)
    user_profile_settings_screen_page.clear_text_area(UserSettingsScreenPageLocators.INSTRUMENT_NAME_TEXT_AREA, length=length)
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@then(cfparse('User validates the {instrument_name} was saved and displayed on lock screen'))
def validate_instrument_name_display(lock_screen_page: LockScreen, instrument_name):
    lock_screen_page.validate_lock_screen()
    assert lock_screen_page.get_text(LockScreenPageLocators.INSTRUMENT_NAME_LABEL) == instrument_name


@then(cfparse('User validates the comment card shows correct numbers with "{length}" characters'))
def validate_system_name_comment_card(user_profile_settings_screen_page: UserProfileSettingsScreen, user_profile_hub_screen_page: UserProfileHubScreen,
                                      dashboard_screen_page: DashBoardScreen, length):
    try:
        user_profile_settings_screen_page.validate_user_settings_screen()
        user_profile_settings_screen_page.tap(UserProfileHubPageLocators.INSTRUMENT_NAME)
        user_profile_settings_screen_page.validate_instrument_name_screen()
        expected_comment_card_string = length + "/30 characters"
        actual_comment_card_string = user_profile_settings_screen_page.get_system_name_comment_card_string()
        assert actual_comment_card_string == expected_comment_card_string, f" actual_comment_card_string = {actual_comment_card_string}"

    finally:
        tap_done_button(user_profile_settings_screen_page)
        navigate_return_dashboard(user_profile_hub_screen_page, dashboard_screen_page)


@then(cfparse('User validates the "{system_name}" was saved and displayed on user preferences screen'))
def validate_system_name(user_profile_settings_screen_page: UserProfileSettingsScreen, user_profile_hub_screen_page: UserProfileHubScreen,
                         dashboard_screen_page: DashBoardScreen, system_name):
    try:
        user_profile_settings_screen_page.validate_user_settings_screen()
        actual_system_name = user_profile_settings_screen_page.get_system_name()
        assert actual_system_name == system_name, f" actual_system_name = {actual_system_name}"

    finally:
        navigate_return_dashboard(user_profile_hub_screen_page, dashboard_screen_page)


##############################
# -- Lock Screen Settings -- #
##############################

@when('User taps the lock screen tab')
def tap_lock_screen_tab(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap(UserProfileHubPageLocators.LOCK_SCREEN)


@when(cfparse('User selects the lock screen period as "{lock_screen_period}"'))
def select_lock_screen_period(user_profile_settings_screen_page: UserProfileSettingsScreen, lock_screen_period):
    user_profile_settings_screen_page.validate_user_settings_screen()
    user_profile_settings_screen_page.select_screen_lock_period(lock_screen_period)
    user_profile_settings_screen_page.tap(UserSettingsScreenPageLocators.DONE_BUTTON)


@then(cfparse('User validates lock screen tab for duration "{lock_screen_period}"'))
def validate_lock_screen_duration(user_profile_settings_screen_page: UserProfileSettingsScreen, lock_screen_period,
                                  user_profile_hub_screen_page: UserProfileHubScreen,
                                  dashboard_screen_page: DashBoardScreen):
    try:
        user_profile_settings_screen_page.validate_user_settings_screen()
        actual_lock_duration_text = user_profile_settings_screen_page.get_screen_lock_duration()
        assert lock_screen_period in actual_lock_duration_text, f" {lock_screen_period} could not find in {actual_lock_duration_text}"
    finally:
        navigate_return_dashboard(user_profile_hub_screen_page, dashboard_screen_page)
