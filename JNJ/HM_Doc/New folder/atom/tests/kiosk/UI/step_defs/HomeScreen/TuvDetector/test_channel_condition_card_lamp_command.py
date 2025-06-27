import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.commands import CommandsConstants
from web_framework.kiosk.common.Constants.UI.condition_card_constants import TUVConditionCardConstants
from web_framework.kiosk.pages.Commands.commands_screen import CommandsScreen
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.TuvDetector.channel_settings_screen import ChannelSettingsScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Locators.Home.TuvDetector.channel_common_condition_card import ChannelSettingScreenLocators
from web_framework.kiosk.pages.Locators.Home.TuvDetector.tuv_home_screen import TUVHomeScreenLocators as hsl
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/TuvDetector/channel_condition_card_lamp_on.feature',
              '../../../features/HomeScreen/TuvDetector/channel_condition_card_lamp_off.feature')

logger = Logger("test_channel_condition_card_lamp_on")


@given("Turn on the Lamp")
def turn_lamp_on(dashboard_screen_page: DashBoardScreen, command_screen_page: CommandsScreen):
    dashboard_screen_page.tap_commands()
    command_screen_page.turn_on_lamp()


@given("Turn off the Lamp")
def turn_lamp_off(dashboard_screen_page: DashBoardScreen, command_screen_page: CommandsScreen):
    dashboard_screen_page.tap_commands()
    command_screen_page.turn_off_lamp()


@given("User navigates to TUV home screen")
def navigate_to_tuv_home_screen(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_plots_icon()
    dashboard_screen_page.tap_home()
    dashboard_screen_page.tap_tuv_schematic_icon()


@pytest.fixture
def channel_settings_screen_page(page_builder):
    page = page_builder(ChannelSettingsScreen)
    page.implicitly_wait()
    return page


@when("The user taps the cancel button")
def tap_cancel_button(channel_settings_screen_page: ChannelSettingsScreen):
    channel_settings_screen_page.tap_cancel_button()


@then(cfparse('Validate the single wave length info "{expected_first_wavelength}" on the condition card'))
def validate_conditional_card_single_wavelength_info(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                                     expected_first_wavelength):
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    start_time = time.time()
    while time.time() - start_time <= 10:
        actual_single_wavelength = tuv_detector_home_screen_page.get_first_wavelength()
        logger.info(f"The value of the wavelength in the condition card {actual_single_wavelength}")
        if actual_single_wavelength == expected_first_wavelength:
            break
        time.sleep(1)

    logger.info(f"The value of the wavelength in the condition card {actual_single_wavelength}")
    assert actual_single_wavelength == expected_first_wavelength, f"failed to show the set wavelength, actual first wavelength => {actual_single_wavelength} in the  wavelength conditional card "


@when('Navigate to the channel A settings screen')
def navigate_to_channel_a_settings_screen(tuv_detector_home_screen_page: TUVDetectorHomeScreen):
    logger.info("*************The test starts for the channel A condition card*****************************")
    tuv_detector_home_screen_page.tap_channel_a_condition_card()


@when(cfparse('User selects the wavelength mode "{wavelength_mode}"'))
def select_wavelength_mode(channel_settings_screen_page: ChannelSettingsScreen, wavelength_mode):
    channel_settings_screen_page.validate_wavelength_setting_screen()
    if wavelength_mode == "Single":
        channel_settings_screen_page.tap_single_mode_selector_component()
        logger.info("The single wavelength is tapped")
    else:
        channel_settings_screen_page.tap_dual_mode_selector_component()
        logger.info("The dual wavelength is tapped")


@when(cfparse('Enter the wavelength "{actual_first_wave_length}"'))
def enter_wavelength(channel_settings_screen_page: ChannelSettingsScreen, actual_first_wave_length):
    channel_settings_screen_page.validate_wavelength_setting_screen()
    channel_settings_screen_page.tap_single_mode_selector_component()
    channel_settings_screen_page.set_spinner_value(ChannelSettingScreenLocators.WAVELENGTH_LIST,
                                                   actual_first_wave_length)
    time.sleep(1)  ## will be removed once ins-26326
    channel_settings_screen_page.validate_first_wavelength(actual_first_wave_length)


@when('User confirms the settings')
def tap_done_button(channel_settings_screen_page: ChannelSettingsScreen):
    channel_settings_screen_page.tap_done_button()


@then(cfparse('Validate Channel A condition card for "{expected_first_wavelength}" for "{lamp_state}"'))
def validate_channel_a_condition_card(tuv_detector_home_screen_page: TUVDetectorHomeScreen, dashboard_screen_page: DashBoardScreen,
                                      lamp_state, expected_first_wavelength):
    try:
        wait_time = 10
        start_time = time.time()
        while time.time() - start_time <= wait_time:
            current_first_wavelength = tuv_detector_home_screen_page.get_first_wavelength()
            logger.info(
                f" The  actual wavelength =>{current_first_wavelength} ")
            logger.info(
                f" The  expected wavelength  =>{expected_first_wavelength} ")

            if current_first_wavelength == expected_first_wavelength:
                break
            time.sleep(1)

        assert current_first_wavelength == expected_first_wavelength, \
            f"failed to show the set wavelength, actual first wavelength => {current_first_wavelength} in the  wavelength conditional card "

        if lamp_state == CommandsConstants.LampStateOn:

            actual_single_absorbance_value = tuv_detector_home_screen_page.get_channel_a_absorbance_value()
            actual_single_absorbance_value = TypeConverter.to_float(actual_single_absorbance_value)
            channel_a_absorbance_unit = tuv_detector_home_screen_page.get_container_text(hsl.CHANNEL_A_ABSORBANCE_UNITS)
            assert channel_a_absorbance_unit == TUVConditionCardConstants.AbsorbanceUnits, f"channel_a_absorbance_unit is {channel_a_absorbance_unit}"
            logger.info(f"actual_single_absorbance_value====>>>{actual_single_absorbance_value}")
            assert TUVConditionCardConstants.MinAbsorbanceValue < actual_single_absorbance_value < TUVConditionCardConstants.MaxAbsorbanceValue

        elif lamp_state == CommandsConstants.LampStateOff:
            actual_single_absorbance_value = tuv_detector_home_screen_page.get_channel_a_absorbance_value()
            expected_a_value = TUVConditionCardConstants.NoAbsorbanceValue
            actual_read_back_status = tuv_detector_home_screen_page.get_channel_a_status()
            expected_read_back_status = TUVConditionCardConstants.ChannelReadBackStatus
            assert actual_read_back_status == expected_read_back_status, f"The actual read back status is {actual_read_back_status}"
            assert actual_single_absorbance_value == expected_a_value, f" The actual single absorbance value is {actual_single_absorbance_value}"


    finally:
        dashboard_screen_page.tap_home()

        logger.info(
            "*************The test ends for the channel condition card for lamp on *****************************")


@then(cfparse('Validate Channel B condition card for "{expected_second_wavelength}" for "{lamp_state}"'))
def validate_channel_b_condition_card(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                      dashboard_screen_page: DashBoardScreen,
                                      expected_second_wavelength, lamp_state):
    dashboard_screen_page.tap_tuv_schematic_icon()
    try:
        start_time = time.time()
        while time.time() - start_time <= 5:
            current_first_wavelength = tuv_detector_home_screen_page.get_second_wavelength()
            logger.info(
                f" The  actual wavelength is first =>{current_first_wavelength} ")
            if current_first_wavelength == expected_second_wavelength:
                break
            time.sleep(.5)
        assert current_first_wavelength == expected_second_wavelength, f"failed to show the set wavelength, actual first wavelength => {expected_second_wavelength} in the  wavelength conditional card "

        if lamp_state == CommandsConstants.LampStateOn:
            actual_absorbance_value = tuv_detector_home_screen_page.get_channel_b_absorbance_value()
            actual_absorbance_value = TypeConverter.to_float(actual_absorbance_value)
            channel_b_absorbance_unit = tuv_detector_home_screen_page.get_container_text(hsl.CHANNEL_B_ABSORBANCE_UNITS)
            assert channel_b_absorbance_unit == TUVConditionCardConstants.AbsorbanceUnits, f"channel_a_absorbance_unit is {channel_b_absorbance_unit}"
            assert TUVConditionCardConstants.MinAbsorbanceValue < actual_absorbance_value < TUVConditionCardConstants.MaxAbsorbanceValue

        elif lamp_state == CommandsConstants.LampStateOff:
            actual_single_absorbance_value = tuv_detector_home_screen_page.get_channel_b_absorbance_value()
            logger.info(f" actual_single_absorbance_value====={actual_single_absorbance_value}")
            expected_b_value = TUVConditionCardConstants.NoAbsorbanceValue
            actual_read_back_status = tuv_detector_home_screen_page.get_channel_b_status()
            expected_read_back_status = TUVConditionCardConstants.ChannelReadBackStatus
            assert actual_read_back_status == expected_read_back_status, f"The actual read back status is {actual_read_back_status}"
            assert actual_single_absorbance_value == expected_b_value, f" actual single absorbance value => {actual_single_absorbance_value}"


    finally:
        dashboard_screen_page.tap_home()

        logger.info(
            "*************The test ends for the channel condition card for lamp on *****************************")


@then('Validate the user cannot navigate to the wavelength conditional card screen')
def validate_setting_screen(channel_settings_screen_page: ChannelSettingsScreen):
    try:
        channel_settings_screen_page.validate_wavelength_setting_screen()
        is_done_button_inactive = channel_settings_screen_page.is_button_inactive(BasePageLocators.DONE_BUTTON)
        assert is_done_button_inactive, "The Done button is active"
    finally:
        channel_settings_screen_page.tap_cancel_button()

    logger.info("*************The test ends for the channel condition card for lamp on *****************************")


@then(cfparse('Validate dual wavelength "{expected_first_wavelength}" "{expected_second_wavelength}" on the condition card'))
def validate_conditional_card_dual_wavelength_info(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                                   expected_first_wavelength, expected_second_wavelength):
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    start_time = time.time()
    while time.time() - start_time <= 5:
        actual_first_wavelength = tuv_detector_home_screen_page.get_first_wavelength()
        actual_second_wavelength = tuv_detector_home_screen_page.get_second_wavelength()
        logger.info(f" The  actual wavelength is first =>{actual_first_wavelength} second =>{actual_second_wavelength}")

        if actual_first_wavelength == expected_first_wavelength and actual_second_wavelength == expected_second_wavelength:
            break
        time.sleep(.5)

    assert actual_first_wavelength == expected_first_wavelength, f"failed to show the set wavelength, actual first wavelength => {actual_first_wavelength} in the  wavelength conditional card "
    assert actual_second_wavelength == expected_second_wavelength, f"failed to show the set wavelength, actual second wavelength => {actual_second_wavelength} in the  wavelength conditional card "

    logger.info("*************The test ends for the channel A condition card*****************************")


@when('User cancels the settings')
def tap_cancel_button(channel_settings_screen_page: ChannelSettingsScreen):
    channel_settings_screen_page.tap_cancel_button()


@when(cfparse('Enter the dual wavelength "{actual_first_wave_length}" "{actual_second_wave_length}"'))
def enter_dual_wavelength(channel_settings_screen_page: ChannelSettingsScreen, actual_first_wave_length,
                          actual_second_wave_length):
    channel_settings_screen_page.validate_wavelength_setting_screen()
    channel_settings_screen_page.tap(ChannelSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER)
    channel_settings_screen_page.set_spinner_value(ChannelSettingScreenLocators.WAVELENGTH_LIST,
                                                   actual_first_wave_length)
    channel_settings_screen_page.tap(ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER)
    channel_settings_screen_page.set_spinner_value(ChannelSettingScreenLocators.WAVELENGTH_LIST,
                                                   actual_second_wave_length)


@when(cfparse('User enter the dual wavelength "{first_wave_length}" "{second_wave_length}"'))
def enter_dual_wavelength(channel_settings_screen_page: ChannelSettingsScreen, first_wave_length, second_wave_length):
    channel_settings_screen_page.validate_wavelength_setting_screen()
    channel_settings_screen_page.tap(ChannelSettingScreenLocators.SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER)
    channel_settings_screen_page.set_spinner_value(ChannelSettingScreenLocators.WAVELENGTH_LIST,
                                                   first_wave_length)
    channel_settings_screen_page.validate_first_wavelength(first_wave_length)

    channel_settings_screen_page.tap(ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER)
    channel_settings_screen_page.set_spinner_value(ChannelSettingScreenLocators.WAVELENGTH_LIST,
                                                   second_wave_length)
    channel_settings_screen_page.validate_second_wavelength(second_wave_length)


@then(cfparse('Validate "{expected_second_wavelength}" in the settings screen'))
def validate_edit_field(channel_settings_screen_page: ChannelSettingsScreen, expected_second_wavelength):
    try:
        actual_first_wavelength = channel_settings_screen_page.get_text(
            ChannelSettingScreenLocators.DUAL_WAVE_LENGTH_ENTRY_FIELD)
        start_time = time.time()
        while time.time() - start_time <= 5:
            if actual_first_wavelength == expected_second_wavelength:
                break
            time.sleep(1)
        assert actual_first_wavelength == expected_second_wavelength, f"The actual first wavelength value => {actual_first_wavelength}"

    finally:
        channel_settings_screen_page.tap_cancel_button()
        logger.info(
            "*************The test ends for the channel condition card for lamp on *****************************")


@then(cfparse('User validates the TUV card reader for "{wavelength_mode}" "{expected_first_wavelength}" "{expected_second_wavelength}"'))
def validate_card_reader(dashboard_screen_page: DashBoardScreen, wavelength_mode,
                         expected_first_wavelength, expected_second_wavelength):
    current_lamp_state = dashboard_screen_page.get_lamp_state()
    logger.info(f'The current lamp state  {current_lamp_state}')
    actual_first_wavelength = dashboard_screen_page.get_single_wavelength_value()
    assert actual_first_wavelength == expected_first_wavelength

    try:
        if current_lamp_state == CommandsConstants.LampStateOn and wavelength_mode == "Single":
            logger.info("validate card reader when the wavelength is single and lamp is on")
            dashboard_screen_page.validate_lamp_state_on_for_single_wavelength()

        elif current_lamp_state == CommandsConstants.LampStateOn and wavelength_mode == "Dual":
            logger.info("validate card reader when the wavelength is Dual and lamp is on")
            dashboard_screen_page.validate_lamp_on_for_dual_wavelength()

        elif current_lamp_state == CommandsConstants.LampStateOff and wavelength_mode == "Single":
            logger.info("validate card reader when the wavelength is Single and lamp is off")
            dashboard_screen_page.validate_lamp_off_for_single_wavelength()

        elif current_lamp_state == CommandsConstants.LampStateOff and wavelength_mode == "Dual":
            logger.info("validate card reader when the wavelength is dual and lamp is off")
            dashboard_screen_page.validate_lamp_off_for_dual_wavelength(expected_second_wavelength)

    finally:
        dashboard_screen_page.tap_tuv_schematic_icon()
        logger.info(
            "*************The test ends for the channel condition card for lamp on *****************************")


@when('Navigate to the channel B settings Screen')
def tap_channel_b_condition_card(tuv_detector_home_screen_page: TUVDetectorHomeScreen):
    start_time = time.time()
    while time.time() - start_time <= 10:
        is_channel_b_card_visible = tuv_detector_home_screen_page.is_displayed(hsl.CHANNEL_B_CONDITION_CARD)
        logger.info(
            f" is_channel_b_card_visible =>{is_channel_b_card_visible} ")
        if is_channel_b_card_visible:
            break
        time.sleep(1)
    assert is_channel_b_card_visible, f"is_channel_b_card_visible==>>{is_channel_b_card_visible}"
    tuv_detector_home_screen_page.tap_channel_b_condition_card()
