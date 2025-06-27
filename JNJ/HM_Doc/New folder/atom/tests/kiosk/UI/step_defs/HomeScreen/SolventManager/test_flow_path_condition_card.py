import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.logger import Logger
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants as wait
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SolventManager.flow_path_settings_screen import FlowPathSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.sm_home_screen import SolventManagerHomeScreenLocators as sml

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/flow_path_condition_card.feature')

logger = Logger("test_flow_path_condition_card")


@pytest.fixture
def flow_path_settings_screen_page(page_builder):
    page = page_builder(FlowPathSettingsScreen)
    page.implicitly_wait()
    return page


@given('User navigates to the third solvent manager page')
def navigate_solvent_manager_third_page(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    logger.info("**************************The flow path condition card test starts**********************")
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap_third_page()


@when('User navigates to the flow path settings screen')
def navigate_flow_path_card(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                            flow_path_settings_screen_page: FlowPathSettingsScreen):
    solvent_manager_home_screen_page.tap_flow_path_conditional_card()
    flow_path_settings_screen_page.validate_flow_path_settings_screen()


@when(cfparse('User taps the "{flow_path}"'))
def tap_flow_path_option(flow_path_settings_screen_page, flow_path):
    flow_path_settings_screen_page.validate_flow_path_settings_screen()
    logger.info(f"Selecting the following flow path========>>>>>>{flow_path}")
    flow_path_settings_screen_page.tap_flow_path(flow_path)


@then(cfparse('User validates the "{flow_path}" was changed'))
def validate_flow_path(solvent_manager_home_screen_page: SolventManagerHomeScreen, flow_path):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen_page_three()
    solvent_manager_home_screen_page.validate_simple_text_wait_condition(sml.DISPLAYED_FLOW_PATH, flow_path, wait.SmallWait)


@then('User returns to the solvent manager home screen')
def navigate_sm_home_screen(session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.tap_solvent_manager_schematic_icon()


@then(cfparse('User validates the "{expected_flow_path}" is unchanged'))
def validate_flow_path_cancellation(solvent_manager_home_screen_page: SolventManagerHomeScreen, expected_flow_path):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen_page_three()
    solvent_manager_home_screen_page.validate_simple_text_wait_condition(sml.DISPLAYED_FLOW_PATH, expected_flow_path, wait.SmallWait)


@when('User confirms the flow path change')
def tap_done_button(flow_path_settings_screen_page: FlowPathSettingsScreen):
    flow_path_settings_screen_page.tap_done_button()


@when('User cancels the flow path change')
def tap_cancel_button(flow_path_settings_screen_page: FlowPathSettingsScreen):
    flow_path_settings_screen_page.tap_cancel_button()
