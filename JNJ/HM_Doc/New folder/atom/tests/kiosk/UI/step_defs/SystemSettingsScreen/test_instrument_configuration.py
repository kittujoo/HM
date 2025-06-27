import pytest
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.instrument_configuration_screen import InstrumentConfigurationScreenLocators
from web_framework.kiosk.pages.Locators.System.instrument_configuration_settings_screen import \
    InstrumentConfigurationSettingsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.Locators.base_page_locators import BasePageLocators
from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
from web_framework.kiosk.pages.System.instrument_configuration_screen import InstrumentConfigurationScreen
from web_framework.kiosk.pages.System.instrument_configuration_settings_screen import InstrumentConfigurationSettingsScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/instrument_configuration.feature')

logger = Logger(__name__)


@pytest.fixture
def instrument_module_configuration_screen(page_builder):
    page = page_builder(InstrumentConfigurationScreen)
    return page


@when('User navigates to the instrument settings screen')
def navigate_instrument_settings(instrument_module_configuration_screen: InstrumentConfigurationScreen,
                                 instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen, dashboard_screen_page: DashBoardScreen,
                                 system_settings_screen: SystemSettingsScreen):
    dashboard_screen_page.wait_element_to_be_clickable(DashBoardsScreenPageLocators.INSTRUMENT, dashboard_screen_page.wait_time)
    dashboard_screen_page.tap_system()
    system_settings_screen.validate_settings_screen()
    system_settings_screen.tap(SystemSettingsScreenLocators.CONFIGURATION_TAB)
    instrument_module_configuration_screen.validate_instrument_configuration_screen()
    instrument_configuration_settings_screen_page.tap(InstrumentConfigurationScreenLocators.OPTIONS_PANEL)
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()


@when('Information appears providing a warning about effects of changing this value')
def validate_warning_info(instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    instrument_configuration_settings_screen_page.is_displayed(InstrumentConfigurationSettingsScreenLocators.INFORMATION_BANNER)


@when('User navigates to options screen')
def navigate_to_options(instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.tap(InstrumentConfigurationScreenLocators.OPTIONS_PANEL)
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()


@when('User navigates to home screen')
def navigate_to_home(dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_home()


@when(cfparse('User taps the "{option_tab_name}" panel'))
def tap_option_tab(option_tab_name, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    if option_tab_name == "dwell-volume":
        instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_TAB)
    elif option_tab_name == "units":
        instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.UNITS_TAB)
    elif option_tab_name == "tubing-kit":
        instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.TUBING_KIT_TAB)
    else:
        assert False, f"Unrecognized tab: {option_tab_name}"


@when('User cancels the settings')
def tap_cancel(instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.tap_cancel()


@when('User saves the changes')
def save_changes(instrument_module_configuration_screen: InstrumentConfigurationScreen,
                 instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen, dashboard_screen_page: DashBoardScreen):
    instrument_configuration_settings_screen_page.tap_done_button()
    instrument_module_configuration_screen.wait_for_settings_save()
    dashboard_screen_page.validate_dashboard_screen()


@when(cfparse('User enters "{dwell_value}"'))
def enter_dwell_value(dwell_value: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    instrument_configuration_settings_screen_page.wait_element_to_be_clickable(InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_FIELD,
                                                                               instrument_configuration_settings_screen_page.wait_time)
    instrument_configuration_settings_screen_page.clear_num_pad_entries(InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_FIELD)
    instrument_configuration_settings_screen_page.enter_value(dwell_value)


@when(cfparse('User selects a "{pressure_unit}" option'))
def select_pressure_unit(pressure_unit: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    instrument_configuration_settings_screen_page.select_pressure_unit(pressure_unit)


@when(cfparse('User selects "{tubing_kit_option}"'))
def select_tubing_kit_option(tubing_kit_option: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    instrument_configuration_settings_screen_page.select_tubing_kit_option(tubing_kit_option)


@then(cfparse('User validates the tubing kit option "{tubing_kit_option}" was saved'))
def validate_tubing_kit_option(tubing_kit_option: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    assert instrument_configuration_settings_screen_page.validate_tubing_kit_option(
        tubing_kit_option), f"The Correct Tubing Kit unit was not selected. Expected:{tubing_kit_option}"


@then(cfparse('User validates the "{pressure_unit}" option was saved'))
def validate_pressure_unit(pressure_unit: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    assert instrument_configuration_settings_screen_page.validate_pressure_unit_selection(
        pressure_unit), f"The Correct pressure unit was not selected. Expected:[{pressure_unit}]"


@then(cfparse('User validates the dwell value "{dwell_value}" was saved'))
def validate_dwell_volume_value(dwell_value: str, instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    current_value = instrument_configuration_settings_screen_page.get_user_input_text(
        InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_FIELD)
    assert dwell_value == current_value, f"The dwell volume value was not saved properly. Expected:[{dwell_value}] Actual:[{current_value}]"


@then(cfparse('User validates the pressure units in the dashboard is "{unit}"'))
def validate_pressure_unit(unit: str, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.validate_dashboard_screen()
    dashboard_screen_page.wait_time_to_load_value(DashBoardsScreenPageLocators.PRESSURE_UNIT, ignore_message='')
    assert unit == dashboard_screen_page.get_text(
        DashBoardsScreenPageLocators.PRESSURE_UNIT), f"The unit of pressure is not as expected. Expected:[{unit}] Actual:[{dashboard_screen_page.get_text(DashBoardsScreenPageLocators.PRESSURE_UNIT)}]"


@then('User validates the error condition is met')
def validate_dwell_volume_error(instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    assert not instrument_configuration_settings_screen_page.is_active(BasePageLocators.DONE_BUTTON), "The Entry field is expected to have error"
    instrument_configuration_settings_screen_page.clear_num_pad_entries(InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_FIELD)


@then(cfparse('User validates the "{actual_dwell_value}" "{actual_pressure_unit}" and "{actual_tubing_kit_option}" were saved'))
def validate_data(actual_dwell_value: str, actual_pressure_unit: str, actual_tubing_kit_option: str,
                  instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    current_value = instrument_configuration_settings_screen_page.get_user_input_text(
        InstrumentConfigurationSettingsScreenLocators.DWELL_VOLUME_FIELD)
    assert actual_dwell_value == current_value, f"The dwell volume value was not saved properly. Expected:[{actual_dwell_value}] Actual:[{current_value}]"
    instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.UNITS_TAB)
    assert instrument_configuration_settings_screen_page.validate_pressure_unit_selection(
        actual_pressure_unit), f"The Correct pressure unit was not selected. Expected:[{actual_pressure_unit}]"
    instrument_configuration_settings_screen_page.tap(InstrumentConfigurationSettingsScreenLocators.TUBING_KIT_TAB)
    assert instrument_configuration_settings_screen_page.validate_tubing_kit_option(
        actual_tubing_kit_option), f"The Correct Tubing Kit unit was not selected. Expected:{actual_tubing_kit_option}"


@then('Information appears providing a warning about effects of changing this value')
def validate_warning_info(instrument_configuration_settings_screen_page: InstrumentConfigurationSettingsScreen):
    instrument_configuration_settings_screen_page.validate_instrument_configuration_settings_screen()
    assert instrument_configuration_settings_screen_page.is_displayed(
        InstrumentConfigurationSettingsScreenLocators.INFORMATION_BANNER), "The warning for changing the value is not displayed"
