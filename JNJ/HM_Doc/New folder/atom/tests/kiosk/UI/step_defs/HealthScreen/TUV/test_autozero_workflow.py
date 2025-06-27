import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from utilities.logger import Logger
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.TUV.autozero_workflow_screen import AutozeroWorkflowSetupScreen
from web_framework.kiosk.pages.Health.health_home_screen import HealthHomeScreen
from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.Locators.Health.TUV.autozero_workflow_locators import AutozeroWorkflowLocators
from web_framework.kiosk.pages.Locators.Health.health_screen_locators import HealthScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HealthScreen/TUV/autozero_workflow.feature')
logger = Logger("test_noise_drift_workflow")


@pytest.fixture
def autozero_screen(page_builder):
    page = page_builder(AutozeroWorkflowSetupScreen)
    return page


@given("the lamp is On")
def set_lamp_state_on(session_dash_board_screen_page: DashBoardScreen, command_screen_page: CommandsScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    lamp_state = session_dash_board_screen_page.get_lamp_state()    
    if lamp_state == "Off":
        session_dash_board_screen_page.tap_commands()
        command_screen_page.turn_on_lamp()   


@when("User navigates to health troubleshoot area")
def navigate_troubleshoot_tuv(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.TROUBLESHOOT_PANEL)


@when("User navigates to TUV section")
def navigate_instrument_diagnostic(instrument_diagnostic_page: InstrumentDiagnosticScreen):
    instrument_diagnostic_page.tap(HealthScreenLocators.TUV_SECTION_ICON)


@when("User taps Autozero Offsets panel")
def start_noise_drift_workflow(health_screen_page: HealthHomeScreen):
    health_screen_page.tap(HealthScreenLocators.AUTOZERO_START_PANEL)


@when("User validates the Information autozero offsets screen")
def validate_autozero_screen(autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.validate_autozero_screen()


@when("User taps autozero button")
def tap_autozero_button(autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.tap(AutozeroWorkflowLocators.AUTOZERO_BUTTON)


@when("User taps reset button")
def tap_reset_button(autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.tap(AutozeroWorkflowLocators.RESET_BUTTON)


@then("User validates that the Channel A Offset and Channel B Offset displayed values are zero")
def validate_reset_function(autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.validate_channel_reset_values()


@then("User validates that the Channel A Offset and Channel B Offset displayed values are non-zero")
def validate_autozero_function(autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.validate_channel_autozero_values()


@then("User navigates to home area")
def navigate_home(dashboard_screen_page: DashBoardScreen, autozero_screen: AutozeroWorkflowSetupScreen):
    autozero_screen.tap(AutozeroWorkflowLocators.BACK_BUTTON)
    dashboard_screen_page.tap_home()


@then("User validates the Channel Offset value is zero")
def validate_absorbance_values(session_dash_board_screen_page: DashBoardScreen):
    channel_a_absorbance = session_dash_board_screen_page.get_channel_a_absorbance_value()
    channel_a_absorbance = float(channel_a_absorbance)
    # TODO: Add channel b check when available INSISPP-8103
    assert channel_a_absorbance == 0.0000, f"Absorbance A: {channel_a_absorbance} does not equal 0.0000"


@then("User validates the Channel Offset value is non-zero")
def validate_absorbance_values(session_dash_board_screen_page: DashBoardScreen):
    channel_a_absorbance = session_dash_board_screen_page.get_channel_a_absorbance_value()
    channel_a_absorbance = float(channel_a_absorbance)
    # TODO: Add channel b check when available INSISPP-8103
    assert channel_a_absorbance != 0.0000, f"Absorbance A: {channel_a_absorbance} equals 0.0000"
