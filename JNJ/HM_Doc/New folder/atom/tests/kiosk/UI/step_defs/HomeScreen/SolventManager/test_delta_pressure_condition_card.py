import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import DeltaPressureConditionCardConstants as deltaConstant
from web_framework.kiosk.pages.Home.SolventManager.delta_pressure_settings_screen import DeltaPressureSettingsScreen
from web_framework.kiosk.pages.Home.SolventManager.solvent_manager_home_screen import SolventManagerHomeScreen
from web_framework.kiosk.pages.Locators.Home.SolventManager.delta_pressure_condition_card import DeltaPressureSettingsScreenLocators
from web_framework.kiosk.pages.Locators.Home.SolventManager.sm_home_screen import SolventManagerHomeScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/SolventManager/delta_pressure_condition_card.feature')

logger = Logger("test_delta_pressure_condition_card")


@pytest.fixture
def delta_pressure_settings_screen_page(page_builder):
    page = page_builder(DeltaPressureSettingsScreen)
    page.implicitly_wait()
    return page


@given('User navigates to the delta pressure settings screen')
def navigate_delta_pressure_settings(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                                     delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap(SolventManagerHomeScreenLocators.DELTA_PRESSURE_CONDITION_CARD)
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()


@when('User toggles the pressure monitor on')
def on_toggle_pressure_monitor(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    delta_pressure_settings_screen_page.switch_on_pressure_monitor()


@when('User toggles the pressure monitor off')
def off_toggle_pressure_monitor(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    delta_pressure_settings_screen_page.switch_off_pressure_monitor()


@when('User navigates back to the delta pressure settings')
def back_nav_delta_pressure_settings(solvent_manager_home_screen_page: SolventManagerHomeScreen,
                                     delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    solvent_manager_home_screen_page.validate_solvent_manager_home_screen()
    solvent_manager_home_screen_page.tap(SolventManagerHomeScreenLocators.DELTA_PRESSURE_CONDITION_CARD)
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()


@then('User validates the pressure monitor features are available')
def validate_pressure_monitor_features_available(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    assert delta_pressure_settings_screen_page.is_displayed(
        DeltaPressureSettingsScreenLocators.PRESSURE_READ_BACK_HEADER)
    assert delta_pressure_settings_screen_page.is_displayed(DeltaPressureSettingsScreenLocators.PRESSURE_PICKER_HEADER)


@then('User validates the pressure monitor features are not available')
def validate_pressure_monitor_features_not_available(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    assert not delta_pressure_settings_screen_page.is_displayed(
        DeltaPressureSettingsScreenLocators.PRESSURE_READ_BACK_HEADER)
    assert not delta_pressure_settings_screen_page.is_displayed(
        DeltaPressureSettingsScreenLocators.PRESSURE_PICKER_HEADER)


@when(cfparse('User sets target pressure to "{target_pressure_value}"'))
def enter_target_pressure_value(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen, target_pressure_value):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    delta_pressure_settings_screen_page.set_spinner_value(
        DeltaPressureSettingsScreenLocators.DELTA_PRESSURE_LIST, target_pressure_value)


@then('User validates changes can not be saved')
def validate_no_save(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    assert not delta_pressure_settings_screen_page.is_active(BasePageLocators.DONE_BUTTON)


@then(cfparse('User validates the "{target_pressure_value}" was saved'))
def validate_pressure_value_saved(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen, target_pressure_value):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    actual_pressure = delta_pressure_settings_screen_page.get_text(
        DeltaPressureSettingsScreenLocators.PRESSURE_READ_BACK_MESSAGE)
    actual_delta_pressure = actual_pressure[2:5]
    actual_delta_pressure = TypeConverter.to_float(actual_delta_pressure)
    target_pressure_value = TypeConverter.to_float(target_pressure_value)
    assert actual_delta_pressure == target_pressure_value, f" actual_temperature => {actual_delta_pressure} "


@when('User saves the changes')
def tap_done_button(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    delta_pressure_settings_screen_page.tap_done_button()


@then('User navigates back to the solvent manager home screen')
def navigate_sm_home_screen(delta_pressure_settings_screen_page: DeltaPressureSettingsScreen):
    delta_pressure_settings_screen_page.validate_delta_pressure_settings_screen()
    delta_pressure_settings_screen_page.tap_cancel_button()


@then(cfparse('Validate the read back message in the condition card for "{target_pressure_value}"'))
def validate_condition_card_indicator(solvent_manager_home_screen_page: SolventManagerHomeScreen, target_pressure_value):
    solvent_manager_home_screen_page.validate_delta_pressure_value()
    solvent_manager_home_screen_page.validate_pressure_read_back_units()
    solvent_manager_home_screen_page.validate_pressure_units_per_min()

    current_delta_pressure_value = solvent_manager_home_screen_page.get_current_delta_pressure()
    current_delta_pressure = TypeConverter.to_float(current_delta_pressure_value)
    current_indicator_status = solvent_manager_home_screen_page.get_indicator_message()
    logger.info(f"current_color====>>>>{current_indicator_status}")
    target_pressure_value = TypeConverter.to_float(target_pressure_value)
    property_name = "background-color"
    actual_color_code = solvent_manager_home_screen_page.get_title_icon_color_code(
        DeltaPressureSettingsScreenLocators.INDICATOR_BAR_STATUS, property_name)

    if current_delta_pressure < 2 * target_pressure_value:
        assert current_indicator_status == deltaConstant.InRangeIndicatorMessage, f"current_indicator_status => {current_indicator_status}"
        assert deltaConstant.DeltaPressureInRangeColorCode in actual_color_code, f"actual_color_code => {actual_color_code}"
    elif current_delta_pressure >= 2 * target_pressure_value:
        assert current_indicator_status == deltaConstant.OutOfRangeIndicatorMessage, f"current_indicator_status =>{current_indicator_status}"
        assert deltaConstant.DeltaPressureOutOfRangeColorCode in actual_color_code, f"actual_color_code => {actual_color_code}"


@then('Validate the indicator bar in the condition card grey out')
def validate_tolerance_pressure_disabled(solvent_manager_home_screen_page: SolventManagerHomeScreen):
    property_name = "background-color"
    actual_color_code = solvent_manager_home_screen_page.get_title_icon_color_code(
        DeltaPressureSettingsScreenLocators.INDICATOR_BAR_STATUS, property_name)
    logger.info(f"actual_color_code====>>>>{actual_color_code}")
    expected_color_code = deltaConstant.DeltaPressureDisableColorCode
    assert expected_color_code in actual_color_code, f" The indicator bar did not turn grey"
