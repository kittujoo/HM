from pathlib import Path
from pytest_bdd import scenarios, given, when, then, step
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.SolventManager.pump_module_configuration_screen import \
    PumpModuleConfigurationScreenlocators
from web_framework.kiosk.pages.Locators.System.SolventManager.pump_module_configuration_settings_screen import \
    MixerConfigurationTabLocators, FluidicChamberLightTabLocators, LeakDetectionTabLocators, PumpModuleConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.SolventManager.pump_module_configuration_screen import PumpModuleConfigurationScreen
from web_framework.kiosk.pages.System.SolventManager.pump_module_configuration_settings_screen import PumpModuleConfigurationSettingsScreen
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/pump_module_configuration_settings_screen.feature')
logger = Logger("test_pump_module_configuration_settings_screen")


@given('User navigates to the pump module configuration screen')
def navigate_solvent_manager_configuration(instrument_configuration_screen: InstrumentConfigurationScreen,
                                           pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                           dashboard_screen_page: DashBoardScreen,
                                           system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_solvent_manager_icon()
    pump_module_configuration_screen.validate_pump_module_configuration_screen()


@step('User navigates to the leak sensor configuration screen')
def navigate_leak_sensor_configuration(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                       dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@given(cfparse('Pump leak sensor was "{initial_state:bool}"', CONVERTERS))
def set_qsm_sensor(leak_sensor_configuration_screen: LeakSensorScreen, initial_state: bool):
    leak_sensor_configuration_screen.switch_pump_leak_sensor_toggle(initial_state)
    leak_sensor_configuration_screen.tap_done_button()


@given(cfparse('Pump leak configuration was "{initial_state:bool}"', CONVERTERS))
def set_module_settings_qsm_sensor(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                   pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, initial_state: bool):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.switch_pump_leak_sensor_toggle_to_state("leak sensor", initial_state)
    pump_module_configuration_settings_screen.tap_done()
    pump_module_configuration_screen.validate_pump_module_configuration_screen()


@given('The state of the pump configuration settings are opposite')
def set_pump_configuration_settings_opposite(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.set_toggle_button(LeakDetectionTabLocators.LEAK_DETECTION_TOGGLE, False)
    pump_module_configuration_settings_screen.set_toggle_button(FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LIGHT_TOGGLE, False)
    pump_module_configuration_settings_screen.tap_done()


@step('User navigates to the pump module configuration settings screen')
def navigate_solvent_manager_configuration_settings(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                                    pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_screen.tap(PumpModuleConfigurationScreenlocators.OPTIONS_PANEL)
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()


@step('User navigates to the configuration settings screen')
def navigate_pump_configuration_settings(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                         pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen,
                                         instrument_configuration_screen: InstrumentConfigurationScreen,
                                         dashboard_screen_page: DashBoardScreen,
                                         system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_solvent_manager_icon()
    pump_module_configuration_screen.tap(PumpModuleConfigurationScreenlocators.OPTIONS_PANEL)
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()


@when(cfparse('User switches the pump leak sensor "{expected_state:bool}"', CONVERTERS))
def toggle_qsm_sensor(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                      dashboard_screen_page: DashBoardScreen, expected_state: bool):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
    leak_sensor_configuration_screen.switch_pump_leak_sensor_toggle(expected_state)
    leak_sensor_configuration_screen.tap_done_button()


@when(cfparse('User switches the pump leak configuration sensor "{expected_state:bool}"', CONVERTERS))
def set_sensor_configuration_state(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                   pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, expected_state: bool):
    pump_module_configuration_screen.tap(PumpModuleConfigurationScreenlocators.OPTIONS_PANEL)
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.switch_pump_leak_sensor_toggle_to_state("leak sensor", expected_state)
    pump_module_configuration_settings_screen.tap_done()


@when('User switches the pump leak sensor setting to ON')
def switch_pump_leak_sensor_on(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.set_toggle_button(LeakDetectionTabLocators.LEAK_DETECTION_TOGGLE, True)


@when('User switches the light when door is opened setting to ON')
def switch_pump_light_when_door_open_on(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.set_toggle_button(FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LIGHT_TOGGLE, True)


@when('User navigates to the leak sensor screen')
def navigate_leak_sensor(system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                         dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@when('User confirms the change')
def tap_done_button(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                    pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.tap_done()
    pump_module_configuration_screen.validate_pump_module_configuration_screen()


@when('User cancels the change')
def tap_cancel_button(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                      pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.tap_cancel()
    pump_module_configuration_screen.validate_pump_module_configuration_screen()


@when(cfparse('User selects the "{mixer_option}"'))
def select_mixer_option(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, mixer_option):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.select_mixer_option(mixer_option)


@when('User selects the None mixer option')
def select_none_mixer_option(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.select_mixer_option("None")


@when(cfparse('User enters the "{mixer_value}"'))
def enter_mixer_value(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, mixer_value):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    pump_module_configuration_settings_screen.tap(MixerConfigurationTabLocators.FIELD_CONTAINER)
    pump_module_configuration_settings_screen.clear_num_pad_entries(MixerConfigurationTabLocators.CUSTOM_MIXER_FIELD)
    pump_module_configuration_settings_screen.enter_value(mixer_value)


@then(cfparse('User validates the "{done_button_status}" status'))
def validate_done_inactive(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, done_button_status):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()

    if done_button_status == 'Disabled':
        assert pump_module_configuration_settings_screen.validate_done_button_inactive(), f"The done button is active when it should not be"
    else:
        assert pump_module_configuration_settings_screen.is_button_active(
            PumpModuleConfigurationSettingsScreenLocators.DONE_BUTTON_LABEL) is True, f"The done button is not active when it should be"


@then('User validates the changed pump module configuration settings are ON')
def validate_pump_module_configuration_settings_on(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    assert pump_module_configuration_settings_screen.is_toggle_component_enabled(
        LeakDetectionTabLocators.LEAK_DETECTION_TOGGLE) is True, "The pump leak sensor toggle is not on"
    assert pump_module_configuration_settings_screen.is_toggle_component_enabled(
        FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LIGHT_TOGGLE) is True, "The light when door is opened toggle is not on"


@then('User validates the changed pump module configuration settings are OFF')
def validate_pump_module_configuration_settings_off(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    assert pump_module_configuration_settings_screen.is_toggle_component_enabled(
        LeakDetectionTabLocators.LEAK_DETECTION_TOGGLE) is False, "The pump leak sensor toggle is on"
    assert pump_module_configuration_settings_screen.is_toggle_component_enabled(
        FluidicChamberLightTabLocators.FLUIDIC_CHAMBER_LIGHT_TOGGLE) is False, "The light when door is opened toggle is on"


@then(cfparse('User validates the leak sensor configuration state is "{expected_state:bool}"', CONVERTERS))
def validate_solvent_configuration_switch_state(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen,
                                                system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                                dashboard_screen_page: DashBoardScreen,
                                                expected_state: bool):
    try:
        pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
        assert pump_module_configuration_settings_screen.get_solvent_configuration_switch_state(
            "leak sensor") == expected_state, f"The leak detection toggle is not as expected. Expected:{expected_state}"
    finally:
        pump_module_configuration_settings_screen.wait_element_to_be_clickable(BasePageLocators.DONE_BUTTON,
                                                                               pump_module_configuration_settings_screen.wait_time)
        pump_module_configuration_settings_screen.tap_cancel_button()
        dashboard_screen_page.tap_system()
        system_settings_screen.tap_leak_sensor_tab()
        leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
        leak_sensor_configuration_screen.switch_pump_leak_sensor_toggle(True)
        leak_sensor_configuration_screen.tap_done_button()
        dashboard_screen_page.validate_dashboard_screen()


@then(cfparse('User validates the leak sensor state is "{expected_state:bool}"', CONVERTERS))
def validate_solvent_configuration_switch_state(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen,
                                                system_settings_screen: SystemSettingsScreen, leak_sensor_configuration_screen: LeakSensorScreen,
                                                dashboard_screen_page: DashBoardScreen, pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                                instrument_configuration_screen: InstrumentConfigurationScreen,
                                                expected_state: bool):
    try:
        leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()
        assert leak_sensor_configuration_screen.get_leak_sensor_switch_state() == expected_state, \
            f"The leak detection toggle is not as expected. Expected:{expected_state}"
    finally:
        leak_sensor_configuration_screen.tap_done_button()
        dashboard_screen_page.tap_system()
        system_settings_screen.tap_configuration_tab()
        instrument_configuration_screen.tap_solvent_manager_icon()
        pump_module_configuration_screen.tap(PumpModuleConfigurationScreenlocators.OPTIONS_PANEL)
        pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
        pump_module_configuration_settings_screen.switch_pump_leak_sensor_toggle_to_state("leak sensor", True)
        pump_module_configuration_settings_screen.tap_done()
        dashboard_screen_page.validate_dashboard_screen()


@then(cfparse('User validates the "{mixer_value}" is properly displayed in the label'))
def validate_mixer_volume_label_value(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen, mixer_value):
    pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
    assert mixer_value == pump_module_configuration_settings_screen.get_text(MixerConfigurationTabLocators.MIXER_VOLUME_VALUE)


@then('User validates the mixer volume is not shown')
def validate_mixer_volume_not_shown(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    assert pump_module_configuration_settings_screen.is_displayed(
        MixerConfigurationTabLocators.MIXER_VOLUME_LABEL) is False, f"The mixer volume label is displayed when it should not be"


@then(cfparse('User validates the custom "{mixer_value}" was properly saved'))
def validate_custom_mixer_value(pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen,
                                pump_module_configuration_screen: PumpModuleConfigurationScreen,
                                mixer_value):
    try:
        pump_module_configuration_settings_screen.validate_pump_module_configuration_settings_screen()
        assert mixer_value == pump_module_configuration_settings_screen.get_entered_value(MixerConfigurationTabLocators.CUSTOM_MIXER_FIELD)
    finally:
        pump_module_configuration_settings_screen.tap_cancel()
        pump_module_configuration_screen.validate_pump_module_configuration_screen()


# Need separate confirm to handle scroll list
@then('User confirms the mixer change')
def confirm_mixer_change(pump_module_configuration_screen: PumpModuleConfigurationScreen,
                         pump_module_configuration_settings_screen: PumpModuleConfigurationSettingsScreen):
    pump_module_configuration_settings_screen.validate_mixer_configuration_screen()
    pump_module_configuration_settings_screen.tap_done()
    pump_module_configuration_screen.validate_pump_module_configuration_screen()
