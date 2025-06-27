import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import AmbientTemperatureConditionCardConstants
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SampleManager.ambient_temperature_settings_screen import AmbientTemperatureSettingsScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.ambient_temperature_condition_card import \
    AmbientTemperatureSettingScreenLocators
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../../UI/features/HomeScreen/SampleManager/ambient_temperature_condition_card.feature')
logger = Logger(__name__)


@pytest.fixture
def ambient_temperature_settings_page(page_builder):
    page = page_builder(AmbientTemperatureSettingsScreen)
    return page


@given('Navigate to the ambient temperature settings screen')
def tap_sample_temperature_settings_gear_icon(sample_manager_home_screen_page: SampleManagerHomeScreen):
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    current_ambient_temperature = sample_manager_home_screen_page.get_ambient_temperature()
    sample_manager_home_screen_page.set_current_ambient_temperature(current_ambient_temperature)
    logger.info(f"current_ambient_temperature ==== > {current_ambient_temperature}")
    sample_manager_home_screen_page.tap_room_temperature_condition_card()
    logger.info("\n*******************The test starts for Ambient temperature condition card***********************")


@given('User validate the information text')
def validate_info_text(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()
    expected_text = ambient_temperature_settings_page.get_container_text(AmbientTemperatureSettingScreenLocators.INFORMATION_TEXT)
    actual_text = AmbientTemperatureConditionCardConstants.InformationText
    assert actual_text == expected_text, f"actual_text ==>> {actual_text}"


@when(cfparse('Set target ambient temperature as "{ambient_temperature}"'))
def set_target_ambient_temperature(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen, ambient_temperature):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()

    ambient_temperature_settings_page.tap_toggle_button_on(AmbientTemperatureSettingScreenLocators.TOGGLE_BUTTON)
    ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.AMBIENT_TEMPERATURE_LIST, ambient_temperature)
    current_button_state = ambient_temperature_settings_page.is_disabled(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)
    assert current_button_state is False, " The default button is not disabled"


@when('Navigate to the ambient temperature settings screen')
def tap_sample_temperature_settings_gear_icon1(sample_manager_home_screen_page: SampleManagerHomeScreen):
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    sample_manager_home_screen_page.tap_room_temperature_condition_card()


@when(cfparse('User sets the "{ambient_tolerance_temperature}" and "{tolerance_range}"'))
def set_tolerance_ambient_temperature(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen, ambient_tolerance_temperature, tolerance_range):
    
        ambient_temperature_settings_page.validate_room_temperature_settings_screen()
        ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.TOLERANCE_TEMPERATURE_LIST, ambient_tolerance_temperature)
        ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.TOLERANCE_RANGE_LIST, tolerance_range)
        ambient_temperature_settings_page.validate_display_info(ambient_tolerance_temperature, tolerance_range)
        current_button_state = ambient_temperature_settings_page.is_disabled(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)
        assert current_button_state is False, " The default button is disabled"

@when('User confirms the settings')  
def confirm_settings(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen): 
    ambient_temperature_settings_page.tap_done_button()


@when(cfparse('User sets the ambient temperature as "{ambient_tolerance_temperature}" and tolerance range as "{tolerance_range}"'))
def select_tolerance_ambient_temperature(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen, ambient_tolerance_temperature, tolerance_range):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()
    ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.TOLERANCE_TEMPERATURE_LIST, ambient_tolerance_temperature)
    ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.TOLERANCE_RANGE_LIST, tolerance_range)
    ambient_temperature_settings_page.validate_display_info(ambient_tolerance_temperature, tolerance_range)
    current_button_state = ambient_temperature_settings_page.is_disabled(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)
    assert current_button_state is False, " The default button is disabled"


@then(cfparse('User validates the display info for "{ambient_tolerance_temperature}" and "{tolerance_range}"'))
def validate_display_message(sample_manager_home_screen_page: SampleManagerHomeScreen, ambient_tolerance_temperature, tolerance_range):
    ambient_tolerance_temperature = float(ambient_tolerance_temperature)
    tolerance_range = float(tolerance_range)
    current_ambient_temperature = sample_manager_home_screen_page.get_ambient_temperature()
    current_ambient_temperature = float(current_ambient_temperature)
    lowest_temperature_range = ambient_tolerance_temperature - tolerance_range
    highest_temperature_range = ambient_tolerance_temperature + tolerance_range

    logger.info(f"lowest_temperature_range======>{lowest_temperature_range}")
    logger.info(f"current_ambient_temperature======>{current_ambient_temperature}")
    logger.info(f"highest_temperature_range======>{highest_temperature_range}")

    if not lowest_temperature_range <= current_ambient_temperature <= highest_temperature_range:
        logger.info(f"When the ambient temperature is not in the tolerance range")
        readback_message = sample_manager_home_screen_page.get_text(SampleManagerHomeScreenLocators.AMBIENT_TEMPERATURE_READBACK_MESSAGE)
        assert readback_message == AmbientTemperatureConditionCardConstants.OutOfRangeMessage
        sample_manager_home_screen_page.validate_title_icon_color(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_TITLE_ICON,
                                                                  AmbientTemperatureConditionCardConstants.TitleIconTemperatureOutOfRangeColorCode)
    else:
        sample_manager_home_screen_page.validate_title_icon_color(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_TITLE_ICON,
                                                                  AmbientTemperatureConditionCardConstants.TitleIconTemperatureInRangeColorCode)


@when(cfparse('user sets the ambient temperature range as "{tolerance_range}"'))
def set_tolerance_range(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen, tolerance_range):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()
    ambient_temperature_settings_page.tap_toggle_button_on(AmbientTemperatureSettingScreenLocators.TOGGLE_BUTTON)
    ambient_temperature_settings_page.set_spinner_value(AmbientTemperatureSettingScreenLocators.TOLERANCE_RANGE_LIST, tolerance_range)


@then("User validates the default button is disabled")
def validate_default_button(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    try:
        time.sleep(20)
        current_button_state = ambient_temperature_settings_page.is_disabled(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)
        assert current_button_state is False, " The default button is disabled"

    finally:
        ambient_temperature_settings_page.tap_done_button()


@when('User turns off the toggle button')
def toggle_button_turn_off(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()
    ambient_temperature_settings_page.tap_toggle_button_off(AmbientTemperatureSettingScreenLocators.TOGGLE_BUTTON)


@when('User taps the default button')
def validate_done_button(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    ambient_temperature_settings_page.validate_room_temperature_settings_screen()
    ambient_temperature_settings_page.tap_toggle_button_on(AmbientTemperatureSettingScreenLocators.TOGGLE_BUTTON)
    ambient_temperature_settings_page.tap(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)


@then('Validate the spinner component is invisible')
def validate_spinner_component(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    try:
        ambient_temperature_settings_page.validate_room_temperature_settings_screen()
        is_spinner_component_exists = ambient_temperature_settings_page.is_scroll_window_exists(AmbientTemperatureSettingScreenLocators.SCROLL_WINDOW_HEADER)
        time.sleep(1)
        assert is_spinner_component_exists is False, f" The spinner component does exists"

    finally:
        ambient_temperature_settings_page.tap_cancel_button()


@then('User validate the temperature set to default')
def validate_default_temperature(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    try:

        temperature_set = ambient_temperature_settings_page.get_text(AmbientTemperatureSettingScreenLocators.TEMPERATURE)
        logger.info(f"temperature_set ===>{temperature_set}")
        assert temperature_set == AmbientTemperatureConditionCardConstants.DefaultTemperature
        current_button_state = ambient_temperature_settings_page.is_disabled(AmbientTemperatureSettingScreenLocators.TEMPERATURE_DEFAULT_BUTTON)
        assert current_button_state, " The default button is not disabled"

    finally:
        ambient_temperature_settings_page.tap_cancel_button()
        logger.info("\n*******************The test ends for Ambient temperature condition card***********************")


@then(cfparse('User validates the displayed "{ambient_temperature}" and "{tolerance_temperature}" in the settings screen'))
def validate_temperature(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen, ambient_temperature, tolerance_temperature):        
        temperature_set = ambient_temperature_settings_page.get_text(AmbientTemperatureSettingScreenLocators.TEMPERATURE)
        logger.info(f" The temperature displayed in the settings screen===>>{temperature_set}")
        temperature_set = temperature_set.split()
        ambient_temperature_displayed = temperature_set[0]
        tolerance_temperature_set = temperature_set[2]
        logger.info(f" The ambient temperature displayed in the settings screen===>>{ambient_temperature_displayed}")
        logger.info(f" The tolerance temperature displayed in the settings screen===>>{tolerance_temperature_set}")
        assert ambient_temperature_displayed == ambient_temperature, f"ambient_temperature_displayed==>>{ambient_temperature_displayed}"
        assert tolerance_temperature_set == tolerance_temperature, f"tolerance_temperature_set===>>>{tolerance_temperature_set}"          
       
        logger.info("\n*******************The test ends for Ambient temperature condition card***********************")


@then(cfparse('Validate the condition card readback messages for "{ambient_temperature}" and "{tolerance_temperature}"'))
def validate_read_back_messages(sample_manager_home_screen_page: SampleManagerHomeScreen, ambient_temperature, tolerance_temperature):
    time.sleep(5)  # TODO WIll be removed once we get the correct requirement
    ambient_temperature = TypeConverter.to_float(ambient_temperature)
    tolerance_temperature = TypeConverter.to_float(tolerance_temperature)
    lowest_temperature_range = ambient_temperature - tolerance_temperature
    highest_temperature_range = ambient_temperature + tolerance_temperature
    start_time = time.time()
    while time.time() - start_time < AmbientTemperatureConditionCardConstants.MaxTimeToReachTemperature:

        current_temperature = sample_manager_home_screen_page.get_temperature(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_NUMBER_VALUE,
                                                                              SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_DECIMAL_VALUE)
        current_temperature = TypeConverter.to_float(current_temperature)
        sample_manager_home_screen_page.set_ambient_temperature(current_temperature)

        if current_temperature is not None:
            if lowest_temperature_range <= current_temperature <= highest_temperature_range:
                logger.info(f"The current temperature is with in the range   {current_temperature}")
                sample_manager_home_screen_page.validate_final_title_icon_color(SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_TITLE_ICON,
                                                                                AmbientTemperatureConditionCardConstants.TitleIconTemperatureInRangeColorCode)
            else:
                current_read_back_message = sample_manager_home_screen_page.get_room_temperature_read_back_value()
                logger.info("The current temperature is out of range")
                sample_manager_home_screen_page.validate_final_title_icon_color(
                    SampleManagerHomeScreenLocators.ROOM_TEMPERATURE_TITLE_ICON,
                    AmbientTemperatureConditionCardConstants.TitleIconTemperatureOutOfRangeColorCode)
                assert current_read_back_message == AmbientTemperatureConditionCardConstants.OutOfRangeMessage
            break
        time.sleep(1)
    logger.info("\n*******************The test ends for Ambient temperature condition card***********************")


@then('The user validates ambient_temperature info in the sample manager card reader')
def validate_card_reader(dashboard_screen_page: DashBoardScreen, sample_manager_home_screen_page: SampleManagerHomeScreen):
    try:
        ambient_temperature = sample_manager_home_screen_page.get_ambient_temperature()
        expected_temperature = TypeConverter.to_float(ambient_temperature)
        dashboard_screen_page.tap_home()
        dashboard_screen_page.validate_dashboard_screen()
        actual_temperature = dashboard_screen_page.get_temperature(TopLevelDashBoardScreenLocators.AMBIENT_TEMPERATURE,
                                                                   TopLevelDashBoardScreenLocators.AMBIENT_TEMPERATURE_AFTER_DECIMAL)

        actual_temperature = TypeConverter.to_float(actual_temperature)

        assert actual_temperature == expected_temperature, f" The actual temperature is {actual_temperature}"
        actual_temperature_units = dashboard_screen_page.get_temperature_units(TopLevelDashBoardScreenLocators.AMBIENT_TEMPERATURE_UNITS)
        expected_temperature_units = AmbientTemperatureConditionCardConstants.TemperatureUnits
        assert actual_temperature_units == expected_temperature_units, f"actual sample temperature unit in card reader => {actual_temperature_units}"

    finally:
        dashboard_screen_page.tap_sample_manager_schematic_icon()
    logger.info("\n*******************The test ends for ambient temperature condition card***********************")


@when('The user confirms the set temperature')
def tap_done_button(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    ambient_temperature_settings_page.tap_done_button()


@when("User cancels the settings")
def tap_cancel_button(ambient_temperature_settings_page: AmbientTemperatureSettingsScreen):
    ambient_temperature_settings_page.tap_cancel_button()
