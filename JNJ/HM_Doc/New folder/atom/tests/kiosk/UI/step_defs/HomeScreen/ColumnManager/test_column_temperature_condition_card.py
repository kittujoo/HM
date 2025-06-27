import math

import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.assert_timeout import AssertTimeout
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TemperatureConditionCardConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_manager_home_screen import ColumnManagerHomeScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_temperature_settings_screen import ColumnTemperatureSettingsScreen
from web_framework.kiosk.pages.Locators.Home.ColumnManager.column_temperature_condition_card import \
    ColumnTemperatureSettingScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/ColumnManager/column_temperature_condition_card.feature')


@pytest.fixture
def column_temperature_settings_screen_page(page_builder):
    page = page_builder(ColumnTemperatureSettingsScreen)
    return page


@given('Navigate to the column temperature setting screen')
@when('Navigate to the column temperature setting screen')
def navigate_to_column_temperature_settings_screen(column_manager_home_screen_page: ColumnManagerHomeScreen):
    column_manager_home_screen_page.validate_column_manager_home_screen()
    column_manager_home_screen_page.tap_column_temperature_condition_card()


@given(cfparse('Column manager temperature was set as "{actual_temperature}"'))
def set_temperature(actual_temperature: str, column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen,
                    column_manager_home_screen_page: ColumnManagerHomeScreen, assert_timeout: AssertTimeout):
    column_temperature_settings_screen_page.validate_column_temperature_settings_screen()
    column_temperature_settings_screen_page.wait_for_element_load(ColumnTemperatureSettingScreenLocators.TOGGLE_BUTTON,
                                                                  column_temperature_settings_screen_page.wait_time)
    is_toggle_button_enabled = column_temperature_settings_screen_page.is_toggle_button_enabled()

    if not is_toggle_button_enabled:
        column_temperature_settings_screen_page.tap_toggle_button()
        column_temperature_settings_screen_page.wait_for_element_load(ColumnTemperatureSettingScreenLocators.COLUMN_TEMPERATURE_LIST,
                                                                      column_temperature_settings_screen_page.wait_time)
    if actual_temperature != column_temperature_settings_screen_page.get_set_point():
        column_temperature_settings_screen_page.select_spinner_text(
            ColumnTemperatureSettingScreenLocators.COLUMN_TEMPERATURE_LIST,
            actual_temperature)
    column_temperature_settings_screen_page.wait_element_to_be_clickable(BasePageLocators.DONE_BUTTON, column_temperature_settings_screen_page.wait_time)
    column_temperature_settings_screen_page.tap_done_button()
    actual_temperature = int(actual_temperature)
    assert_timeout.is_true(lambda: math.isclose(column_manager_home_screen_page.get_column_temperature(), actual_temperature, abs_tol=1),
                           "The Expected Temperature Was Not Reached", WaitTimeConstants.SetTemperatureWait)


@when(cfparse('Set column manager temperature as "{actual_temperature}"'))
def set_temperature(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen, actual_temperature):
    column_temperature_settings_screen_page.validate_column_temperature_settings_screen()
    column_temperature_settings_screen_page.wait_for_element_load(ColumnTemperatureSettingScreenLocators.TOGGLE_BUTTON,
                                                                  column_temperature_settings_screen_page.wait_time)
    is_toggle_button_enabled = column_temperature_settings_screen_page.is_toggle_button_enabled()

    # removing the decimal for set spinner
    if '.' in actual_temperature:
        actual_temperature = actual_temperature[:-2]

    if not is_toggle_button_enabled:
        column_temperature_settings_screen_page.tap_toggle_button()
        column_temperature_settings_screen_page.wait_for_element_load(ColumnTemperatureSettingScreenLocators.COLUMN_TEMPERATURE_LIST,
                                                                      column_temperature_settings_screen_page.wait_time)
    if actual_temperature != column_temperature_settings_screen_page.get_set_point():
        column_temperature_settings_screen_page.select_spinner_text(
            ColumnTemperatureSettingScreenLocators.COLUMN_TEMPERATURE_LIST,
            actual_temperature)


@when('User taps the toggle button to turn off the temperature control')
def turn_off_toggle_button(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    is_toggle_button_enabled = column_temperature_settings_screen_page.is_toggle_button_enabled()

    if is_toggle_button_enabled:
        column_temperature_settings_screen_page.tap_toggle_button()


@when('User taps the toggle button to turn on the temperature control')
def turn_off_toggle_button(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    is_toggle_button_enabled = column_temperature_settings_screen_page.is_toggle_button_enabled()

    if not is_toggle_button_enabled:
        column_temperature_settings_screen_page.tap_toggle_button()


@when('Tap the CANCEL button')
def tap_cancel_button(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    column_temperature_settings_screen_page.tap_cancel_button()


@when('User taps the DONE button')
def tap_done_button(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    column_temperature_settings_screen_page.tap_done_button()


@when('User navigates to home screen')
def navigate_to_home(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_home()


@then('Validate the setpoint temperature is not OFF')
def validate_set_point_temperature(column_manager_home_screen_page: ColumnManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: column_manager_home_screen_page.get_setpoint() != "OFF",
                           f"The Setpoint is not as expected. Expected:[Not Off] Actual[{column_manager_home_screen_page.get_setpoint()}]")


@then('Validate the temperature setpoint is OFF')
def validate_no_setpoint(column_manager_home_screen_page: ColumnManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: column_manager_home_screen_page.get_setpoint(), "OFF",
                             f"The Setpoint is not as expected. Expected:[OFF] Actual[{column_manager_home_screen_page.get_setpoint()}]")


@then(cfparse('Validate the status changes to "{status}"'))
def validate_status(status: str, column_manager_home_screen_page: ColumnManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: column_manager_home_screen_page.get_setpoint_status(), status, "The Expected Set Point Was Not Reached",
                             WaitTimeConstants.SetTemperatureWait)


@then(cfparse('Validate the temperature is "{expected_temperature:d}"'))
def validate_temperature(expected_temperature: int, column_manager_home_screen_page: ColumnManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: math.isclose(column_manager_home_screen_page.get_column_temperature(), expected_temperature, abs_tol=1),
                           "The Expected Temperature Was Not Reached", WaitTimeConstants.SetTemperatureWait)


@then(cfparse('The user validates "{expected_temperature}" info in the column manager card reader'))
def validate_card_reader(expected_temperature, dashboard_screen_page: DashBoardScreen, assert_timeout: AssertTimeout):
    dashboard_screen_page.validate_dashboard_screen()
    actual_temperature = dashboard_screen_page.get_temperature(
        TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE,
        TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_AFTER_DECIMAL)

    actual_temperature = float(actual_temperature)
    expected_temperature = float(expected_temperature)
    assert_timeout.is_true(lambda: math.isclose(expected_temperature, actual_temperature, abs_tol=1),
                           "The Expected Temperature Was Not Reached", WaitTimeConstants.SetTemperatureWait)
    actual_temperature_units = dashboard_screen_page.get_temperature_units(
        TopLevelDashBoardScreenLocators.COLUMN_TEMPERATURE_UNITS)
    expected_temperature_units = TemperatureConditionCardConstants.TemperatureUnits
    assert actual_temperature_units == expected_temperature_units, f"actual column temperature unit in card " \
                                                                   f"reader is {actual_temperature_units} Expected is {expected_temperature_units}"


@then('User validates the user cannot set the temperature')
def validate_temperature_edit_field_disabled(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    scroll_window_disabled = column_temperature_settings_screen_page.is_scroll_window_exists(
        ColumnTemperatureSettingScreenLocators.SCROLL_WINDOW_HEADER)

    assert not scroll_window_disabled, "Failed to navigate to column temperature setting "


@then('Validate the spinner component is visible')
def validate_spinner_component(column_temperature_settings_screen_page: ColumnTemperatureSettingsScreen):
    column_temperature_settings_screen_page.validate_temperature_setpoint_header()
    is_spinner_component_exists = column_temperature_settings_screen_page.is_scroll_window_exists \
        (ColumnTemperatureSettingScreenLocators.SCROLL_WINDOW_HEADER)
    assert is_spinner_component_exists, f" The spinner component does not exists"
