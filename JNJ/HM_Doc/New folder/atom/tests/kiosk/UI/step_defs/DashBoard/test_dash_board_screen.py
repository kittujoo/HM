from pathlib import Path
import pytest
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_manager_home_screen import ColumnManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Home.SolventBottle.solvent_bottle_home_screen import SolventBottleHomeScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
from web_framework.kiosk.pages.UserProfileSettings.user_profile_hub_screen import UserProfileHubScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/DashBoard/dash_board_screen.feature',
              '../../features/DashBoard/schematic_icon.feature')


@pytest.fixture
def solvent_manager_home_screen(page_builder):
    page = page_builder(SolventManagerHomeScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def sample_manager_home_screen(page_builder):
    page = page_builder(SampleManagerHomeScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def column_home_screen(page_builder):
    page = page_builder(ColumnManagerHomeScreen)
    page.implicitly_wait()
    return page


@given(cfparse('The user taps the "{icon_selected}" icon'))
def select_navigation_icon(icon_selected: str, session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.select_icon(icon_selected)


@then('the dashboard home page is displayed')
def dashboard_page_is_displayed(session_dash_board_screen_page: DashBoardScreen):
    assert session_dash_board_screen_page.is_home_icon_displayed(), \
        "Expected to find the home icon on the Dashboard Page but it was not found"


@when(cfparse('The user taps the "{icon_selected}" icon'))
def select_icon(icon_selected: str, session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.select_icon(icon_selected)


@when('User taps the home icon')
def tap_home_icon(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_home()
    dashboard_screen_page.validate_top_level_dashboard()


@when('User opens kiosk app')
def select_user_settings(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()


@when('The user taps on the user settings icon')
def select_user_settings(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap(DashBoardsScreenPageLocators.USER_SETTINGS)


@when('The user cancels the settings')
def select_user_settings(user_profile_hub_screen_page: UserProfileHubScreen):
    user_profile_hub_screen_page.validate_user_hub_screen()
    user_profile_hub_screen_page.tap_done_button()


@then('User taps on the solvent manager schematic icon')
@when('User taps on the solvent manager schematic icon')
def tap_solvent_schematic_icon(dashboard_screen_page: DashBoardScreen, solvent_manager_home_screen: SolventManagerHomeScreen):
    dashboard_screen_page.tap_solvent_manager_schematic_icon()
    solvent_manager_home_screen.validate_solvent_manager_home_screen()


@when('User taps on the sample manager schematic icon')
@then('User taps on the sample manager schematic icon')
def tap_sample_schematic_icon(dashboard_screen_page: DashBoardScreen, sample_manager_home_screen: SampleManagerHomeScreen):
    dashboard_screen_page.tap_sample_manager_schematic_icon()
    sample_manager_home_screen.validate_sample_manager_home_screen()


@then('User taps on the tuv schematic icon')
@when('User taps on the tuv schematic icon')
def tap_tuv_schematic_icon(dashboard_screen_page: DashBoardScreen, tuv_detector_home_screen_page: TUVDetectorHomeScreen):
    dashboard_screen_page.tap_tuv_schematic_icon()
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()


@when('User taps on the column manager schematic icon')
@then('User taps on the column manager schematic icon')
def tap_column_schematic_icon(dashboard_screen_page: DashBoardScreen, column_home_screen: ColumnManagerHomeScreen):
    dashboard_screen_page.tap_column_manager_schematic_icon()
    column_home_screen.validate_column_manager_home_screen()


@when('User taps on the solvent bottle schematic icon')
def tap_solvent_bottle_schematic_icon(solvent_bottles_home_screen: SolventBottleHomeScreen, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_solvent_bottle_icon()
    solvent_bottles_home_screen.validate_mobile_phase_home_screen()


@then('User validates the solvent bottle schematic icon is highlighted')
def validate_solvent_bottle_schematic_highlight(dashboard_screen_page: DashBoardScreen, solvent_manager_home_screen: SolventManagerHomeScreen):
    element_background_color = solvent_manager_home_screen.get_element_background_color(TopLevelDashBoardScreenLocators.BOTTLE_ICON_MIN)
    dashboard_screen_page.validate_white_background(element_background_color)


@then('User validates the solvent manager schematic icon is highlighted')
def validate_solvent_bottle_schematic_highlight(dashboard_screen_page: DashBoardScreen, solvent_manager_home_screen: SolventManagerHomeScreen):
    element_background_color = solvent_manager_home_screen.get_element_background_color(TopLevelDashBoardScreenLocators.SOLVENT_ICON_MIN)
    dashboard_screen_page.validate_white_background(element_background_color)


@then('User validates the sample manager schematic icon is highlighted')
def validate_solvent_bottle_schematic_highlight(dashboard_screen_page: DashBoardScreen, sample_manager_home_screen: SampleManagerHomeScreen):
    element_background_color = sample_manager_home_screen.get_element_background_color(TopLevelDashBoardScreenLocators.SAMPLE_ICON_MIN)
    dashboard_screen_page.validate_white_background(element_background_color)


@then('User validates the column manager schematic icon is highlighted')
def validate_solvent_bottle_schematic_highlight(dashboard_screen_page: DashBoardScreen, column_home_screen: ColumnManagerHomeScreen):
    element_background_color = column_home_screen.get_element_background_color(TopLevelDashBoardScreenLocators.COLUMN_ICON_MIN)
    dashboard_screen_page.validate_white_background(element_background_color)


@then('User validates the tuv schematic icon is highlighted')
def validate_solvent_bottle_schematic_highlight(dashboard_screen_page: DashBoardScreen, tuv_detector_home_screen_page: TUVDetectorHomeScreen):
    element_background_color = tuv_detector_home_screen_page.get_element_background_color(TopLevelDashBoardScreenLocators.COLUMN_ICON_MIN)
    dashboard_screen_page.validate_white_background(element_background_color)


@then('User validates none of the schematic icons are highlighted')
def validate_no_icon_highlights(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_default_icon_highlight()


@then(cfparse('The "{icon_selected}" should not be highlighted'))
def validate_inactive_icon(icon_selected: str, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.validate_inactive_icon(icon_selected)


@then(cfparse('The "{expected_icon}" should be highlighted'))
def validate_active_icon(expected_icon: str, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.validate_active_icon(expected_icon)


@then('User confirms the error state in the dashboard')
def validate_error_state(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_error_state()
