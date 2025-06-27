import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from web_framework.kiosk.pages.Locators.System.Administration.system_qualification_screen_locators import SystemQualificationScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.Administration.administration_configuration_screen_locators import AdministrationConfigurationScreenLocators
from web_framework.kiosk.pages.System.Administration.administration_screen import AdministrationScreen
from web_framework.kiosk.pages.System.Administration.system_qualification_screen import SystemQualificationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/system_qualification.feature')


@pytest.fixture
def system_qualification_configuration_screen(page_builder):
    page = page_builder(SystemQualificationScreen)
    return page


@given('User navigates to the administration - system qualification screen')
def navigate_administration_qualification_screen(dashboard_screen_page: DashBoardScreen, system_settings_screen: SystemSettingsScreen,
                                                 administration_configuration_screen: AdministrationScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_administration_tab()
    administration_configuration_screen.validate_administration_configuration_screen()
    administration_configuration_screen.tap(AdministrationConfigurationScreenLocators.SYSTEM_QUALIFICATION_TAB)


@when(cfparse('User sets the toggle component to "{toggle_state: bool}"', CONVERTERS))
def set_toggle_state(toggle_state, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.set_system_qualification_toggle_status(toggle_state)


@when('User confirms the changes')
def tap_done_button(system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.tap(BasePageLocators.DONE_BUTTON)


@when('User navigates to the system qualification screen')
def navigate_system_qualification_screen(administration_configuration_screen: AdministrationScreen,
                                         system_qualification_configuration_screen: SystemQualificationScreen):
    administration_configuration_screen.validate_administration_configuration_screen()
    administration_configuration_screen.tap(AdministrationConfigurationScreenLocators.SYSTEM_QUALIFICATION_TAB)
    system_qualification_configuration_screen.validate_system_qualification_screen()


@when(cfparse('User sets the qualification expire to "{qualification_expiry}"'))
def set_qualification_expiry(qualification_expiry, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.select_spinner_text(SystemQualificationScreenLocators.MONTHS_PICKER_WHEEL, qualification_expiry)


@when(cfparse('User sets the toggle button as "{initial_toggle_status: bool}"', CONVERTERS))
def set_alternate_toggle_status(initial_toggle_status: bool, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.set_system_qualification_toggle_status(initial_toggle_status)


@when(cfparse('User sets the toggle as "{new_toggle_status: bool}"', CONVERTERS))
def set_toggle_button(new_toggle_status: bool, administration_configuration_screen: AdministrationScreen,
                      system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.tap(BasePageLocators.DONE_BUTTON)
    navigate_system_qualification_screen(administration_configuration_screen, system_qualification_configuration_screen)
    system_qualification_configuration_screen.set_system_qualification_toggle_status(new_toggle_status)


@when('User sets the toggle button as enable')
def enable_toggle_button(system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.enable_system_qualification()


@when(cfparse('User sets qualification expires as "{desired_qualification_expires}"'))
def set_desired_qualification_expiry(desired_qualification_expires, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.enable_system_qualification()
    system_qualification_configuration_screen.select_spinner_text(SystemQualificationScreenLocators.MONTHS_PICKER_WHEEL, desired_qualification_expires)


@when(cfparse('User set qualification expires as "{actual_qualification_expires}"'))
def set_actual_qualification_expiry(actual_qualification_expires, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.enable_system_qualification()
    system_qualification_configuration_screen.select_spinner_text(SystemQualificationScreenLocators.MONTHS_PICKER_WHEEL, actual_qualification_expires)
    system_qualification_configuration_screen.tap(BasePageLocators.DONE_BUTTON)


@when('User taps the default button')
def tap_default_button(system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.tap(SystemQualificationScreenLocators.DEFAULT_MONTH_BUTTON)
    system_qualification_configuration_screen.tap(BasePageLocators.DONE_BUTTON)


@when('User cancels the setting')
def tap_cancel_button(system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.tap(BasePageLocators.CANCEL_BUTTON)


@then(cfparse('User validates the toggle state is "{toggle_state: bool}"', CONVERTERS))
def validate_toggle_state(toggle_state: bool, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.validate_system_qualification_toggle_state(toggle_state)


@then(cfparse('the qualification expiration date is "{expected_qualification_expiry}"'))
def validate_qualification_expiry(expected_qualification_expiry, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    actual_qualification_expiry = system_qualification_configuration_screen.get_selected_expiry_system_qualification()
    assert expected_qualification_expiry == actual_qualification_expiry, (f"Unexpected qualification expiration. Expected: {expected_qualification_expiry}, "
                                                                          f"Actual: {actual_qualification_expiry}")


@then(cfparse('User validates the toggle button is saved as "{expected_toggle_state: bool}"', CONVERTERS))
def validate_temporary_toggle_status(expected_toggle_state: bool, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    system_qualification_configuration_screen.wait_time_to_load_value(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_MENU)
    actual_toggle_state = system_qualification_configuration_screen.is_toggle_component_enabled(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE)
    assert actual_toggle_state == expected_toggle_state, f"Unexpected toggle state. Expected: [{expected_toggle_state}], Actual: [{actual_toggle_state}"


@then(cfparse('User validates the toggle button gets saved to "{initial_toggle_status:bool}"', CONVERTERS))
def validate_expected_toggle_status(initial_toggle_status: bool, administration_configuration_screen: AdministrationScreen,
                                    system_qualification_configuration_screen: SystemQualificationScreen):
    navigate_system_qualification_screen(administration_configuration_screen, system_qualification_configuration_screen)
    system_qualification_configuration_screen.validate_system_qualification_toggle_state(initial_toggle_status)


@then(cfparse('qualification expires value is "{expected_qualification_expiry}"'))
def validate_actual_qualification_expiry(expected_qualification_expiry, system_qualification_configuration_screen: SystemQualificationScreen):
    system_qualification_configuration_screen.validate_system_qualification_screen()
    actual_qualification_expiry = system_qualification_configuration_screen.get_selected_expiry_system_qualification()
    assert expected_qualification_expiry == actual_qualification_expiry, (f"The expiry system qualification on system qualification screen was unexpected. "
                                                                          f"Expected: {expected_qualification_expiry}, Actual: {actual_qualification_expiry}")


@then('User validate the qualification expires date is set to default')
def validate_default_qualification_expiry(administration_configuration_screen: AdministrationScreen,
                                          system_qualification_configuration_screen: SystemQualificationScreen):
    navigate_system_qualification_screen(administration_configuration_screen, system_qualification_configuration_screen)
    actual_month_expiry = system_qualification_configuration_screen.get_selected_expiry_system_qualification()
    default_month = '12'
    assert actual_month_expiry == default_month, (f"The expiry system qualification on system qualification screen was unexpected. "
                                                          f"Actual month Expiration: {actual_month_expiry}, Expected: {default_month}")
