import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.logs import LogsScreenConstants, LogTableHeaders
from web_framework.kiosk.common.Constants.UI.system_leak_test_constant import SystemLeakTestConstant
from web_framework.kiosk.pages.Health.PumpModule.pump_module_home_screen import PumpModuleHomeScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_results_screen import SystemLeakTestResultsScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_setup_screen import SystemLeakTestSetupScreen
from web_framework.kiosk.pages.Health.SystemLeakTest.system_leak_test_summary_screen import SystemLeakTestSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import (SystemLeakTestLocators,
                                                                                 SystemLeakTestWorkflowSetupLocators,
                                                                                 SystemLeakTestWorkflowResultsLocators,
                                                                                 SystemLeakTestWorkFlowSummaryLocators)
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen


if __name__ == Path(__file__).stem:
    scenarios('../../features/HealthScreen/system_leak_test_workflow.feature')
logger = Logger("dynamic_test_leak_test_work_flow ")


@pytest.fixture
def dynamic_leak_test_results_screen(page_builder):
    page = page_builder(SystemLeakTestResultsScreen)
    return page


@pytest.fixture
def pump_module_home_screen(page_builder):
    page = page_builder(PumpModuleHomeScreen)
    return page


@given('User navigates the troubleshoot tab')
def tap_trouble_shoot_tab(health_screen_page: HealthHomeScreen):
    health_screen_page.tap_trouble_shoot_panel()


@when('User navigates to the welcome screen in leak test workflow')
def navigate_to_welcome_screen(pump_module_home_screen: PumpModuleHomeScreen):
    pump_module_home_screen.validate_idle_state()
    pump_module_home_screen.tap(SystemLeakTestLocators.DYNAMIC_LEAK_TEST_PANEL)


@when(cfparse('User selects "{solvent_line}", "{acc_pressure}", primary_pressure will be automatically set 2000 psi less than acc pressure, '
              '"{end_point}", "{prime_option}"'))
def set_option_for_custom_settings(solvent_line, acc_pressure, end_point, prime_option,
                                   leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    selected_summary_details = leak_test_setup_screen_page.get_leak_test_selected_summary_details(solvent_line,
                                                                                                  acc_pressure,
                                                                                                  end_point,
                                                                                                  prime_option)
    leak_test_setup_screen_page.set_selected_summary_details(selected_summary_details)
    selected_target_pressure_difference = selected_summary_details.accumulator_target_pressure - selected_summary_details.primary_target_pressure
    assert selected_target_pressure_difference == SystemLeakTestConstant.Target_pressure_difference, \
        f"Primary target pressure expected to be 2000 psi less than accumulator target pressure:[{selected_summary_details.accumulator_target_pressure}]" \
        f" but primary target pressure was [{selected_summary_details.primary_target_pressure}]"


@when(cfparse('The user enters the "{enter_pressure}"'))
def enter_flow_rate(enter_pressure, leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    leak_test_setup_screen_page.enter_value_for_specific_module(
        SystemLeakTestWorkflowSetupLocators.ACCUMULATOR_TARGET_FIELD,
        enter_pressure)


@when(cfparse('User aborts the leak test workflow after "{stop_time:d}" seconds'))
def abort_workflow(stop_time, dynamic_leak_test_summary_screen_page: SystemLeakTestSummaryScreen):
    dynamic_leak_test_summary_screen_page.validate_simple_text_wait_condition \
        (SystemLeakTestWorkflowResultsLocators.RESULTS_HEADER, SystemLeakTestConstant.StatusValidateText, SystemLeakTestConstant.SystemLeakTestTime)
    time.sleep(stop_time)
    dynamic_leak_test_summary_screen_page.tap_stop_button()


@when('User navigates to the next screen')
def navigate_to_setup_screen(leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    leak_test_setup_screen_page.tap_next_button()


@then('User validates the better results text in the welcome screen')
def validate_better_results_text(leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    actual_results_text = leak_test_setup_screen_page.get_better_results_text()
    expected_results_text = SystemLeakTestConstant.expected_better_results_text
    assert actual_results_text == expected_results_text, f"Results text was not as expected. Expected: [{expected_results_text}] " \
                                                         f"Actual: [{actual_results_text}]"


@then('User validates the welcome context in the welcome screen')
def validate_welcome_screen_text(leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    actual_paragraph_text = leak_test_setup_screen_page.get_welcome_paragraph_text()
    expected_paragraph_text = SystemLeakTestConstant.expected_welcome_paragraph_text
    assert actual_paragraph_text == expected_paragraph_text, f"Paragraph text was not as expected. Expected: [{expected_paragraph_text}] " \
                                                             f"Actual: [{actual_paragraph_text}]"


@then(cfparse(
    'User validates the result screen for "{acc_pressure}" and "{primary_pressure}": Leak rate (nL/min), Maximum pressure (psi),'
    ' Final Stroke (%), Compression attempts'))
def validate_dynamic_leak_test_results(dynamic_leak_test_results_screen: SystemLeakTestResultsScreen):
    # for standard test it take 10 minutes to get the results
    dynamic_leak_test_results_screen.validate_simple_text_wait_condition(
        SystemLeakTestWorkflowResultsLocators.RESULTS_HEADER,
        SystemLeakTestConstant.ResultValidateText, SystemLeakTestConstant.SystemLeakTestTime)
    dynamic_leak_test_results_screen.validate_arrow_status()
    dynamic_leak_test_results_screen.tap(SystemLeakTestWorkflowResultsLocators.EXTEND_ICON)
    dynamic_leak_test_results_screen.wait_time_to_load_value(SystemLeakTestWorkflowResultsLocators.PRIMARY_RESULT_STATE)
    current_primary_results = dynamic_leak_test_results_screen.get_current_primary_results()
    current_accumulator_results = dynamic_leak_test_results_screen.get_current_accumulator_results()

    if current_primary_results.result_state == SystemLeakTestConstant.LeakTestPassedState:

        assert current_primary_results.leak_rate <= SystemLeakTestConstant.PrimaryLeakRate, f"Primary leak rate expected to be less than or equal to  " \
                                                                                            f"[{SystemLeakTestConstant.PrimaryLeakRate}] " \
                                                                                            f"Actual: [{current_primary_results.leak_rate}]"
        assert current_primary_results.final_stroke <= SystemLeakTestConstant.PrimaryFinalStroke, \
            f"Primary final stroke expected to be less than or equal to [{SystemLeakTestConstant.PrimaryFinalStroke}] " \
            f"Actual: [{current_primary_results.final_stroke}]"
    else:
        assert current_primary_results.result_state == SystemLeakTestConstant.LeakTestFailedState, \
            f"Primary leak rate was not as expected. Expected: [{SystemLeakTestConstant.LeakTestFailedState}] Actual: [{current_primary_results.result_state}]"

    if current_accumulator_results.result_state == SystemLeakTestConstant.LeakTestPassedState:
        assert current_accumulator_results.leak_rate <= SystemLeakTestConstant.AccumulatorLeakRate, \
            f"Accumulator leak rate expected to be less than or equal to [{SystemLeakTestConstant.AccumulatorLeakRate}] " \
            f"Actual: [{current_accumulator_results.leak_rate}]"
        assert current_accumulator_results.final_stroke <= SystemLeakTestConstant.AccumulatorFinalStroke, \
            f"Accumulator final stroke was expected to be less than or equal to [{SystemLeakTestConstant.AccumulatorFinalStroke}] " \
            f"Actual: [{current_accumulator_results.final_stroke}]"
    else:
        assert current_accumulator_results.result_state == SystemLeakTestConstant.LeakTestFailedState, \
            f"The accumulator result state to be [{SystemLeakTestConstant.LeakTestFailedState}] Actual: [{current_accumulator_results.result_state}]"
    dynamic_leak_test_results_screen.tap_done_button()


@then('User validates the summary details for the leak test')
def validate_custom_settings(context, dynamic_leak_test_summary_screen_page: SystemLeakTestSummaryScreen,
                             leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    dynamic_leak_test_summary_screen_page.validate_summary_screen()
    current_summary_details = dynamic_leak_test_summary_screen_page.get_current_summary_details()
    expected_summary_details = leak_test_setup_screen_page.get_selected_summary_details()
    current_accumulator_target_pressure = current_summary_details.accumulator_target_pressure
    current_primary_target_pressure = current_summary_details.primary_target_pressure
    current_target_pressure_difference = current_accumulator_target_pressure - current_primary_target_pressure
    assert current_summary_details.Solvent == expected_summary_details.Solvent, f"Current summary solvent is not as expected. " \
                                                                                f"Expected: [{expected_summary_details.Solvent}]" \
                                                                                f" Actual: [{current_summary_details.Solvent}]"
    assert current_accumulator_target_pressure == expected_summary_details.accumulator_target_pressure, \
        f"Current accumulator target pressure was not as expected. Expected: [{expected_summary_details.accumulator_target_pressure}] " \
        f"Actual: [{current_accumulator_target_pressure}]"
    assert current_summary_details.end_point.title() == expected_summary_details.end_point.title(), \
        f"Current end point was not as expected. Expected: [{expected_summary_details.end_point.title()}] Actual: [{current_summary_details.end_point.title()}]"
    assert current_target_pressure_difference == SystemLeakTestConstant.Target_pressure_difference, \
        f"Primary target pressure was not as expected" \
        f"Expected: [{current_accumulator_target_pressure}] Actual: [{current_primary_target_pressure}]"
    assert current_primary_target_pressure == expected_summary_details.primary_target_pressure, \
        f"Current primary target pressure was not as expected. Expected: [{expected_summary_details.primary_target_pressure}] " \
        f"Actual: [{current_primary_target_pressure}]"
    assert current_summary_details.prime_option.title() == expected_summary_details.prime_option.title(), \
        f"Current prime option was not as expected. Expected: [{expected_summary_details.prime_option.title()}] " \
        f"Actual: [{current_summary_details.prime_option.title()}]"

    context['current_date_time'] = current_date()
    dynamic_leak_test_summary_screen_page.tap(SystemLeakTestWorkFlowSummaryLocators.START_BUTTON)


@then('the log entry is created with correct time, date, category and action details')
def validate_log_entry_data(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    time_diff = is_within_tolerance(context['current_date_time'], log_entry[LogTableHeaders.date_and_time], SystemLeakTestConstant.MaximumToleranceInMinutes)

    assert LogsScreenConstants.WorkFlowCategory in log_entry[LogTableHeaders.category], \
        f"The Category  is not as expected. Expected category: [{LogsScreenConstants.WorkFlowCategory}] " \
        f"Actual category: [{log_entry[LogTableHeaders.category]}]"
    assert LogsScreenConstants.SystemLeakTestSource in log_entry[LogTableHeaders.source], \
        f"The Source  is not as expected. Expected source: [{LogsScreenConstants.SystemLeakTestSource}] Actual Source: [{log_entry[LogTableHeaders.source]}]"
    assert time_diff, \
        f"The Date and time  is not as expected. Expected Date: [{context['current_date_time']}] Actual date: [{log_entry[LogTableHeaders.date_and_time]}]"

    system_logs_screen.tap_row_element(LogsScreenConstants.SystemLeakTestSource)
    system_logs_screen.validate_system_logs_screen()
    category_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    date_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    time_diff = is_within_tolerance(context['current_date_time'], date_text, SystemLeakTestConstant.MaximumToleranceInMinutes)

    assert time_diff, \
        f"The Date and time  is not as expected. Expected Date: [{context['current_date_time']}] Actual date: [{log_entry[LogTableHeaders.date_and_time]}]"
    assert LogsScreenConstants.WorkFlowCategory in category_text, \
        f"The Category  is not as expected. Expected category: [{LogsScreenConstants.WorkFlowCategory}] Actual category: [{category_text}]"
    assert source_text == LogsScreenConstants.SystemLeakTestSource, \
        f"The Source  is not as expected. Expected source: [{LogsScreenConstants.SystemLeakTestSource}] Actual Source: [{source_text}]"


@then('User validates the status screen for the leak test')
def validate_status_screen(dynamic_leak_test_summary_screen_page: SystemLeakTestSummaryScreen):
    dynamic_leak_test_summary_screen_page.validate_abort_status_screen()


@then(cfparse('Validate the pressure edit field shows "{error_state:bool}"', CONVERTERS))
def validate_error_state(error_state: bool, leak_test_setup_screen_page: SystemLeakTestSetupScreen):
    leak_test_setup_screen_page.validate_pressure_setup_screen()
    edit_field_error_state = leak_test_setup_screen_page.is_edit_field_in_error_state(
        SystemLeakTestWorkflowSetupLocators.EDIT_FIELD_STATE)
    assert edit_field_error_state == error_state, f"The edit field state is not as expected. Expected: [{error_state}] Actual: [{edit_field_error_state}]"
