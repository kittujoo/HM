import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.commands import CommandsConstants
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.commands_screen_locators import CommandsScreenPageLocators


if __name__ == Path(__file__).stem:
    scenarios('../../features/CommandScreen/commands_screen.feature')
logger = Logger("test_commands_screen")


@pytest.fixture
def command_screen_page(dashboard_screen_page: DashBoardScreen, page_builder):
    dashboard_screen_page.tap_commands()
    # animation for fly-out menu
    time.sleep(4)
    page = page_builder(CommandsScreen)
    return page


@when('User taps the flow button to turn on the flow')
def tap_resume_flow(command_screen_page: CommandsScreen):
    command_screen_page.turn_flow_on()


@when(cfparse('Flow is "{current_flow_control}"'))
def set_flow_control(current_flow_control, command_screen_page: CommandsScreen):
    command_screen_page.select_flow(current_flow_control)


@when(cfparse('User taps the flow button to set flow to "{new_flow_control}"'))
def set_new_flow_control(new_flow_control, command_screen_page: CommandsScreen):
    command_screen_page.select_flow(new_flow_control)


@when('User verifies the flowing state is True')
def validate_flow_on(dashboard_screen_page: DashBoardScreen):
    try:
        dashboard_screen_page.tap_commands()
        dashboard_screen_page.tap_home()
        assert dashboard_screen_page.get_flow_state() is True

    finally:
        dashboard_screen_page.tap_commands()


@then('User verifies the flowing state is False')
def validate_flow_off(dashboard_screen_page: DashBoardScreen, assert_timeout: AssertTimeout):
    try:
        dashboard_screen_page.tap_commands()
        dashboard_screen_page.tap_home()
        assert_timeout.are_equal(lambda: dashboard_screen_page.get_flow_state() , False, "The flow is not Off", timeout_in_seconds=WaitTimeConstants.SmallWait, polling_period_in_seconds=1)                                     
    
    finally:
        dashboard_screen_page.tap_commands()


@then(cfparse('Kiosk Commands page shows flow control "{new_flow_control}"'))
def validate_flow_control(new_flow_control, command_screen_page: CommandsScreen):
    command_screen_page.validate_flow_control(new_flow_control)


@then(cfparse('User verifies the "{flowing_state:bool}"', CONVERTERS))
def validate_flow_state(flowing_state: bool, dashboard_screen_page: DashBoardScreen):
    try:
        dashboard_screen_page.tap_commands()
        dashboard_screen_page.tap_home()
        assert dashboard_screen_page.get_flow_state() is flowing_state

    finally:
        dashboard_screen_page.tap_commands()


@when(cfparse('Detector lamp is "{current_lamp_state}"'))
def set_lamp_state(current_lamp_state, command_screen_page: CommandsScreen):
    time.sleep(CommandsConstants.CommandsSlideAnimationTime)  # sleep time added for left navigation menu animation
    command_screen_page.select_lamp(current_lamp_state)


@when(cfparse('User taps the detector lamp button to set lamp to "{new_lamp_state}"'))
def set_new_lamp_state(new_lamp_state, command_screen_page: CommandsScreen):
    time.sleep(CommandsConstants.CommandsSlideAnimationTime)  # sleep time added for left navigation menu animation
    command_screen_page.select_lamp(new_lamp_state)


@then(cfparse('Kiosk Commands page shows detector lamp "{new_lamp_state}"'))
def validate_commands_page_lamp_state(new_lamp_state, dashboard_screen_page: DashBoardScreen):
    new_lamp_state = new_lamp_state.lower()

    if new_lamp_state == CommandsConstants.LampOnRequest:
        try:
            locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT
            expected_condition = CommandsConstants.LampOnReadBackMessage
            error_message = "The lamp is not ON"
            wait_time = CommandsConstants.LampWarmingTime
            dashboard_screen_page.wait_till_condition_met(locator, expected_condition, error_message, wait_time)
        finally:
            dashboard_screen_page.tap_home()

    else:
        try:
            locator = CommandsScreenPageLocators.UV_LAMP_COMMAND_BUTTON_TEXT
            expected_condition = CommandsConstants.LampOffReadBackMessage
            error_message = "The lamp is not OFF"
            wait_time = CommandsConstants.LampTurnOffTime
            dashboard_screen_page.wait_till_condition_met(locator, expected_condition, error_message, wait_time)
        finally:
            dashboard_screen_page.tap_home()


@when('User taps the commands page button')
def tap_commands_page_button(dashboard_screen_page: DashBoardScreen):
    time.sleep(CommandsConstants.CommandsSlideAnimationTime)  # sleep time added for left navigation menu animation
    dashboard_screen_page.tap_commands()


@then(cfparse('User Verifies the UV lamp is "{new_lamp_state}" on the dashboard'))
def validate_dashboard_lamp_state(new_lamp_state, dashboard_screen_page: DashBoardScreen):
    current_lamp_state = dashboard_screen_page.get_lamp_state()
    current_lamp_state = current_lamp_state.lower()
    new_lamp_state = new_lamp_state.lower()
    assert current_lamp_state == new_lamp_state, f"current_lamp_state= {current_lamp_state}"


@when('User taps the emergency stop button')
def hold_estop_button(command_screen_page: CommandsScreen):
    command_screen_page.start_emergency_stop()


@when('User taps the reset button')
def tap_reset_button(command_screen_page: CommandsScreen):
    command_screen_page.tap_reset()


@then('User verify the system is reset')
def verify_reset(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_resetting_state()


@then('User validates Kiosk page shows IDLE state')
def validate_kiosk_idle_state(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_idle_state()
