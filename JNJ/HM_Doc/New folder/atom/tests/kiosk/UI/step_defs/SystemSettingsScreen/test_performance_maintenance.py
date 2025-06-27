import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.Administration.performace_maintenence_screen_locators import \
    PerformanceMaintenanceScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.Administration.administration_screen import AdministrationScreen
from web_framework.kiosk.pages.System.Administration.performance_maintenance_screen import PerformanceMaintenanceScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/performance_maintenance.feature')


@pytest.fixture
def performance_maintenance_screen(page_builder):
    page = page_builder(PerformanceMaintenanceScreen)
    return page


@given('User navigates to the administration screen')
def tap_administration(dashboard_screen_page: DashBoardScreen, system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap(SystemSettingsScreenLocators.ADMINISTRATION_TAB)


@when('User navigates to the performance maintenance screen')
def navigates_to_maintenance_screen(administration_configuration_screen: AdministrationScreen):
    administration_configuration_screen.validate_administration_configuration_screen()
    administration_configuration_screen.tap(PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE)


@when(cfparse('User sets the toggle component to "{toggle_status:bool}"', CONVERTERS))
def set_maintenance_toggle_button(toggle_status: bool, performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.validate_performance_maintenance_screen()
    performance_maintenance_screen.set_performance_maintenance_toggle_status(toggle_status)


@when('User confirms the changes')
def tap_done_button(performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.wait_time_to_load_value(BasePageLocators.DONE_BUTTON)
    performance_maintenance_screen.tap(BasePageLocators.DONE_BUTTON)


@when('User cancels the setting')
def tap_cancel_button(performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.wait_time_to_load_value(BasePageLocators.CANCEL_BUTTON)
    performance_maintenance_screen.tap(BasePageLocators.CANCEL_BUTTON)


@when('User taps the default button')
def tap_default_button(administration_configuration_screen: AdministrationScreen, performance_maintenance_screen: PerformanceMaintenanceScreen):
    administration_configuration_screen.validate_administration_configuration_screen()
    performance_maintenance_screen.tap(PerformanceMaintenanceScreenLocators.DEFAULT_MONTH_BUTTON)


@when(cfparse('User sets next performance maintenance to "{expected_months}"'))
def set_expiry_date(context, expected_months: str, performance_maintenance_screen: PerformanceMaintenanceScreen):
    context['expected_expiry'] = performance_maintenance_screen.get_expiry_date_from_current_date(expected_months)
    performance_maintenance_screen.select_spinner_text(PerformanceMaintenanceScreenLocators.MONTHS_PICKER_WHEEL,
                                                       expected_months)


@when('User taps the note tab')
def tap_note_tab(performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.tap_toggle_button_on(PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_TOGGLE)
    performance_maintenance_screen.tap(PerformanceMaintenanceScreenLocators.NOTE_TAB)


@when(cfparse('User enters text to the "{note}"'))
def enter_note_text(context, note: str, performance_maintenance_screen: PerformanceMaintenanceScreen):
    context['expected_note'] = note
    performance_maintenance_screen.validate_add_or_edit_note_screen()
    performance_maintenance_screen.enter_note_content(note)
    performance_maintenance_screen.tap(PerformanceMaintenanceScreenLocators.DONE_BUTTON_FOR_NOTES)


@then(cfparse('User validates the toggle button is saved to "{toggle_status:bool}"', CONVERTERS))
def validate_toggle_status(toggle_status: bool, performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.wait_time_to_load_value(
        PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_TOGGLE)
    actual_toggle_state = performance_maintenance_screen.is_toggle_component_enabled(
        PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_TOGGLE)
    assert actual_toggle_state == toggle_status, f"Unexpected toggle state for maintenance screen. Expected: [{toggle_status}], Actual: [{actual_toggle_state}"


@then('User validats the performance maintenance expiration date is displayed under the performance tab')
def validate_expiration_on_performance_tab(context, performance_maintenance_screen: PerformanceMaintenanceScreen):
    actual_expiry = performance_maintenance_screen.get_container_text(
        PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_TAB_EXPIRY)
    assert context['expected_expiry'] in actual_expiry, f"Unexpected maintenance expiration date. " \
                                                        f"Expected: {context['expected_expiry']}, Actual: {actual_expiry}"


@then(cfparse('User validates the performance maintenance expiration date as "{expected_months}"'))
def validate_performance_expiration(expected_months: str, performance_maintenance_screen: PerformanceMaintenanceScreen):
    actual_expiry = performance_maintenance_screen.get_selected_expiry_performance_maintenance()
    assert expected_months == actual_expiry, (f"Unexpected maintenance expiration date. Expected: {expected_months}, "
                                              f"Actual: {actual_expiry}")


@then(cfparse('User validate the maintenance expires date is set to default as "{default_month}"'))
def validate_default_qualification_expiry(default_month: str, performance_maintenance_screen: PerformanceMaintenanceScreen):
    performance_maintenance_screen.validate_performance_maintenance_screen()
    actual_month_expiry = performance_maintenance_screen.get_selected_expiry_performance_maintenance()
    assert actual_month_expiry == default_month, (f"Unexpected default expiry for performance maintenance screen. "
                                                  f"Actual: {actual_month_expiry}, Expected: {default_month}")


@then(cfparse('User validates the comment card shows correct numbers with "{expected_length:d}" characters'))
def validate_note_length(context, expected_length: int, performance_maintenance_screen: PerformanceMaintenanceScreen):
    actual_note_text = performance_maintenance_screen.get_container_text(
        PerformanceMaintenanceScreenLocators.NOTE_TAB_CONTENT)
    assert context['expected_note'] == actual_note_text, f"Unexpected note in performance maintenance. " \
                                                         f"Expected: {context['expected_note']}, Actual: {actual_note_text}"

    assert expected_length == len(actual_note_text), f"Unexpected note length in performance maintenance. " \
                                                     f"Expected: {expected_length}, Actual: {actual_note_text}"
