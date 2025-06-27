import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_metering_pump_constants import SampleMeteringPumpConstants
from web_framework.kiosk.common.Constants.UI.logs import LogTableHeaders, SampleMeteringPumpLogConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_results_screen import SampleMeteringPumpResultsScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_screen import SampleMeteringPumpSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_metering_pump_workflow_summary_screen import SampleMeteringPumpSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_metering_pump_workflow_locators import (SampleMeteringPumpLocators, \
                                                                                                            SampleMeteringPumpSetupLocators,
                                                                                                            SampleMeteringPumpSummaryLocators,
                                                                                                            SampleMeteringPumpResultsLocators,
                                                                                                            SampleMeteringPumpStatusLocators,
                                                                                                            SampleMeteringPumpLogScreenLocators)
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.Locators.User.user_profile_hub import UserProfileHubPageLocators
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen
from web_framework.kiosk.pages.UserProfileSettings.user_profile_settings_screen import UserProfileSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/SampleManager/sample_metering_pump_workflow.feature')


@pytest.fixture
def sample_metering_pump_workflow_results_page(page_builder):
    page = page_builder(SampleMeteringPumpResultsScreen)
    return page


@given("User navigates to sample manager section within health troubleshoot area")
def navigate_troubleshoot_sample_manager(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
    health_screen_page.tap(HealthScreenLocators.SAMPLE_MANAGER_ICON)


@given(cfparse('User sets pre-required date and time format'))
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


@when('User navigates to the target pressure screen')
def navigate_target_pressure(sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    sample_metering_pump_workflow_setup_page.tap_next_button()
    sample_metering_pump_workflow_setup_page.tap_next_button()


@when('User enters the log screen')
def navigate_log_screen(dashboard_screen_page: DashBoardScreen, system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap(SystemSettingsScreenLocators.LOGS_TAB)


@when('User taps sample metering pump leak test start panel')
def start_metering_pump_workflow(health_screen_page: HealthHomeScreen,
                                 sample_metering_pump_workflow_setup_page):
    health_screen_page.validate_idle_state()
    health_screen_page.tap(HealthScreenLocators.SAMPLE_METERING_PUMP_PANEL)
    sample_metering_pump_workflow_setup_page.validate_welcome_screen()


@when(cfparse('User chooses the prime "{toggle_position:bool}"', CONVERTERS))
def toggle_priming_option(toggle_position: bool, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    if sample_metering_pump_workflow_setup_page.is_toggle_button_enabled(SampleMeteringPumpSetupLocators.PRIME_TOGGLE) != toggle_position:
        sample_metering_pump_workflow_setup_page.tap(SampleMeteringPumpSetupLocators.PRIME_TOGGLE)

    elif not sample_metering_pump_workflow_setup_page.is_toggle_button_enabled(SampleMeteringPumpSetupLocators.PRIME_TOGGLE) and toggle_position == "true":
        sample_metering_pump_workflow_setup_page.tap(SampleMeteringPumpSetupLocators.PRIME_TOGGLE)

    sample_metering_pump_workflow_setup_page.set_selected_prime_option(toggle_position)
    sample_metering_pump_workflow_setup_page.tap_next_button()


@when(cfparse('User enters the solvent details "{line_1}", "{line_2}", "{line_3}", "{line_4}" for Setup'))
def set_solvent_option(context, line_1, line_2, line_3, line_4, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    context['current_solvent_composition'] = sample_metering_pump_workflow_setup_page.selected_and_get_solvent_details(line_1, line_2, line_3, line_4)


@when(cfparse('User enters the "{pressure_value}" details'))
def enter_pressure_value(pressure_value, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    sample_metering_pump_workflow_setup_page.wait_for_element_load(SampleMeteringPumpSetupLocators.PRESSURE_TEXT_FIELD,
                                                                   sample_metering_pump_workflow_setup_page.wait_time)
    sample_metering_pump_workflow_setup_page.enter_value_for_specific_module(SampleMeteringPumpSetupLocators.PRESSURE_TEXT_FIELD, pressure_value)


@when("User taps next")
def tap_next_button(sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    sample_metering_pump_workflow_setup_page.tap_next_button()


@when("User taps start")
def tap_start_button(context, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen,
                     sample_metering_pump_workflow_summary_page: SampleMeteringPumpSummaryScreen):
    context['current_date_time'] = current_date()
    sample_metering_pump_workflow_summary_page.validate_summary_screen()
    sample_metering_pump_workflow_summary_page.tap(SampleMeteringPumpLocators.START_BUTTON)
    sample_metering_pump_workflow_setup_page.wait_for_test_end()


@when(cfparse('User starts and then aborts the sample metering pump workflow at different "{stop_time:d}"'))
def abort_workflow(context, stop_time, sample_metering_pump_workflow_summary_page: SampleMeteringPumpSummaryScreen):
    context['current_date_time'] = current_date()
    sample_metering_pump_workflow_summary_page.validate_summary_screen()
    sample_metering_pump_workflow_summary_page.tap(SampleMeteringPumpLocators.START_BUTTON)
    time.sleep(stop_time)
    sample_metering_pump_workflow_summary_page.tap(SampleMeteringPumpStatusLocators.STOP_BUTTON)


@then(cfparse('User validates the total composition is "{total_composition:f}"'))
def validate_composition(context, total_composition: float):
    current_composition = 0
    for solvent in context['current_solvent_composition'].get_solvent_lines():
        solvent = float(solvent)
        current_composition += solvent
    assert current_composition == total_composition, f"Composition was not as expected. Expected: [{total_composition}], Actual: [{current_composition}]"


@then(cfparse('User validates the "{error_state:bool}"', CONVERTERS))
def validate_edit_field_state(error_state: bool, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    edit_field_error_state = sample_metering_pump_workflow_setup_page.is_edit_field_in_error_state(SampleMeteringPumpSetupLocators.PRESSURE_FIELD)
    assert edit_field_error_state == error_state, f"Edit field state is not as expected. Expected: [{error_state}], " \
                                                  f"Actual:[{edit_field_error_state}]"


@then('User validates welcome context in the welcome screen')
def validate_welcome_text(sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen):
    actual_paragraph_text = sample_metering_pump_workflow_setup_page.get_welcome_paragraph_text()

    expected_paragraph_text = SampleMeteringPumpConstants.expected_welcome_paragraph_text
    assert actual_paragraph_text == expected_paragraph_text, f"Paragraph text was not as expected. Expected: [{expected_paragraph_text}], " \
                                                             f"Actual: [{actual_paragraph_text}]"


@then(cfparse('User validates the summary screen details for "{line_1}", "{line_2}", "{line_3}", "{line_4}", "{toggle_position:bool}" and "{pressure_value}"',
              CONVERTERS))
def validate_summary_screen_details(toggle_position: bool, line_1,
                                    line_2, line_3, line_4, pressure_value, sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen,
                                    sample_metering_pump_workflow_summary_page: SampleMeteringPumpSummaryScreen):
    sample_metering_pump_workflow_summary_page.validate_summary_screen()

    expected_composition = sample_metering_pump_workflow_setup_page.get_expected_composition(line_1, line_2, line_3, line_4)
    current_composition = sample_metering_pump_workflow_summary_page.get_container_text(SampleMeteringPumpSummaryLocators.COMPOSITION_LABEL)

    assert current_composition == expected_composition, f"Composition was not as expected. Expected: [{expected_composition}], Actual: [{current_composition}]"

    if toggle_position:
        sample_metering_pump_workflow_summary_page.wait_time_to_load_value(SampleMeteringPumpSummaryLocators.PRIMING_OPTION_INFO_LABEL, "")
        actual_priming_option = sample_metering_pump_workflow_summary_page.get_text(SampleMeteringPumpSummaryLocators.PRIMING_OPTION_INFO_LABEL)
    else:
        actual_priming_option = None

    actual_system_pressure = sample_metering_pump_workflow_summary_page.get_container_text(SampleMeteringPumpSummaryLocators.TARGET_PRESSURE_INFO_LABEL)
    expected_system_pressure = pressure_value
    expected_priming_option = sample_metering_pump_workflow_setup_page.get_expected_prime_option()
    assert expected_system_pressure in actual_system_pressure, f"System pressure was not as expected. Expected: [{expected_system_pressure}], " \
                                                               f"Actual: [{actual_system_pressure}]"
    assert expected_priming_option == actual_priming_option, f"Priming option was not as expected. Expected: [{expected_priming_option}], " \
                                                             f"Actual: [{actual_priming_option}]"


@then('User verifies the results screen details with optional leak rate in uL/min')
def validate_results_details(sample_metering_pump_workflow_setup_page: SampleMeteringPumpSetupScreen,
                             sample_metering_pump_workflow_results_page: SampleMeteringPumpResultsScreen):
    sample_metering_pump_workflow_results_page.tap(SampleMeteringPumpResultsLocators.TABLE_TOGGLE_ARROW)
    sample_metering_pump_workflow_results_page.wait_time_to_load_value(SampleMeteringPumpResultsLocators.LEAK_RATE_INFO_LABEL, "")
    leak_rate_text = sample_metering_pump_workflow_results_page.get_text(SampleMeteringPumpResultsLocators.LEAK_RATE_INFO_LABEL)
    current_leak_rate = TypeConverter.to_float(leak_rate_text)
    assert SampleMeteringPumpConstants.min_leak_rate <= current_leak_rate <= SampleMeteringPumpConstants.max_leak_rate, \
        f"Leak rate was not within expected limits. " \
        f"Expected: [{SampleMeteringPumpConstants.min_leak_rate}] to [{SampleMeteringPumpConstants.max_leak_rate}]," \
        f"Actual: [{current_leak_rate}]"

    sample_metering_pump_workflow_setup_page.tap(SampleMeteringPumpLocators.DONE_BUTTON)


@then('User validates status screen after aborting')
def validate_status_screen(sample_metering_pump_workflow_summary_page: SampleMeteringPumpSummaryScreen):
    sample_metering_pump_workflow_summary_page.validate_abort_status_screen()


@then('the log entry is created with correct time, date, category and action details')
def validate_log_entry_data(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    time_diff = is_within_tolerance(context['current_date_time'], log_entry[LogTableHeaders.date_and_time],
                                    SampleMeteringPumpConstants.MaximumToleranceInMinutes)

    assert SampleMeteringPumpLogConstants.WorkFlowCategory in log_entry[LogTableHeaders.category], (
        f"The Category was not as expected. Expected: [{SampleMeteringPumpLogConstants.WorkFlowCategory}], Actual: [{log_entry[LogTableHeaders.category]}]")

    assert SampleMeteringPumpLogConstants.Source in log_entry[LogTableHeaders.source], (
        f"The Source was not as expected. Expected: [{SampleMeteringPumpLogConstants.Source}], "
        f"Actual: [{log_entry[LogTableHeaders.source]}]")

    assert time_diff, \
        f"The Date and time was not as expected. Expected: [{context['current_date_time']}], Actual: [{log_entry[LogTableHeaders.date_and_time]}]"

    system_logs_screen.tap(SampleMeteringPumpLogScreenLocators.SampleMeteringPumpLogSource)
    system_logs_screen.validate_system_logs_screen()
    category_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    date_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    time_diff = is_within_tolerance(context['current_date_time'], date_text, SampleMeteringPumpConstants.MaximumToleranceInMinutes)

    assert time_diff, \
        f"The Date and time  was not as expected. Expected: [{context['current_date_time']}], Actual: [{log_entry[LogTableHeaders.date_and_time]}]"

    assert SampleMeteringPumpLogConstants.WorkFlowCategory in category_text, \
        f"The category was not as expected. Expected: [{SampleMeteringPumpLogConstants.WorkFlowCategory}], Actual: [{category_text}]"

    assert source_text == SampleMeteringPumpLogConstants.Source, \
        f"The Source was not found in the category list. Expected: [{SampleMeteringPumpLogConstants.Source}], Actual: [{source_text}]"
