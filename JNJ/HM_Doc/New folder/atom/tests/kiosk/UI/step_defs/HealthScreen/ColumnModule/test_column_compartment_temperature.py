import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.date_utilities import is_within_tolerance, current_date
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.heater_cooler_constants import HeaterCoolerConstants
from web_framework.kiosk.common.Constants.UI.logs import LogTableHeaders, ColumnCompartmentTemperatureLogConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.ColumnModule.heater_cooler_workflow import HeaterCoolerWorkflowSetupScreen
from web_framework.kiosk.pages.Health.ColumnModule.heater_cooler_workflow_summary_screen import HeaterCoolerWorkflowSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Locators.Health.ColumnModule.heater_cooler_workflow_locators import HeaterCoolerWorkflowLocators, \
    HeaterCoolerPreconditionLocators, HeaterCoolerResultsLocators, HeaterCoolerSummaryLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/ColumnModule/column_compartment_temperature.feature')


@pytest.fixture
def heater_cooler_workflow_setup_page(page_builder):
    page = page_builder(HeaterCoolerWorkflowSetupScreen)
    return page


@pytest.fixture
def heater_cooler_workflow_summary_page(page_builder):
    page = page_builder(HeaterCoolerWorkflowSummaryScreen)
    return page


@when("User taps column compartment temperature test panel")
def navigate_column_temperature_test(dashboard_screen_page: DashBoardScreen, health_screen_page: HealthHomeScreen):
    dashboard_screen_page.validate_idle_state()
    health_screen_page.tap(HealthScreenLocators.HEATER_COOLER_WORKFLOW_START)


@given('User navigates to column section within health troubleshoot area')
def navigate_troubleshoot_column_manager(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)
    health_screen_page.tap(HealthScreenLocators.COLUMN_MANAGER_ICON)


@then("User validates the welcome context in the welcome screen")
def validate_welcome_screen_text(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    heater_cooler_workflow_setup_page.validate_welcome_screen()
    actual_paragraph_text = heater_cooler_workflow_setup_page.get_welcome_paragraph_text()
    expected_paragraph_text = HeaterCoolerConstants.expected_welcome_paragraph_text
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"
    heater_cooler_workflow_setup_page.tap_next_button()


@then("User validates the Next button is disabled")
def validate_next_button_disabled(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    assert heater_cooler_workflow_setup_page.validate_next_button_inactive()
    assert not heater_cooler_workflow_setup_page.is_checkbox_checked(
        HeaterCoolerPreconditionLocators.CONFIRMATION_CHECK)


@when('User checks the confirmation check box')
def tap_confirmation_checkbox(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    heater_cooler_workflow_setup_page.wait_for_element_enable(HeaterCoolerPreconditionLocators.CONFIRMATION_CHECK,heater_cooler_workflow_setup_page.wait_time)
    heater_cooler_details = heater_cooler_workflow_setup_page.get_summary_details()
    heater_cooler_workflow_setup_page.set_heater_cooler_details(heater_cooler_details)
    heater_cooler_workflow_setup_page.tap(HeaterCoolerPreconditionLocators.CONFIRMATION_CHECK)


@when('User validates the preconditions')
def validate_preconditions(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    validate_welcome_screen_text(heater_cooler_workflow_setup_page)
    heater_cooler_workflow_setup_page.validate_precondition_screen()
    tap_confirmation_checkbox(heater_cooler_workflow_setup_page)
    heater_cooler_workflow_setup_page.tap_next_button()


@when('User taps Start')
def tap_start_test(context, heater_cooler_workflow_summary_page: HeaterCoolerWorkflowSummaryScreen):
    heater_cooler_workflow_summary_page.validate_summary_screen()
    heater_cooler_workflow_summary_page.wait_till_condition_met(HeaterCoolerSummaryLocators.COLUMN_DOOR_STATE,
                                                                HeaterCoolerConstants.ClosedDoorStatus,
                                                                HeaterCoolerConstants.FailureMessage,
                                                                HeaterCoolerConstants.TimeToLoadDoorState)
    context["date_time"] = current_date()
    context["category"] = ColumnCompartmentTemperatureLogConstants.Category
    heater_cooler_workflow_summary_page.tap(HeaterCoolerWorkflowLocators.START_BUTTON)


@when('User validates the summary screen information')
def validate_summary_screen_details(heater_cooler_workflow_summary_page: HeaterCoolerWorkflowSummaryScreen,
                                    heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    heater_cooler_workflow_summary_page.validate_summary_screen()
    heater_cooler_workflow_summary_page.wait_time_to_load_value(HeaterCoolerSummaryLocators.COLUMN_DOOR_INFO_LABEL)
    current_summary_details = heater_cooler_workflow_summary_page.get_current_summary_details()
    expected_summary_details = heater_cooler_workflow_setup_page.get_selected_summary_details()
    assert current_summary_details == expected_summary_details, f"current_summary_details=>{current_summary_details},expected_summary_details=>{expected_summary_details} "


@then('User validates the results screen information with ambient temperature, target temperature and measured temperature')
def validate_results_screen_details(heater_cooler_workflow_summary_page: HeaterCoolerWorkflowSummaryScreen):
    heater_cooler_workflow_summary_page.validate_results_screen()
    heater_cooler_workflow_summary_page.tap(HeaterCoolerResultsLocators.RESULTS_TABLE_TOGGLE)
    heater_cooler_workflow_summary_page.validate_results_values()


@when(cfparse('User aborts the column compartment temperature workflow after {wait_time: d} seconds'))
def stop_workflow(wait_time, context, heater_cooler_workflow_summary_page):
    heater_cooler_workflow_summary_page.wait_till_condition_met(HeaterCoolerSummaryLocators.COLUMN_DOOR_STATE,
                                                                HeaterCoolerConstants.ClosedDoorStatus,
                                                                HeaterCoolerConstants.FailureMessage,
                                                                HeaterCoolerConstants.TimeToLoadDoorState)
    heater_cooler_workflow_summary_page.tap(HeaterCoolerWorkflowLocators.START_BUTTON)
    context["date_time"] = current_date()
    context["category"] = ColumnCompartmentTemperatureLogConstants.AbortCategory
    time.sleep(wait_time)  ## not condition involved, physically wait for 3 sec before aborting the workflow
    heater_cooler_workflow_summary_page.validate_status_screen()
    heater_cooler_workflow_summary_page.tap_stop_button()


@then('User validates the status stopped for the column compartment temperature workflow')
def validate_stop_workflow(heater_cooler_workflow_summary_page):
    heater_cooler_workflow_summary_page.validate_abort_status_screen()


@then("User validates the preconditions")
def validate_column_temperature_preconditions(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    heater_cooler_workflow_setup_page.validate_precondition_screen()


@then("User confirms the Next button is enabled")
def validate_next_button_enabled(heater_cooler_workflow_setup_page: HeaterCoolerWorkflowSetupScreen):
    assert heater_cooler_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)
    heater_cooler_workflow_setup_page.tap_next_button()


@then('User validates the column compartment temperature test process')
def validate_sample_temperature_test_process(heater_cooler_workflow_summary_page: HeaterCoolerWorkflowSummaryScreen):
    heater_cooler_workflow_summary_page.wait_for_column_test_end()


@then(cfparse('User validates the test passes if the measured change is greater than {measured_change_temp: d} degree Celsius'))
def validate_results_screen_measured_change(measured_change_temp, heater_cooler_workflow_summary_page: HeaterCoolerWorkflowSummaryScreen,
                                            dashboard_screen_page: DashBoardScreen):
    heater_cooler_workflow_summary_page.validate_measured_change(measured_change_temp)
    heater_cooler_workflow_summary_page.tap(BasePageLocators.DONE_BUTTON)
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_diagnose()
    dashboard_screen_page.validate_idle_state()


@then('User verifies the column compartment temperature test log is generated')
def validate_sample_temperature_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    current_date_value = context["date_time"]
    category_value = context["category"]
    actual_log_date = log_entry[LogTableHeaders.date_and_time]
    time_diff = is_within_tolerance(current_date_value, actual_log_date, HeaterCoolerConstants.ToleranceTime)
    actual_log_category = log_entry[LogTableHeaders.category]
    actual_log_source = log_entry[LogTableHeaders.source]
    assert time_diff, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {current_date_value}. Actual date: {actual_log_date}')

    assert actual_log_category == category_value, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {category_value}. Actual category: {actual_log_category}')

    assert actual_log_source == ColumnCompartmentTemperatureLogConstants.Source, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {ColumnCompartmentTemperatureLogConstants.Source}. Actual source: {actual_log_source}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    time_diff = is_within_tolerance(current_date_value, date_text, HeaterCoolerConstants.ToleranceTime)
    assert time_diff, f"The Date and time is not as expected. Expected Date: {current_date_value}. Actual date: {date_text}"
    assert category_text == category_value, (f"The Category  is not as expected. Expected Category: "
                                             f"{category_value}. Actual Category: {category_text}")
    assert source_text == ColumnCompartmentTemperatureLogConstants.Source, (f"The Source is not as expected. Expected Source: "
                                                                            f"{ColumnCompartmentTemperatureLogConstants.Source}. Actual Source: {source_text}")

