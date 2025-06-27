import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from pytest_bdd.parsers import cfparse
from utilities.datatables.converters import CONVERTERS
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.sm_configuration_settings_constants import SMConfigurationScreenConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_screen import SMConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_settings_screen import OptionsTab, \
    CompartmentLightTab, VolumeSettingsTab, SMConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_leak_sensor_screen_locators import LeakSensorScreenLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.System.LeakSensors.leak_sensor_screen import LeakSensorScreen
from web_framework.kiosk.pages.System.Models.sm_configuration_settings import OptionSettings
from web_framework.kiosk.pages.System.SampleManager.sm_configuration_screen import SMConfigurationScreen
from web_framework.kiosk.pages.System.SampleManager.sm_configuration_settings_screen import SMConfigurationSettingsScreen
from web_framework.kiosk.pages.System.SampleManager.sm_configuration_settings_screen_locators_lookup import \
    SMConfigurationSettingsScreenLocatorsLookup
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/sample_manager_configuration_settings.feature')


@pytest.fixture
def sm_configuration_screen_page(session_instrument_configuration_screen_page: InstrumentConfigurationScreen,
                                 page_builder):
    session_instrument_configuration_screen_page.tap_sm_icon()
    page = page_builder(SMConfigurationScreen)
    return page


##########################
### --- TEST STEPS --- ###
##########################

@given('User navigates to the SM configuration settings screen')
def navigate_sm_configuration_setting(sm_module_config_screen: SMConfigurationScreen,
                                      dashboard_screen_page: DashBoardScreen,
                                      system_settings_screen: SystemSettingsScreen,
                                      instrument_configuration_screen: InstrumentConfigurationScreen,
                                      sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_sm_icon()
    sm_module_config_screen.tap(SMConfigurationScreenLocators.OPTIONS_TAB)
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(
        SMConfigurationSettingsScreenLocators.SM_CONFIGURATION_HEADER, "sm configuration settings screen")


@given('User navigates to the leak sensor configuration screen')
def navigate_leak_sensor_configuration(system_settings_screen: SystemSettingsScreen,
                                       leak_sensor_configuration_screen: LeakSensorScreen,
                                       dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.wait_time_to_load_value(DashBoardsScreenPageLocators.INSTRUMENT)
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@given(cfparse('User switches all the toggles in sample manager configuration to "{initial_state: bool}"', CONVERTERS))
def switch_on_sm_configuration_settings(initial_state: bool,
                                        sm_configuration_screen_page: SMConfigurationScreen,
                                        sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    navigate_to_volume_settings(sm_configuration_screen_page, sm_configuration_settings_screen_page)
    sm_configuration_settings_screen_page.set_toggle_button(VolumeSettingsTab.EXTENSION_LOOP_TOGGLE, initial_state)
    sm_configuration_settings_screen_page.tap(CompartmentLightTab.LIGHT_PREFERENCE_TAB)
    sm_configuration_settings_screen_page.set_toggle_button(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE, initial_state)
    sm_configuration_settings_screen_page.tap(OptionsTab.OPTIONS_TAB)
    sm_configuration_settings_screen_page.set_toggle_button(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON, initial_state)
    sm_configuration_settings_screen_page.set_toggle_button(OptionsTab.MULTI_DRAW_TOGGLE_BUTTON, initial_state)
    sm_configuration_settings_screen_page.tap_done_button()


@when(cfparse('User toggles the SM leak sensor to "{expected_state: bool}"', CONVERTERS))
def toggle_sm_leak_sensor(expected_state: bool, leak_sensor_configuration_screen: LeakSensorScreen):
    leak_sensor_configuration_screen.wait_time_to_load_value(LeakSensorScreenLocators.SM_LEAK_STATUS)
    leak_sensor_configuration_screen.switch_sm_leak_sensor_toggle(expected_state)
    leak_sensor_configuration_screen.tap_done_button()


@when(cfparse('User toggles SM configure leak sensor to "{expected_state: bool}"', CONVERTERS))
def toggle_sm_config_sensor(expected_state: bool, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    sm_configuration_settings_screen_page.switch_sm_config_setting_leak_sensor_toggle(expected_state)
    sm_configuration_settings_screen_page.tap_done_button()


@when('User navigates to the configuration settings screen')
def navigate_sm_configuration_settings(sm_module_config_screen: SMConfigurationScreen,
                                       dashboard_screen_page: DashBoardScreen,
                                       system_settings_screen: SystemSettingsScreen,
                                       instrument_configuration_screen: InstrumentConfigurationScreen,
                                       sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap_configuration_tab()
    instrument_configuration_screen.tap_sm_icon()
    sm_module_config_screen.tap(SMConfigurationScreenLocators.OPTIONS_TAB)
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(
        SMConfigurationSettingsScreenLocators.SM_CONFIGURATION_HEADER, "sm configuration settings screen")


@when('User navigates to the leak sensors screen')
def navigate_sm_configuration_settings(session_system_settings_screen_page: SystemSettingsScreen,
                                       dashboard_screen_page: DashBoardScreen,
                                       leak_sensor_configuration_screen: LeakSensorScreen):
    dashboard_screen_page.tap_system()
    session_system_settings_screen_page.tap_leak_sensor_tab()
    leak_sensor_configuration_screen.validate_leak_sensor_configuration_screen()


@when('User navigates to volume settings screen')
@then('User navigates to volume settings screen')
def navigate_to_volume_settings(sm_configuration_screen_page: SMConfigurationScreen, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_screen_page.validate_sm_configuration_screen()
    sm_configuration_screen_page.tap_volume_settings()
    sm_configuration_settings_screen_page.tap(CompartmentLightTab.LIGHT_PREFERENCE_TAB)
    sm_configuration_settings_screen_page.tap(OptionsTab.OPTIONS_TAB)
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    sm_configuration_settings_screen_page.tap(VolumeSettingsTab.VOLUMES_TAB)


@when('User navigates to chamber light preference settings screen')
def navigate_to_light_preference_settings_screen(sm_configuration_screen_page: SMConfigurationScreen):
    sm_configuration_screen_page.validate_sm_configuration_screen()
    sm_configuration_screen_page.tap(SMConfigurationScreenLocators.COMPARTMENT_LIGHT_TAB)


@when('User navigates to options settings screen')
def navigate_to_options_settings_screen(sm_configuration_screen_page: SMConfigurationScreen):
    sm_configuration_screen_page.validate_sm_configuration_screen()
    sm_configuration_screen_page.tap(SMConfigurationScreenLocators.OPTIONS_TAB)


@when('User taps the volume settings tab')
def tap_volume_settings_tab(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.tap(VolumeSettingsTab.VOLUMES_TAB)


@when('User taps the compartment light preference settings tab')
@then('User taps the compartment light preference settings tab')
def tap_light_preference_tab(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.tap(CompartmentLightTab.LIGHT_PREFERENCE_TAB)


@when('User taps the options tab')
@then('User taps the options tab')
def tap_options_tab(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(
        SMConfigurationSettingsScreenLocators.SM_CONFIGURATION_HEADER, "sm configuration settings screen")
    sm_configuration_settings_screen_page.tap(OptionsTab.OPTIONS_TAB)


@when(cfparse('User selects the "{extension_loop_volume}"'))
def select_single_draw_volume(extension_loop_volume, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(
        VolumeSettingsTab.VOLUMES_HEADER, "sm_volume_screen")
    sm_configuration_settings_screen_page.set_toggle_button(VolumeSettingsTab.EXTENSION_LOOP_TOGGLE, True)
    # time is needed for core selector animation to play out
    time.sleep(3)
    sm_configuration_settings_screen_page.select_sm_configuration(
        extension_loop_volume, SMConfigurationSettingsScreenLocatorsLookup.extension_loop_dictionary)


@when(cfparse('User toggles the light preference to "{door_open_toggle: bool}"', CONVERTERS))
def set_light_preference_toggle(door_open_toggle: bool, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE, "sm_compartment_light_screen")
    sm_configuration_settings_screen_page.set_toggle_button(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE, door_open_toggle)


@when(cfparse('User toggles leak sensor mode "{leak_sensor_enabled: bool}"', CONVERTERS))
def toggle_leak_sensor(leak_sensor_enabled: bool,
                       sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    sm_configuration_settings_screen_page.set_toggle_button(
        OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON, leak_sensor_enabled)


@when(cfparse('User toggles multi draw mode "{multi_draw_enabled: bool}"', CONVERTERS))
def toggle_multi_draw_mode(multi_draw_enabled: bool, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(
        OptionsTab.OPTIONS_HEADER, "sm_options_screen")
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    sm_configuration_settings_screen_page.set_toggle_button(OptionsTab.MULTI_DRAW_TOGGLE_BUTTON, multi_draw_enabled)


@when('User disable the Extension loop installed')
def disable_extension_loop_installed(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.disable_extension_loop()
    sm_configuration_settings_screen_page.wait_till_element_is_invisible(VolumeSettingsTab.EXTENSION_LOOP_VOLUME,
                                                                         sm_configuration_settings_screen_page.wait_time)


@when(cfparse('User switches the "{toggle_name}" to "{new_toggle_state: bool}"', CONVERTERS))
def switch_sm_configuration_toggle(new_toggle_state: bool, toggle_name, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    if toggle_name == SMConfigurationScreenConstants.VolumesToggle:
        sm_configuration_settings_screen_page.set_toggle_button(VolumeSettingsTab.EXTENSION_LOOP_TOGGLE, new_toggle_state)
    elif toggle_name == SMConfigurationScreenConstants.CompartmentLight:
        sm_configuration_settings_screen_page.set_toggle_button(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE, new_toggle_state)
    elif toggle_name == SMConfigurationScreenConstants.LeakToggleOption:
        sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
        sm_configuration_settings_screen_page.set_toggle_button(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON, new_toggle_state)
    elif toggle_name == SMConfigurationScreenConstants.MultiDrawOption:
        sm_configuration_settings_screen_page.set_toggle_button(OptionsTab.MULTI_DRAW_TOGGLE_BUTTON, new_toggle_state)
    else:
        assert False, f"Incorrect toggle name provided. Expected: {SMConfigurationScreenConstants.VolumesToggle} or \
                         {SMConfigurationScreenConstants.CompartmentLight} or {SMConfigurationScreenConstants.LeakToggleOption} or \
                         {SMConfigurationScreenConstants.MultiDrawOption}. Actual Toggle Name: {toggle_name}"


@when('User cancels the change')
def tap_cancel_button(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.tap_cancel_button()


@when('User confirms the configuration settings for the sample manager')
def tap_done_button(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.tap_done_button()


@then(cfparse('Validate "{expected_extension_loop_volume}" option has been selected in volume settings'))
def validate_volume_settings_option(expected_extension_loop_volume, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    if expected_extension_loop_volume == SMConfigurationScreenConstants.HunderedMicroLitreVolume:
        sm_configuration_settings_screen_page.wait_for_extension_loop_active()
    for actual_extension_loop_volume in SMConfigurationScreenConstants.MultiDrawDisabledVolumesList:
        is_extension_loop_volume_enabled = sm_configuration_settings_screen_page.validate_sm_configuration(
            actual_extension_loop_volume, SMConfigurationSettingsScreenLocatorsLookup.extension_loop_dictionary)
        if is_extension_loop_volume_enabled:
            assert actual_extension_loop_volume == expected_extension_loop_volume, f"The Extension loop volume value {expected_extension_loop_volume} \
                                                        is not selected. Expected: {expected_extension_loop_volume} Actual: {actual_extension_loop_volume}"


@then(cfparse('User validates the "{expected_door_open_toggle: bool}" state', CONVERTERS))
def validate_door_open_toggle(expected_door_open_toggle: bool, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    actual_door_open_toggle = sm_configuration_settings_screen_page.is_toggle_component_enabled(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE)
    assert actual_door_open_toggle == expected_door_open_toggle, \
        f" The Door Open Toggle was not as expected. Expected Door Open Toggle: {expected_door_open_toggle}. Actual: {actual_door_open_toggle}"


@then(cfparse('Validate options settings with "{leak_sensor_enabled: bool}" and "{multi_draw_enabled: bool}"', CONVERTERS))
def validate_options_settings(leak_sensor_enabled: bool, multi_draw_enabled: bool,
                              sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    current_option_settings = get_option_settings(sm_configuration_settings_screen_page)

    expected_option_settings = build_option_settings(leak_sensor_enabled, multi_draw_enabled)
    assert_option_settings(current_option_settings, expected_option_settings)


@then(cfparse('User validates the SM configure leak sensor state is "{expected_state: bool}"', CONVERTERS))
def validate_sm_configuration_switch_state(expected_state: bool,
                                           sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    actual_leak_toggle_state = sm_configuration_settings_screen_page.is_toggle_component_enabled(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON)
    assert actual_leak_toggle_state == expected_state, f"The SM leak detection toggle is not as expected. Expected:{expected_state}. \
                                                            Actual: {actual_leak_toggle_state}"


@then(cfparse('User validates the SM leak sensor state is "{expected_leak_sensor_state: bool}"', CONVERTERS))
def validate_sm_leak_sensor_switch_state(expected_leak_sensor_state: bool,
                                         leak_sensor_configuration_screen: LeakSensorScreen):
    leak_sensor_configuration_screen.wait_time_to_load_value(LeakSensorScreenLocators.SM_LEAK_STATUS)
    actual_leak_sensor_state = leak_sensor_configuration_screen.is_toggle_component_enabled(LeakSensorScreenLocators.SM_LEAK_SENSOR)
    assert actual_leak_sensor_state == expected_leak_sensor_state, \
        f"The SM leak detection toggle is not as expected. Expected:{expected_leak_sensor_state} Actual: {actual_leak_sensor_state}"


@then('User validates the extension loop volume is not shown')
def validate_extension_loop_volume(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    actual_result = sm_configuration_settings_screen_page.is_displayed(VolumeSettingsTab.EXTENSION_LOOP_VOLUME)
    assert not actual_result, f"The extension loop volume is being displayed even after disabling extension loop installed. Expected: {actual_result}. \
                                    Actual: {not actual_result}"


@then(cfparse('User validates that all the toggles are "{expected_toggle_state: bool}"', CONVERTERS))
def validate_toggle_changes_not_saved(expected_toggle_state: bool, sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    actual_extension_loop_volume_state = sm_configuration_settings_screen_page.is_toggle_component_enabled(VolumeSettingsTab.EXTENSION_LOOP_TOGGLE)
    assert actual_extension_loop_volume_state, \
        f"Extension Loop Toggle was not as expected. Expected Extension Loop Toggle {expected_toggle_state}. Actual: {actual_extension_loop_volume_state}"
    sm_configuration_settings_screen_page.tap(CompartmentLightTab.LIGHT_PREFERENCE_TAB)
    actual_door_open_toggle_state = sm_configuration_settings_screen_page.is_toggle_component_enabled(CompartmentLightTab.LIGHT_PREFERENCE_TOGGLE)
    assert actual_door_open_toggle_state, \
        f"When the door is open toggle was not as expected. Expected Door Open Toggle: {expected_toggle_state}. Actual: {actual_door_open_toggle_state}"
    sm_configuration_settings_screen_page.tap(OptionsTab.OPTIONS_TAB)
    sm_configuration_settings_screen_page.wait_time_to_load_value(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON_STATUS)
    actual_leak_sensor_toggle_state = sm_configuration_settings_screen_page.is_toggle_component_enabled(OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON)
    assert actual_leak_sensor_toggle_state, \
        f"Leak sensor toggle was not as expected. Expected Leak Sensor Toggle: {expected_toggle_state} Actual:  {actual_leak_sensor_toggle_state}"
    actual_multi_draw_toggle_state = sm_configuration_settings_screen_page.is_toggle_component_enabled(OptionsTab.MULTI_DRAW_TOGGLE_BUTTON)
    assert actual_multi_draw_toggle_state, \
        f"Multi Draw toggle was not as expected. Expected Multi Draw Toggle: {expected_toggle_state} but was found to be  {actual_multi_draw_toggle_state}"


def build_option_settings(leak_sensor_enabled, multi_draw_enabled) -> OptionSettings:
    """
    This function builds the expected data/condition from the given parameters that comes from feature file
    @param auto_rotate_samples_enabled: bool type date from the feature file
    @param leak_sensor_enabled:  bool type date from the feature file
    @param multi_draw_enabled:  bool type date from the feature file
    @return: OptionSettings

    """
    option_settings = OptionSettings()
    option_settings.leak_sensor_enabled = TypeConverter.to_bool(leak_sensor_enabled)
    option_settings.multi_draw_enabled = TypeConverter.to_bool(multi_draw_enabled)
    return option_settings


def get_option_settings(sm_configuration_settings_screen_page: SMConfigurationSettingsScreen) -> OptionSettings:
    """
    This function gets the current condition of the component toggle button and returns it as OptionSettings object type.
    which can be use to validate its property
    @param sm_configuration_settings_screen_page: This is fixture where all the user action on configuration settings page located
    @return: OptionSettings
    """
    current_option_settings = OptionSettings()
    current_option_settings.leak_sensor_enabled = sm_configuration_settings_screen_page.is_toggle_component_enabled(
        OptionsTab.LEAK_SENSOR_TOGGLE_BUTTON)
    current_option_settings.multi_draw_enabled = sm_configuration_settings_screen_page.is_toggle_component_enabled(
        OptionsTab.MULTI_DRAW_TOGGLE_BUTTON)
    return current_option_settings


def assert_option_settings(current_option_settings, expected_option_settings):
    """
    This function validate the current options settings with the expected option settings
    @param current_option_settings:
    @param expected_option_settings:
    """
    assert current_option_settings.leak_sensor_enabled == expected_option_settings.leak_sensor_enabled, f" The current leak sensor option is" \
                                                                                                        f" {current_option_settings.leak_sensor_enabled}"
    assert current_option_settings.multi_draw_enabled == expected_option_settings.multi_draw_enabled, f" The current multi draw option is " \
                                                                                                      f"{current_option_settings.multi_draw_enable}"


@then(cfparse('User validates the volume options and "{multi_draw_installation_text}" depending on "{multi_draw_enabled: bool}"', CONVERTERS))
def validate_multi_draw_volume_options(multi_draw_installation_text, multi_draw_enabled: bool,
                                       sm_configuration_settings_screen_page: SMConfigurationSettingsScreen):
    sm_configuration_settings_screen_page.validate_sm_configuration_settings_screen(VolumeSettingsTab.VOLUMES_HEADER, "sm_volume_screen")
    multi_draw_read_back_message = sm_configuration_settings_screen_page.get_text(VolumeSettingsTab.MULTI_DRAW_READ_BACK_MESSAGE)
    if multi_draw_enabled:
        assert sm_configuration_settings_screen_page.is_displayed(VolumeSettingsTab.TWO_THOUSAND_MICRO_LITRE_OPTION), \
            f"Maximum extension loop volume of {SMConfigurationScreenConstants.TwoThousandMicroLitreVolume} micro litre is not displayed even when Multi draw is {multi_draw_enabled}"
        assert multi_draw_installation_text == multi_draw_read_back_message, \
            f"Multi draw read back message is not as expected. Expected Message: {multi_draw_installation_text} Actual Message: {multi_draw_read_back_message}"
    else:
        assert not sm_configuration_settings_screen_page.is_displayed(VolumeSettingsTab.TWO_THOUSAND_MICRO_LITRE_OPTION), \
            f"Maximum extension loop volume of {SMConfigurationScreenConstants.TwoThousandMicroLitreVolume} micro litre is displayed even when Multi draw is {multi_draw_enabled}"
        assert multi_draw_installation_text == multi_draw_read_back_message, \
            f"Multi draw read back message is not as expected. Expected Message: {multi_draw_installation_text} Actual Message: {multi_draw_read_back_message}"
