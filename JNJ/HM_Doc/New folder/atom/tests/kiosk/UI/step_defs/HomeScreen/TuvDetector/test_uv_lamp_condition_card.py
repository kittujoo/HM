import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Models.ConditionalCard.LampDetails import LampDetails
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Home.TuvDetector.uv_lamp_settings_screen import UVLampSettingsScreen
from web_framework.kiosk.pages.Locators.Home.TuvDetector.tuv_home_screen import TUVHomeScreenLocators
from web_framework.kiosk.pages.Locators.Home.TuvDetector.uv_lamp_condition_card_locators import UVLampConditionCardLocators, UVLampConditionCardSettingsLocators
from web_framework.kiosk.pages.Locators.System.PerformanceCounters.performance_counters_screen import PerformanceCounterScreenLocators
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
from web_framework.kiosk.pages.System.PerformanceCounters.performance_counters_screen import PerformanceCountersScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/TuvDetector/uv_lamp_condition_card.feature')

logger = Logger(__name__)


@pytest.fixture
def uv_lamp_condition_card_settings_screen(page_builder):
    page = page_builder(UVLampSettingsScreen)
    return page


@pytest.fixture
def tuv_home_screen_page(dashboard_screen_page: DashBoardScreen, page_builder):
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_tuv_schematic_icon()
    page = page_builder(TUVDetectorHomeScreen)
    return page


@pytest.fixture
def performance_counters_screen(page_builder):
    page = page_builder(PerformanceCountersScreen)
    return page


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


@given('User is at the UV lamp settings screen')
def validate_uv_lamp_settings_screen(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen, tuv_home_screen_page: TUVDetectorHomeScreen):
    tuv_home_screen_page.tap(TUVHomeScreenLocators.UV_LAMP_CONDITIONAL_CARD)
    uv_lamp_condition_card_settings_screen.validate_uv_lamp_settings_screen()


@when('User navigates to the actions tab')
def navigate_actions_tab(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardLocators.ACTIONS_NAV_BUTTON)


@when('User navigates to the details tab')
def navigate_details_tab(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardLocators.DETAILS_NAV_BUTTON)


@when('User navigates to the settings tab')
@then('User navigates to the settings tab')
def navigate_settings_tab(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardLocators.SETTINGS_NAV_BUTTON)


@when(cfparse('User sets the warning to "{warning_state}"'))
def set_warning_state(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen, warning_state):
    if warning_state == 'True':
        if not uv_lamp_condition_card_settings_screen.is_toggle_component_enabled(UVLampConditionCardSettingsLocators.LIFE_WARNING_TOGGLE):
            uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardSettingsLocators.LIFE_WARNING_TOGGLE)
    else:
        if uv_lamp_condition_card_settings_screen.is_toggle_component_enabled(UVLampConditionCardSettingsLocators.LIFE_WARNING_TOGGLE):
            uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardSettingsLocators.LIFE_WARNING_TOGGLE)


@then('User validates the UV lamp details information')
def validate_details_screen_information(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    try:
        uv_lamp_condition_card_settings_screen.wait_time_to_load_value(UVLampConditionCardSettingsLocators.SERIAL_NUMBER_INFO_LABEL)
        actual_serial_number = uv_lamp_condition_card_settings_screen.get_container_text(UVLampConditionCardSettingsLocators.SERIAL_NUMBER_INFO_LABEL)
        actual_install_date = uv_lamp_condition_card_settings_screen.get_container_text(UVLampConditionCardSettingsLocators.INSTALL_DATE_INFO_LABEL)
        actual_lamp_hour_used = uv_lamp_condition_card_settings_screen.get_hours()
        actual_successful_ignitions = uv_lamp_condition_card_settings_screen.get_container_text(UVLampConditionCardSettingsLocators.SUCCESSFUL_IGNITIONS)
        actual_successful_ignitions = int(actual_successful_ignitions)
        logger.info(f"actual_successful_ignitions ===>>{actual_successful_ignitions}")
        actual_failed_ignitions = uv_lamp_condition_card_settings_screen.get_container_text(UVLampConditionCardSettingsLocators.FAILED_IGNITIONS)
        actual_failed_ignitions = int(actual_failed_ignitions)

        Lamp_details = LampDetails(serial_number=actual_serial_number,
                                   install_date=actual_install_date,
                                   lamp_hours_used=actual_lamp_hour_used,
                                   successful_ignitions=actual_successful_ignitions,
                                   failed_ignitions=actual_failed_ignitions)
        logger.info(f"Lamp_details {Lamp_details}")
    finally:
        uv_lamp_condition_card_settings_screen.tap_close_button()


@then(cfparse('User verifies the warning is set to "{warning_state}"'))
def validate_lamp_warning_state(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen, warning_state):
    assert uv_lamp_condition_card_settings_screen.is_toggle_component_enabled(UVLampConditionCardSettingsLocators.LIFE_WARNING_TOGGLE) == TypeConverter.to_bool(
        warning_state), f"The warning toggle was not saved properly"


@then('User returns to the UV lamp settings screen')
def navigate_return_uv_lamp_settings_screen(tuv_detector_home_screen_page: TUVDetectorHomeScreen):
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    tuv_detector_home_screen_page.tap(TUVHomeScreenLocators.UV_LAMP_CONDITIONAL_CARD)


@then('User taps cancel')
def tap_cancel(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardLocators.CANCEL_BUTTON)


@then('User confirms the changes')
def tap_done(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.tap(UVLampConditionCardLocators.DONE_BUTTON)


@when("User get the lamp hours used info from the lamp details")
def get_lamp_info(uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    uv_lamp_condition_card_settings_screen.wait_for_element_visibility(5, UVLampConditionCardSettingsLocators.LAMP_HOURS_INFO_LABEL)
    actual_hours_info = uv_lamp_condition_card_settings_screen.get_container_text(UVLampConditionCardSettingsLocators.LAMP_HOURS_INFO_LABEL)
    uv_lamp_condition_card_settings_screen.set_lamp_hours_info(actual_hours_info)
    logger.info(f"actual_hours_info ===>>> {actual_hours_info}")
    uv_lamp_condition_card_settings_screen.tap_close_button()


@then("User validates the lamp hours info in the condition card")
def validate_lamp_details(tuv_home_screen_page: TUVDetectorHomeScreen, uv_lamp_condition_card_settings_screen: UVLampSettingsScreen,
                          assert_timeout: AssertTimeout):
    actual_lamp_hours_info = uv_lamp_condition_card_settings_screen.lamp_hours_separator(TUVHomeScreenLocators.LAMP_READBACK_STATUS, "of")
    actual_lamp_used_hours = actual_lamp_hours_info[0]
    actual_lamp_total_hours = actual_lamp_hours_info[1]

    expected_lamp_used_hours = uv_lamp_condition_card_settings_screen.get_lamp_used_hours()
    expected_lamp_total_hours = uv_lamp_condition_card_settings_screen.get_lamp_total_hours()

    assert_timeout.are_equal(lambda: actual_lamp_used_hours, expected_lamp_used_hours, "There is a mismatch between the lamp hours displayed", 5, 1)
    assert_timeout.are_equal(lambda: actual_lamp_total_hours, expected_lamp_total_hours, "There is a mismatch between the lamp hours displayed", 5, 1)

    tuv_home_screen_page.validate_lamp_hours_state(TUVHomeScreenLocators.LAMP_STATUS_BAR, actual_lamp_used_hours, actual_lamp_total_hours)


@then("User validates the lamp hours used info in the card reader")
def validate_card_reader_lamp_info(dashboard_screen_page: DashBoardScreen, uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    expected_lamp_used_hours = uv_lamp_condition_card_settings_screen.get_lamp_used_hours()
    expected_lamp_total_hours = uv_lamp_condition_card_settings_screen.get_lamp_total_hours()

    dashboard_screen_page.tap_home()
    actual_lamp_used_hours = dashboard_screen_page.get_container_text(TopLevelDashBoardScreenLocators.LAMP_USED_HOURS_READBACK_MESSAGE)
    actual_lamp_total_hours = dashboard_screen_page.get_total_lamp_hours()

    assert actual_lamp_used_hours == expected_lamp_used_hours, "There is a mismatch between the lamp hours displayed "
    assert actual_lamp_total_hours == expected_lamp_total_hours, "There is a mismatch between the lamp hours displayed"


@then("User validates the lamp hours info in the performance counters screen")
def validate_performance_counter_lamp_info(system_settings_screen: SystemSettingsScreen, dashboard_screen_page: DashBoardScreen,
                                           performance_counters_screen: PerformanceCountersScreen,
                                           uv_lamp_condition_card_settings_screen: UVLampSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_performance_counters_tab()
    performance_counters_screen.validate_performance_counters_screen()

    actual_lamp_hours_info = performance_counters_screen.lamp_hours_separator(PerformanceCounterScreenLocators.LAMP_LIFE_HOURS, "of")
    actual_lamp_used_hours = actual_lamp_hours_info[0]
    actual_lamp_total_hours = actual_lamp_hours_info[1]
    actual_lamp_hours_counter = performance_counters_screen.get_container_text(PerformanceCounterScreenLocators.LAMP_HOURS_COUNTER)

    expected_lamp_used_hours = uv_lamp_condition_card_settings_screen.get_lamp_used_hours()
    expected_lamp_total_hours = uv_lamp_condition_card_settings_screen.get_lamp_total_hours()

    lamp_hours_progress_bar = performance_counters_screen.get_lamp_progress_bar()
    actual_lamp_used_hours_float = TypeConverter.to_float(actual_lamp_used_hours)
    actual_lamp_total_hours_float = TypeConverter.to_float(actual_lamp_total_hours)
    lamp_life_usage = round((actual_lamp_used_hours_float / actual_lamp_total_hours_float) * 100, 2)

    assert actual_lamp_used_hours == expected_lamp_used_hours, "There is a mismatch between the lamp used hours displayed "
    assert actual_lamp_total_hours == expected_lamp_total_hours, "There is a mismatch between the lamp total hours displayed"
    assert actual_lamp_hours_counter == expected_lamp_used_hours, "There is a mismatch between the lamp counter hours displayed"
    assert lamp_hours_progress_bar == lamp_life_usage, "There is a mismatch between the lamp progress displayed"
