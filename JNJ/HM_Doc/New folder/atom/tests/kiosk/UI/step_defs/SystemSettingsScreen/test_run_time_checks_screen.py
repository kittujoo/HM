import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.Administration.run_time_checks_screen_locators import RunTimeChecksScreenLocators
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.solvent_bottle_configuration_screen_locators import \
    SolventBottleConfigurationScreenLocators
from web_framework.kiosk.pages.System.Administration.administration_screen import AdministrationScreen
from web_framework.kiosk.pages.System.Administration.run_time_checks_screen import RunTimeChecksScreen
from web_framework.kiosk.pages.System.SolventBottlesManager.mobile_phase_configuration_settings_screen import MobilePhaseConfigurationSettingsScreen
from web_framework.kiosk.pages.System.SolventBottlesManager.solvent_configuration_screen import SolventConfigurationScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/run_time_checks_screen.feature')

logger = Logger(__name__)


@pytest.fixture
def solvent_configuration_screen(page_builder):
    page = page_builder(SolventConfigurationScreen)
    return page


@pytest.fixture
def mobile_phase_configuration_screen(page_builder):
    page = page_builder(MobilePhaseConfigurationSettingsScreen)
    return page


@pytest.fixture
def administration_screen(page_builder):
    page = page_builder(AdministrationScreen)
    return page


@pytest.fixture
def run_time_checks_screen(page_builder):
    page = page_builder(RunTimeChecksScreen)
    return page


@given('User navigates to system screen')
def navigate_to_system_screen(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()


@given('User navigates to the Solvents system settings')
def navigate_to_solvents_system_settings(system_settings_screen: SystemSettingsScreen, instrument_configuration_screen: InstrumentConfigurationScreen):
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_module_configuration_tab()
    instrument_configuration_screen.validate_instrument_configuration_screen()
    instrument_configuration_screen.tap_bottle_icon()


@when('User configures the mobile phase and wash solvent')
def configure_solvent(instrument_configuration_screen: InstrumentConfigurationScreen, solvent_configuration_screen: SolventConfigurationScreen,
                      mobile_phase_configuration_screen: MobilePhaseConfigurationSettingsScreen, dashboard_screen_page: DashBoardScreen):
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.MOBILE_PHASE_PANEL)
    mobile_phase_configuration_screen.validate_mobile_phase_settings_screen()
    mobile_phase_configuration_screen.set_toggle_status('A', True)
    mobile_phase_configuration_screen.tap_done_button()
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.WASH_SOLVENTS_PANEL)
    solvent_configuration_screen.validate_solvent_configuration_screen()
    solvent_configuration_screen.set_toggle_status('Needle_Wash', True)
    solvent_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@when('User navigates to the Administration tab')
def navigate_to_administration_tab(system_settings_screen: SystemSettingsScreen):
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_administration_tab()


@when('User navigates to the Acquisition checks tab')
def navigate_to_acquisition_checks_tab(administration_screen: AdministrationScreen):
    administration_screen.validate_administration_configuration_screen()
    administration_screen.tap_acquisition_checks_tab()


@when('User navigates to Run Time Checks tab')
def navigate_to_run_time_checks_tab(administration_screen: AdministrationScreen):
    administration_screen.validate_acquisition_checks_screen()
    administration_screen.tap_run_time_checks_tab()


@then('User validates the status of the mobile phase, wash solvent, leak detected, and vial missing toggles')
def validate_status_of_mobile_phase_wash_solvent_leak_detected_and_vial_missing_toggles(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    run_time_checks_screen.validate_run_time_checks_toggle_defaults()


@then('User validates leak is detected and vial is missing toggle buttons are not editable')
def validate_leak_is_detected_and_vial_is_missing_toggle_buttons_are_not_editable(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_leak_disabled_status = run_time_checks_screen.is_disabled(RunTimeChecksScreenLocators.LEAK_DETECTED_TOGGLE)
    actual_vial_disabled_status = run_time_checks_screen.is_disabled(RunTimeChecksScreenLocators.VIAL_MISSING_TOGGLE)
    assert actual_leak_disabled_status is True, \
        f"Expected Leak Detected disabled toggle status: True, Actual Leak Detected disabled toggle status: {actual_leak_disabled_status}"
    assert actual_vial_disabled_status is True, \
        f"Expected Vial Missing disabled toggle status: True, Actual Vial Missing disabled toggle status: {actual_vial_disabled_status}"


@then('User validates the low solvent limits is 10%')
def validate_low_solvent_limits_is_10_percent(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    assert run_time_checks_screen.is_displayed(RunTimeChecksScreenLocators.MOBILE_PHASE_10_PERCENT) is True
    assert run_time_checks_screen.is_displayed(RunTimeChecksScreenLocators.WASH_SOLVENT_10_PERCENT) is True


@when('User unconfigures all Mobile Phase solvent lines')
def unconfigure_all_mobile_phase_solvent_lines(instrument_configuration_screen: InstrumentConfigurationScreen, dashboard_screen_page: DashBoardScreen,
                                               mobile_phase_configuration_screen: MobilePhaseConfigurationSettingsScreen):
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.MOBILE_PHASE_PANEL)
    mobile_phase_configuration_screen.validate_mobile_phase_settings_screen()
    mobile_phase_configuration_screen.set_toggle_status('A', False)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('B')
    mobile_phase_configuration_screen.set_toggle_status('B', False)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('C')
    mobile_phase_configuration_screen.set_toggle_status('C', False)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('D')
    mobile_phase_configuration_screen.set_toggle_status('D', False)
    mobile_phase_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@then('User validates the mobile phase toggle button is disabled and not editable')
def validate_mobile_phase_toggle_button_is_disabled_and_not_editable(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_mobile_phase_disabled_status = run_time_checks_screen.is_disabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
    assert actual_mobile_phase_disabled_status is True, \
        f"Expected Mobile Phase disabled toggle status: True, Actual Mobile Phase disabled toggle status: {actual_mobile_phase_disabled_status}"


@when(cfparse(
    'User configures "{solvent_line_a_toggle}", "{solvent_line_b_toggle}", "{solvent_line_c_toggle}", "{solvent_line_d_toggle}" Mobile Phase solvent lines'))
def configure_mobile_phase_solvent_lines(instrument_configuration_screen: InstrumentConfigurationScreen, dashboard_screen_page: DashBoardScreen,
                                         mobile_phase_configuration_screen: MobilePhaseConfigurationSettingsScreen, solvent_line_a_toggle,
                                         solvent_line_b_toggle, solvent_line_c_toggle, solvent_line_d_toggle):
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.MOBILE_PHASE_PANEL)
    mobile_phase_configuration_screen.validate_mobile_phase_settings_screen()
    mobile_phase_configuration_screen.set_toggle_status('A', solvent_line_a_toggle)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('B')
    mobile_phase_configuration_screen.set_toggle_status('B', solvent_line_b_toggle)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('C')
    mobile_phase_configuration_screen.set_toggle_status('C', solvent_line_c_toggle)
    mobile_phase_configuration_screen.tap_mobile_phase_tab('D')
    mobile_phase_configuration_screen.set_toggle_status('D', solvent_line_d_toggle)
    mobile_phase_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@then('User validates the mobile phase toggle button is enabled')
def validate_mobile_phase_toggle_button_is_enabled(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_mobile_phase_enabled_status = run_time_checks_screen.is_enabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
    assert actual_mobile_phase_enabled_status is True, \
        f"Expected Mobile Phase enabled toggle status: True, Actual Mobile Phase enabled toggle status: {actual_mobile_phase_enabled_status}"


@when('User disables the mobile phase and wash solvent toggle buttons')
def disable_mobile_phase_and_wash_solvent_toggle_button(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    run_time_checks_screen.set_toggle_button(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE, False)
    run_time_checks_screen.set_toggle_button(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE, False)


@when('User sets the mobile phase and wash solvent toggles to the opposite configuration')
def set_mobile_phase_and_wash_solvent_toggles_to_opposite_configuration(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    mobile_phase_toggle_state = run_time_checks_screen.store_mobile_phase_state()
    wash_solvent_toggle_state = run_time_checks_screen.store_wash_solvent_state()
    run_time_checks_screen.set_toggle_button(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE, not mobile_phase_toggle_state)
    run_time_checks_screen.set_toggle_button(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE, not wash_solvent_toggle_state)


@when('User confirms the changes')
def confirm_changes(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.tap_done_button()


@when('User cancels the changes')
def cancel_changes(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.tap_cancel_button()


@then('User confirms the mobile phase and wash solvent toggle buttons are disabled')
def confirm_mobile_phase_and_wash_toggle_button_are_disabled(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_mobile_phase_enabled_status = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
    actual_wash_solvent_enabled_status = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
    assert actual_mobile_phase_enabled_status is False, \
        f"Expected Mobile Phase disabled toggle status: False, Actual Mobile Phase disabled toggle status: {actual_mobile_phase_enabled_status}"
    assert actual_wash_solvent_enabled_status is False, \
        f"Expected Wash Solvent disabled toggle status: False, Actual Wash Solvent disabled toggle status: {actual_wash_solvent_enabled_status}"


@then('User confirms the mobile phase and wash solvent toggle button changes did not save')
def confirm_mobile_phase_and_wash_toggle_buttons_did_not_save(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_mobile_phase_state = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
    actual_wash_solvent_state = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
    stored_mobile_phase_state = run_time_checks_screen.get_stored_mobile_phase_state()
    stored_wash_solvent_state = run_time_checks_screen.get_stored_wash_solvent_state()
    assert actual_mobile_phase_state is stored_mobile_phase_state, "Mobile Phase toggle button changes saved when they should not."
    assert actual_wash_solvent_state is stored_wash_solvent_state, "Wash Solvent toggle button changes saved when they should not."


@then('User confirms the mobile phase and wash solvent toggle button changes did save')
def confirm_mobile_phase_and_wash_toggle_buttons_did_save(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_mobile_phase_state = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.MOBILE_PHASE_LOW_TOGGLE)
    actual_wash_solvent_state = run_time_checks_screen.is_toggle_component_enabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
    stored_mobile_phase_state = run_time_checks_screen.get_stored_mobile_phase_state()
    stored_wash_solvent_state = run_time_checks_screen.get_stored_wash_solvent_state()
    assert actual_mobile_phase_state is not stored_mobile_phase_state, "Mobile Phase toggle button changes did not save when they should have."
    assert actual_wash_solvent_state is not stored_wash_solvent_state, "Wash Solvent toggle button changes did not save when they should have."


@when('User unconfigures the seal wash and needle wash')
def unconfigure_seal_wash_and_needle_wash(instrument_configuration_screen: InstrumentConfigurationScreen, dashboard_screen_page: DashBoardScreen,
                                          solvent_configuration_screen: SolventConfigurationScreen):
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.WASH_SOLVENTS_PANEL)
    solvent_configuration_screen.validate_solvent_configuration_screen()
    solvent_configuration_screen.set_toggle_status('Needle_Wash', False)
    solvent_configuration_screen.tap_solvent_phase_tab('Seal_Wash')
    solvent_configuration_screen.set_toggle_status('Seal_Wash', False)
    solvent_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@then('User validates wash solvent toggle button is disabled and not editable')
def validate_wash_solvent_toggle_button_is_disabled_and_not_editable(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_wash_solvent_disabled_status = run_time_checks_screen.is_disabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
    assert actual_wash_solvent_disabled_status is True, \
        f"Expected Wash Solvent disabled toggle status: True, Actual Wash Solvent disabled toggle status: {actual_wash_solvent_disabled_status}"


@when(cfparse('User configures "{seal_wash_toggle}" and "{needle_wash_toggle}"'))
def configure_seal_wash_and_needle_wash(instrument_configuration_screen: InstrumentConfigurationScreen, dashboard_screen_page: DashBoardScreen,
                                        solvent_configuration_screen: SolventConfigurationScreen, seal_wash_toggle, needle_wash_toggle):
    instrument_configuration_screen.tap(SolventBottleConfigurationScreenLocators.WASH_SOLVENTS_PANEL)
    solvent_configuration_screen.validate_solvent_configuration_screen()
    solvent_configuration_screen.set_toggle_status('Needle_Wash', needle_wash_toggle)
    solvent_configuration_screen.tap_solvent_phase_tab('Seal_Wash')
    solvent_configuration_screen.set_toggle_status('Seal_Wash', seal_wash_toggle)
    solvent_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@then('User validates the wash solvent toggle button is enabled')
def validate_wash_solvent_toggle_button_is_enabled(run_time_checks_screen: RunTimeChecksScreen):
    run_time_checks_screen.validate_run_time_checks_screen()
    actual_wash_solvent_enabled_status = run_time_checks_screen.is_enabled(RunTimeChecksScreenLocators.WASH_SOLVENT_LOW_TOGGLE)
    assert actual_wash_solvent_enabled_status is True, \
        f"Expected Wash Solvent enabled toggle status: True, Actual Wash Solvent enabled toggle status: {actual_wash_solvent_enabled_status}"
