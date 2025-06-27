import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then

from utilities.assert_timeout import AssertTimeout
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.System.PerformanceCounters.performance_counters_screen import PerformanceCounterScreenLocators
from web_framework.kiosk.pages.System.PerformanceCounters.performance_counters_screen import PerformanceCountersScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SampleManager/injection_count_condition_card.feature')


@pytest.fixture
def performance_counters_screen(page_builder):
    page = page_builder(PerformanceCountersScreen)
    return page


@given('User navigates to the system - performance counters screen')
def navigate_performance_counter_screen(system_settings_screen: SystemSettingsScreen, dashboard_screen_page: DashBoardScreen,
                                        performance_counters_screen: PerformanceCountersScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_performance_counters_tab()
    performance_counters_screen.validate_performance_counters_screen()


@when('User taps to reset the total injection count')
def tap_reset_injection_count(performance_counters_screen: PerformanceCountersScreen):
    performance_counters_screen.validate_performance_counters_screen()
    performance_counters_screen.tap_more_options_button()
    time.sleep(2)  # required for the slider animation to complete
    performance_counters_screen.wait_for_element_visibility(3, PerformanceCounterScreenLocators.RESET_BUTTON)
    performance_counters_screen.tap_reset_button()
    performance_counters_screen.tap_reset_confirm_button()


@then('User validates the total injection count was reset')
def validate_injection_count_reset_settings_screen(performance_counters_screen: PerformanceCountersScreen, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: performance_counters_screen.get_text(PerformanceCounterScreenLocators.INJECTION_COUNT), "0",
                             "The injection count was not reset within the settings screen", 10, 1)


@then('User validates the sample injections was reset in the card reader')
def validate_injection_count_reset_card_reader(performance_counters_screen: PerformanceCountersScreen, dashboard_screen_page: DashBoardScreen,
                                               assert_timeout: AssertTimeout):
    performance_counters_screen.tap_performance_counter_back_button()
    dashboard_screen_page.tap_home()
    assert_timeout.are_equal(lambda: dashboard_screen_page.get_sample_injection_count(), "0", "The injection count was not reset within the card reader", 10, 1)


@then('User validates the injection count was reset in the condition card')
def validate_injection_count_reset_condition_card(sample_manager_home_screen_page: SampleManagerHomeScreen, assert_timeout: AssertTimeout):
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    sample_manager_home_screen_page.tap_second_page()
    assert_timeout.are_equal(lambda: sample_manager_home_screen_page.get_text(SampleManagerHomeScreenLocators.INJECTION_COUNT_VALUE), "0",
                             "The injection count was not reset on the condition card", 10, 1)
