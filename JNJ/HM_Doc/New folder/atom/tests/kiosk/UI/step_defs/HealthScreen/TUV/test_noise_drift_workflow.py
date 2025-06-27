import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.date_utilities import current_date, is_within_tolerance
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.noise_and_drift_constants import NoiseAndDriftConstants
from web_framework.kiosk.common.Constants.UI.commands import CommandsConstants
from web_framework.kiosk.common.Constants.UI.logs import LogTableHeaders, NoiseDriftConstants
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_results_screen import NoiseDriftWorkflowResultsScreen
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_screen import NoiseDriftWorkflowSetupScreen
from web_framework.kiosk.pages.Health.TUV.noise_drift_workflow_summary_screen import NoiseDriftWorkflowSummaryScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.Locators.Health.TUV.noise_drift_workflow_locators import NoiseDriftSummaryLocators
from web_framework.kiosk.pages.Locators.Health.TUV.noise_drift_workflow_locators import NoiseDriftWorkflowLocators, \
    NoiseDriftSetupLocators, NoiseDriftResultsLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.commands_screen_locators import CommandsScreenPageLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/TUV/noise_drift_workflow.feature')
logger = Logger("test_noise_drift_workflow")


@pytest.fixture
def noise_drift_workflow_setup_page(page_builder):
    page = page_builder(NoiseDriftWorkflowSetupScreen)
    return page


@pytest.fixture
def noise_drift_workflow_summary_page(page_builder):
    page = page_builder(NoiseDriftWorkflowSummaryScreen)
    return page


@pytest.fixture
def noise_drift_workflow_results_page(page_builder):
    page = page_builder(NoiseDriftWorkflowResultsScreen)
    return page


@pytest.fixture
def instrument_diagnostic_screen_page(page_builder):
    page = page_builder(InstrumentDiagnosticScreen)
    return page


@given("User navigates to health troubleshoot area")
def navigate_troubleshoot_tuv(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)


@given(cfparse('User set the lamp detector "{lamp_state}"'))
def set_lamp_state(lamp_state, command_screen_page: CommandsScreen):
    command_screen_page.validate_command_screen()
    command_screen_page.turn_off_lamp() if lamp_state == "Off" else command_screen_page.turn_on_lamp()


@given("User navigates to Commands area")
def navigate_to_commands(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_commands()


@given("User navigates to TUV section")
def navigate_instrument_diagnostic(instrument_diagnostic_screen_page: InstrumentDiagnosticScreen):
    instrument_diagnostic_screen_page.validate_idle_state()
    instrument_diagnostic_screen_page.tap(HealthScreenLocators.TUV_SECTION_ICON)


@when("User taps noise-drift start panel")
def start_noise_drift_workflow(health_screen_page: HealthHomeScreen):
    health_screen_page.validate_idle_state()
    health_screen_page.tap(HealthScreenLocators.NOISE_DRIFT_START_PANEL)


@when('User validates the welcome context in the welcome screen')
def validate_welcome_text(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    actual_paragraph_text = noise_drift_workflow_setup_page.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = NoiseAndDriftConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    assert actual_paragraph_text == expected_paragraph_text, f"actual_paragraph_text ==>{actual_paragraph_text}"


@when(cfparse('User enters the "{flow_rate}", "{line_1}", "{line_2}", "{line_3}", "{line_4}"'))
def enter_flow_and_solvent(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                           flow_rate, line_1, line_2, line_3, line_4):
    try:
        selected_solvent_details = noise_drift_workflow_setup_page.selected_and_get_solvent_details(flow_rate, line_1,
                                                                                                    line_2, line_3,
                                                                                                    line_4)
        logger.info(f"selected_solvent_details====={selected_solvent_details}")
        noise_drift_workflow_setup_page.set_selected_solvent_details(selected_solvent_details)

    finally:
        noise_drift_workflow_setup_page.tap_next_button()


@when("User goes back to Commands area")
def navigate_to_commands(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_commands()


@when("User navigates to the summary screen")
def navigate_to_summary_screen(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.tap_next_button()
    noise_drift_workflow_setup_page.tap_next_button()
    noise_drift_workflow_setup_page.tap_next_button()
    noise_drift_workflow_setup_page.tap_next_button()


@when(cfparse('User turns the flow "{flow_state}"'))
def turn_lamp(flow_state, noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    if flow_state == "On":
        time.sleep(1)
        noise_drift_workflow_setup_page.tap_toggle_button_on(NoiseDriftSetupLocators.FLOW_RATE_TOGGLE)
        logger.info("Flow is ON")
        actual_text = noise_drift_workflow_setup_page.get_text(NoiseDriftSetupLocators.FLOW_READ_BACK_MESSAGE)
        expected_text = NoiseAndDriftConstants.FlowOnReadBackMessage
        noise_drift_workflow_setup_page.validate_text(actual_text, expected_text)
    elif flow_state == "Off":
        logger.info("FlowFlow is OFF")
        time.sleep(1)
        noise_drift_workflow_setup_page.tap_toggle_button_off(NoiseDriftSetupLocators.FLOW_RATE_TOGGLE)
        actual_text = noise_drift_workflow_setup_page.get_text(NoiseDriftSetupLocators.FLOW_READ_BACK_MESSAGE)
        expected_text = NoiseAndDriftConstants.FlowOffReadBackMessage
        noise_drift_workflow_setup_page.validate_text(actual_text, expected_text)


@then('User validates the status stopped for the noise and drift workflow')
def validate_stop_screen(noise_drift_workflow_results_page: NoiseDriftWorkflowResultsScreen):
    noise_drift_workflow_results_page.validate_abort_status_screen()


@then('the log entry is created with correct time, date, category and action details')
def validate_needle_seal_log(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    category = context["category"]
    time_diff = is_within_tolerance(context["date_time"], log_entry[LogTableHeaders.date_and_time], 2)

    assert time_diff, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {context["date_time"]}. Actual date: {log_entry[LogTableHeaders.date_and_time]}')

    assert log_entry[LogTableHeaders.category] == category, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {category}. Actual date: {log_entry[LogTableHeaders.category]}')

    assert log_entry[LogTableHeaders.source] == NoiseDriftConstants.Source, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {NoiseDriftConstants.Source}. Actual date: {log_entry[NoiseDriftConstants.Source]}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text: str = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    time_diff = is_within_tolerance(context["date_time"], date_text, 2)

    assert time_diff, (f"The Date and time is not as expected. "
                       f"Expected Date: {date_text}. "
                       f"Actual date: {date_text}")
    assert category_text == category, (f"The Category  is not as expected. Expected Category: {category}. "
                                       f"Actual Category: {category_text}")
    assert source_text == NoiseDriftConstants.Source, (f"The Source is not as expected. Expected Source: {NoiseDriftConstants.Source}. "
                                                       f"Actual Source: {source_text}")


@then('User validate the lamp state in the summary screen is Off')
def validate_lamp_off(noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    current_lamp_state = noise_drift_workflow_summary_page.get_text(NoiseDriftSummaryLocators.LAMP_INFO_LABEL)
    assert current_lamp_state == NoiseAndDriftConstants.LampOffReadBackMessage, "Lamp was not OFF"


@then('User validate the lamp state in the summary screen is On')
def validate_lamp_off(noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    current_lamp_state = noise_drift_workflow_summary_page.get_text(NoiseDriftSummaryLocators.LAMP_INFO_LABEL)
    assert NoiseAndDriftConstants.LampOnReadBackMessage in current_lamp_state, "Lamp was not On"


@then("User validate the lamp state is Off")
def validate_lamp_off(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.validate_flow_rate_screen()
    noise_drift_workflow_setup_page.wait_time_to_load_value(NoiseDriftSetupLocators.LAMP_STATE)
    current_lamp_state = noise_drift_workflow_setup_page.get_text(NoiseDriftSetupLocators.LAMP_STATE)
    assert current_lamp_state == NoiseAndDriftConstants.LampOffReadBackMessage, "Lamp is not Off"


@when(cfparse('User sets the "{channel_a_value}"'))
def set_channel_a_wavelength(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen, channel_a_value):
    noise_drift_workflow_setup_page.tap(NoiseDriftSetupLocators.CHANNEL_A_PANEL)
    noise_drift_workflow_setup_page.set_spinner_value(NoiseDriftSetupLocators.WAVELENGTH_PICKER, channel_a_value)


@when(cfparse('User sets the data rate as "{data_rate_value}" and filter time as "{filter_time_constant}"'))
def set_frequency_and_time_constant(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                                    data_rate_value, filter_time_constant):
    selected_data_rate_details = noise_drift_workflow_setup_page.select_and_get_data_rate(data_rate_value,
                                                                                          filter_time_constant)
    logger.info(f"selected_data_rate_details===>>>{selected_data_rate_details}")
    noise_drift_workflow_setup_page.set_selected_frequency_rate_details(selected_data_rate_details)
    noise_drift_workflow_setup_page.tap_next_button()


@when('User navigates to summary screen')
def navigate_to_summary_screen(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                               noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    noise_drift_workflow_setup_page.tap_next_button()
    noise_drift_workflow_summary_page.validate_summary_screen()


@then('User validates the solvent details')
def validate_summary_screen_details(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                                    noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    noise_drift_workflow_summary_page.validate_summary_screen()
    current_solvent_details = noise_drift_workflow_summary_page.get_solvent_details()
    expected_solvent_details = noise_drift_workflow_setup_page.get_selected_solvent_details()
    assert current_solvent_details == expected_solvent_details, f"current_solvent_details=>{current_solvent_details},expected_solvent_details=>{expected_solvent_details} "


@then(cfparse('User validates the wavelength details for "{wavelength_mode}"'))
def validate_wavelength_details(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                                noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen, wavelength_mode):
    current_wavelength_details = noise_drift_workflow_summary_page.get_wavelength_details(wavelength_mode)
    noise_drift_workflow_setup_page.set_selected_wavelength_details(current_wavelength_details)
    expected_wavelength_details = noise_drift_workflow_setup_page.get_selected_wavelength_details()
    assert current_wavelength_details == expected_wavelength_details, f"current_wavelength_details==>{current_wavelength_details}" \
                                                                      f"expected_wavelength_details==>{expected_wavelength_details}"


@then('User validates the data rate details and filter')
def validate_date_rate_details(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                               noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    current_data_rate_details = noise_drift_workflow_summary_page.get_data_rate_details()
    expected_data_rate_details = noise_drift_workflow_setup_page.get_selected_frequency_details()
    assert current_data_rate_details == expected_data_rate_details, f"current_data_rate_details ==> {current_data_rate_details}" \
                                                                    f"expected_data_rate_details ==> {expected_data_rate_details}"


@when("User taps start")
def tap_start_button(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.tap(NoiseDriftWorkflowLocators.START_BUTTON)


@then("User verifies the test was completed")
def validate_noise_drift_test(context, noise_drift_workflow_summary_page: NoiseDriftWorkflowSummaryScreen):
    noise_drift_workflow_summary_page.wait_for_test_end()
    context["date_time"] = current_date()
    context["category"] = NoiseDriftConstants.Category


@when(cfparse('User sets the flow rate to "{flow_rate}"'))
def set_default_flowrate(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen, flow_rate):
    noise_drift_workflow_setup_page.enter_value(flow_rate)


@then('User validates the results data in the result screen')
def validate_results_screen(noise_drift_workflow_results_page: NoiseDriftWorkflowResultsScreen,
                            noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_results_page.tap(NoiseDriftResultsLocators.DOWN_ARROW_ICON)
    noise_drift_workflow_results_page.validate_results_data_table()
    actual_solvent_details = noise_drift_workflow_results_page.get_solvent_details()
    expected_solvent_details = noise_drift_workflow_setup_page.get_selected_solvent_details()
    logger.info(f"actual_solvent_details=====>>>>>>>{actual_solvent_details}")
    logger.info(f"expected_solvent_details=====>>>>>>>{expected_solvent_details}")
    assert actual_solvent_details == expected_solvent_details, f"The solvent composition in the condition block is incorrect"
    noise_drift_workflow_results_page.tap_done_button()


@then('User validates the results page')
def validate_results_screen(noise_drift_workflow_results_page: NoiseDriftWorkflowResultsScreen):
    noise_drift_workflow_results_page.tap(NoiseDriftResultsLocators.DOWN_ARROW_ICON)
    noise_drift_workflow_results_page.validate_results_data_table()
    noise_drift_workflow_results_page.tap_done_button()


@when(cfparse('User sets the "{data_rate_value}", "{use_filter}" and "{filter_time_constant}"'))
def set_params(data_rate_value, use_filter, filter_time_constant, noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    selected_data_rate_details = noise_drift_workflow_setup_page.select_and_get_data_rate(data_rate_value,
                                                                                          filter_time_constant)
    logger.info(f"selected_data_rate_details===>>>{selected_data_rate_details}")
    noise_drift_workflow_setup_page.set_selected_frequency_rate_details(selected_data_rate_details)
    if use_filter == "On":
        noise_drift_workflow_setup_page.tap_toggle_button_on(NoiseDriftSetupLocators.FILTER_STATE_TOGGLE)
    elif use_filter == "Off":
        noise_drift_workflow_setup_page.tap_toggle_button_off(NoiseDriftSetupLocators.FILTER_STATE_TOGGLE)
    noise_drift_workflow_setup_page.tap_next_button()


@when(cfparse('User stops the workflow after "{stop_time:d}"'))
def stop_workflow(context, stop_time, noise_drift_workflow_results_page: NoiseDriftWorkflowResultsScreen):
    time.sleep(stop_time)  # not condition involved, physically wait for n sec before aborting the workflow
    context["date_time"] = current_date()
    context["category"] = NoiseDriftConstants.AbortCategory
    noise_drift_workflow_results_page.tap_stop_button()


@when("User taps next")
def tap_next_button(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.tap_next_button()


@when("User goes back to composition screen")
def navigate_back_to_composition_screen(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.wait_element_to_be_clickable(BasePageLocators.BACK_BUTTON, noise_drift_workflow_setup_page.wait_time)
    noise_drift_workflow_setup_page.tap_back_button()
    noise_drift_workflow_setup_page.validate_data_rate_screen()
    noise_drift_workflow_setup_page.tap_back_button()


@when('User sets 100% A composition button')
def set_default_composition(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.reset_composition()
    noise_drift_workflow_setup_page.tap_next_button()
    noise_drift_workflow_setup_page.validate_data_rate_screen()


@then('User validate the lamp state is On')
def validate_lamp_state_off(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.validate_flow_rate_screen()
    current_lamp_state = noise_drift_workflow_setup_page.get_text(NoiseDriftSetupLocators.LAMP_STATE)
    assert NoiseAndDriftConstants.LampOnReadBackMessage in current_lamp_state, "Lamp is not On"


@then(cfparse('Validate that the edit field shows "{error_state}"'))
def validate_error_state(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen,
                         error_state):
    noise_drift_workflow_setup_page.validate_flow_rate_screen()
    error_state = TypeConverter.to_bool(error_state)
    edit_field_error_state = noise_drift_workflow_setup_page.is_edit_field_in_error_state(
        NoiseDriftSetupLocators.FLOW_RATE_FIELD)
    assert edit_field_error_state == error_state, "Edit field did not show error state"
    assert noise_drift_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL) != edit_field_error_state


@then(cfparse('Validate the Next button is enabled'))
def validate_error_state(noise_drift_workflow_setup_page: NoiseDriftWorkflowSetupScreen):
    noise_drift_workflow_setup_page.validate_flow_rate_screen()
    assert noise_drift_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)


@then('User validate the lamp state is On in command screen')
def validate_lamp_state_on_in_command(command_screen_page: CommandsScreen):
    command_screen_page.validate_command_screen()
    command_screen_page.wait_time_to_load_value(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT)
    current_state = command_screen_page.get_text(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT)
    assert current_state == CommandsConstants.LampOnReadBackMessage, "Lamp is not ON"


@then('User validate the lamp state is Off in command screen')
def validate_lamp_state_in_command(command_screen_page: CommandsScreen):
    command_screen_page.validate_command_screen()
    command_screen_page.wait_time_to_load_value(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT)
    current_state = command_screen_page.get_text(CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT)
    assert current_state == CommandsConstants.LampOffReadBackMessage, "Lamp is not Off"


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
