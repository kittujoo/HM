from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.assert_timeout import AssertTimeout
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TemperatureConditionCardConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_temperature_settings_screen import SampleTemperatureSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.sample_temperature_condition_card import \
    SampleTemperatureSettingScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SampleManager/sample_temperature_condition_card.feature')


@when('User navigate to the sample temperature settings screen')
@given('Navigate to the sample temperature settings screen')
def tap_sample_temperature_settings_gear_icon(dashboard_screen_page: DashBoardScreen, sample_manager_home_screen_page: SampleManagerHomeScreen):
    dashboard_screen_page.validate_idle_state()
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    sample_manager_home_screen_page.tap_sample_temperature_condition_card()


@given(cfparse('Sample manager temperature was set as "{actual_temperature}"'))
def set_initial_temperature(actual_temperature: str, sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen,
                            sample_manager_home_screen_page: SampleManagerHomeScreen):
    sample_temperature_settings_screen_page.validate_sample_temperature_settings_screen()
    sample_temperature_settings_screen_page.wait_for_element_load(SampleTemperatureSettingScreenLocators.TOGGLE_BUTTON,
                                                                  sample_temperature_settings_screen_page.wait_time)
    is_toggle_button_enabled = sample_temperature_settings_screen_page.is_toggle_button_enabled()

    # removing the decimal for set spinner
    actual_temperature = actual_temperature[:-2]

    if not is_toggle_button_enabled:
        sample_temperature_settings_screen_page.tap_toggle_button()
        sample_temperature_settings_screen_page.wait_for_element_load(SampleTemperatureSettingScreenLocators.SAMPLE_TEMPERATURE_LIST,
                                                                      sample_temperature_settings_screen_page.wait_time)
    if actual_temperature != sample_manager_home_screen_page.get_set_point():
        sample_temperature_settings_screen_page.set_spinner_value(
            SampleTemperatureSettingScreenLocators.SAMPLE_TEMPERATURE_LIST,
            actual_temperature)
    sample_temperature_settings_screen_page.wait_element_to_be_clickable(BasePageLocators.DONE_BUTTON, sample_temperature_settings_screen_page.wait_time)
    sample_temperature_settings_screen_page.tap_done_button()


@when(cfparse('Set sample manager temperature as "{actual_temperature}"'))
def set_temperature(actual_temperature: str, sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    sample_temperature_settings_screen_page.validate_sample_temperature_settings_screen()
    is_toggle_button_enabled = sample_temperature_settings_screen_page.is_toggle_button_enabled()

    # removing the decimal for set spinner
    actual_temperature = actual_temperature[:-2]

    if not is_toggle_button_enabled:
        sample_temperature_settings_screen_page.tap_toggle_button()

    sample_temperature_settings_screen_page.set_spinner_value(
        SampleTemperatureSettingScreenLocators.SAMPLE_TEMPERATURE_LIST,
        actual_temperature)


@when('Tap the DONE button')
def tap_done_button(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    sample_temperature_settings_screen_page.tap_done_button()


@when('User navigates to home screen')
def navigate_to_home(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_home()


@when('Tap the CANCEL button')
def tap_cancel_button(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    sample_temperature_settings_screen_page.tap_cancel_button()


@when('Tap the toggle button to turn off the temperature control')
def turn_off_toggle_button(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    is_toggle_button_enabled = sample_temperature_settings_screen_page.is_toggle_button_enabled()

    if is_toggle_button_enabled:
        sample_temperature_settings_screen_page.tap_toggle_button()


@when('Tap the toggle button to turn on the temperature control')
def turn_on_toggle_button(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    is_toggle_button_enabled = sample_temperature_settings_screen_page.is_toggle_button_enabled()

    if not is_toggle_button_enabled:
        sample_temperature_settings_screen_page.tap_toggle_button()


@then('Validate the temperature setpoint is OFF')
def validate_no_setpoint(sample_manager_home_screen_page: SampleManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: sample_manager_home_screen_page.get_set_point(), "OFF",
                             f"The Setpoint is not as expected. Expected:[OFF] Actual[{sample_manager_home_screen_page.get_set_point()}]")


@then(cfparse('Validate the input "{expected_entered_value}" should not be affected by the hide/show of the edit field'))
def validate_text_edit_field(expected_entered_value: str, sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    current_entered_value = sample_temperature_settings_screen_page.get_set_temperature()
    assert current_entered_value == expected_entered_value, f"The Temperature " \
                                                            f"is not as expected. Expected:[{expected_entered_value}] Actual:[{current_entered_value}]"


@then('Validate the user cannot set the temperature')
def validate_temperature_edit_field_disabled(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    try:
        edit_field_disabled = sample_temperature_settings_screen_page.is_edit_field_exists(
            SampleTemperatureSettingScreenLocators.TEMPERATURE_EDIT_FIELD_COMPONENT)
        scroll_window_disabled = sample_temperature_settings_screen_page.is_scroll_window_exists(
            SampleTemperatureSettingScreenLocators.SCROLL_WINDOW_HEADER)

        assert (edit_field_disabled and scroll_window_disabled) is False, \
            "Failed to navigate to sample temperature setting "

    finally:
        sample_temperature_settings_screen_page.tap_cancel_button()


@then(cfparse('The user validates "{expected_temperature}" info in the sample manager card reader'))
def validate_card_reader(expected_temperature, dashboard_screen_page: DashBoardScreen):
    try:
        dashboard_screen_page.validate_dashboard_screen()
        actual_temperature = dashboard_screen_page.get_temperature(
            TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE,
            TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE_AFTER_DECIMAL)

        actual_temperature = TypeConverter.to_float(actual_temperature)
        expected_temperature = TypeConverter.to_float(expected_temperature)
        assert (actual_temperature - 1) <= expected_temperature <= (
                actual_temperature + 1), f" The actual temperature is {actual_temperature} Expected is {expected_temperature}"
        actual_temperature_units = dashboard_screen_page.get_temperature_units(
            TopLevelDashBoardScreenLocators.SAMPLE_TEMPERATURE_UNITS)
        expected_temperature_units = TemperatureConditionCardConstants.TemperatureUnits
        assert actual_temperature_units == expected_temperature_units, f"actual sample temperature unit in card " \
                                                                       f"reader is {actual_temperature_units} Expected is {expected_temperature_units}"

    finally:
        dashboard_screen_page.tap_sample_manager_schematic_icon()


@then(cfparse('User validates the temperature option is "{expected_temperature}"'))
def validate_scroll_options(expected_temperature: str, sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    current_entered_value = sample_temperature_settings_screen_page.get_set_temperature()
    assert current_entered_value == expected_temperature, f"The Temperature " \
                                                          f"is not as expected. Expected:[{expected_temperature}] Actual:[{current_entered_value}]"


@then('Validate the spinner component is visible')
def validate_spinner_component(sample_temperature_settings_screen_page: SampleTemperatureSettingsScreen):
    try:
        sample_temperature_settings_screen_page.validate_temperature_setpoint_header()
        is_spinner_component_exists = sample_temperature_settings_screen_page.is_scroll_window_exists \
            (SampleTemperatureSettingScreenLocators.SCROLL_WINDOW_HEADER)
        assert is_spinner_component_exists, f" The spinner component does not exists"

    finally:
        sample_temperature_settings_screen_page.tap_toggle_button_off()
        sample_temperature_settings_screen_page.tap_done_button()


@then('Validate the setpoint temperature is not OFF')
def validate_set_point_temperature(sample_manager_home_screen_page: SampleManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: sample_manager_home_screen_page.get_set_point() != "OFF",
                           f"The Setpoint is not as expected. Expected:[Not Off] Actual[{sample_manager_home_screen_page.get_set_point()}]")


@then(cfparse('Validate the status changes to "{status}"'))
def validate_status(status: str, sample_manager_home_screen_page: SampleManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: sample_manager_home_screen_page.get_setpoint_status(), status, "The Expected Set Point Was Not Reached",
                             WaitTimeConstants.SetTemperatureWait, polling_period_in_seconds = 0.01)


@given(cfparse('The temperature is "{expected_temperature:f}"'))
@then(cfparse('Validate the temperature is "{expected_temperature:f}"'))
def validate_temperature(expected_temperature: float, sample_manager_home_screen_page: SampleManagerHomeScreen, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: (expected_temperature - 1) <= sample_manager_home_screen_page.get_sample_temperature() <= (expected_temperature + 1),
                           "The Expected Temperature Was Not Reached", WaitTimeConstants.SetTemperatureWait)
