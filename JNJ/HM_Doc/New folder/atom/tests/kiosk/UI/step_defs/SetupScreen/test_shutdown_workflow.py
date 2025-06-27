import math
import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from utilities.assert_timeout import AssertTimeout
from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.shutdown_constants import ShutdownConstants
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import SolventCompositionTabScreen as solcomp
from web_framework.kiosk.pages.Locators.Setup.setup_screen_locators import SetupScreenLocators
from web_framework.kiosk.pages.Locators.Setup.shutdown_workflow_locators import ShutdownWorkflowLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Setup.Models.summary_workflow import SolventSummaryDetails
from web_framework.kiosk.pages.Setup.setup_home_screen import SetupHomeScreen
from web_framework.kiosk.pages.Setup.shutdown_workflow_screen import ShutdownWorkflowSetupScreen
from web_framework.kiosk.pages.Setup.shutdown_workflow_summary_screen import ShutdownWorkflowSummaryScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SetupScreen/shutdown_workflow.feature')
logger = Logger("test_shutdown_workflow")


@pytest.fixture
def shutdown_workflow_setup_page(page_builder):
    page = page_builder(ShutdownWorkflowSetupScreen)
    return page


@pytest.fixture
def shutdown_workflow_summary_page(page_builder):
    page = page_builder(ShutdownWorkflowSummaryScreen)
    return page


@when('User taps the setup button in the home screen')
def tap_setup_button(session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.validate_idle_state()
    session_dash_board_screen_page.tap_setup()


@when('User taps the shutdown workflow panel')
def tap_shutdown_panel(setup_screen_page: SetupHomeScreen):
    setup_screen_page.validate_setup_screen()
    setup_screen_page.validate_idle_state()
    setup_screen_page.tap(SetupScreenLocators.SHUTDOWN_WORKFLOW_START)


@when('User validates the welcome context in the welcome screen')
def validate_welcome_text(shutdown_workflow_setup_page):
    shutdown_workflow_setup_page.validate_welcome_screen()
    actual_paragraph_text = shutdown_workflow_setup_page.get_welcome_paragraph_text()
    logger.info(f"Actual_paragraph_text======>>>>>{actual_paragraph_text}")

    expected_paragraph_text = ShutdownConstants.expected_welcome_paragraph_text
    logger.info(f"expected_paragraph_text======>>>>>{expected_paragraph_text}")
    if not actual_paragraph_text == expected_paragraph_text:
        shutdown_workflow_setup_page.tap(ShutdownWorkflowLocators.CANCEL_BUTTON)
        shutdown_workflow_setup_page.tap(BasePageLocators.BACK_BUTTON)
    elif actual_paragraph_text == expected_paragraph_text:
        shutdown_workflow_setup_page.tap_next_button()


@when(cfparse('User set the sample temperature as "{sample_temperature}"'))
def set_sample_temperature(shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen, sample_temperature):
    time.sleep(1)
    try:
        shutdown_workflow_setup_page.validate_sample_temperature_screen()

        if sample_temperature == "Off":
            shutdown_workflow_setup_page.set_toggle_button(ShutdownWorkflowLocators.TOGGLE_BUTTON, False)
        else:
            logger.info(f"sample test else condition")
            shutdown_workflow_setup_page.set_toggle_button(ShutdownWorkflowLocators.TOGGLE_BUTTON, True)
            time.sleep(4)
            shutdown_workflow_setup_page.set_spinner_value(
                ShutdownWorkflowLocators.SAMPLE_TEMPERATURE_LIST,
                sample_temperature)

    finally:
        shutdown_workflow_setup_page.tap_next_button()


@when(cfparse('User set the column temperature as "{column_temperature}"'))
def set_column_temperature(shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen, column_temperature):
    time.sleep(1)
    logger.info(f"When the column temp is OFF")
    try:
        shutdown_workflow_setup_page.validate_column_temperature_screen()

        if column_temperature == "Off":
            logger.info(f"When the column temp is OFF")
            shutdown_workflow_setup_page.set_toggle_button(ShutdownWorkflowLocators.COLUMN_TOGGLE_BUTTON, False)

        else:
            logger.info(f"When the column temp is On")
            shutdown_workflow_setup_page.set_toggle_button(ShutdownWorkflowLocators.COLUMN_TOGGLE_BUTTON, True)

            shutdown_workflow_setup_page.set_spinner_value(
                ShutdownWorkflowLocators.COLUMN_TEMPERATURE_LIST,
                column_temperature)

    finally:
        shutdown_workflow_setup_page.tap_next_button()


@when(cfparse('User turns "{lamp_state}" the lamp'))
def set_lamp(shutdown_workflow_setup_page, lamp_state):
    time.sleep(1)
    try:
        shutdown_workflow_setup_page.validate_lamp_screen()
        if lamp_state == "Off":
            shutdown_workflow_setup_page.tap_toggle_button_off(ShutdownWorkflowLocators.LAMP_TOGGLE_BUTTON)
        else:
            shutdown_workflow_setup_page.tap_toggle_button_on(ShutdownWorkflowLocators.LAMP_TOGGLE_BUTTON)

    finally:
        shutdown_workflow_setup_page.tap_next_button()


@when(cfparse('User enters the solvent "{line_1:str?}", "{line_2:str?}", "{line_3:str?}", "{line_4:str?}" for "{flow_rate}"', CONVERTERS))
def set_get_composition_flow_rate(line_1, line_2, line_3, line_4, flow_rate, shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen):
    time.sleep(1)
    try:
        shutdown_workflow_setup_page.validate_flow_rate_screen()

        if flow_rate == "Off":
            logger.info(f"When the flow is OFF")
            shutdown_workflow_setup_page.tap_toggle_button_off(ShutdownWorkflowLocators.FLOW_TOGGLE_BUTTON)

        else:
            shutdown_workflow_setup_page.tap_toggle_button_on(ShutdownWorkflowLocators.FLOW_TOGGLE_BUTTON)
            shutdown_workflow_setup_page.clear_num_pad_entries(ShutdownWorkflowLocators.FLOW_RATE_EDIT_FIELD)
            shutdown_workflow_setup_page.enter_flow_rate(flow_rate)
            current_flow_rate = flow_rate
            current_flow_rate = TypeConverter.to_float(current_flow_rate)
            shutdown_workflow_setup_page.tap_next_button()
            shutdown_workflow_setup_page.validate_solvent_screen()
            shutdown_workflow_setup_page.reset_composition()
            solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
            shutdown_workflow_setup_page.enter_composition(solvent_composition)
            current_solvent_a = shutdown_workflow_setup_page.get_user_input_text(solcomp.SOLVENT_A_EDIT_FIELD)
            current_solvent_a = TypeConverter.to_float(current_solvent_a)
            current_solvent_b = shutdown_workflow_setup_page.get_user_input_text(solcomp.SOLVENT_B_EDIT_FIELD)
            current_solvent_b = TypeConverter.to_float(current_solvent_b)
            current_solvent_c = shutdown_workflow_setup_page.get_user_input_text(solcomp.SOLVENT_C_EDIT_FIELD)
            current_solvent_c = TypeConverter.to_float(current_solvent_c)
            current_solvent_d = shutdown_workflow_setup_page.get_user_input_text(solcomp.SOLVENT_D_EDIT_FIELD)
            current_solvent_d = TypeConverter.to_float(current_solvent_d)
            solvent_summary_details = SolventSummaryDetails(current_flow_rate, current_solvent_a, current_solvent_b,
                                                            current_solvent_c, current_solvent_d)
            logger.info(f"solvent_summary_details++++++=======>>>>>>>{solvent_summary_details}")
            shutdown_workflow_setup_page.set_selected_solvent_details(solvent_summary_details)

    finally:
        shutdown_workflow_setup_page.tap_next_button()


@then(cfparse('User validates the summary screen details for temperature "{sample_temperature}", "{column_temperature}"'))
def validate_temperature_details(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen,
                                 sample_temperature, column_temperature):
    shutdown_workflow_summary_page.validate_summary_screen()

    if sample_temperature != "Off" and column_temperature != "Off":
        expected_sample_temperature = TypeConverter.to_float(sample_temperature)
        expected_column_temperature = TypeConverter.to_float(column_temperature)
        time.sleep(1)
        current_temperature_details = shutdown_workflow_summary_page.get_current_temperature_details()
        expected_temperature_details = shutdown_workflow_summary_page.get_expected_temperature_details(
            expected_sample_temperature, expected_column_temperature)
        assert current_temperature_details == expected_temperature_details, f" current_temperature_details========>>>>{current_temperature_details}" \
                                                                            f"expected_temperature_details========>>>>{expected_temperature_details}"

    elif sample_temperature == "Off" and column_temperature == "Off":
        time.sleep(3)
        current_sample_temperature = shutdown_workflow_summary_page.get_text(
            ShutdownWorkflowLocators.SAMPLE_TEMPERATURE_INFO)
        current_column_temperature = shutdown_workflow_summary_page.get_text(
            ShutdownWorkflowLocators.COLUMN_TEMPERATURE_INFO)
        assert current_sample_temperature == ShutdownConstants.SampleTempOffMessage
        assert current_column_temperature == ShutdownConstants.ColumnTempOffMessage
        logger.info(f" current_temperature_details========>>>>{current_sample_temperature}")


@then('User validates the summary screen details for "<flow_rate>"')
@then(cfparse('User validates the summary screen details for "{flow_rate}"'))
def validate_prime_solvent_details(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen,
                                   shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen,
                                   flow_rate):
    time.sleep(1)
    shutdown_workflow_summary_page.validate_summary_screen()
    if flow_rate == "Off":
        current_flow_info = shutdown_workflow_summary_page.get_text(ShutdownWorkflowLocators.FLOW_RATE_INFO)
        assert current_flow_info == ShutdownConstants.FlowOffMessage

    else:
        current_solvent_details = shutdown_workflow_summary_page.get_solvent_details()
        logger.info(f" current_solvent_details========>>>>{current_solvent_details}")
        expected_solvent_details = shutdown_workflow_setup_page.get_selected_solvent_summary_details()
        logger.info(f" expected_solvent_details========>>>>{expected_solvent_details}")
        assert current_solvent_details == expected_solvent_details, f"expected_solvent_details ==>{expected_solvent_details} "


@then(cfparse('User validates the lamp state "{lamp_state}"'))
def validate_lamp(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen, lamp_state):
    shutdown_workflow_summary_page.validate_summary_screen()
    if lamp_state == "Off":
        current_lamp_state = shutdown_workflow_summary_page.get_text(ShutdownWorkflowLocators.LAMP_INFO_OFF)
        assert current_lamp_state == ShutdownConstants.LampOffInfo, "The Lamp is on"

    else:
        current_lamp_state = shutdown_workflow_summary_page.get_text(ShutdownWorkflowLocators.LAMP_INFO)
        assert current_lamp_state == ShutdownConstants.LampOnInfo, "The Lamp is off"


@then('User aborts the prime workflow')
def stop_workflow(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen):
    time.sleep(3)  ## not condition involved, physically wait for 3 sec before aborting the workflow
    shutdown_workflow_summary_page.validate_status_screen()
    shutdown_workflow_summary_page.tap_stop_button()


@then('User validates the status screen for the shutdown workflow')
def validate_stop_workflow(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen):
    shutdown_workflow_summary_page.validate_abort_status_screen()


@then('User taps on start button')
def tap_start_button(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen):
    shutdown_workflow_summary_page.validate_summary_screen()
    shutdown_workflow_summary_page.tap(BasePageLocators.START_BUTTON)


@then('User validates the test completes successfully')
def start_shutdown_process(shutdown_workflow_summary_page: ShutdownWorkflowSummaryScreen, dashboard_screen_page: DashBoardScreen):
    locator = ShutdownWorkflowLocators.WORKFLOW_COMPLETE_STATE
    expected_condition = ShutdownConstants.WorkFlowCompleteState
    error_message = ShutdownConstants.error_message
    wait_time = ShutdownConstants.TimeToComplete
    shutdown_workflow_summary_page.wait_till_condition_met(locator, expected_condition, error_message, wait_time)
    time.sleep(1)
    shutdown_workflow_summary_page.tap_done_button()
    dashboard_screen_page.tap_home()


@then(cfparse('User validates the home screen for lamp state "{lamp_state}"'))
def validate_home_screen_lamp_state(dashboard_screen_page: DashBoardScreen, lamp_state):
    lamp_on_states = ["on", "warming", "igniting"]
    current_lamp_state = dashboard_screen_page.get_lamp_state().lower()
    lamp_state = lamp_state.lower()

    if lamp_state == "off":
        assert current_lamp_state == lamp_state, f"Expected lamp state was [{lamp_state}], actual: [{current_lamp_state}]"
    else:
        assert current_lamp_state in lamp_on_states, f"Expected lamp state was on, warming, or igniting, actual: [{current_lamp_state}]"


@then(cfparse('User validates the home screen for flow rate "{flow_rate}"'))
def validate_home_screen_flow_rate(dashboard_screen_page: DashBoardScreen, flow_rate, assert_timeout: AssertTimeout):
    dashboard_screen_page.validate_dashboard_screen()
    current_flow = dashboard_screen_page.get_current_flow()
    assert assert_timeout.are_equal(lambda: current_flow, flow_rate, "The flow rate is not matching", 300, 1)


@then(cfparse('User validates the home screen for sample temperature "{sample_temperature:d}"'))
def validate_home_screen_sample_temperature(dashboard_screen_page: DashBoardScreen, sample_temperature: float):
    # Validate the sample temperature setpoint
    sample_temperature_setpoint = dashboard_screen_page.get_sample_temperature_setpoint()
    assert sample_temperature_setpoint == sample_temperature, "The sample temperature setpoint is not matching"

    # Validate the sample temperature actual is at or getting closer to target setpoint
    current_sample_temperature = dashboard_screen_page.get_sample_temperature()
    sample_temperature_change_start = abs(sample_temperature - current_sample_temperature)
    sample_temperature_change_after_start = abs(sample_temperature - current_sample_temperature)
    sample_target_change = min(abs(sample_temperature - current_sample_temperature), 1)
    sample_temperature_difference = abs(sample_temperature_change_start - sample_temperature_change_after_start)

    start_time = time.time()
    temperature_test_duration = 300
    while time.time() - start_time < temperature_test_duration:
        current_sample_temperature = dashboard_screen_page.get_sample_temperature()
        sample_temperature_setpoint = sample_temperature
        sample_temperature_change_after_start = abs(sample_temperature_setpoint - current_sample_temperature)
        sample_temperature_difference = abs(sample_temperature_change_start - sample_temperature_change_after_start)
        if sample_temperature_difference > sample_target_change or math.isclose(sample_temperature_change_after_start, 0, abs_tol=2):
            break
        time.sleep(1)
    assert sample_temperature_difference > sample_target_change or math.isclose(sample_temperature_change_after_start, 0, abs_tol=2), \
        "The sample temperature is not getting closer to target"


@then(cfparse('User validates the home screen for column temperature "{column_temperature:d}"'))
def validate_home_screen_column_temperature(dashboard_screen_page: DashBoardScreen, column_temperature: float):
    # Validate the column temperature setpoint
    column_temperature_setpoint = dashboard_screen_page.get_column_temperature()
    assert column_temperature_setpoint == column_temperature, "The column temperature setpoint is not matching"

    # Validate the column temperature actual is at or getting closer to target setpoint
    current_column_temperature = dashboard_screen_page.get_column_temperature_actual()
    column_temperature_change_start = abs(column_temperature - current_column_temperature)
    column_temperature_change_after_start = abs(column_temperature - current_column_temperature)
    column_target_change = min(abs(column_temperature - current_column_temperature), 1)
    column_temperature_difference = abs(column_temperature_change_start - column_temperature_change_after_start)

    start_time = time.time()
    temperature_test_duration = 300
    while time.time() - start_time < temperature_test_duration:
        current_column_temperature = dashboard_screen_page.get_column_temperature_actual()
        column_temperature_setpoint = column_temperature
        column_temperature_change_after_start = abs(column_temperature_setpoint - current_column_temperature)
        column_temperature_difference = abs(column_temperature_change_start - column_temperature_change_after_start)
        if column_temperature_difference > column_target_change or math.isclose(column_temperature_change_after_start, 0, abs_tol=2):
            break
        time.sleep(1)
    assert column_temperature_difference > column_target_change or math.isclose(column_temperature_change_after_start, 0, abs_tol=2), \
        "The column temperature is not getting closer to target"


@when('User navigates to the flow settings screen')
def navigate_to_flow_screen(shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen):
    shutdown_workflow_setup_page.tap_next_button()
    shutdown_workflow_setup_page.tap_next_button()
    shutdown_workflow_setup_page.tap_next_button()


@then(cfparse('Validate that the edit field shows "{error_state}" for "{flow_rate}"'))
def validate_error_state(shutdown_workflow_setup_page: ShutdownWorkflowSetupScreen, error_state, flow_rate):
    try:
        shutdown_workflow_setup_page.validate_flow_rate_screen()
        shutdown_workflow_setup_page.tap_toggle_button_on(ShutdownWorkflowLocators.FLOW_TOGGLE_BUTTON)
        shutdown_workflow_setup_page.enter_value(flow_rate)
        error_state = TypeConverter.to_bool(error_state)
        time.sleep(2)
        edit_field_error_state = shutdown_workflow_setup_page.is_edit_field_in_error_state(
            ShutdownWorkflowLocators.FLOW_EDIT_FIELD_STATE)
        logger.info(f"edit_field_error_state======>>>>>{edit_field_error_state}")
        assert edit_field_error_state == error_state
        if edit_field_error_state:
            assert not shutdown_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)
        else:
            assert shutdown_workflow_setup_page.is_button_active(BasePageLocators.NEXT_BUTTON_LABEL)

    finally:
        shutdown_workflow_setup_page.tap_cancel_button()


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
