import time
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.date_utilities import current_date
from utilities.logger import Logger
from utilities.string_utility import remove_substring
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.logs import NeedleSealLogConstants, LogTableHeaders
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.needle_seal_readiness_constants import NeedleSealReadinessConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_results_screen import NeedleSealReadinessResultsScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_screen import NeedleSealReadinessSetupScreen
from web_framework.kiosk.pages.Health.SampleManager.needle_seal_readiness_workflow_summary_screen import NeedleSealReadinessSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Locators.Health.SampleManager.needle_seal_readiness_workflow_locators import (
    NeedleSealReadinessLocators, NeedleSealReadinessSummaryLocators, NeedleSealReadinessResultsLocators,
    NeedleSealReadinessWelcomeLocators, NeedleSealReadinessSetupLocators)
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.Health.instrument_diagnostic_locators import InstrumentDiagnosticLocators
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import SolventCompositionTabScreen
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/SampleManager/needle_seal_readiness_workflow.feature')
logger = Logger("test_needle_seal_readiness_workflow")


@given("User gets the system pressure from the dashboard")
def get_system_pressure(dashboard_screen_page: DashBoardScreen, health_screen_page: HealthHomeScreen):
    dashboard_screen_page.tap_home()
    current_system_pressure = dashboard_screen_page.get_system_pressure_with_units()
    logger.info(f"current_system_pressure======>>>>>{current_system_pressure}")
    dashboard_screen_page.set_current_system_pressure(current_system_pressure)
    dashboard_screen_page.tap_diagnose()
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)


@when("User navigates to sample manager section")
def navigate_troubleshoot_sample_manager(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.SAMPLE_MANAGER_ICON)


@when('User taps needle seal readiness test start panel')
def tap_needle_seal_readiness_panel(instrument_diagnostic_page: InstrumentDiagnosticScreen):
    instrument_diagnostic_page.validate_idle_state()
    instrument_diagnostic_page.tap(InstrumentDiagnosticLocators.NEEDLE_SEAL_READINESS_PANEL)


@when('User validates the welcome context in the welcome screen')
def validate_welcome_screen_text(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen):
    actual_paragraph_text = needle_seal_readiness_workflow_setup_page.get_welcome_paragraph_text()
    logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")
    first_para = needle_seal_readiness_workflow_setup_page.get_text(
        NeedleSealReadinessWelcomeLocators.WELCOME_PARAGRAPH_ONE)
    logger.info(f"first_para======>>>>>{first_para}")
    expected_paragraph_text = NeedleSealReadinessConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")

    actual_instruction_text = needle_seal_readiness_workflow_setup_page.get_instruction_text()
    expected_instruction_text = NeedleSealReadinessConstants.expected_instruction_text

    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"
    assert actual_instruction_text == expected_instruction_text, f"actual_instruction_text ==>" \
                                                                 f"{actual_instruction_text}"
    needle_seal_readiness_workflow_setup_page.tap_next_button()


@when(cfparse('User enters the "{flow_rate}"'))
def enter_flow_rate(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen, flow_rate):
    needle_seal_readiness_workflow_setup_page.validate_flow_settings_screen()

    flow_setup_context(needle_seal_readiness_workflow_setup_page)
    needle_seal_readiness_workflow_setup_page.enter_value(flow_rate)
    needle_seal_readiness_workflow_setup_page.validate_flow_default_value()
    needle_seal_readiness_workflow_setup_page.tap_next_button()


@when(cfparse('User enters the composition "{line_1}" "{line_2}" "{line_3}" "{line_4}"'))
def set_composition(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen,
                    flow_setting_screen_page: FlowSettingsScreen,
                    line_1, line_2, line_3, line_4):
    flow_setting_screen_page.validate_composition_settings_screen()
    composition_setup_context(needle_seal_readiness_workflow_setup_page)

    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    flow_setting_screen_page.enter_composition(solvent_composition)
    needle_seal_readiness_workflow_setup_page.validate_comp_default_value()
    flow_setting_screen_page.tap_next_button()


@then(cfparse('User validate the solvent edit field shows "{error_state}" for "{actual_composition}"'))
def add_solvent(flow_setting_screen_page: FlowSettingsScreen,
                needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen,
                actual_composition, error_state):
    flow_setting_screen_page.reset_composition()
    flow_setting_screen_page.tap(SolventCompositionTabScreen.SOLVENT_B_EDIT_FIELD)

    flow_setting_screen_page.set_composition(actual_composition,
                                             SolventCompositionTabScreen.SOLVENT_B_EDIT_FIELD)

    error_state = TypeConverter.to_bool(error_state)
    edit_field_error_state = needle_seal_readiness_workflow_setup_page.is_edit_field_in_error_state(
        NeedleSealReadinessSetupLocators.COMP_EDIT_FIELD_STATE)
    logger.info(f"edit_field_error_state======>>>>>{edit_field_error_state}")
    assert edit_field_error_state == error_state, "Edit field did not have error taste"
    assert needle_seal_readiness_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL) != edit_field_error_state


@then('the log entry is created with correct time, date, category and action details')
def validate_needle_seal_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    current_date_value = context["date_time"]

    assert log_entry[LogTableHeaders.date_and_time] == current_date_value, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {current_date_value}. Actual date: {log_entry[LogTableHeaders.date_and_time]}')

    assert log_entry[LogTableHeaders.category] == NeedleSealLogConstants.Category, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {NeedleSealLogConstants.Category}. Actual date: {log_entry[LogTableHeaders.category]}')

    assert log_entry[LogTableHeaders.source] == NeedleSealLogConstants.Source, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {NeedleSealLogConstants.Source}. Actual date: {log_entry[NeedleSealLogConstants.Source]}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)

    assert date_text == current_date_value, (f"The Date and time is not as expected. "
                                             f"Expected Date: {current_date_value}. "
                                             f"Actual date: {date_text}")
    assert category_text == NeedleSealLogConstants.Category, (f"The Category  is not as expected. Expected Category: {NeedleSealLogConstants.Category}. "
                                                              f"Actual Category: {category_text}")
    assert source_text == NeedleSealLogConstants.Source, (f"The Source is not as expected. Expected Source: {NeedleSealLogConstants.Source}. "
                                                          f"Actual Source: {source_text}")


@then(cfparse('User validates the summary screen details for "{flow_rate}" "{line_1}" "{line_2}" "{line_3}" "{line_4}"'))
def validate_summary_screen_details(needle_seal_readiness_workflow_summary_page: NeedleSealReadinessSummaryScreen,
                                    dashboard_screen_page: DashBoardScreen,
                                    flow_rate: float, line_1, line_2, line_3, line_4):
    needle_seal_readiness_workflow_summary_page.validate_summary_screen()
    validate_summary_context(needle_seal_readiness_workflow_summary_page)

    solvent_comp_info_list = needle_seal_readiness_workflow_summary_page.get_expected_solvent_composition(line_1,
                                                                                                          line_2,
                                                                                                          line_3,
                                                                                                          line_4)
    logger.info(f"solvent_comp_info======>>>>>{solvent_comp_info_list}")
    current_composition = needle_seal_readiness_workflow_summary_page.get_container_text(
        NeedleSealReadinessSummaryLocators.COMPOSITION_LABEL)
    logger.info(f"current_composition======>>>>>{current_composition}")

    for solvent in range(len(solvent_comp_info_list)):
        if current_composition.find(solvent_comp_info_list[solvent]) != -1:
            assert True
        else:
            assert False
    current_flow_rate_info = needle_seal_readiness_workflow_summary_page.get_container_text(
        NeedleSealReadinessSummaryLocators.FLOW_RATE_INFO_LABEL)
    logger.info(f"current_flow_rate======>>>>>{current_flow_rate_info}")
    current_flow = remove_substring(current_flow_rate_info, "mL/min")
    current_flow = current_flow.strip()
    logger.info(f"current_flow======>>>>>{current_flow}")
    assert current_flow == flow_rate

    actual_system_pressure = needle_seal_readiness_workflow_summary_page.get_container_text(
        NeedleSealReadinessSummaryLocators.SYSTEM_PRESSURE_INFO_LABEL)
    expected_system_pressure = dashboard_screen_page.get_current_system_pressure()
    logger.info(f"expected_system_pressure======>>>>>{expected_system_pressure}")
    logger.info(f"actual_system_pressure======>>>>>{actual_system_pressure}")


@then(cfparse('User validates the result screen for the needle readiness test for "{flow_rate}"'))
def validate_results_screen(needle_test_result_page: NeedleSealReadinessResultsScreen,
                            dashboard_screen_page: DashBoardScreen, flow_rate):
    needle_test_result_page.validate_status_screen()
    validate_status_context(needle_test_result_page)
    needle_test_result_page.validate_element_wait_condition(
        NeedleSealReadinessResultsLocators.STATUS_BANNER, NeedleSealReadinessSummaryLocators.RESULTS_BANNER,
        WaitTimeConstants.NeedleSealReadinessTest)
    result_shown_state = needle_test_result_page.is_result_shown(
        NeedleSealReadinessResultsLocators.RESULTS_SHOW_ICON_STATUS)
    if result_shown_state is False:
        needle_test_result_page.tap(NeedleSealReadinessResultsLocators.RESULTS_SHOW_ICON)
        logger.info("The results were shown after tapping the arrow button")

    needle_test_result_page.validate_results_table()
    current_pressure_difference = needle_test_result_page.get_text(
        NeedleSealReadinessResultsLocators.PRESSURE_DIFFERENCE_LABEL)
    logger.info(f"current_pressure_difference==>>{current_pressure_difference}")
    current_pressure_difference = float(current_pressure_difference)

    if current_pressure_difference < 0:
        result_state = needle_test_result_page.get_text(NeedleSealReadinessResultsLocators.TEST_RESULT)
        assert result_state == NeedleSealReadinessConstants.FailedResultState

    if current_pressure_difference >= 0:
        result_state = needle_test_result_page.get_text(NeedleSealReadinessResultsLocators.TEST_RESULT)
        assert result_state == NeedleSealReadinessConstants.PassedResultState

    current_flow_rate = needle_test_result_page.get_text(NeedleSealReadinessResultsLocators.FLOW_RATE_INFO)
    assert current_flow_rate == flow_rate, f" The flow_rate ===>>>{flow_rate}"
    validate_results_context(needle_test_result_page)
    needle_test_result_page.tap_done_button()
    dashboard_screen_page.tap_diagnose()


@then('User aborts the prime workflow')
def stop_workflow(needle_test_result_page: NeedleSealReadinessResultsScreen):
    time.sleep(3)  # not condition involved, physically wait for 3 sec before aborting the workflow
    needle_test_result_page.validate_status_screen()
    needle_test_result_page.tap_stop_button()


@then('User validates the status screen for the needle readiness workflow')
def validate_stop_workflow(needle_test_result_page: NeedleSealReadinessResultsScreen):
    needle_test_result_page.validate_abort_status_screen()
    needle_test_result_page.tap(BasePageLocators.BACK_BUTTON)


@then(cfparse('Validate that the edit field shows "{error_state}" for "{flow_rate}"'))
def validate_error_state(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen,
                         error_state, flow_rate):
    needle_seal_readiness_workflow_setup_page.validate_flow_settings_screen()
    flow_setup_context(needle_seal_readiness_workflow_setup_page)
    needle_seal_readiness_workflow_setup_page.enter_value(flow_rate)
    error_state = TypeConverter.to_bool(error_state)
    edit_field_error_state = needle_seal_readiness_workflow_setup_page.is_edit_field_in_error_state(
        NeedleSealReadinessSetupLocators.FLOW_EDIT_FIELD_STATE)
    assert edit_field_error_state == error_state, "Edit field did not show error state"
    assert needle_seal_readiness_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL) != edit_field_error_state


def validate_results_context(needle_test_result_page: NeedleSealReadinessResultsScreen):
    actual_paragraph_text = needle_test_result_page.get_results_info()
    logger.info(f"actual_paragraph_text in results screen======>>>>>{actual_paragraph_text}")
    expected_paragraph_text = NeedleSealReadinessConstants.expected_results_info
    logger.info(f"expected_paragraph_text in results screen======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


def validate_summary_context(needle_seal_readiness_workflow_summary_page: NeedleSealReadinessSummaryScreen):
    actual_paragraph_text = needle_seal_readiness_workflow_summary_page.get_summary_text()
    logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")
    expected_paragraph_text = NeedleSealReadinessConstants.expected_summary_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


@then("User starts the needle seal readiness test")
def tap_start_button(context, needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen,
                     needle_seal_readiness_workflow_summary_page: NeedleSealReadinessSummaryScreen):
    context["date_time"] = current_date()
    needle_seal_readiness_workflow_summary_page.validate_summary_screen()
    needle_seal_readiness_workflow_setup_page.tap(NeedleSealReadinessLocators.START_BUTTON)


def flow_setup_context(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen):
    actual_paragraph_text = needle_seal_readiness_workflow_setup_page.get_setup_text()
    logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")
    expected_paragraph_text = NeedleSealReadinessConstants.expected_setup_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


def composition_setup_context(needle_seal_readiness_workflow_setup_page: NeedleSealReadinessSetupScreen):
    actual_line_text = needle_seal_readiness_workflow_setup_page.get_comp_setup_text()
    logger.info(f"actual_line_text======>>>>>{actual_line_text}")
    expected_line_text = NeedleSealReadinessConstants.expected_comp_setup_text
    logger.info(f"actual_line_text======>>>>>{expected_line_text}")
    assert actual_line_text == expected_line_text, f"actual_paragraph_text ==>{actual_line_text}"


def validate_status_context(needle_test_result_page: NeedleSealReadinessResultsScreen):
    actual_paragraph_text = needle_test_result_page.get_text(NeedleSealReadinessResultsLocators.STATUS_LINE_ONE)
    logger.info(f"actual_paragraph_text======>>>>>{actual_paragraph_text}")
    expected_paragraph_text = NeedleSealReadinessConstants.StatusLineOne
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


def build_solvent_composition_data(line_1, line_2, line_3, line_4):
    """
    This function builds and returns a list using the input data from the feature file
    :param line_1: Test data from the feature file
    :param line_2: Test data from the feature file
    :param line_3: Test data from the feature file
    :param line_4: Test data from the feature file
    :return: solvent_composition
    """
    solvent_line_1 = SolventLine.parse(line_1)
    solvent_line_2 = SolventLine.parse(line_2)
    solvent_line_3 = SolventLine.parse(line_3)
    solvent_line_4 = SolventLine.parse(line_4)
    return build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4)


def build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4):
    """
    This function builds solvent composition for the given solvent line
    :param solvent_line_1: parsed data from the feature file
    :param solvent_line_2: parsed data from the feature file
    :param solvent_line_3: parsed data from the feature file
    :param solvent_line_4: parsed data from the feature file
    :return: solvent_composition
    """
    solvent_composition = SolventComposition()
    solvent_composition.add(solvent_line_1)
    solvent_composition.add(solvent_line_2)
    solvent_composition.add(solvent_line_3)
    solvent_composition.add(solvent_line_4)
    return solvent_composition
