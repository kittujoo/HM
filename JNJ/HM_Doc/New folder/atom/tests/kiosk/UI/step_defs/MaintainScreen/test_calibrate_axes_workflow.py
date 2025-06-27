import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.calibrate_axes_constants import CalibrateAxesConstants
from web_framework.kiosk.common.Constants.UI.logs import LogTableHeaders, CalibrateAxesLogConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Maintain.calibrate_axes_locators import CalibrateAxesWorkflowLocators
from web_framework.kiosk.pages.Locators.Maintain.maintain_screen_locators import MaintainScreenPageLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Maintain.calibrate_axes_summary_screen import CalibrateAxesWorkflowSummaryScreen
from web_framework.kiosk.pages.Maintain.calibrate_axes_workflow_screen import CalibrateAxesWorkflowSetupScreen
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/MaintainScreen/calibrate_axes_workflow.feature')
logger = Logger("test_calibrate_axes_workflow")


@pytest.fixture
def calibrate_axes_summary_screen_page(page_builder):
    page = page_builder(CalibrateAxesWorkflowSummaryScreen)
    return page


@pytest.fixture
def calibrate_axes_setup_screen_page(page_builder) -> CalibrateAxesWorkflowSetupScreen:
    page = page_builder(CalibrateAxesWorkflowSetupScreen)
    return page


@when('User taps the calibrate axes start')
def begin_calibrate_axes_workflow(maintain_screen_page: MaintainScreen):
    maintain_screen_page.validate_maintain_screen()
    maintain_screen_page.validate_idle_state()
    maintain_screen_page.tap(MaintainScreenPageLocators.CALIBRATE_PANEL)


@when('User taps the Z-Axis path')
def tap_z_axis(context, calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    context['axis'] = CalibrateAxesConstants.ZAxis
    calibrate_axes_setup_screen_page.validate_functions_banner()
    calibrate_axes_setup_screen_page.tap(CalibrateAxesWorkflowLocators.ZAXIS_PATH)


@when('User taps the Zp-Axis path')
def tap_zp_axis(context, calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    context['axis'] = CalibrateAxesConstants.ZpAxis
    calibrate_axes_setup_screen_page.validate_functions_banner()
    calibrate_axes_setup_screen_page.tap(CalibrateAxesWorkflowLocators.ZPAXIS_PATH)


@when('User taps the Hard-Stop path')
def tap_hard_stop_axis(context, calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    context['axis'] = CalibrateAxesConstants.HardStopAxis
    calibrate_axes_setup_screen_page.validate_functions_banner()
    calibrate_axes_setup_screen_page.tap(CalibrateAxesWorkflowLocators.HARD_STOP_PATH)


@when('User Taps Next')
def tap_next_button(calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    calibrate_axes_setup_screen_page.tap_next_button()


@when('User taps next to the summary screen')
def navigate_summary_screen(calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    while not calibrate_axes_setup_screen_page.is_displayed(CalibrateAxesWorkflowLocators.SUMMARY_PAGE_BANNER):
        calibrate_axes_setup_screen_page.tap_next_button()


@when('User taps the confirmation check')
def tap_confirmation_checkbox(calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    calibrate_axes_setup_screen_page.wait_time_to_load_value(CalibrateAxesWorkflowLocators.COMPARTMENT_DOOR_INFO_LABEL)
    calibrate_axes_setup_screen_page.tap(CalibrateAxesWorkflowLocators.CONFIRMATION_CHECK)


@when('User taps start')
def tap_start_test(context, calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen,
                   calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen):
    calibrate_axes_summary_screen_page.validate_summary_screen()
    calibrate_axes_setup_screen_page.tap(CalibrateAxesWorkflowLocators.START_BUTTON)
    context["date_time"] = current_date()


@when('User validates the test was completed')
@then('User validates the test was completed')
def validate_calibrate_cycle(calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen):
    calibrate_axes_summary_screen_page.validate_element_wait_condition(CalibrateAxesWorkflowLocators.STATUS_PAGE_BANNER,
                                                                       CalibrateAxesWorkflowLocators.RESULTS_PAGE_BANNER,
                                                                       CalibrateAxesConstants.DefaultAxesPathTestTime)
    calibrate_axes_summary_screen_page.validate_results_screen()


@then('User validates the welcome screen')
def validate_welcome_screen_text(context, calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen):
    axis = context['axis']
    if axis == CalibrateAxesConstants.ZAxis:
        calibrate_axes_summary_screen_page.validate_z_axis_welcome_text()
    elif axis == CalibrateAxesConstants.ZpAxis:
        calibrate_axes_summary_screen_page.validate_zp_axis_welcome_text()
    else:
        calibrate_axes_summary_screen_page.validate_hard_stop_axis_welcome_text()


@then('User validates the Cautions screen')
def validate_axes_cautions_screen(calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    calibrate_axes_setup_screen_page.validate_cautions_banner()


@then('Start becomes enable')
def activate_start_button(calibrate_axes_setup_screen_page: CalibrateAxesWorkflowSetupScreen):
    assert calibrate_axes_setup_screen_page.is_button_active(BasePageLocators.START_BUTTON)


@then('User validates the Z-Axis results screen details')
def validate_z_axis_results_screen_details(context,
                                           calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen,
                                           dashboard_screen_page: DashBoardScreen):
    context['log_source_constants'] = CalibrateAxesLogConstants.ZSource
    calibrate_axes_summary_screen_page.validate_results_screen()
    calibrate_axes_summary_screen_page.tap(CalibrateAxesWorkflowLocators.COLLAPSIBLE_TABLE_TOGGLE)
    calibrate_axes_summary_screen_page.validate_axis_results()
    calibrate_axes_summary_screen_page.tap_done_button()
    dashboard_screen_page.validate_idle_state()


@then('User validates the Zp-Axis results screen details')
def validate_zp_axis_results_screen_details(context,
                                            calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen,
                                            dashboard_screen_page: DashBoardScreen):
    context['log_source_constants'] = CalibrateAxesLogConstants.ZpSource
    calibrate_axes_summary_screen_page.validate_results_screen()
    calibrate_axes_summary_screen_page.tap(CalibrateAxesWorkflowLocators.COLLAPSIBLE_TABLE_TOGGLE)
    calibrate_axes_summary_screen_page.validate_axis_results()
    calibrate_axes_summary_screen_page.tap_done_button()
    dashboard_screen_page.validate_idle_state()


@then('User validates the Hard-Stop results screen details')
def validate_hard_stop_axis_results_screen_details(
        calibrate_axes_summary_screen_page: CalibrateAxesWorkflowSummaryScreen):
    calibrate_axes_summary_screen_page.validate_results_screen()
    calibrate_axes_summary_screen_page.tap(CalibrateAxesWorkflowLocators.COLLAPSIBLE_TABLE_TOGGLE)
    calibrate_axes_summary_screen_page.validate_axis_results()


@then('User verifies the Calibrate Z-Axis log is generated')
@then('User verifies the Calibrate Zp-Axis log is generated')
def validate_axis_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    current_date_value = context["date_time"]
    source_value = context['log_source_constants']
    actual_date_time = log_entry[LogTableHeaders.date_and_time]
    time_diff = is_within_tolerance(current_date_value, actual_date_time, CalibrateAxesConstants.MaximumToleranceInMinutes)
    assert time_diff, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {current_date_value}. Actual date: {actual_date_time}')
    actual_category = log_entry[LogTableHeaders.category]
    assert actual_category == CalibrateAxesLogConstants.Category, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {CalibrateAxesLogConstants.Category}. Actual category: {actual_category}')
    actual_source = log_entry[LogTableHeaders.source]
    assert actual_source == source_value, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {source_value}. Actual date: {actual_source}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    time_diff = is_within_tolerance(current_date_value, date_text, CalibrateAxesConstants.MaximumToleranceInMinutes)
    assert time_diff, f"The Date and time is not as expected. Expected Date: {current_date_value}. Actual date: {date_text}"
    assert category_text == CalibrateAxesLogConstants.Category, (
        f"The Category  is not as expected. Expected Category: "
        f"{CalibrateAxesLogConstants.Category}. Actual Category: {category_text}")
    assert source_text == source_value, (f"The Source is not as expected. Expected Source: {source_value}. "
                                         f"Actual Source: {source_text}")
