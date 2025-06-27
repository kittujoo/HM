import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.TUVDetector.tuv_configuration_screen import TUVConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.System.TUVDetector.tuv_configuration_settings_screen import TUVConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_leak_sensor_screen_locators import LeakSensorScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.TUVDetector.tuv_configuration_screen import TUVConfigurationScreen
from web_framework.kiosk.pages.System.TUVDetector.tuv_configuration_settings_screen import TUVConfigurationSettingsScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/tuv_configuration_settings_screen.feature')
logger = Logger("test_tuv_configuration_settings_screen")


@pytest.fixture
def tuv_configuration_screen(session_instrument_configuration_screen_page: InstrumentConfigurationScreen, page_builder):
    session_instrument_configuration_screen_page.tap_tuv_icon()
    page = page_builder(TUVConfigurationScreen)
    return page


@given(cfparse('The settings are opposite of the desired "{desired_close_shutter_preference}" and "{leak_sensor_enabled}" options'))
def set_tuv_configuration_settings_opposite(desired_close_shutter_preference, leak_sensor_enabled, tuv_configuration_screen: TUVConfigurationScreen,
                                            tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    # navigate to the TUV system settings
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap(TUVConfigurationScreenLocators.LAMP_PANEL)
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()

    # set the close shutter preference
    opposite_close_shutter_preference = not TypeConverter.to_bool(desired_close_shutter_preference)
    tuv_configuration_tuv_configuration_screen.tap_preferences_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    tuv_configuration_tuv_configuration_screen.set_toggle_button(TUVConfigurationSettingsScreenLocators.CLOSE_SHUTTER_TOGGLE, opposite_close_shutter_preference)
    assert tuv_configuration_tuv_configuration_screen.is_toggle_component_enabled(
        TUVConfigurationSettingsScreenLocators.CLOSE_SHUTTER_TOGGLE) is opposite_close_shutter_preference, "Failed to set the close shutter preference"

    # set the leak sensor
    opposite_leak_sensor_enabled = not TypeConverter.to_bool(leak_sensor_enabled)
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.validate_options_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    tuv_configuration_tuv_configuration_screen.set_leak_sensor_monitor_mode(opposite_leak_sensor_enabled)
    assert tuv_configuration_tuv_configuration_screen.is_toggle_component_enabled(
        TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON) is opposite_leak_sensor_enabled

    # confirm the settings
    tuv_configuration_tuv_configuration_screen.tap_done_button()


@given('User navigates to the leak sensor configuration screen')
def navigate_leak_sensor_configuration(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                       session_dash_board_screen_page: DashBoardScreen):
    session_dash_board_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@given(cfparse('TUV leak sensor was "{initial_state}"'))
def set_tuv_sensor(initial_state, leak_sensor_configuration_screen: LeakSensorScreen):
    leak_sensor_configuration_screen.switch_tuv_leak_sensor_toggle(to_toggle_state(initial_state))
    leak_sensor_configuration_screen.tap_done_button()


@given('User navigates to the TUV module configuration screen')
def navigate_tuv_module_configuration(instrument_configuration_screen: InstrumentConfigurationScreen,
                                      tuv_configuration_screen: TUVConfigurationScreen,
                                      session_dash_board_screen_page: DashBoardScreen,
                                      system_settings_screen: SystemSettingsScreen):
    session_dash_board_screen_page.validate_dashboard_screen()
    session_dash_board_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_tuv_icon()
    tuv_configuration_screen.validate_tuv_settings_screen()


@given(cfparse('TUV leak configuration was "{initial_state}"'))
def set_module_settings_tuv_sensor(initial_state, tuv_configuration_screen: TUVConfigurationScreen,
                                   tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.switch_tuv_leak_sensor_toggle_to_state(to_toggle_state(initial_state))
    tuv_configuration_tuv_configuration_screen.tap_done_button()
    tuv_configuration_screen.validate_tuv_settings_screen()


@when('User navigates to the TUV system settings')
@then('User navigates to the TUV system settings')
def navigate_tuv_settings_screen(tuv_configuration_screen: TUVConfigurationScreen, tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap(TUVConfigurationScreenLocators.LAMP_PANEL)
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()


@then('User validates the lamp information is present')
def validate_lamp_information(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap(TUVConfigurationSettingsScreenLocators.LAMP_TAB)
    tuv_configuration_tuv_configuration_screen.wait_time_to_load_value(TUVConfigurationSettingsScreenLocators.LAMP_SERIAL_NUMBER_LABEL)


@then('User validates the flow cell information is present')
def validate_lamp_information(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap(TUVConfigurationSettingsScreenLocators.FLOW_CELL_TAB)
    tuv_configuration_tuv_configuration_screen.wait_time_to_load_value(TUVConfigurationSettingsScreenLocators.FLOW_CELL_PART_NUMBER_LABEL)


@when('User navigate to the configuration settings screen through selection of "close shutter preference"')
def select_close_shutter_preference(tuv_configuration_screen: TUVConfigurationScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_close_shutter_preference_tab()


@when(cfparse('User sets the optics temperature stabilization as "{actual_temperature}"'))
def set_optics_temperature_stabilization(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen, actual_temperature):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap_preferences_tab()
    tuv_configuration_tuv_configuration_screen.set_temperature_stabilization_settings(actual_temperature)


@when(cfparse('User toggles lamp with resident id "{lamp_resident_id_enabled}" and flow cell with resident id "{flow_cell_resident_id_enabled}"'))
def required_option_for_operations(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen,
                                   lamp_resident_id_enabled, flow_cell_resident_id_enabled):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.set_lamp_with_resident_id_mode(lamp_resident_id_enabled)
    tuv_configuration_tuv_configuration_screen.set_flow_cell_with_resident_id_mode(flow_cell_resident_id_enabled)


@when('User navigates to the configuration settings screen by tapping the "close shutter preference" tab')
def set_close_shutter_preference(tuv_configuration_screen: TUVConfigurationScreen, tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_close_shutter_preference_settings()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()


@when(cfparse('User toggles leak sensor mode "{leak_sensor_enabled}" to monitor the leak sensor in the system'))
@then(cfparse('User toggles leak sensor mode "{leak_sensor_enabled}" to monitor the leak sensor in the system'))
def monitor_leak_sensor(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen, leak_sensor_enabled):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.validate_options_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    tuv_configuration_tuv_configuration_screen.set_leak_sensor_monitor_mode(leak_sensor_enabled)


@when('User confirms the selection')
@then('User confirms the selection')
def tap_done_button(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.tap_done_button()


@when('User cancels the selection')
@then('User cancels the selection')
def tap_cancel_button(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.tap_cancel_button()


@then('User validates that there is no change in the configuration settings')
def validate_no_configuration_settings_change(tuv_configuration_screen: TUVConfigurationScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    current_tuv_configuration_settings = tuv_configuration_screen.get_tuv_configuration_settings_value()
    expected_tuv_configurations_settings = tuv_configuration_screen.get_previous_tuv_configuration_settings()
    assert current_tuv_configuration_settings == expected_tuv_configurations_settings, f" failed to show the previous configuration settings"
    logger.info("***************The TUV configuration settings screen test ends *************")


@when('User gets the current configuration settings of the TUV module')
def get_current_configuration_settings(tuv_configuration_screen: TUVConfigurationScreen):
    current_tuv_configuration_settings = tuv_configuration_screen.get_tuv_configuration_settings_value()
    tuv_configuration_screen.set_previous_tuv_configuration_settings(current_tuv_configuration_settings)


@when('User navigates to the configuration settings screen by tapping the "required operation for options" tab')
def select_required_operation_for_options(tuv_configuration_screen: TUVConfigurationScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_options_tab()


@when('User navigates to the configuration settings screen by tapping the "Preferences" tab')
def select_required_operation_for_options(tuv_configuration_screen: TUVConfigurationScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_preferences_tab()


@when('User navigates to the configuration settings screen by tapping the options tab')
def select_option(tuv_configuration_screen: TUVConfigurationScreen):
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_options_tab()


@when(cfparse('User sets the close shutter preference as "{desired_close_shutter_preference}"'))
@then(cfparse('User sets the close shutter preference as "{desired_close_shutter_preference}"'))
def set_close_shutter_preference(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen, desired_close_shutter_preference):
    tuv_configuration_tuv_configuration_screen.tap_preferences_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    tuv_configuration_tuv_configuration_screen.set_toggle_button(TUVConfigurationSettingsScreenLocators.CLOSE_SHUTTER_TOGGLE, desired_close_shutter_preference)


@when(cfparse('User switches the TUV leak sensor "{expected_state}"'))
def toggle_tuv_sensor(expected_state, system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                      dashboard_screen_page: DashBoardScreen):
    navigate_leak_sensor_settings(system_settings_screen, leak_sensor_configuration_screen, dashboard_screen_page)
    leak_sensor_configuration_screen.switch_tuv_leak_sensor_toggle(to_toggle_state(expected_state))
    leak_sensor_configuration_screen.tap_done_button()


@when('User navigates to the configuration settings screen')
def navigate_tuv_configuration_settings(tuv_configuration_screen: TUVConfigurationScreen,
                                        tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen,
                                        instrument_configuration_screen: InstrumentConfigurationScreen,
                                        dashboard_screen_page: DashBoardScreen,
                                        system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_tuv_icon()
    tuv_configuration_screen.validate_tuv_settings_screen()
    tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()


@when(cfparse('User switches the TUV leak configuration sensor "{expected_state}"'))
def toggle_tuv_sensor_configuration_state(expected_state, tuv_configuration_screen: TUVConfigurationScreen,
                                          tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_screen.tap_options_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    tuv_configuration_tuv_configuration_screen.switch_tuv_leak_sensor_toggle_to_state(to_toggle_state(expected_state))
    tuv_configuration_tuv_configuration_screen.tap_done_button()


@when('User navigates to the leak sensor screen')
def navigate_leak_sensor_settings(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                  dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@then(cfparse('validate {expected_temperature} in the TUV configuration screen'))
def validate_temperature(tuv_configuration_screen: TUVConfigurationScreen, expected_temperature):
    tuv_configuration_screen.validate_tuv_settings_screen()
    current_temperature = tuv_configuration_screen.get_optics_temperature_settings_read_back_value()
    assert current_temperature == expected_temperature, f"Failed to update the set temperature, current_temperature => {current_temperature}"


@then(cfparse('User validates the "{expected_close_shutter_preference}" preference option was saved'))
def validate_preferences_options(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen, expected_close_shutter_preference):
    tuv_configuration_tuv_configuration_screen.tap_preferences_tab()
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    close_shutter_preference_status = TypeConverter.to_bool(expected_close_shutter_preference)
    assert tuv_configuration_tuv_configuration_screen.is_toggle_component_enabled(
        TUVConfigurationSettingsScreenLocators.CLOSE_SHUTTER_TOGGLE) == close_shutter_preference_status


@then('User navigates to the TUV options screen')
def navigate_tuv_options(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.tap_options_tab()


@then(cfparse('User validates the "{expected_leak_sensor_options}" leak sensor option was saved'))
def validate_leak_sensor_options(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen, expected_leak_sensor_options):
    tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
    tuv_configuration_tuv_configuration_screen.tap_options_tab()
    leak_sensor_toggle_status = TypeConverter.to_bool(expected_leak_sensor_options)
    tuv_configuration_tuv_configuration_screen.wait_for_isym_toggle()
    assert tuv_configuration_tuv_configuration_screen.is_toggle_component_enabled(
        TUVConfigurationSettingsScreenLocators.LEAK_SENSOR_TOGGLE_BUTTON) == leak_sensor_toggle_status


@then('User returns to the main TUV configuration screen')
def return_main_tuv_screen(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen):
    tuv_configuration_tuv_configuration_screen.tap_cancel_button()


@then(cfparse('User validates the leak sensor configuration state is "{expected_state}"'))
def validate_tuv_configuration_switch_state(expected_state, tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen,
                                            system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                            dashboard_screen_page: DashBoardScreen):
    try:
        tuv_configuration_tuv_configuration_screen.validate_tuv_configuration_settings_screen()
        assert tuv_configuration_tuv_configuration_screen.get_tuv_configuration_switch_state() == (to_toggle_state(expected_state)), \
            f"The TUV leak detection toggle is not as expected. Expected:{expected_state}"
    finally:
        tuv_configuration_tuv_configuration_screen.wait_element_to_be_clickable(BasePageLocators.DONE_BUTTON,
                                                                                tuv_configuration_tuv_configuration_screen.wait_time)
        tuv_configuration_tuv_configuration_screen.tap_cancel_button()
        navigate_leak_sensor_settings(system_settings_screen, leak_sensor_configuration_screen, dashboard_screen_page)
        leak_sensor_configuration_screen.switch_tuv_leak_sensor_toggle(True)
        leak_sensor_configuration_screen.tap_done_button()


@then(cfparse('User validates the TUV leak sensor state is "{expected_state}"'))
def validate_tuv_leak_sensor_switch_state(tuv_configuration_tuv_configuration_screen: TUVConfigurationSettingsScreen,
                                          system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                          dashboard_screen_page: DashBoardScreen, tuv_configuration_screen: TUVConfigurationScreen,
                                          instrument_configuration_screen: InstrumentConfigurationScreen,
                                          expected_state):
    try:
        leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
        assert leak_sensor_configuration_screen.get_leak_sensor_toggle_state(LeakSensorScreenLocators.TUV_LEAK_SENSOR) == (to_toggle_state(expected_state)), \
            f"The TUV leak detection toggle is not as expected. Expected:{expected_state}"
    finally:
        leak_sensor_configuration_screen.tap_done_button()
        navigate_tuv_configuration_settings(tuv_configuration_screen, tuv_configuration_tuv_configuration_screen, instrument_configuration_screen,
                                            dashboard_screen_page, system_settings_screen)
        tuv_configuration_tuv_configuration_screen.switch_tuv_leak_sensor_toggle_to_state(True)
        tuv_configuration_tuv_configuration_screen.tap_done_button()
        dashboard_screen_page.validate_dashboard_screen()


def to_toggle_state(toggle_state) -> bool:
    """
        This function converts the given parameter to a boolean value
        @param toggle_state: String type data from the feature file
        @return: True or False
    """
    return True if toggle_state == 'ON' else False
