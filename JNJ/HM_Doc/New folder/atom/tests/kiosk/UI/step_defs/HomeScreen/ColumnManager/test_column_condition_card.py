import time
import traceback
import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from utilities.type_converter import TypeConverter
from web_framework.kiosk.common.Constants.UI.condition_card_constants import ColumnConditionCardConstant
from web_framework.kiosk.common.Models.ConditionalCard.ColumnDetails import ColumnDetails
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_manager_home_screen import ColumnManagerHomeScreen
from web_framework.kiosk.pages.Home.ColumnManager.column_settings_screen import ColumnSettingsScreen
from web_framework.kiosk.pages.Locators.Home.ColumnManager.column_condition_card import ColumnDetailsLocators, ColumnSettingsScreenLocators

if __name__ == Path(__file__).stem:
    scenarios('../../../features/HomeScreen/ColumnManager/column_condition_card.feature')
logger = Logger("test_column_condition_card")


@pytest.fixture
def column_setting_screen_page(page_builder):
    page = page_builder(ColumnSettingsScreen)
    return page


@given('Navigate to the column settings screen')
def navigate_to_column_settings_screen(column_manager_home_screen_page: ColumnManagerHomeScreen,
                                       column_setting_screen_page: ColumnSettingsScreen):
    logger.info("**************************The column condition card test starts**********************")
    column_manager_home_screen_page.validate_column_manager_home_screen()
    column_manager_home_screen_page.tap_column_condition_card()


@then('Navigate to the column settings screen')
@when('Navigate to the column settings screen')
def tap_column_setting_gear_icon(column_manager_home_screen_page: ColumnManagerHomeScreen,
                                 column_setting_screen_page: ColumnSettingsScreen):
    logger.info("**************************The column condition card test starts**********************")
    column_manager_home_screen_page.validate_column_manager_home_screen()
    column_manager_home_screen_page.tap_column_condition_card()
    column_setting_screen_page.tap_settings_icon()


@when('The user taps the done button')
@then('The user confirms the monitor injection count')
@when('The user confirms the monitor injection count')
def tap_done_button(column_setting_screen_page: ColumnSettingsScreen):
    logger.info("The done button is tapped")
    column_setting_screen_page.tap_done_button()


@when('The user cancels the monitor injection count')
@when('The user cancels the column position selection')
def tap_cancel_button(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap_cancel_button()


@then('The user navigates to the monitor injection count settings screen')
@when('The user navigates to the monitor injection count settings screen')
def tap_monitor_injection_control_tab(column_manager_home_screen_page: ColumnManagerHomeScreen,
                                      column_setting_screen_page: ColumnSettingsScreen):
    # column_setting_screen_page.validate_column_settings_screen()
    column_manager_home_screen_page.tap_column_condition_card()
    column_setting_screen_page.tap_settings_icon()


@when(cfparse('The user sets "{warning_toggle_button_state}" for the set injection warning toggle button'))
def set_injection_warning_toggle_button(column_setting_screen_page: ColumnSettingsScreen, warning_toggle_button_state):
    column_setting_screen_page.validate_column_settings_screen()
    column_setting_screen_page.set_toggle_button(ColumnSettingsScreenLocators.INJECTION_WARNING_TOGGLE_BUTTON,
                                                 warning_toggle_button_state)


@when(cfparse('The user sets "{alarm_toggle_button_state}" for the set injection alarm toggle button'))
def set_injection_alarm_toggle_button(column_setting_screen_page: ColumnSettingsScreen, alarm_toggle_button_state):
    column_setting_screen_page.validate_column_settings_screen()
    column_setting_screen_page.set_toggle_button(ColumnSettingsScreenLocators.INJECTION_ALARM_TOGGLE_BUTTON,
                                                 alarm_toggle_button_state)


@then(cfparse('The user validate the injection count edit field is "{edit_field_displayed_state}"'))
def validate_injection_count_edit_field(column_setting_screen_page: ColumnSettingsScreen, edit_field_displayed_state):
    try:
        column_setting_screen_page.validate_column_settings_screen()
        edit_field_displayed_state = TypeConverter.to_bool(edit_field_displayed_state)
        is_edit_field_exists = column_setting_screen_page.is_edit_field_exists(
            ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)
        assert is_edit_field_exists == edit_field_displayed_state, f"The injection count edit field state {is_edit_field_exists}"

    finally:
        column_setting_screen_page.tap_cancel_button()


@then('The user navigates to the temperature control screen')
@when('The user navigates to the temperature control screen')
def tap_temperature_control_tab(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.MAXIMUM_TEMPERATURE_TAB)


@when(cfparse('The user sets the maximum warning temperature as "{maximum_warning_temperature}"'))
def set_maximum_warming_temperature(column_setting_screen_page: ColumnSettingsScreen, maximum_warning_temperature):
    time.sleep(1)
    column_setting_screen_page.set_spinner_value(ColumnSettingsScreenLocators.MAXIMUM_TEMPERATURE_LIST,
                                                 maximum_warning_temperature)


@then(cfparse('Validate the enabled state of the maximum temperature button "{is_button_disabled}"'))
def validate_maximum_temperature_button(column_setting_screen_page: ColumnSettingsScreen, is_button_disabled):
    try:
        is_button_disabled = TypeConverter.to_bool(is_button_disabled)
        time.sleep(1)  # TODO timer will be removed once INS-27585 is resolved
        is_temperature_button_disabled = column_setting_screen_page.is_disabled(
            ColumnSettingsScreenLocators.MAXIMUM_TEMPERATURE_BUTTON)
        assert is_temperature_button_disabled == is_button_disabled, f"is_temperature_button_enabled {is_temperature_button_disabled} "

    finally:
        column_setting_screen_page.tap_done_button()


@when(cfparse('The user enter the monitor injection count as "{monitor_injection_count}"'))
def enter_monitor_injection_count(column_setting_screen_page: ColumnSettingsScreen, monitor_injection_count):
    logger.info(f"monitor_injection_count ==>{monitor_injection_count}")
    column_setting_screen_page.clear_num_pad_entries(ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)
    column_setting_screen_page.enter_maximum_injection(monitor_injection_count)


@then(cfparse('The user enter the monitor injection count as "{monitor_injection_count}"'))
def enter_monitor_injection_count(column_setting_screen_page: ColumnSettingsScreen, monitor_injection_count):
    logger.info(f"monitor_injection_count ==>{monitor_injection_count}")
    column_setting_screen_page.clear_num_pad_entries(ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)
    column_setting_screen_page.enter_maximum_injection(monitor_injection_count)


@then('The user validates the done button is disabled')
def validate_done_button(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.validate_done_button_inactive()


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@then(cfparse('User validates the monitor injection count as "{expected_monitor_injection_count}"'))
@when(cfparse('User validates the monitor injection count as "{expected_monitor_injection_count}"'))
def validate_monitor_injection_count(column_setting_screen_page: ColumnSettingsScreen, expected_monitor_injection_count):
    wait_time = 5
    column_setting_screen_page.validate_column_settings_screen()
    try:
        start_time = time.time()
        while time.time() - start_time <= wait_time:
            actual_monitor_injection_count = column_setting_screen_page.get_entered_value(
                ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)
            logger.info(f"The actua===>{actual_monitor_injection_count}")
            if actual_monitor_injection_count == expected_monitor_injection_count:
                break
            time.sleep(.5)
        assert actual_monitor_injection_count == expected_monitor_injection_count, f"Failed to update the actual injection count => {actual_monitor_injection_count}"
    finally:
        column_setting_screen_page.tap_done_button()
    logger.info("*************************The test ends for the column condition card*****************************")


# TODO duplication can be removed when pytest-bdd updated to latest version ATOM-80
@when(cfparse('User validates the maximum temperature as "{maximum_warning_temperature}"'))
@then(cfparse('User validates the maximum temperature as "{maximum_warning_temperature}"'))
def validate_maximum_temperature(column_setting_screen_page: ColumnSettingsScreen, maximum_warning_temperature):
    try:
        actual_maximum_temperature = column_setting_screen_page.get_text(
            ColumnSettingsScreenLocators.MAX_TEMPERATURE_READ_BACK_MESSAGE)
        logger.info(f" expected_maximum_warning_temperature===>>>{maximum_warning_temperature}")
        time.sleep(4)
        assert actual_maximum_temperature == maximum_warning_temperature, f"actual_maximum_temperature===>>>{actual_maximum_temperature}"

    finally:
        column_setting_screen_page.tap_cancel_button()


@then('The system indicates injection count is out of range')
def validate_monitor_injection_count_out_of_range(column_setting_screen_page: ColumnSettingsScreen):
    injection_count_entry_field_exists = False

    try:
        time.sleep(.1)
        injection_count_entry_field_exists = column_setting_screen_page.is_injection_edit_field_component_exists()
    except Exception as generic_exception:
        traceback.print_exception(type(generic_exception), generic_exception, generic_exception.__traceback__)
        logger.debug(f"column temperature setting screen is not displayed  :{injection_count_entry_field_exists}")
        assert injection_count_entry_field_exists is True, "The temperature entry field does not exist"

    finally:
        column_setting_screen_page.tap_cancel_button()
    logger.info("*************************The test ends for the column condition card*****************************")


@then(cfparse('The user validates "{expected_column_position}" info in the column manager card reader'))
def validate_card_reader(dashboard_screen_page: DashBoardScreen, expected_column_position):
    try:
        dashboard_screen_page.validate_dashboard_screen()
        actual_column_position = dashboard_screen_page.get_column_position_read_back()
        expected_column_position = TypeConverter.to_str(expected_column_position)
        logger.info(f"############################The colum position in card reader is {actual_column_position}")
        assert actual_column_position == expected_column_position, f"The actual column position is {actual_column_position}"

    finally:
        dashboard_screen_page.tap_column_manager_schematic_icon()

    logger.info("*************************The test ends for the column condition card*****************************")


@then(cfparse('Validate the injection count  edit field shows "{error_state}"'))
def validate_error_state(column_setting_screen_page: ColumnSettingsScreen, error_state):
    try:
        edit_field_error_state = column_setting_screen_page.is_injection_edit_field_in_error_state()
        error_state = TypeConverter.to_bool(error_state)
        assert edit_field_error_state == error_state, f" actual edit field error state is ==>> {edit_field_error_state}"

    finally:
        column_setting_screen_page.tap_cancel_button()


@when('The user turns off the toggle button')
def turn_toggle_button_off(column_setting_screen_page: ColumnSettingsScreen):
    is_toggle_button_enabled = column_setting_screen_page.is_toggle_button_enabled()

    if is_toggle_button_enabled:
        logger.info("*** Toggle button is  enabled")
        column_setting_screen_page.tap_toggle_button()
    else:
        logger.info("** The toggle button is not enabled")


@then('Validate the disabled mode in the column settings screen')
def validate_monitor_injection_count(column_setting_screen_page: ColumnSettingsScreen):
    wait_time = 5
    expected_monitor_injection_count = "Disabled"
    column_setting_screen_page.validate_column_settings_screen()
    try:
        start_time = time.time()
        while time.time() - start_time <= wait_time:
            actual_monitor_injection_count = column_setting_screen_page.get_text(
                ColumnSettingsScreenLocators.MONITOR_INJECTION_COUNT_INFO)
            if actual_monitor_injection_count == ColumnConditionCardConstant.InjectionMonitorDisabledState:
                break
            time.sleep(.5)
        assert actual_monitor_injection_count == expected_monitor_injection_count, f"Failed to update the actual injection count => {actual_monitor_injection_count}"
    finally:
        column_setting_screen_page.tap_done_button()
    logger.info("*************************The test ends for the column condition card*****************************")


@when('The user navigates to the info screen')
def navigate_to_info_screen(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.INFO_ICON)


@when('The user navigates to the settings screen')
def navigate_to_settings_screen(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.SETTINGS_ICON)
    column_setting_screen_page.validate_column_settings_screen()


@when('The user navigates to the monitor injection count screen')
def navigate_to_settings_screen(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.MONITOR_INJECTION_COUNT_TAB)


@when('The user navigates to the history screen')
def navigate_to_history_screen(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.HISTORY_ICON)


@when('User taps the comments tab')
def tap_comments_tab(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.COMMENTS_TAB)


@when(cfparse('User enters "{comments}" in the comments tab'))
def tap_comments_tab(column_setting_screen_page: ColumnSettingsScreen, comments):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.COMMENTS_SECTION)
    column_setting_screen_page.send_keys(comments)


@when('User taps the monitor injection count tab')
def tap_monitor_injection_tab(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.validate_column_settings_screen()
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.MONITOR_INJECTION_COUNT_TAB)


@then(cfparse('Validates the text enter as "{comments}"'))
def validates_comments(column_setting_screen_page: ColumnSettingsScreen, comments):
    try:
        expected_text = column_setting_screen_page.get_comments_text(ColumnSettingsScreenLocators.COMMENTS_SECTION)
        logger.info(f" expected_text ===>>>>{expected_text}")
        logger.info(f" comments ===>>>>{comments}")
        assert expected_text == comments

    finally:
        column_setting_screen_page.tap_cancel_button()


@then(cfparse('The user validates the value in the edit field is "{monitor_injection_count}"'))
def validate_edit_field(column_setting_screen_page: ColumnSettingsScreen, monitor_injection_count):
    try:
        actual_edit_field_value = column_setting_screen_page.get_user_input_text(
            ColumnSettingsScreenLocators.INJECTION_COUNT_ENTRY_FIELD)
        logger.info(f"actual_edit_field_value===>>>{actual_edit_field_value}")
        expected_edit_field_value = monitor_injection_count
        assert actual_edit_field_value == expected_edit_field_value, f"expected_edit_field_value==>{expected_edit_field_value} "

    finally:
        column_setting_screen_page.tap_cancel_button()


@when('The user taps the read icon')
def read_column_info(column_setting_screen_page: ColumnSettingsScreen):
    column_setting_screen_page.tap(ColumnSettingsScreenLocators.READ_ICON)
    column_setting_screen_page.wait_time_to_load_value(ColumnSettingsScreenLocators.COLUMN_NAME)


@then('The user validates the information text')
def validate_info_text(column_setting_screen_page: ColumnSettingsScreen):
    actual_info_text = column_setting_screen_page.get_text(ColumnSettingsScreenLocators.INFO_TEXT)
    logger.info(f"actual_info_text======>>>>>{actual_info_text}")
    expected_info_text = ColumnConditionCardConstant.InformationText
    logger.info(f"expected_info_text======>>>>>{expected_info_text}")
    actual_instruction_text = column_setting_screen_page.get_instruction_text()
    logger.info(f"actual_instruction_text======>>>>>{actual_instruction_text}")
    expected_instruction_text = ColumnConditionCardConstant.expected_instruction_text
    logger.info(f"expected_instruction_text======>>>>>{expected_instruction_text}")
    assert actual_instruction_text == expected_instruction_text, f"The instruction info is incorrect"
    assert actual_info_text == expected_info_text, " The information text is incorrect"


@then('The users validates the column information')
def validate_column_info(column_setting_screen_page: ColumnSettingsScreen,
                         dashboard_screen_page: DashBoardScreen):
    try:
        actual_column_name = column_setting_screen_page.get_container_text(ColumnDetailsLocators.COLUMN_NAME_INFO)
        actual_description = column_setting_screen_page.get_container_text(ColumnDetailsLocators.COLUMN_DESCRIPTION_INFO)
        actual_serial_number = column_setting_screen_page.get_container_text(ColumnDetailsLocators.SERIAL_NUMBER_INFO)
        actual_gtin = column_setting_screen_page.get_container_text(ColumnDetailsLocators.GTIN_INFO)
        actual_part_number = column_setting_screen_page.get_container_text(ColumnDetailsLocators.PART_NUMBER)
        actual_maximum_pressure = column_setting_screen_page.get_container_text(ColumnDetailsLocators.MAXIMUM_PRESSURE_INFO)
        actual_maximum_temperature = column_setting_screen_page.get_container_text(ColumnDetailsLocators.MAXIMUN_TEMPERATURE_INFO)
        actual_ph_lower_limit = column_setting_screen_page.get_container_text(ColumnDetailsLocators.LOW_PH_INFO)
        actual_ph_lower_limit = int(actual_ph_lower_limit)
        actual_ph_higher_limit = column_setting_screen_page.get_container_text(ColumnDetailsLocators.HIGH_PH_INFO)
        actual_ph_higher_limit = int(actual_ph_higher_limit)

        column_details = ColumnDetails(column_name=actual_column_name,
                                       description=actual_description,
                                       serial_number=actual_serial_number,
                                       gtin=actual_gtin,
                                       part_number=actual_part_number,
                                       maximum_pressure=actual_maximum_pressure,
                                       maximum_temperature=actual_maximum_temperature,
                                       ph_lower_limit=actual_ph_lower_limit,
                                       ph_higher_limit=actual_ph_higher_limit)
    finally:
        column_setting_screen_page.tap_cancel_button()
        dashboard_screen_page.tap_home()
