import time
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.TuvDetector.tuv_detector_home_screen import TUVDetectorHomeScreen
from web_framework.kiosk.pages.Home.TuvDetector.wavelength_settings_screen import WavelengthSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/TuvDetector/wavelength_condition_card.feature')
logger = Logger("test_wavelength_condition_card")


@pytest.fixture
def tuv_detector_home_screen_page(session_dash_board_screen_page: DashBoardScreen, page_builder):
    session_dash_board_screen_page.tap_home()
    session_dash_board_screen_page.tap_tuv_schematic_icon()
    page = page_builder(TUVDetectorHomeScreen)
    page.implicitly_wait()
    return page


@pytest.fixture
def wavelength_setting_screen_page(page_builder):
    page = page_builder(WavelengthSettingsScreen)
    page.implicitly_wait()
    return page


@given('Navigate to the wavelength settings screen')
def navigate_to_tuv_settings_screen(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                    wavelength_setting_screen_page: WavelengthSettingsScreen):
    logger.info("*************The test starts for the wavelength condition card*****************************")
    tuv_detector_home_screen_page.tap_wavelength_setting_icon()
    wavelength_setting_screen_page.validate_wavelength_setting_screen()


@then('Navigate to the wavelength settings screen')
@when('Navigate to the wavelength settings screen')
def tap_wavelength_setting_icon(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                wavelength_setting_screen_page: WavelengthSettingsScreen):
    tuv_detector_home_screen_page.tap_wavelength_setting_icon()
    wavelength_setting_screen_page.validate_wavelength_setting_screen()


@when(cfparse('Enter the wavelength "{actual_first_wave_length}"'))
def enter_wavelength(wavelength_setting_screen_page: WavelengthSettingsScreen, actual_first_wave_length):
    wavelength_setting_screen_page.validate_wavelength_setting_screen()
    wavelength_setting_screen_page.enter_first_wavelength(actual_first_wave_length)


@when('Navigate to the wavelength conditional card')
def tap_done_button(wavelength_setting_screen_page: WavelengthSettingsScreen):
    wavelength_setting_screen_page.tap_done_button()


@when("The user taps the cancel button")
def tap_cancel_button(wavelength_setting_screen_page: WavelengthSettingsScreen):
    wavelength_setting_screen_page.tap_cancel_button()


@then(cfparse('Validate the single wave length info "{expected_first_wave_length}" on the condition card'))
def validate_conditional_card_single_wavelength_info(tuv_detector_home_screen_page: TUVDetectorHomeScreen, expected_first_wave_length):
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    start_time = time.time()
    while time.time() - start_time <= 5:
        actual_single_wavelength = tuv_detector_home_screen_page.get_first_wavelength()
        logger.info(f"The value of the wavelength in the condition card {actual_single_wavelength}")
        if actual_single_wavelength == expected_first_wave_length:
            break
        time.sleep(.5)

    logger.info(f"The value of the wavelength in the condition card {actual_single_wavelength}")
    assert actual_single_wavelength == expected_first_wave_length, f"failed to show the set wavelength, actual first wavelength => {actual_single_wavelength} in the  wavelength conditional card "


@then(cfparse('Validate wavelength current info "{expected_first_wave_length}" "{expected_second_wave_length}" "{expected_wavelength_mode}" on the setting screen'))
def validate_setting_screen_wavelength_info(wavelength_setting_screen_page: WavelengthSettingsScreen, expected_first_wave_length,
                                            expected_second_wave_length, expected_wavelength_mode):
    try:
        wavelength_setting_screen_page.validate_wavelength_setting_screen()
        actual_first_wavelength = wavelength_setting_screen_page.get_first_wavelength()
        actual_second_wavelength = wavelength_setting_screen_page.get_second_wavelength()
        actual_wavelength_mode = wavelength_setting_screen_page.get_wavelength_mode()
        assert actual_first_wavelength == expected_first_wave_length, f"failed to show the set wavelength, actual first wavelength => {actual_first_wavelength} in the setting screen' "
        assert actual_second_wavelength == expected_second_wave_length, f"failed to show the set wavelength, actual second wavelength => {actual_second_wavelength} in the setting screen' "
        assert actual_wavelength_mode == expected_wavelength_mode, f"failed to show the set wavelength mode, actual wavelength mode => {actual_wavelength_mode} in the setting screen' "

    finally:
        wavelength_setting_screen_page.tap_done_button()
        logger.info("*************The test ends for the wavelength condition card*****************************")


@then('Validate the user cannot navigate to the wavelength conditional card screen')
def validate_setting_screen(wavelength_setting_screen_page: WavelengthSettingsScreen):
    wavelength_setting_screen_page.validate_wavelength_setting_screen()
    wavelength_setting_screen_page.tap_cancel_button()
    logger.info("*************The test ends for the wavelength condition card*****************************")


@when('Select the dual wavelength mode')
def select_dual_wavelength_mode(wavelength_setting_screen_page: WavelengthSettingsScreen):
    is_dual_mode_enabled = wavelength_setting_screen_page.is_dual_mode_enabled()
    if is_dual_mode_enabled:
        logger.info("The dual mode is on")
    else:
        logger.info("Tap the selector component to enable the dual mode")
        wavelength_setting_screen_page.tap_dual_selector_component()
        wavelength_setting_screen_page.validate_single_wave_length_mode_enabled()
        wavelength_setting_screen_page.validate_dual_wave_length_mode_enabled()


@when(cfparse('Enter the dual wavelength "{actual_first_wave_length}" "{actual_second_wave_length}"'))
def enter_dual_wavelength(wavelength_setting_screen_page: WavelengthSettingsScreen, actual_first_wave_length,
                          actual_second_wave_length):
    logger.info(f"from the enter the dual wavelength actual first {actual_first_wave_length},  second {actual_second_wave_length}")
    wavelength_setting_screen_page.validate_wavelength_setting_screen()
    wavelength_setting_screen_page.enter_first_wavelength(actual_first_wave_length)
    wavelength_setting_screen_page.enter_second_wavelength(actual_second_wave_length)


@then(cfparse('Validate dual wavelength "{expected_first_wave_length}" "{expected_second_wave_length}" on the condition card'))
def validate_conditional_card_dual_wavelength_info(tuv_detector_home_screen_page: TUVDetectorHomeScreen,
                                                   expected_first_wave_length, expected_second_wave_length):
    tuv_detector_home_screen_page.validate_tuv_detector_home_screen()
    start_time = time.time()
    while time.time() - start_time <= 5:
        actual_first_wavelength = tuv_detector_home_screen_page.get_first_wavelength()
        actual_second_wavelength = tuv_detector_home_screen_page.get_second_wavelength()
        logger.info(f" The  actual wavelength is first =>{actual_first_wavelength} second =>{actual_second_wavelength}")

        if actual_first_wavelength == expected_first_wave_length and actual_second_wavelength == expected_second_wave_length:
            break
        time.sleep(.5)
    assert actual_first_wavelength == expected_first_wave_length, f"failed to show the set wavelength, actual first wavelength => {actual_first_wavelength} in the  wavelength conditional card "
    assert actual_second_wavelength == expected_second_wave_length, f"failed to show the set wavelength, actual second wavelength => {actual_second_wavelength} in the  wavelength conditional card "
