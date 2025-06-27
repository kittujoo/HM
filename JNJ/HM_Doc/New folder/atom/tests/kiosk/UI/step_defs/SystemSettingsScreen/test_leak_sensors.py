from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.system_leak_sensor_screen_locators import LeakSensorScreenLocators
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/leak_sensors.feature')

logger = Logger(__name__)


@given('User navigates to the leak sensors configuration screen')
def navigate_leak_sensors_configuration(session_dash_board_screen_page: DashBoardScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                        system_settings_screen: SystemSettingsScreen):
    session_dash_board_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@given(cfparse('Leak sensors was set to "{initial_state}" state'))
def set_leak_sensor_initial_state(leak_sensor_configuration_screen: LeakSensorScreen, initial_state: str):
    initial_state = True if initial_state == 'ON' else False
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(initial_state, LeakSensorScreenLocators.QSM_LEAK_SENSOR, LeakSensorScreenLocators.QSM_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(initial_state, LeakSensorScreenLocators.CHC_LEAK_SENSOR, LeakSensorScreenLocators.CHC_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(initial_state, LeakSensorScreenLocators.TUV_LEAK_SENSOR, LeakSensorScreenLocators.TUV_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(initial_state, LeakSensorScreenLocators.SM_LEAK_SENSOR, LeakSensorScreenLocators.SM_LEAK_STATUS)
    leak_sensor_configuration_screen.tap_done_button()


@when(cfparse('User switches the leak sensor to "{expected_state}" state'))
def set_sensor_new_state(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen, expected_state: str):
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
    expected_state = True if expected_state == 'ON' else False
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(expected_state, LeakSensorScreenLocators.QSM_LEAK_SENSOR, LeakSensorScreenLocators.QSM_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(expected_state, LeakSensorScreenLocators.CHC_LEAK_SENSOR, LeakSensorScreenLocators.CHC_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(expected_state, LeakSensorScreenLocators.TUV_LEAK_SENSOR, LeakSensorScreenLocators.TUV_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_leak_sensor_toggle(expected_state, LeakSensorScreenLocators.SM_LEAK_SENSOR, LeakSensorScreenLocators.SM_LEAK_STATUS)
    leak_sensor_configuration_screen.tap_done_button()


@then(cfparse('User validates the leak sensor state is "{expected_state}"'))
def validate_sensor_status(system_settings_screen: SystemSettingsScreen,
                           leak_sensor_configuration_screen: LeakSensorScreen, dashboard_screen_page: DashBoardScreen, expected_state: str):
    try:
        system_settings_screen.tap_leak_sensor_tab()
        leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
        expected_state = True if expected_state == 'ON' else False
        leak_sensor_configuration_screen.validate_leak_sensor_status(LeakSensorScreenLocators.QSM_LEAK_STATUS, expected_state)
        leak_sensor_configuration_screen.validate_leak_sensor_status(LeakSensorScreenLocators.CHC_LEAK_STATUS, expected_state)
        leak_sensor_configuration_screen.validate_leak_sensor_status(LeakSensorScreenLocators.TUV_LEAK_STATUS, expected_state)
        leak_sensor_configuration_screen.validate_leak_sensor_status(LeakSensorScreenLocators.SM_LEAK_STATUS, expected_state)
    finally:
        leak_sensor_configuration_screen.tap_done_button()
        system_settings_screen.validate_settings_screen()
        dashboard_screen_page.validate_dashboard_screen()
