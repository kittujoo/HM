import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.solvent_bottles import SolventLineColorsConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from utilities.datatables.converters import CONVERTERS
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.solvent_bottle_configuration_screen_locators import \
    SolventBottleConfigurationScreenLocators
from web_framework.kiosk.pages.System.SolventBottlesManager.mobile_phase_configuration_settings_screen import MobilePhaseConfigurationSettingsScreen
from web_framework.kiosk.pages.System.SolventBottlesManager.solvent_configuration_screen import SolventConfigurationScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/mobile_phase_solvent_configuration.feature')
logger = Logger("mobile_phase_solvent_configuration_settings_screen")


@pytest.fixture
def instrument_configuration_screen(page_builder):
    page = page_builder(InstrumentConfigurationScreen)
    return page


@pytest.fixture
def solvent_configuration_screen(page_builder):
    page = page_builder(SolventConfigurationScreen)
    return page


@pytest.fixture
def mobile_phase_configuration_settings_screen(page_builder):
    page = page_builder(MobilePhaseConfigurationSettingsScreen)
    return page


@when('User taps System - Module Configuration - Solvents')
def navigate_to_solvents(system_settings_screen: SystemSettingsScreen, session_dash_board_screen_page: DashBoardScreen,
                         instrument_configuration_screen: InstrumentConfigurationScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_module_configuration_tab()
    instrument_configuration_screen.validate_instrument_configuration_screen()
    instrument_configuration_screen.tap_bottle_icon()


@when('User taps Mobile Phase Configuration screen')
def tap_mobile_phase_panel(solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.tap(SolventBottleConfigurationScreenLocators.MOBILE_PHASE_PANEL)


@when('User taps Wash Solvent Configuration screen')
def tap_mobile_phase_panel(solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.tap(SolventBottleConfigurationScreenLocators.WASH_SOLVENTS_PANEL)


@when(cfparse('User selects the mobile phase "{mobile_phase}" tab'))
def select_mobile_phase(mobile_phase, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.validate_mobile_phase_settings_screen()
    mobile_phase_configuration_settings_screen.tap_mobile_phase_tab(mobile_phase)


@when(cfparse('User selects the "{wash_solvent}" tab'))
def select_mobile_phase(wash_solvent, solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.validate_solvent_configuration_screen()
    solvent_configuration_screen.tap_solvent_phase_tab(wash_solvent)


@when(cfparse('User toggles the "{mobile_phase}" toggle to "{toggle_status}"'))
def set_toggle(mobile_phase, toggle_status, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.set_toggle_status(mobile_phase, toggle_status)


@when(cfparse('User toggles the solvent "{wash_solvent}" toggle to "{toggle_status}"'))
def set_solvent_toggle(wash_solvent, toggle_status, solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.set_toggle_status(wash_solvent, toggle_status)


@when(cfparse('User selects the "{bottle_volume}" volume for "{mobile_phase}"'))
def set_bottle_volume(bottle_volume, mobile_phase, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.select_bottle_volume(mobile_phase, bottle_volume)


@when(cfparse('User selects the solvent "{bottle_volume}" volume for "{wash_solvent}"'))
def set_solvent_bottle_volume(bottle_volume, wash_solvent, solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.select_bottle_volume(wash_solvent, bottle_volume)


@when(cfparse('User selects the "{line_color}" color for "{mobile_phase}"'))
def set_color(line_color, mobile_phase, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.select_line_color(mobile_phase, line_color)


@when(cfparse('User selects the solvent "{line_color}" color for "{wash_solvent}"'))
def set_color(line_color, wash_solvent, solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.select_line_color(wash_solvent, line_color)


@when(cfparse('User selects "{color}" color for all mobile phases'))
def set_all_color(color, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.set_color_for_mobile_phase("A", color)
    mobile_phase_configuration_settings_screen.set_color_for_mobile_phase("B", color)
    mobile_phase_configuration_settings_screen.set_color_for_mobile_phase("C", color)
    mobile_phase_configuration_settings_screen.set_color_for_mobile_phase("D", color)


@when(cfparse('User selects "{color}" color for all solvent phases'))
def set_all_color(color, solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.set_color_for_wash_solvent("Needle_Wash", color)
    solvent_configuration_screen.set_color_for_wash_solvent("Seal_Wash", color)


@when('User cancels the setting')
def tap_cancel(mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.tap_cancel_button()


@when('User cancels the setting to default')
def tap_cancel(mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.cancel_reset()


@when('User taps set all to default color')
def set_default(mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.set_default_color("A")


@when('User taps set all to default solvent color')
def set_solvent_default(solvent_configuration_screen: SolventConfigurationScreen):
    solvent_configuration_screen.set_default_color("Needle_Wash")


@when('User taps Reset button')
def tap_reset(mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.tap_reset_button()


@then('User confirms the changes')
def save_change(mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    mobile_phase_configuration_settings_screen.tap_done_button()


@then(cfparse('User verifies the "{mobile_phase}" toggle is "{expected_status:bool}"', CONVERTERS))
def validate_toggle(mobile_phase, expected_status, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    status = mobile_phase_configuration_settings_screen.get_toggle_status(mobile_phase)
    assert status == expected_status, f"Toggle is not in expected state. Expected:{expected_status} Actual:{status}"


@then(cfparse('User verifies the solvent "{wash_solvent}" toggle is "{expected_status:bool}"', CONVERTERS))
def validate_solvent_toggle(wash_solvent, expected_status, solvent_configuration_screen: SolventConfigurationScreen):
    status = solvent_configuration_screen.get_toggle_status(wash_solvent)
    assert status == expected_status, f"Toggle is not in expected state. Expected:{expected_status} Actual:{status}"


@then(cfparse('User verifies "{bottle_volume}" and "{line_color}" were saved for "{mobile_phase}"'))
def validate_data(bottle_volume, line_color, mobile_phase, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    actual_volume = mobile_phase_configuration_settings_screen.get_volume(mobile_phase)
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color(mobile_phase)
    assert actual_line_color == getattr(SolventLineColorsConstants, line_color), f"The actual line color selected is not the same in {mobile_phase}"
    assert actual_volume == bottle_volume, f"The actual volume selected is not the same in {mobile_phase}"


@then(cfparse('User verifies "{bottle_volume}" and "{line_color}" were saved for solvent "{wash_solvent}"'))
def validate_data(bottle_volume, line_color, wash_solvent, solvent_configuration_screen: SolventConfigurationScreen):
    actual_volume = solvent_configuration_screen.get_volume(wash_solvent)
    actual_line_color = solvent_configuration_screen.get_line_color(wash_solvent)
    assert actual_line_color == getattr(SolventLineColorsConstants, line_color), f"The actual line color selected is not the same in {wash_solvent}"
    assert actual_volume == bottle_volume, f"The actual volume selected is not the same in {wash_solvent}"


@then(cfparse('User validate the "{mobile_phase}" line color was set to "{color}"'))
def validate_default(mobile_phase, color, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color(mobile_phase)
    assert actual_line_color == getattr(SolventLineColorsConstants, color), f"The actual line color selected is not the same in {mobile_phase}"


@then(cfparse('User validate the solvent "{wash_solvent}" line color was set to "{color}"'))
def validate_solvent_default(wash_solvent, color, solvent_configuration_screen: SolventConfigurationScreen):
    actual_line_color = solvent_configuration_screen.get_line_color(wash_solvent)
    assert actual_line_color == getattr(SolventLineColorsConstants, color), f"The actual line color selected is not the same in {wash_solvent}"


@then(cfparse('User validates the line colors "{color}"'))
def validate_all_colors(color, mobile_phase_configuration_settings_screen: MobilePhaseConfigurationSettingsScreen):
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color("A")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in A"
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color("B")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in B"
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color("C")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in C"
    actual_line_color = mobile_phase_configuration_settings_screen.get_line_color("D")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in D"


@then(cfparse('User validates the solvent line colors "{color}"'))
def validate_all_colors(color, solvent_configuration_screen: SolventConfigurationScreen):
    actual_line_color = solvent_configuration_screen.get_line_color("Needle_Wash")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in Needle_Wash"
    actual_line_color = solvent_configuration_screen.get_line_color("Seal_Wash")
    assert actual_line_color == getattr(SolventLineColorsConstants, color), "The actual line color selected is not the same in Seal_Wash"
