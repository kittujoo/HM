import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.Administration.pre_run_checks_screen_locators import PreRunChecksScreenLocators
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.solvent_bottle_configuration_screen_locators import \
    SolventBottleConfigurationScreenLocators
from web_framework.kiosk.pages.System.Administration.administration_screen import AdministrationScreen
from web_framework.kiosk.pages.System.Administration.pre_run_checks_screen import PreRunChecksScreen
from web_framework.kiosk.pages.System.SolventBottlesManager.mobile_phase_configuration_settings_screen import MobilePhaseConfigurationSettingsScreen
from web_framework.kiosk.pages.System.SolventBottlesManager.solvent_configuration_screen import SolventConfigurationScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/pre_run_checks_setting_screen.feature')

logger = Logger(__name__)


@pytest.fixture
def administration_screen(page_builder):
    page = page_builder(AdministrationScreen)
    return page


@pytest.fixture
def pre_run_checks_screen(page_builder):
    page = page_builder(PreRunChecksScreen)
    return page


@pytest.fixture
def mobile_phase_configuration_screen(page_builder):
    page = page_builder(MobilePhaseConfigurationSettingsScreen)
    return page


@pytest.fixture
def solvent_configuration_screen(page_builder):
    page = page_builder(SolventConfigurationScreen)
    return page


@when('User navigates to system screen')
def navigate_to_system_screen(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()


@when('User navigates to the Administration tab')
def navigate_to_administration_tab(system_settings_screen: SystemSettingsScreen):
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_administration_tab()


@when('User navigates to the Acquisition checks tab')
def navigate_to_acquisition_checks_tab(administration_screen: AdministrationScreen):
    administration_screen.validate_administration_configuration_screen()
    administration_screen.tap_acquisition_checks_tab()


@when('User configures the solvent')
def configure_solvent(system_settings_screen: SystemSettingsScreen, instrument_configuration_screen: InstrumentConfigurationScreen,
                      solvent_configuration_screen: SolventConfigurationScreen, mobile_phase_configuration_screen: MobilePhaseConfigurationSettingsScreen,
                      dashboard_screen_page: DashBoardScreen):
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap_module_configuration_tab()
    instrument_configuration_screen.validate_instrument_configuration_screen()
    instrument_configuration_screen.tap_bottle_icon()
    solvent_configuration_screen.tap(SolventBottleConfigurationScreenLocators.MOBILE_PHASE_PANEL)
    mobile_phase_configuration_screen.validate_mobile_phase_settings_screen()
    mobile_phase_configuration_screen.set_toggle_status('A', True)
    mobile_phase_configuration_screen.tap_done_button()
    dashboard_screen_page.tap_system()


@when('User navigates to the Pre-run Checks tab')
def navigate_to_pre_run_checks_tab(administration_screen: AdministrationScreen):
    administration_screen.validate_acquisition_checks_screen()
    administration_screen.tap_pre_run_checks_tab()


@then(cfparse('User validates that the status of "{toggle}" is "{toggle_status}"'))
def validate_pre_run_checks_toggle_status(pre_run_checks_screen: PreRunChecksScreen, toggle, toggle_status):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    toggle_locator = pre_run_checks_screen.toggle_locator_selector(toggle)
    actual_toggle_status = pre_run_checks_screen.is_toggle_component_enabled(toggle_locator)

    if toggle_status == "Enabled":
        toggle_status = True
        assert actual_toggle_status == toggle_status, f"Expected toggle status: {toggle_status}, Actual toggle status: {actual_toggle_status}"

    else:
        toggle_status = False
        assert actual_toggle_status == toggle_status, f"Expected toggle status: {toggle_status}, Actual toggle status: {actual_toggle_status}"


@when('User disables the Sample Plates must be installed toggle button')
def disable_sample_plates_must_be_installed_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.SAMPLE_PLATES_INSTALLED_TOGGLE, False)


@then('User validates the Sample Plates must match method toggle button is disabled and non-editable')
def validate_sample_plates_must_match_method_toggle_button_disabled(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_disabled_status = pre_run_checks_screen.is_disabled(PreRunChecksScreenLocators.SAMPLE_PLATES_MATCH_TOGGLE)
    assert actual_toggle_disabled_status is True, f"Expected toggle disabled status: True, Actual toggle disabled status: {actual_toggle_disabled_status}"


@when('User enables the Sample Plates must be installed toggle button')
def enable_sample_plates_must_be_installed_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.SAMPLE_PLATES_INSTALLED_TOGGLE, True)


@then('User validates the Sample Plates must match method toggle button is not disabled and editable')
def validate_sample_plates_must_match_method_toggle_button_enabled(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_enabled_status = pre_run_checks_screen.is_enabled(PreRunChecksScreenLocators.SAMPLE_PLATES_MATCH_TOGGLE)
    assert actual_toggle_enabled_status is True, f"Expected toggle enabled status: True, Actual toggle enabled status: {actual_toggle_enabled_status}"


@when('User enables the Sample Plates must match method toggle button')
def enable_sample_plates_must_match_method_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.SAMPLE_PLATES_MATCH_TOGGLE, True)


@when('User saves the data')
def save_pre_run_checks_configuration(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.tap_done_button()


@then('User validates the Sample Plates data was correctly saved')
def validate_pre_run_checks_configuration(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_status = pre_run_checks_screen.is_toggle_component_enabled(PreRunChecksScreenLocators.SAMPLE_PLATES_MATCH_TOGGLE)
    assert actual_toggle_status is True, f"Expected toggle status: True, Actual toggle status: {actual_toggle_status}"


@when('User enables all toggles buttons')
def enable_all_toggles_buttons(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_all_toggle_buttons(True)


@when('User disables all toggles buttons')
def disable_all_toggles_buttons(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_all_toggle_buttons(False)


@when('User cancels the changes')
def cancel_pre_run_checks_configuration(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.tap_cancel_button()


@then('User validates that all toggle buttons are enabled')
def validate_all_toggle_buttons_enabled(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.validate_all_toggle_buttons_enabled()


@when('User disables the eConnected Column must be installed toggle button')
def disable_econnected_column_must_be_installed_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.COLUMN_INSTALLED_TOGGLE, False)


@then('User validates the eConnected Column must match method toggle button is disabled and non-editable')
def validate_econnected_column_must_match_method_toggle_button_disabled(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_disabled_status = pre_run_checks_screen.is_disabled(PreRunChecksScreenLocators.COLUMN_MATCHES_TOGGLE)
    assert actual_toggle_disabled_status is True, f"Expected toggle disabled status: True, Actual toggle disabled status: {actual_toggle_disabled_status}"


@when('User enables the eConnected Column must be installed toggle button')
def enable_econnected_column_must_be_installed_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.COLUMN_INSTALLED_TOGGLE, True)


@then('User validates the eConnected Column must match method toggle button is not disabled and editable')
def validate_econnected_column_must_match_method_toggle_button_enabled(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_enabled_status = pre_run_checks_screen.is_enabled(PreRunChecksScreenLocators.COLUMN_MATCHES_TOGGLE)
    assert actual_toggle_enabled_status is True, f"Expected toggle enabled status: True, Actual toggle enabled status: {actual_toggle_enabled_status}"


@when('User enables the eConnected Column must match method toggle button')
def enable_econnected_column_must_match_method_toggle_button(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    pre_run_checks_screen.set_toggle_button(PreRunChecksScreenLocators.COLUMN_MATCHES_TOGGLE, True)


@then('User validates the eConnected Column data was correctly saved')
def validate_econnected_column_data_was_correctly_saved(pre_run_checks_screen: PreRunChecksScreen):
    pre_run_checks_screen.validate_pre_run_checks_screen()
    actual_toggle_status = pre_run_checks_screen.is_toggle_component_enabled(PreRunChecksScreenLocators.COLUMN_MATCHES_TOGGLE)
    assert actual_toggle_status is True, f"Expected toggle status: True, Actual toggle status: {actual_toggle_status}"
