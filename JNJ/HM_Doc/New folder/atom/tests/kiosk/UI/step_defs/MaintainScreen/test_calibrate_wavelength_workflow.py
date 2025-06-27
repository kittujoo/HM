import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.calibrate_wavelength_constant import CalibrateWavelengthConstant
from web_framework.kiosk.common.Constants.UI.logs import CalibrateWavelengthLogConstants, LogTableHeaders, VerifyCalibrateWavelengthLogConstants
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.calibrate_wavelength_locators import CalibrateWavelengthWorkflowLocators, \
    CalibrateWavelengthSummaryLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Maintain.Models.calibrate_wavelength_summary import CalibrateWavelengthSummaryDetails
from web_framework.kiosk.pages.Maintain.calibrate_wavelength_summary_screen import CalibrateWavelengthSummaryScreen
from web_framework.kiosk.pages.Maintain.calibrate_wavelength_workflow_screen import CalibrateWavelengthWorkflowScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/MaintainScreen/calibrate_wavelength_workflow.feature',
              '../../features/MaintainScreen/verify_calibration_workflow.feature')
logger = Logger("test_calibrate_wavelength_workflow")


@pytest.fixture
def calibrate_wavelength_workflow_page(page_builder):
    page = page_builder(CalibrateWavelengthWorkflowScreen)
    return page


@pytest.fixture
def calibrate_wavelength_summary_page(page_builder):
    page = page_builder(CalibrateWavelengthSummaryScreen)
    return page


@given(cfparse('User set the lamp detector "{lamp_state}"'))
def set_lamp_state(lamp_state, command_screen_page: CommandsScreen):
    command_screen_page.validate_command_screen()
    command_screen_page.turn_off_lamp() if lamp_state == "Off" else command_screen_page.turn_on_lamp()


@given("User navigates to Commands area")
def navigate_to_commands(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_commands()


@when('User taps Calibrate Detector option')
def begin_calibrate_workflow(maintain_screen_page: MaintainScreen):
    maintain_screen_page.validate_idle_state()
    maintain_screen_page.tap_calibrate_wavelength_tab()


@when('User taps the next button')
def navigate_to_next_screen(calibrate_wavelength_workflow_page):
    calibrate_wavelength_workflow_page.tap_next_button()


@when('User selects the Calibrate Wavelengths option')
def select_calibrate_option(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.validate_function_screen()
    calibrate_wavelength_workflow_page.tap(CalibrateWavelengthWorkflowLocators.CALIBRATE_WAVELENGTH_OPTION)


@when('User starts the calibration for the wavelength')
def start_calibration(context, calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    context["category"] = CalibrateWavelengthLogConstants.Category
    calibrate_wavelength_workflow_page.tap(BasePageLocators.START_BUTTON)
    calibrate_wavelength_workflow_page.wait_for_test_end()
    context["date_time"] = current_date()


@when('User selects the verify calibration function')
def select_calibrate_option(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.validate_function_screen()
    calibrate_wavelength_workflow_page.tap(CalibrateWavelengthWorkflowLocators.VERIFY_WAVELENGTH_OPTION)


@when(cfparse('User sets the flowrate as "{flow_rate}"'))
def set_flow_rate(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen, flow_rate):
    calibrate_wavelength_workflow_page.validate_flow_control_screen()
    calibrate_wavelength_workflow_page.set_flow(flow_rate)


@when('User starts the verify calibration')
def start_calibration(context, calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    context["category"] = VerifyCalibrateWavelengthLogConstants.Category
    calibrate_wavelength_workflow_page.tap(BasePageLocators.START_BUTTON)
    calibrate_wavelength_workflow_page.wait_for_test_end()
    context["date_time"] = current_date()


@when(cfparse('User validates the summary screen details for "{is_flush_on}" and "{is_pre_flush_on}" for "{flow_rate}"'))
def validate_summary_screen_details(calibrate_wavelength_summary_page: CalibrateWavelengthSummaryScreen, is_flush_on: str, is_pre_flush_on: str,
                                    flow_rate: str):
    calibrate_wavelength_summary_page.validate_summary_screen()
    calibrate_wavelength_summary_page.wait_time_to_load_value(CalibrateWavelengthSummaryLocators.FLOW_CELL_INFO_LABEL, "")
    is_flush_on = TypeConverter.to_bool(is_flush_on)
    is_pre_flush_on = TypeConverter.to_bool(is_pre_flush_on)
    current_summary_details = calibrate_wavelength_summary_page.get_current_summary_screen_details(is_flush_on)
    logger.info(f"current_summary_details ==={current_summary_details}")

    if is_flush_on and is_pre_flush_on:
        logger.info(f"Both the toggle button is turned on")
        expected_summary_details = CalibrateWavelengthSummaryDetails(CalibrateWavelengthConstant.PreFlushSelectedMessage,
                                                                     CalibrateWavelengthConstant.FlushSelectedMessage,
                                                                     CalibrateWavelengthConstant.flow_cell_state,
                                                                     CalibrateWavelengthConstant.lamp_state)
        logger.info(f"expected_summary_details ==={expected_summary_details}")
        assert current_summary_details == expected_summary_details, f"The summary screen details do not match. Current: {current_summary_details} | Expected: {expected_summary_details} "

        current_flow_rate_info = calibrate_wavelength_summary_page.get_flowrate()
        current_flow_rate_info = TypeConverter.to_float(current_flow_rate_info)
        expected_flow_rate_info = TypeConverter.to_float(flow_rate)

        assert current_flow_rate_info == expected_flow_rate_info, f"The summary screen details " \
                                                                  f"do not match. Current: {current_flow_rate_info} |" \
                                                                  f" Expected: {expected_flow_rate_info}"

    elif not is_flush_on and not is_pre_flush_on:
        logger.info(f"Both the toggle but is turned off")
        expected_summary_details = CalibrateWavelengthSummaryDetails(CalibrateWavelengthConstant.PreFlushNotSelectedMessage, None,
                                                                     CalibrateWavelengthConstant.flow_cell_state,
                                                                     CalibrateWavelengthConstant.lamp_state)
        assert current_summary_details == expected_summary_details, f"The summary screen details " \
                                                                    f"do not match. Current: {current_summary_details} |" \
                                                                    f" Expected: {expected_summary_details}"


@when('User taps the start button')
def start_calibration(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.tap(BasePageLocators.START_BUTTON)


@when('User taps retry')
def tap_retry(context, calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.tap_retry_button()
    calibrate_wavelength_workflow_page.validate_element_wait_condition(
        CalibrateWavelengthWorkflowLocators.PROGRESS_PAGE_BANNER,
        CalibrateWavelengthWorkflowLocators.RESULTS_PAGE_BANNER, CalibrateWavelengthConstant.MaxiTimeToCalibrate)
    context["date_time"] = current_date()


@when(cfparse('User turns the flush column "{is_flush_on}" and pre flush column "{is_pre_flush_on}"'))
def set_flush_option(calibrate_wavelength_workflow_page, is_flush_on: str, is_pre_flush_on: str):
    calibrate_wavelength_workflow_page.validate_flush_control_screen()
    is_flush_on = TypeConverter.to_bool(is_flush_on)
    is_pre_flush_on = TypeConverter.to_bool(is_pre_flush_on)
    calibrate_wavelength_workflow_page.set_toggle_button(
        CalibrateWavelengthWorkflowLocators.FLUSH_TOGGLE_BUTTON,
        is_flush_on)

    if is_flush_on:
        calibrate_wavelength_workflow_page.tap_next_button()
        calibrate_wavelength_workflow_page.validate_preflush_screen()
        calibrate_wavelength_workflow_page.set_toggle_button(
            CalibrateWavelengthWorkflowLocators.PRE_FLUSH_TOGGLE,
            is_pre_flush_on)
    calibrate_wavelength_workflow_page.tap_next_button()


@when(cfparse('User stops the workflow at different "{stop_time:d}"'))
def terminate_workflow(context, calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen, stop_time):
    time.sleep(stop_time)
    context["category"] = CalibrateWavelengthLogConstants.AbortCategory
    context["date_time"] = current_date()
    calibrate_wavelength_workflow_page.validate_stop_button()
    calibrate_wavelength_workflow_page.tap_stop_button()


@then("User validates the status stopped for the verify calibration workflow")
def validate_workflow_termination(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.validate_flow_interrupted_screen()
    calibrate_wavelength_workflow_page.tap_close_button()
    calibrate_wavelength_workflow_page.set_idle_state()


@then(cfparse('Validate the flow edit field shows "{error_state}"'))
def validate_error_state(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen, error_state: str):
    edit_field_error_state = calibrate_wavelength_workflow_page.is_edit_field_in_error_state(
        CalibrateWavelengthWorkflowLocators.FLOW_EDIT_STATE)
    error_state = TypeConverter.to_bool(error_state)
    assert edit_field_error_state == error_state, f" actual edit field error state is ==>> {edit_field_error_state}"


@then('the log entry is created with correct time, date, category and action details')
def validate_verify_wavelength_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]
    category = context["category"]
    time_diff = is_within_tolerance(context["date_time"], log_entry[LogTableHeaders.date_and_time], 2)

    assert time_diff, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {context["date_time"]}. Actual date: {log_entry[LogTableHeaders.date_and_time]}')

    assert log_entry[LogTableHeaders.category] == category, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {category}. Actual date: {log_entry[LogTableHeaders.category]}')
    if log_entry[LogTableHeaders.source] == 'SystemTuvVerifyWavelengthCalibration':
        assert log_entry[LogTableHeaders.source] == VerifyCalibrateWavelengthLogConstants.Source, (
            f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {VerifyCalibrateWavelengthLogConstants.Source}. Actual date: {log_entry[LogTableHeaders.source]}')
    else:
        assert log_entry[LogTableHeaders.source] == CalibrateWavelengthLogConstants.Source, (
            f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {CalibrateWavelengthLogConstants.Source}. Actual date: {log_entry[LogTableHeaders.source]}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    time_diff = is_within_tolerance(context["date_time"], date_text, 2)

    assert time_diff, f'The Date and time is not as expected Expected Date: {context["date_time"]}. Actual date: {date_text}'
    assert category_text == category, f"The Category  is not as expected. Expected Category: {category}. Actual Category: {category_text}"
    if log_entry[LogTableHeaders.source] == 'SystemTuvVerifyWavelengthCalibration':
        assert source_text == VerifyCalibrateWavelengthLogConstants.Source, f"The Source is not as expected. Expected Source: {VerifyCalibrateWavelengthLogConstants.Source}. Actual Source: {source_text}"
    else:
        assert source_text == CalibrateWavelengthLogConstants.Source, f"The Source is not as expected. Expected Source: {CalibrateWavelengthLogConstants.Source}. Actual Source: {source_text}"


@then('User validates the welcome screen')
def validate_welcome_text(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    actual_paragraph_text = calibrate_wavelength_workflow_page.get_welcome_paragraph_text()

    expected_paragraph_text = CalibrateWavelengthConstant.expected_welcome_paragraph_text
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


@then('Validates the better results point in the welcome screen')
def validate_better_results_test(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    actual_better_results_text = calibrate_wavelength_workflow_page.get_better_results_text()

    expected_better_results_text = CalibrateWavelengthConstant.expected_better_results_text
    assert actual_better_results_text == expected_better_results_text, f"actual_paragraph_text ==>{actual_better_results_text}"


@then('Validates the recommendation text for the calibrate workflow')
def validate_recommendation_text(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    actual_recommendation_text = calibrate_wavelength_workflow_page.get_text(
        CalibrateWavelengthWorkflowLocators.RECOMMENDATION_TEXT)
    expected_recommendation_text = CalibrateWavelengthConstant.RecommendationText
    assert actual_recommendation_text == expected_recommendation_text, f"actual_paragraph_text ==>{actual_recommendation_text}"


@then('User validates the preconditions for the verify wavelength')
@then('User validates the preconditions for the verify calibration')
def validate_precondition(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.wait_time_to_load_value(CalibrateWavelengthWorkflowLocators.FLOW_CELL_TYPE, "")
    actual_precondition = calibrate_wavelength_workflow_page.get_precondition_state()

    expected_preconditon = CalibrateWavelengthConstant.expected_precondition
    assert actual_precondition == expected_preconditon, f"actual_paragraph_text ==>{actual_precondition}"
    calibrate_wavelength_workflow_page.tap_next_button()


@then('User validates the calibration passes')
def validate_wavelength_deviation(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.tap(CalibrateWavelengthWorkflowLocators.RESULTS_ARROW)
    calibrate_wavelength_workflow_page.validate_wavelength_table_data()
    calibrate_wavelength_workflow_page.check_for_deviation()


@then('User validates the calibration passes if all three deviations are less than 1nm')
def validate_wavelength_deviation(calibrate_wavelength_workflow_page: CalibrateWavelengthWorkflowScreen):
    calibrate_wavelength_workflow_page.tap(CalibrateWavelengthWorkflowLocators.RESULTS_ARROW)
    calibrate_wavelength_workflow_page.validate_wavelength_table_data()
    calibrate_wavelength_workflow_page.check_for_deviation()
    calibrate_wavelength_workflow_page.tap_done_button()
    calibrate_wavelength_workflow_page.set_idle_state()
