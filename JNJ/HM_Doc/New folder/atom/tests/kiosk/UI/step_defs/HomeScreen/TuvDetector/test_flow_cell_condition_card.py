import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Home.TuvDetector.uv_lamp_settings_screen import UVLampSettingsScreen
from web_framework.kiosk.pages.Locators.Home.TuvDetector.flow_cell_condition_card_locators import FlowCellConditionCardLocators
from web_framework.kiosk.pages.Locators.Home.TuvDetector.tuv_home_screen import TUVHomeScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/TuvDetector/flow_cell_condition_card.feature')

logger = Logger(__name__)


@pytest.fixture
def flow_cell_condition_card_settings_screen(session_dash_board_screen_page: DashBoardScreen,
                                             tuv_detector_home_screen_page: TUVDetectorHomeScreen, page_builder):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_tuv_schematic_icon()
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    tuv_detector_home_screen_page.tap(TUVHomeScreenLocators.FLOW_CELL_CONDITIONAL_CARD)
    page = page_builder(UVLampSettingsScreen)
    return page


@given('User is at the flow cell settings screen')
def validate_uv_lamp_settings_screen(flow_cell_condition_card_settings_screen):
    flow_cell_condition_card_settings_screen.validate_flow_cell_configuration_screen()


@when('User navigates to the actions tab')
def navigate_actions_tab(flow_cell_condition_card_settings_screen):
    flow_cell_condition_card_settings_screen.tap(FlowCellConditionCardLocators.ACTIONS_NAV_BUTTON)


@when('User navigates to the details tab')
def navigate_details_tab(flow_cell_condition_card_settings_screen):
    flow_cell_condition_card_settings_screen.tap(FlowCellConditionCardLocators.DETAILS_NAV_BUTTON)
