import time
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from tests.kiosk.UI.step_defs.HomeScreen.SolventManager.test_solvent_composition_condition_card import \
    assert_solvent_composition_data, get_current_solvent_composition_value
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import SolventCompositionConditionCardConstants, \
    FlowConditionCardConstants
from utilities.datatables.converters import CONVERTERS
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SolventManager.flow_settings_screen import FlowSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import FlowControlTabScreen as fct
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import \
    SolventCompositionTabScreen as solcomp, FlowControlTabScreen, SolventCompositionTabScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.sm_home_screen import SolventManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/flow_condition_card.feature',
              '../../../features/HomeScreen/SolventManager/solvent_composition.feature',
              '../../../features/HomeScreen/SolventManager/flow_edit_field.feature',
              '../../../features/HomeScreen/SolventManager/flow_hint_messages.feature')

logger = Logger("test_flow_condition_card")


@given('User navigates to the flow control screen')
def tap_flow_condition_card(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    logger.info("**************************The flow condition card test starts**********************")
    solvent_manager_home_screen_page.validate_idle_state()
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.wait_time_to_load_value(SolventManagerHomeScreenLocators.FLOW_RATE, "---")
    solvent_manager_home_screen_page.tap_flow_condition_card()


@when('User navigates to the flow control screen')
def navigate_to_flow_settings_screen(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    logger.info("**************************The flow condition card test starts**********************")
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_flow_condition_card()


@when(cfparse('User adds the solvent composition for solvent line "{line_1:str?}", "{line_2:str?}", "{line_3:str?}", "{line_4:str?}"', CONVERTERS))
def set_composition(flow_setting_screen_page: FlowSettingsScreen, line_1, line_2, line_3, line_4):
    flow_setting_screen_page.tap_solvent_composition_tab()
    flow_setting_screen_page.validate_composition_settings_screen()
    time.sleep(1)  # TODO create a function to validate solvent composition screen
    flow_setting_screen_page.reset_composition()
    solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    flow_setting_screen_page.enter_composition(solvent_composition)


@then(cfparse('User validates the hint messages for "{line_1}" "{line_2}" "{line_3}" "{line_4}" in the condition card'))
def validate_helper_message(flow_setting_screen_page: FlowSettingsScreen, line_1, line_2, line_3, line_4):
    try:
        flow_setting_screen_page.tap_solvent_composition_tab()
        assert flow_setting_screen_page.is_numpad_exists(), f"The Numpad does not exists"
        flow_setting_screen_page.validate_composition_settings_screen()
        time.sleep(1)  # TODO create a function to validate solvent composition screen
        flow_setting_screen_page.reset_composition()
        solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
        flow_setting_screen_page.validate_hint_field(solvent_composition)

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then("User validates the hint messages for the empty flow edit field")
def validate_flow_helper_message(flow_setting_screen_page: FlowSettingsScreen):
    try:
        hint_locator = fct.FLOW_HINT_LOCATOR
        expected_hint_message = SolventCompositionConditionCardConstants.EmptyEditFieldMessage
        flow_setting_screen_page.validate_hint_message(hint_locator, expected_hint_message)

    finally:
        flow_setting_screen_page.tap_cancel_button()


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


@then(cfparse('Validate the solvent line for "{line_1}", "{line_2}", "{line_3}", "{line_4}"'))
def validate_solvent_composition(flow_setting_screen_page: FlowSettingsScreen,
                                 line_1, line_2, line_3, line_4):
    current_solvent_composition = get_current_solvent_composition(flow_setting_screen_page)
    expected_solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    assert_solvent_composition(current_solvent_composition, expected_solvent_composition)


def assert_solvent_composition(current_solvent_composition, expected_solvent_composition):
    """
    This function validates the solvent composition and lock state data from the lists
    :param current_solvent_composition: current solvent data list
    :param expected_solvent_composition: expected solvent data list
    :return:
    """
    for current_solvent in current_solvent_composition.get_solvent_lines():
        for expected_solvent in expected_solvent_composition.get_solvent_lines():
            assert_solvent_line(current_solvent, expected_solvent)


def assert_solvent_line(current_solvent, expected_solvent):
    """
    This function validates current solvent with the expected solvent
    :param current_solvent:
    :param expected_solvent:
    :return:
    """
    if expected_solvent.line_id == current_solvent.line_id:
        expected_solvent.percentage_value = TypeConverter.to_float(expected_solvent.percentage_value)
        current_solvent.percentage_value = TypeConverter.to_float(current_solvent.percentage_value)
        assert expected_solvent.percentage_value == current_solvent.percentage_value


def get_solvent_line(line_id, percentage_value):
    """
    This function constructs solvent line with the given input data
    :param line_id: The line id
    :param percentage_value: composition value
    :return:
    """
    solvent_line = SolventLine(line_id, percentage_value)
    solvent_line.line_id = line_id
    solvent_line.percentage_value = percentage_value
    return solvent_line


def get_current_solvent_composition(flow_setting_screen_page: FlowSettingsScreen):
    """
    This function gets the current solvent line data such as line_id, solvent composition and lock state
    returns in list form
    :param flow_setting_screen_page:
    :return:solvent_composition
    """
    solvent_line_1 = get_solvent_line(flow_setting_screen_page.get_solvent_line_id(solcomp.SOLVENT_A_LINE_ID)
                                      , flow_setting_screen_page.get_composition(solcomp.SOLVENT_A_EDIT_FIELD))

    solvent_line_2 = get_solvent_line(flow_setting_screen_page.get_solvent_line_id(solcomp.SOLVENT_B_LINE_ID)
                                      , flow_setting_screen_page.get_composition(solcomp.SOLVENT_B_EDIT_FIELD))

    solvent_line_3 = get_solvent_line(flow_setting_screen_page.get_solvent_line_id(solcomp.SOLVENT_C_LINE_ID)
                                      , flow_setting_screen_page.get_composition(solcomp.SOLVENT_C_EDIT_FIELD))

    solvent_line_4 = get_solvent_line(flow_setting_screen_page.get_solvent_line_id(solcomp.SOLVENT_D_LINE_ID)
                                      , flow_setting_screen_page.get_composition(solcomp.SOLVENT_D_EDIT_FIELD))

    return build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4)


@then(cfparse('Validate the total composition is "{total_composition}"'))
def validate_composition(total_composition, flow_setting_screen_page: FlowSettingsScreen):
    try:
        current_solvent_composition = get_current_solvent_composition(flow_setting_screen_page)

        total_composition = int(total_composition)
        composition = 0
        for solvent in current_solvent_composition.get_solvent_lines():
            solvent.percentage_value = float(solvent.percentage_value)
            composition += solvent.percentage_value

        logger.info(f"total_composition =>{total_composition},composition =>{composition}")
        assert composition == total_composition, f"The actual composition => {composition}"

    finally:
        flow_setting_screen_page.tap_cancel_button()


@when(cfparse('User adds the solvent composition for lineA "{line_a}"'))
def set_composition(flow_setting_screen_page: FlowSettingsScreen, line_a):
    flow_setting_screen_page.enter_composition(solcomp.SOLVENT_A_LOCK_ICON, line_a, solcomp.SOLVENT_A_EDIT_FIELD)


@when('User navigates to the flow rate control screen')
def tap_flow_control_tab(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap(fct.FLOW_TAB)


@when(cfparse('The user selects the "{flow}"'))
def select_flow(flow_setting_screen_page: FlowSettingsScreen, flow):
    flow_setting_screen_page.validate_flow_settings_screen()
    flow_setting_screen_page.tap_flow_tab()
    flow_setting_screen_page.select_flow(flow)


@when(cfparse('The user enters the "{flow_rate:str?}"', CONVERTERS))
def enter_flow_rate(flow_setting_screen_page: FlowSettingsScreen, flow_rate):
    flow_setting_screen_page.validate_flow_settings_screen()
    time.sleep(2)  # TODO will be removed once the vm issue is resolved
    flow_setting_screen_page.tap_toggle_button_on(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
    flow_setting_screen_page.clear_num_pad_entries(fct.FLOW_RATE_EDIT_FIELD)
    flow_setting_screen_page.enter_flow_rate(flow_rate)


@when(cfparse('User enters the acceleration time "{time_value}"'))
def set_acceleration_time(flow_setting_screen_page: FlowSettingsScreen, time_value):
    flow_setting_screen_page.enter_time(time_value)


@given(cfparse('The user enters the "{flow_rate}"'))
def enter_flow1_rate(flow_setting_screen_page: FlowSettingsScreen, flow_rate):
    flow_setting_screen_page.validate_flow_settings_screen()
    time.sleep(2)  # TODO will be removed once the vm issue is resolved
    flow_setting_screen_page.tap_toggle_button_on(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
    flow_setting_screen_page.clear_num_pad_entries(fct.FLOW_RATE_EDIT_FIELD)
    flow_setting_screen_page.enter_flow_rate(flow_rate)


@when('The user applies the selection')
def tap_apply_button(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap_apply_button()


@when('The user confirms the selection')
def tap_done_button(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap_done_button()


@when('User navigates to the solvent composition screen')
def navigate_to_solvent_screen(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap(SolventCompositionTabScreen.SOLVENT_COMPOSITION_TAB)


@when(cfparse('User adds the solvent "{actual_composition}" for solvent A only'))
def add_first_solvent(flow_setting_screen_page: FlowSettingsScreen, actual_composition):
    flow_setting_screen_page.reset_composition()
    flow_setting_screen_page.set_composition(actual_composition,
                                             solcomp.SOLVENT_A_EDIT_FIELD)


@when('The user cancels the selection')
def tap_done_button(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap_cancel_button()


@then(cfparse('The User validates the solvent composition "{line_1}" "{line_2}" "{line_3}" "{line_4}" in the condition card'))
def validate_composition(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                         line_1, line_2, line_3, line_4):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    current_solvent_composition = get_current_solvent_composition_value(solvent_manager_home_screen_page)
    logger.info(f"From validate composition====>>>>>{current_solvent_composition}")
    expected_solvent_composition = build_solvent_composition_data(line_1, line_2, line_3, line_4)
    logger.info(f"expected_solvent_composition====>>>>>{expected_solvent_composition}")
    assert_solvent_composition_data(current_solvent_composition, expected_solvent_composition)


@then(cfparse('The User validates "{expected_flow_rate}" info in the home screen'))
def validate_flow_rate(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                       dashboard_screen_page: DashBoardScreen, expected_flow_rate):
    try:
        solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
        current_flow_rate = solvent_manager_home_screen_page.get_current_flow_read_back_message()
        assert current_flow_rate == expected_flow_rate, f" The current flow rate is {current_flow_rate}"
    finally:
        dashboard_screen_page.tap_home()


@then(cfparse('The User validates "{expected_flow_rate}" info in the sm home screen'))
def validate_flow_rate(solvent_manager_home_screen_page: SolventManagerHomeScreen, expected_flow_rate):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    ignore_message = FlowConditionCardConstants.OffReadbackMessage
    solvent_manager_home_screen_page.wait_time_to_load_value(SolventManagerHomeScreenLocators.FLOW_RATE, ignore_message)
    current_flow_rate = solvent_manager_home_screen_page.get_current_flow_read_back_message()
    ignore_message = FlowConditionCardConstants.OffReadbackMessage
    solvent_manager_home_screen_page.wait_time_to_load_value(SolventManagerHomeScreenLocators.FLOW_RATE, ignore_message)
    current_flow_rate = TypeConverter.to_float(current_flow_rate)
    expected_flow_rate = TypeConverter.to_float(expected_flow_rate)
    logger.info(f"starting.....current_flow_rate==>>> {current_flow_rate}")
    logger.info(f"starting.....expected_flow_rate==>>> {expected_flow_rate}")
    current_flow_rate_units = solvent_manager_home_screen_page.get_flow_units()
    if current_flow_rate > expected_flow_rate:
        logger.info(f"The current flow is greater then expected flow")
        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            current_flow_rate = solvent_manager_home_screen_page.get_current_flow_read_back_message()
            current_flow_rate = TypeConverter.to_float(current_flow_rate)
            if current_flow_rate == expected_flow_rate:
                logger.info(f"assertion equal statement")
                break
            else:
                logger.info(f"starting.....current_flow_rate==>>> {current_flow_rate}")
                logger.info(f"starting.....expected_flow_rate==>>> {expected_flow_rate}")
                logger.info(f"assertion greater  statement")
                assert current_flow_rate > expected_flow_rate
            time.sleep(1)
    else:
        logger.info(f"The current flow is lesser then expected flow")
        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            current_flow_rate = solvent_manager_home_screen_page.get_current_flow_read_back_message()
            current_flow_rate = TypeConverter.to_float(current_flow_rate)
            if current_flow_rate == expected_flow_rate:
                logger.info(f"assertion equal statement")
                break
            else:
                logger.info(f"assertion lesser statement")
                logger.info(f"starting.....current_flow_rate==>>> {current_flow_rate}")
                logger.info(f"starting.....expected_flow_rate==>>> {expected_flow_rate}")
                assert current_flow_rate < expected_flow_rate

            time.sleep(1)

    assert current_flow_rate_units == FlowConditionCardConstants.FlowUnits, f" The flow unit => {current_flow_rate_units}"
    assert current_flow_rate == expected_flow_rate, f" The current flow rate is {current_flow_rate}"


@then('Tap the toggle button to turn on the flow')
def tap_toggle_off(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                   flow_setting_screen_page: FlowSettingsScreen):
    solvent_manager_home_screen_page.tap_flow_condition_card()
    flow_setting_screen_page.tap_toggle_button_on(FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
    flow_setting_screen_page.tap_done_button()


@then('The user validates the schematic icon for the flow rate')
def validate_schematic_icon(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                            dashboard_screen_page: DashBoardScreen):
    try:
        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            current_flow_state = solvent_manager_home_screen_page.is_flow_on(
                SolventManagerHomeScreenLocators.FLOW_PATH_SCHEMATIC_ICON)

            if current_flow_state is True:
                break
            time.sleep(1)
        assert current_flow_state is True, f"The state of flow in the schematic icon is False"

    finally:
        dashboard_screen_page.tap_home()


@then('The system indicates the flow rate is out range and does not navigate to the condition card screen')
def validate_invalid_flow_rate(flow_setting_screen_page: FlowSettingsScreen):
    try:
        assert flow_setting_screen_page.is_numpad_exists(), "The numpad is not visible"
    finally:
        flow_setting_screen_page.tap_cancel_button()


@when('User navigates to the flow rate control screen')
def tap_flow_control_tab(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap(fct.FLOW_TAB)


@when(cfparse('User validates the "{line_1}" is highlighted'))
def validate_solvent_highlight_state(flow_setting_screen_page: FlowSettingsScreen):
    time.sleep(3)
    is_value_active = flow_setting_screen_page.is_value_highlighted(SolventCompositionTabScreen.SOLVENT_A_FIELD_FOCUS)
    assert is_value_active


@when(cfparse('User add the solvent "{composition}" for solvent A only'))
def add_first_solvent(flow_setting_screen_page: FlowSettingsScreen, composition):
    flow_setting_screen_page.reset_composition()
    flow_setting_screen_page.set_composition(composition, solcomp.SOLVENT_A_EDIT_FIELD)


@when('User add the solvent composition for solvent B only')
def add_first_solvent(flow_setting_screen_page: FlowSettingsScreen):
    first_entered_composition = ".."
    second_entered_composition = "45.50"
    flow_setting_screen_page.reset_composition()
    flow_setting_screen_page.set_composition(solcomp.SOLVENT_B_LOCK_ICON, first_entered_composition,
                                             solcomp.SOLVENT_B_EDIT_FIELD)
    flow_setting_screen_page.tap_delete_button(2)
    flow_setting_screen_page.set_composition(solcomp.SOLVENT_B_LOCK_ICON, second_entered_composition,
                                             solcomp.SOLVENT_B_EDIT_FIELD)


@when('The solvent A edit field focus is lost')
def tap_edit_field(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap(solcomp.SOLVENT_B_EDIT_FIELD)


@then(cfparse('User validates the "{expected_composition}" for solvent line'))
def validate_line_a_composition(flow_setting_screen_page: FlowSettingsScreen, expected_composition):
    try:
        actual_composition = flow_setting_screen_page.get_composition(solcomp.SOLVENT_A_EDIT_FIELD)
        expected_composition = TypeConverter.to_float(expected_composition)
        actual_composition = TypeConverter.to_float(actual_composition)

        assert actual_composition == expected_composition, f" The actual composition is {actual_composition}"
    finally:
        flow_setting_screen_page.tap_cancel_button()


@when('User navigates to the flow control screen')
def navigate_to_flow_settings_screen(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    logger.info("**************************The flow condition card test starts**********************")
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_flow_condition_card()


@then(cfparse('validate the flow rate "{expected_flow_rate}" is not altered'))
def validate_cancel_button(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                           dashboard_screen_page: DashBoardScreen, expected_flow_rate):
    try:

        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            actual_flow_read_back_message = solvent_manager_home_screen_page.get_current_flow_read_back_message()
            actual_flow_read_back_message = TypeConverter.to_float(actual_flow_read_back_message)
            expected_flow_read_back_message = TypeConverter.to_float(expected_flow_rate)

            if actual_flow_read_back_message == expected_flow_read_back_message:
                break
            time.sleep(.1)

        assert actual_flow_read_back_message == expected_flow_read_back_message, f"The actual flow read back message is {actual_flow_read_back_message}"

    finally:
        dashboard_screen_page.tap_home()


@then(cfparse('User validate the numpad visibility is "{is_expected_numpad_visible}"'))
def validate_numpad_visibility(flow_setting_screen_page: FlowSettingsScreen, is_expected_numpad_visible):
    try:
        is_current_numpad_visible = flow_setting_screen_page.is_numpad_exists()
        is_expected_numpad_visible = TypeConverter.to_bool(is_expected_numpad_visible)
        assert is_current_numpad_visible == is_expected_numpad_visible

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then(cfparse('The user validates "{expected_flow_rate}" in the settings screen'))
def validate_edit_field(flow_setting_screen_page: FlowSettingsScreen, expected_flow_rate):
    try:

        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            actual_flow_read_back_message = flow_setting_screen_page.get_flow_rate()
            actual_flow_read_back_message = TypeConverter.to_float(actual_flow_read_back_message)
            expected_flow_read_back_message = TypeConverter.to_float(expected_flow_rate)

            if actual_flow_read_back_message == expected_flow_read_back_message:
                break
            time.sleep(.1)

        assert actual_flow_read_back_message == expected_flow_read_back_message, f"The actual flow read back message is {actual_flow_read_back_message}"

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then(cfparse('The user validates "{expected_flow_rate}" info in the solvent manager card reader'))
def validate_sm_card_reader(dashboard_screen_page: DashBoardScreen, expected_flow_rate):
    time.sleep(5)  # This time is required in simulation
    dashboard_screen_page.validate_dashboard_screen()
    actual_flow_read_back_message = dashboard_screen_page.get_current_flow()
    current_flow_state = dashboard_screen_page.is_flow_on(
        DashBoardsScreenPageLocators.FLOW_PATH_SCHEMATIC_ICON)
    try:

        if actual_flow_read_back_message != FlowConditionCardConstants.OffReadbackMessage:
            actual_read_back_units = dashboard_screen_page.get_current_flow_units()
            start_time = time.time()
            while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
                actual_flow_read_back_message = dashboard_screen_page.get_current_flow()
                actual_flow_read_back_message = TypeConverter.to_float(actual_flow_read_back_message)
                expected_flow_read_back_message = TypeConverter.to_float(expected_flow_rate)
                current_flow_state = dashboard_screen_page.is_flow_on(
                    DashBoardsScreenPageLocators.FLOW_PATH_SCHEMATIC_ICON)

                if actual_flow_read_back_message == expected_flow_read_back_message:
                    break
                time.sleep(.1)
            assert current_flow_state is True, f"The state of flow in the schematic icon is False"
            assert actual_read_back_units == FlowConditionCardConstants.FlowUnits
            assert actual_flow_read_back_message == expected_flow_read_back_message, f"The actual flow read back message is {actual_flow_read_back_message}"

        else:
            assert current_flow_state is False, f"The state of flow in the schematic icon is False"
            assert actual_flow_read_back_message == expected_flow_rate, f"The actual flow read back message is {actual_flow_read_back_message}"

    finally:
        dashboard_screen_page.tap_solvent_manager_schematic_icon()


@when(cfparse('The user sets the flow rate as "{new_flow_rate}"'))
def enter_flow_rate(flow_setting_screen_page: FlowSettingsScreen, new_flow_rate):
    flow_setting_screen_page.tap_toggle_button_on()
    flow_setting_screen_page.clear_num_pad_entries(fct.FLOW_RATE_EDIT_FIELD)
    flow_setting_screen_page.enter_flow_rate(new_flow_rate)


@then(cfparse('The user validates "{expected_flow_rate}" is not affected by the hide/show of the edit field'))
def validate_edit_field(flow_setting_screen_page: FlowSettingsScreen, expected_flow_rate):
    time.sleep(1)
    try:
        actual_flow_rate = flow_setting_screen_page.get_flow_rate()
        actual_flow_rate = TypeConverter.to_float(actual_flow_rate)
        expected_flow_rate = TypeConverter.to_float(expected_flow_rate)

        assert actual_flow_rate == expected_flow_rate, f" The actual flow rate ==>>{actual_flow_rate}"
    finally:
        flow_setting_screen_page.tap_cancel_button()


@when('The user hides the flow edit field')
def turn_edit_field_off(flow_setting_screen_page: FlowSettingsScreen):
    flow_value = "Off"
    flow_setting_screen_page.select_flow(flow_value)


@when('User taps the default flow button')
def tap_defualt_flow_button(flow_setting_screen_page: FlowSettingsScreen):
    flow_setting_screen_page.tap(FlowControlTabScreen.FLOW_DEFAULT_VALUE_BUTTON)


@then('Validate the edit field and numpad is in hidden state')
def validate_edit_field_and_numpad_hidden_state(flow_setting_screen_page: FlowSettingsScreen):
    time.sleep(1)
    try:
        start_time = time.time()
        while time.time() - start_time < 5:
            numpad_exists = flow_setting_screen_page.is_numpad_exists()
            logger.info(f"numpad_exists====> {numpad_exists}")
            edit_field_exists = flow_setting_screen_page.is_displayed(
                FlowControlTabScreen.FLOW_RATE_EDIT_FIELD)
            logger.info(f"edit_field_exists====> {edit_field_exists}")

            # Both numpad and edit field should stay hidden when the user tap the apply button
            # for the Off" flow option
            if not numpad_exists and not edit_field_exists:
                break
            time.sleep(1)
        assert not edit_field_exists, f"The edit field is not hidden"
        assert not numpad_exists, f"The numpad is not hidden"

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then('validate the numpad is in inactive state')
def validate_numpad_inactive_state(flow_setting_screen_page: FlowSettingsScreen):
    try:
        start_time = time.time()
        while time.time() - start_time < 5:
            numpad_active = flow_setting_screen_page.is_enabled(BasePageLocators.NUM_PAD_1_BUTTON)
            if numpad_active is False:
                break
            time.sleep(1)
        assert numpad_active is False, f"The numpad is not inactive"

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then(cfparse('Validate the flow edit field shows "{error_state}"'))
def validate_error_state(flow_setting_screen_page: FlowSettingsScreen, error_state):
    try:
        edit_field_error_state = flow_setting_screen_page.is_flow_edit_field_in_error_state()
        error_state = TypeConverter.to_bool(error_state)
        assert edit_field_error_state == error_state, f" actual edit field error state is ==>> {edit_field_error_state}"
    finally:
        flow_setting_screen_page.tap_cancel_button()


@then(cfparse('User validates the default button disabled is "{is_button_disabled}"'))
def validate_default_flow_button_visibility(flow_setting_screen_page: FlowSettingsScreen, is_button_disabled):
    try:
        flow_setting_screen_page.validate_flow_settings_screen()
        assert TypeConverter.to_bool(is_button_disabled) == flow_setting_screen_page.is_disabled(
            FlowControlTabScreen.FLOW_DEFAULT_VALUE_BUTTON)

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then('The user validates the done button is inactive')
def validate_apply_and_done_button_inactive_state(flow_setting_screen_page: FlowSettingsScreen):
    try:
        flow_setting_screen_page.validate_button_inactive_state(BasePageLocators.DONE_BUTTON)

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then('validate the numpad is in active state')
def validate_edit_field_and_numpad_active_state(flow_setting_screen_page: FlowSettingsScreen):
    time.sleep(1)
    try:
        start_time = time.time()
        while time.time() - start_time < 5:
            numpad_exists = flow_setting_screen_page.is_numpad_exists()
            logger.info(f"numpad_exists====> {numpad_exists}")

            # Both numpad and edit field should stay hidden when the user tap the apply button
            # for the Off" flow option
            if not numpad_exists:
                break
            time.sleep(1)

        assert numpad_exists, f"The numpad is hidden"

    finally:
        flow_setting_screen_page.tap_cancel_button()


@then("User validates the hint messages for the flow")
def validate_flow_helper_message(flow_setting_screen_page: FlowSettingsScreen):
    time.sleep(2)
    try:
        hint_locator = fct.FLOW_HINT_LOCATOR
        expected_hint_message = SolventCompositionConditionCardConstants.FlowHintMessage
        flow_setting_screen_page.validate_hint_message(hint_locator, expected_hint_message)

    finally:
        flow_setting_screen_page.tap_cancel_button()


@when('Tap the toggle button to turn off the flow')
def turn_off_toggle_button(flow_setting_screen_page: FlowSettingsScreen):
    start_time = time.time()
    while time.time() - start_time < 5:
        toggle_button_enabled = flow_setting_screen_page.is_toggle_button_enabled(
            FlowControlTabScreen.FLOW_TOGGLE_BUTTON)
        if toggle_button_enabled:
            logger.info(f"The status of the toggle button ==> {toggle_button_enabled}")
            flow_setting_screen_page.tap_toggle_button()
        else:
            logger.info(f"The status of the toggle button before exiting loop ==> {toggle_button_enabled}")
            break
        time.sleep(1)
    assert toggle_button_enabled is False, 'Toggle button is switched on'


@then('The user validate the flow is turned OFF')
def validate_flow_rate_off(solvent_manager_home_screen_page: SolventManagerHomeScreen, dashboard_screen_page: DashBoardScreen):
    try:
        start_time = time.time()
        while time.time() - start_time < FlowConditionCardConstants.MaxTimeToachieveFlowRate:
            actual_read_back_message = solvent_manager_home_screen_page.get_current_flow_read_back_message()
            if actual_read_back_message == FlowConditionCardConstants.OffReadbackMessage:
                break
            time.sleep(1)
        assert actual_read_back_message == FlowConditionCardConstants.OffReadbackMessage, \
            f"actual_read_back_message=====>>>>>>>{actual_read_back_message}"
        logger.info(f" actual_read_back_message===>{actual_read_back_message} ")

    finally:
        dashboard_screen_page.tap_home()
