from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_manager_home_screen import SampleManagerHomeScreen
from web_framework.kiosk.pages.Home.SampleManager.sample_pressure_settings_screen import SamplePressureSettingsScreen
from web_framework.kiosk.pages.Locators.Home.SampleManager.sm_home_screen import SampleManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SampleManager/sample_pressure_condition_card.feature')

logger = Logger("test_sample_pressure_condition_card")


@given('User navigates to the sample pressure settings screen')
def navigate_sample_pressure_card(sample_manager_home_screen_page: SampleManagerHomeScreen,
                                  sample_pressure_setting_screen_page: SamplePressureSettingsScreen):
    logger.info("**************************The sample pressure condition card test starts**********************")
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    sample_manager_home_screen_page.tap_sample_pressure_condition_card()
    sample_pressure_setting_screen_page.validate_sample_pressure_settings_screen()


@when('User goes back to the sample pressure settings screen')
def tap_system_pressure_card(sample_manager_home_screen_page: SampleManagerHomeScreen,
                             sample_pressure_setting_screen_page: SamplePressureSettingsScreen):
    sample_manager_home_screen_page.validate_sample_manager_home_screen()
    sample_manager_home_screen_page.tap_sample_pressure_condition_card()
    sample_pressure_setting_screen_page.validate_sample_pressure_settings_screen()


@when(cfparse('User changes the unit to "{sample_pressure_unit}"'))
def select_unit_option(sample_pressure_setting_screen_page: SamplePressureSettingsScreen, sample_pressure_unit):
    sample_pressure_setting_screen_page.validate_sample_pressure_settings_screen()
    logger.info(f"Selecting the following pressure unit========>>>>>>{sample_pressure_unit}")
    sample_pressure_setting_screen_page.select_unit_option(sample_pressure_unit)


@then(cfparse('User validates "{expected_pressure_unit}" in the sample pressure conditional card'))
def validate_sample_pressure_conditional_card(sample_manager_home_screen_page: SampleManagerHomeScreen, dashboard_screen_page,
                                              expected_pressure_unit):
    try:

        sample_manager_home_screen_page.validate_sample_manager_home_screen()
        sample_manager_home_screen_page.wait_time_to_load_value(SampleManagerHomeScreenLocators.SAMPLE_PRESSURE_NUMBER_VALUE)
        actual_sample_pressure_unit = sample_manager_home_screen_page.get_text(
            SampleManagerHomeScreenLocators.SAMPLE_PRESSURE_UNIT)
        assert actual_sample_pressure_unit == expected_pressure_unit, f"The actual system pressure unit is {actual_sample_pressure_unit}"

    finally:
        dashboard_screen_page.tap_home()


@when('User checks the currently selected unit')
def check_current_unit(sample_pressure_setting_screen_page: SamplePressureSettingsScreen):
    assert sample_pressure_setting_screen_page.find_active_unit()


@when('User confirms the unit change')
def tap_done_button(sample_pressure_setting_screen_page: SamplePressureSettingsScreen):
    sample_pressure_setting_screen_page.tap_done_button()


@when('User cancels the unit change')
def tap_cancel_button(sample_pressure_setting_screen_page: SamplePressureSettingsScreen):
    sample_pressure_setting_screen_page.tap_cancel_button()


@then(cfparse('User validates "{expected_pressure_unit}" info in the sample manager card reader'))
def validate_card_reader(dashboard_screen_page: DashBoardScreen, expected_pressure_unit):
    try:
        dashboard_screen_page.wait_time_to_load_value(TopLevelDashBoardScreenLocators.SAMPLE_PRESSURE_VALUE)

        actual_pressure_units = dashboard_screen_page.get_sample_pressure_units()
        logger.info(f"The ====>>>>actual_pressure_units======>>>>>{actual_pressure_units}")
        assert actual_pressure_units == expected_pressure_unit, f"actual_pressure_units=={actual_pressure_units}"

    finally:
        logger.info(f" user taps the schematic icon ")
        dashboard_screen_page.tap_sample_manager_schematic_icon()
