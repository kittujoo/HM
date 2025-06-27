import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then, step
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.ColumnManager.column_manager_configuration_screen_locators import ColumnManagerConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.System.ColumnManager.column_manager_configuration_settings_screen_locators import \
    ColumnManagerConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_leak_sensor_screen_locators import LeakSensorScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.ColumnManager.column_manager_configuration_screen import ColumnManagerConfigurationScreen
from web_framework.kiosk.pages.System.ColumnManager.column_manager_configuration_settings_screen import ColumnManagerConfigurationSettingsScreen
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen
from web_framework.kiosk.pages.Utilities.helpers import to_toggle_state

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/column_manager_configuration_settings_screen.feature')
logger = Logger("test_column_manager_configuration_settings_screen")


@given('User navigates to the leak sensor configuration screen')
def navigate_leak_sensor_configuration(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                       dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@given(cfparse('CHC leak sensor was set "{initial_state}" state'))
def set_chc_sensor(initial_state, leak_sensor_configuration_screen: LeakSensorScreen):
    leak_sensor_configuration_screen.switch_chc_leak_sensor_toggle(to_toggle_state(initial_state))
    leak_sensor_configuration_screen.tap_done_button()


@given('User navigates to the CHC module configuration screen')
def navigate_column_manager_configuration(instrument_configuration_screen: InstrumentConfigurationScreen,
                                          column_manager_configuration_screen: ColumnManagerConfigurationScreen,
                                          dashboard_screen_page: DashBoardScreen,
                                          system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_column_manager_icon()
    column_manager_configuration_screen.validate_column_manager_configuration_screen()


@given(cfparse('CHC leak configuration was set "{initial_state}" state'))
def set_module_settings_chc_sensor(initial_state, column_manager_configuration_screen: ColumnManagerConfigurationScreen,
                                   column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen):
    column_manager_configuration_screen.tap(ColumnManagerConfigurationScreenLocators.OPTIONS_PANEL)
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    column_manager_configuration_settings_screen.switch_chc_leak_sensor_toggle_to_state(to_toggle_state(initial_state))
    column_manager_configuration_settings_screen.tap_done_button()
    column_manager_configuration_screen.validate_column_manager_configuration_screen()


@when('User taps the default value button')
def tap_default_value(column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen):
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    column_manager_configuration_settings_screen.tap(ColumnManagerConfigurationSettingsScreenLocators.TEMPERATURE_DEFAULT_BUTTON)


@when(cfparse('User sets the toggle button to "{toggle_status:bool}"', CONVERTERS))
@then(cfparse('User sets the toggle button to "{toggle_status:bool}"', CONVERTERS))
def set_toggle_status(column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen,
                        toggle_status:bool):
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    column_manager_configuration_settings_screen.set_leak_sensor_toggle_status(toggle_status)
    
    
@when(cfparse('User sets the toggle button to "{actual_toggle_status:bool}"', CONVERTERS))
def set_alternate_toggle_status(column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen, actual_toggle_status:bool):
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    column_manager_configuration_settings_screen.set_leak_sensor_toggle_status(actual_toggle_status)
   

@then('User cancels the changes')
def tap_cancel_button(column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen):
    column_manager_configuration_settings_screen.tap(BasePageLocators.CANCEL_BUTTON)


@when(cfparse('User switches the CHC leak sensor to "{expected_state}" state'))
def toggle_chc_sensor(expected_state, system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                      dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
    leak_sensor_configuration_screen.switch_chc_leak_sensor_toggle(to_toggle_state(expected_state))
    leak_sensor_configuration_screen.tap_done_button()

@then('User navigates to the column configuration settings screen')
@when('User navigates to the column configuration settings screen')
def navigate_column_configuration_settings_screen(column_manager_configuration_screen: ColumnManagerConfigurationScreen,
                                                  column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen,
                                                  instrument_configuration_screen: InstrumentConfigurationScreen,
                                                  dashboard_screen_page: DashBoardScreen,
                                                  system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_column_manager_icon()
    column_manager_configuration_screen.tap(ColumnManagerConfigurationScreenLocators.OPTIONS_PANEL)
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()


@when(cfparse('User switches the CHC leak configuration sensor to "{expected_state}" state'))
def set_sensor_configuration_state(expected_state, column_manager_configuration_screen: ColumnManagerConfigurationScreen,
                                   column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen):
    column_manager_configuration_screen.tap(ColumnManagerConfigurationScreenLocators.OPTIONS_PANEL)
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    column_manager_configuration_settings_screen.switch_chc_leak_sensor_toggle_to_state(to_toggle_state(expected_state))
    column_manager_configuration_settings_screen.tap_done_button()


@when('User navigates to the leak sensor screen')
def navigate_leak_sensor(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                         dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@then(cfparse('User validates the CHC leak sensor configuration state is "{expected_state}"'))
def validate_chc_configuration_switch_state(expected_state, column_manager_configuration_settings_screen: ColumnManagerConfigurationSettingsScreen):
    column_manager_configuration_settings_screen.validate_column_manager_configuration_settings_screen()
    actual_chc_switch_state = column_manager_configuration_settings_screen.get_chc_configuration_switch_state()
    assert actual_chc_switch_state == to_toggle_state(
        expected_state), f"The leak detection toggle is not as expected. Expected: [{expected_state}], Actual: [{actual_chc_switch_state}]"


@then(cfparse('User validates the CHC leak sensor state is "{expected_state}"'))
def validate_column_configuration_switch_state(expected_state, leak_sensor_configuration_screen: LeakSensorScreen):
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
    assert (leak_sensor_configuration_screen.get_chc_sensor_toggle_state(LeakSensorScreenLocators.CHC_LEAK_SENSOR_TOGGLE)
            == (to_toggle_state(expected_state))), f"The leak detection toggle is not as expected. Expected:{expected_state}"
