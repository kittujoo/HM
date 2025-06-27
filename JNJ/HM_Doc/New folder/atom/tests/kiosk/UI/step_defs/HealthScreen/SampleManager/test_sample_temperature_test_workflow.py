import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, step
from pytest_bdd.parsers import cfparse
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.sample_temperature_test_constants import SampleTemperatureTestConstants
from web_framework.kiosk.common.Constants.UI.logs import LogTableHeaders, SampleTemperatureLogConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_temperature_test_workflow_results_screen import SampleTemperatureTestResultsScreen
from web_framework.kiosk.pages.Health.SampleManager.sample_temperature_test_workflow_screen import SampleTemperatureTestSetupScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Locators.Health.SampleManager.sample_temperature_test_workflow_locators import SampleTemperatureTestLocators, \
    SampleTemperaturesummaryScreenLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/SampleManager/sample_temperature_test_workflow.feature')
logger = Logger("test_sample_temperature_test_workflow")


@pytest.fixture
def sample_temperature_test_setup_screen(page_builder):
    page = page_builder(SampleTemperatureTestSetupScreen)
    return page


@pytest.fixture
def sample_temperature_test_results_screen(page_builder):
    page = page_builder(SampleTemperatureTestResultsScreen)
    return page


@given("User navigates to sample manager section within health troubleshoot area")
def navigate_troubleshoot_sample_manager(dashboard_screen_page: DashBoardScreen, health_screen_page: HealthHomeScreen):
    dashboard_screen_page.validate_idle_state()
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
    health_screen_page.tap(HealthScreenLocators.SAMPLE_MANAGER_ICON)


@when('User taps sample temperature test panel')
def tap_sample_temp_test_panel(health_screen_page: HealthHomeScreen):
    health_screen_page.validate_idle_state()
    health_screen_page.tap(HealthScreenLocators.SAMPLE_TEMPERATURE_TEST_PANEL)


@when('User taps Start')
def tap_start_button(context, sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_summary_screen()
    sample_temperature_test_setup_screen.wait_till_condition_met(SampleTemperaturesummaryScreenLocators.SUMMARY_DOOR_STATE,
                                                                 SampleTemperatureTestConstants.ClosedDoorStatus,
                                                                 SampleTemperatureTestConstants.FailureMessage,
                                                                 SampleTemperatureTestConstants.TimeToLoadDoorState)
    context["date_time"] = current_date()
    context["category"] = SampleTemperatureLogConstants.Category
    sample_temperature_test_setup_screen.tap(SampleTemperatureTestLocators.START_BUTTON)


@when('User validates the preconditions')
def validate_preconditions(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_preconditions_screen()
    check_confirmation_checkbox(sample_temperature_test_setup_screen)
    sample_temperature_test_setup_screen.tap_next_button()


@when('User checks the confirmation check box')
def check_confirmation_checkbox(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.wait_for_element_enable(SampleTemperatureTestLocators.PRECONDITION_CHECKBOX,
                                                                 sample_temperature_test_setup_screen.long_wait_time)
    sample_temperature_test_setup_screen.tap(SampleTemperatureTestLocators.PRECONDITION_CHECKBOX)


@when('User taps Next button')
def tap_next(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.tap_next_button()


@when(cfparse('User aborts the sample temperature workflow after {wait_time: d} seconds'))
def validate_sample_temperature_test_abort_process(wait_time, context, sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_summary_screen()
    sample_temperature_test_setup_screen.wait_till_condition_met(SampleTemperaturesummaryScreenLocators.SUMMARY_DOOR_STATE,
                                                                 SampleTemperatureTestConstants.ClosedDoorStatus,
                                                                 SampleTemperatureTestConstants.FailureMessage,
                                                                 SampleTemperatureTestConstants.TimeToLoadDoorState)
    sample_temperature_test_setup_screen.tap(SampleTemperatureTestLocators.START_BUTTON)
    context["date_time"] = current_date()
    context["category"] = SampleTemperatureLogConstants.AbortCategory
    time.sleep(wait_time)  ##physically wait for 3 sec before aborting the workflow
    sample_temperature_test_setup_screen.validate_status_screen()
    sample_temperature_test_setup_screen.tap_stop_button()


@step('User validates the summary screen information')
def validate_summary_information(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_summary_screen()


@then('User validates the Next button is disabled')
def validate_next_button_disabled(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    assert not sample_temperature_test_setup_screen.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)


@then('User confirms the Next button is enabled')
def validate_next_button_enabled(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    assert sample_temperature_test_setup_screen.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)


@then('User validates the welcome context in the welcome screen')
def validate_welcome_screen_information(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_welcome_screen()
    assert sample_temperature_test_setup_screen.get_welcome_text() == SampleTemperatureTestConstants.expected_welcome_paragraph_text
    sample_temperature_test_setup_screen.tap_next_button()


@then('User validates the sample temperature test process')
def validate_sample_temperature_test_process(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.wait_for_test_end(SampleTemperatureTestLocators.STATUS_PAGE_BANNER,
                                                           SampleTemperatureTestLocators.RESULTS_PAGE_BANNER)


@then('User validates the results screen information with ambient temperature, target temperature and measured temperature')
def validate_results_screen_information(sample_temperature_test_results_screen: SampleTemperatureTestResultsScreen):
    sample_temperature_test_results_screen.validate_results_screen()
    sample_temperature_test_results_screen.tap(SampleTemperatureTestLocators.RESULTS_GRID_ARROW)
    sample_temperature_test_results_screen.validate_results_value()


@then(cfparse('User validates the test passes if the measured change is greater than {measured_change_temp: d}C'))
def validate_results_screen_measured_change(measured_change_temp, sample_temperature_test_results_screen, dashboard_screen_page: DashBoardScreen):
    sample_temperature_test_results_screen.validate_measured_change(measured_change_temp)
    sample_temperature_test_results_screen.tap_done_button()
    dashboard_screen_page.tap_diagnose()
    dashboard_screen_page.validate_idle_state()


@then('User validates the status stopped for the sample temperature workflow')
def validate_stop_workflow(sample_temperature_test_results_screen):
    sample_temperature_test_results_screen.validate_abort_status_screen()


@then('User validates the preconditions')
def validate_sample_temperature_preconditions(sample_temperature_test_setup_screen: SampleTemperatureTestSetupScreen):
    sample_temperature_test_setup_screen.validate_preconditions_screen()


@then('User verifies the sample temperature test log is generated')
def validate_sample_temperature_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    current_date_value = context["date_time"]
    category_value = context["category"]
    actual_log_date = log_entry[LogTableHeaders.date_and_time]
    time_diff = is_within_tolerance(current_date_value, actual_log_date, SampleTemperatureTestConstants.ToleranceTime)
    actual_log_category = log_entry[LogTableHeaders.category]
    actual_log_source = log_entry[LogTableHeaders.source]
    assert time_diff, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {current_date_value}. Actual date: {actual_log_date}')

    assert actual_log_category == category_value, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {category_value}. Actual category: {actual_log_category}')

    assert actual_log_source == SampleTemperatureLogConstants.Source, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {SampleTemperatureLogConstants.Source}. Actual source: {actual_log_source}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    time_diff = is_within_tolerance(current_date_value, date_text, SampleTemperatureTestConstants.ToleranceTime)
    assert time_diff, f"The Date and time is not as expected. Expected Date: {current_date_value}. Actual date: {date_text}"
    assert category_text == category_value, (f"The Category  is not as expected. Expected Category: "
                                             f"{category_value}. Actual Category: {category_text}")
    assert source_text == SampleTemperatureLogConstants.Source, (f"The Source is not as expected. Expected Source: {SampleTemperatureLogConstants.Source}. "
                                                                 f"Actual Source: {source_text}")

