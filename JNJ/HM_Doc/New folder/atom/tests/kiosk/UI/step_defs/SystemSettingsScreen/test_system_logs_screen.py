import json

from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.color import Color

from utilities.date_utilities import current_date, is_past_event, get_date_with_days_delta
from utilities.logger import Logger
from web_framework.kiosk.common.Constants.UI.logs import LogsScreenConstants, LogTableHeaders
from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Locators.System.system_logs_screen_locators import SystemLogsScreenLocators
from web_framework.kiosk.pages.Locators.System.system_settings_screen import SystemSettingsScreenLocators
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen
from web_framework.kiosk.pages.System.Log.logs_settings_screen import LogSettingsScreen
from web_framework.kiosk.pages.System.system_settings_screen import SystemSettingsScreen

from pathlib import Path
if __name__ == Path(__file__).stem:
    scenarios('../../features/SystemSettingsScreen/system_logs.feature')

logger = Logger(__name__)


@when('Last log details are stored')
def store_data(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    context["initial_date_time"] = log_entry[LogTableHeaders.date_and_time]
    context['category'] = log_entry[LogTableHeaders.category]
    context['source'] = log_entry[LogTableHeaders.source]


@when('User is at the system logs screen')
@when('User navigates to the system logs screen')
def navigate_system_logs_screen(system_settings_screen: SystemSettingsScreen, dashboard_screen_page: DashBoardScreen):
    dashboard_screen_page.tap_system()
    system_settings_screen.tap(SystemSettingsScreenLocators.LOGS_TAB)


@when('User taps the filter icon')
def select_simple_filter(system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    system_logs_screen.tap(SystemLogsScreenLocators.FILTER_BUTTON)
    system_logs_screen.wait_time_to_load_value(SystemLogsScreenLocators.CONTENT_FILTER_LABEL)


@when(cfparse('User swaps the data range filter to "{date_range_option}"'))
def select_simple_filter(context, date_range_option, log_settings_screen: LogSettingsScreen):
    log_settings_screen.validate_system_logs_screen()
    log_settings_screen.tap(SystemLogsScreenLocators.DATE_TAB)
    context['date_range_option'] = date_range_option
    log_settings_screen.select_date_range_filter(date_range_option)


@when(cfparse('User swaps the simple filter to "{content_filter_option}"'))
def select_simple_filter(context, content_filter_option, log_settings_screen: LogSettingsScreen):
    log_settings_screen.validate_system_logs_screen()
    log_settings_screen.tap(SystemLogsScreenLocators.CONTENT_TAB)
    context['content_filter_option'] = content_filter_option.strip('s')
    log_settings_screen.select_content_filter(content_filter_option)


@when('User confirms the settings')
def tap_done_button(system_logs_screen: LogsScreen):
    system_logs_screen.tap_done_button()


@when('User press the Next button')
def tap_next_button(system_logs_screen: LogsScreen):
    system_logs_screen.tap(SystemLogsScreenLocators.NEXT_PAGE)


@when('User press the Back button')
def tap_back_button(system_logs_screen: LogsScreen):
    try:
        system_logs_screen.tap(SystemLogsScreenLocators.BACK_PAGE)
    except NoSuchElementException:
        logger.info("Back button is disabled in page so continuing test")


@when('User taps add entry icon')
def add_log_entry(system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    system_logs_screen.tap(SystemLogsScreenLocators.ADD_ENTRY_BUTTON)


@when('User keeps the scroll down')
def scroll_list(system_logs_screen: LogsScreen):
    system_logs_screen.scroll_to_element(SystemLogsScreenLocators.LAST_ENTRY)


@when('User cancels the change')
def tap_cancel(system_logs_screen: LogsScreen):
    system_logs_screen.tap_cancel_button()


@when('User confirms the change')
def tap_confirm(system_logs_screen: LogsScreen):
    system_logs_screen.tap_done_button()


@when(cfparse('User enters any "{log_note}" and confirms the log entry'))
def add_log_entry(log_note, context, log_settings_screen: LogSettingsScreen):
    log_settings_screen.validate_add_log_entry_screen()
    log_settings_screen.add_new_log_entry(log_note)
    log_settings_screen.tap_done_button()
    context["date_time"] = current_date()
    context["user"] = LogsScreenConstants.User
    context["eventtype"] = LogsScreenConstants.EventType
    context["comments"] = log_note
    log_settings_screen.wait_for_element_visibility(log_settings_screen.wait_time, SystemLogsScreenLocators.FIRST_LOG_ENTRY)


@when(cfparse('User enters "{log_note}"'))
def add_log_entry(log_note, context, log_settings_screen: LogSettingsScreen):
    log_settings_screen.validate_add_log_entry_screen()
    log_settings_screen.add_new_log_entry(log_note)
    context["date_time"] = current_date()
    context["user"] = LogsScreenConstants.User
    context["eventtype"] = LogsScreenConstants.EventType
    context["comments"] = log_note


@then('User verifies new log entry is created with current date time, category and source')
def validate_log_entry_data(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    current_date_value = context["date_time"]

    assert log_entry[LogTableHeaders.date_and_time] == current_date_value, (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {current_date_value}. Actual date: {log_entry[LogTableHeaders.date_and_time]}')

    assert log_entry[LogTableHeaders.category] == LogsScreenConstants.Category, (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {LogsScreenConstants.Category}. Actual date: {log_entry[LogTableHeaders.category]}')

    assert log_entry[LogTableHeaders.source] == LogsScreenConstants.Source, (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {LogsScreenConstants.Source}. Actual date: {log_entry[LogsScreenConstants.Source]}')

    system_logs_screen.tap(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    system_logs_screen.validate_system_logs_screen()

    date_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_DATE)
    category_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_CATEGORY)
    source_text = system_logs_screen.get_text(SystemLogsScreenLocators.LOG_DETAIL_SOURCE)
    details_text_dict = json.loads(system_logs_screen.get_text(SystemLogsScreenLocators.LOG_ENTRY_DETAILS))

    user = context["user"]
    event_type = context["eventtype"]
    log_note = context["comments"]

    assert date_text == current_date_value, f"The Date and time is not as expected. Expected Date: {current_date_value}. Actual date: {date_text}"
    assert category_text == LogsScreenConstants.Category, f"The Category  is not as expected. Expected Category: {LogsScreenConstants.Category}. Actual Category: {category_text}"
    assert source_text == LogsScreenConstants.Source, f"The Source is not as expected. Expected Source: {LogsScreenConstants.Source}. Actual Source: {source_text}"

    assert details_text_dict["user"] == user, f'Details are not as expected. Expected User: [{user}], Actual User: [{details_text_dict["user"]}]'
    assert details_text_dict["eventtype"] == event_type, (
        f'Details are not as expected. Expected User: [{event_type}], Actual User: [{details_text_dict["event_type"]}]')
    assert details_text_dict["comments"] == log_note[:LogsScreenConstants.MaxChar], (
        f'Details are not as expected. Expected User: [{log_note}], Actual User: [{details_text_dict["comments"]}]')


@then('User validates the log entries are displayed in reverse chronological order')
def validate_order(system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    date_now = current_date()
    for data in log_table:
        assert is_past_event(date_now, data['Date and Time']), f"Time is not in order. {data['Date and Time']} time is expected to be before {date_now}"
        date_now = data['Date and Time']


@then('User validates the error logs are color coded in red')
def validate_error_state(system_logs_screen: LogsScreen):
    try:
        system_logs_screen.find_element(SystemLogsScreenLocators.ERROR_ENTRY)
        cell_color = Color.from_string(system_logs_screen.find_element(SystemLogsScreenLocators.ERROR_ROW).value_of_css_property('border-left-color'))
        assert cell_color == LogsScreenConstants.Red, f"Color is not as expected. Expected:[{LogsScreenConstants.Red}] Actual:[{cell_color}]"
    except NoSuchElementException:
        logger.info("No Error event found so continuing test")


@then(cfparse('User validates the page "{count}" log entries are displayed'))
def validate_second_screen(count, system_logs_screen: LogsScreen):
    system_logs_screen.wait_for_element_visibility(system_logs_screen.wait_time, SystemLogsScreenLocators.BACK_PAGE_AVAILABLE)
    system_logs_screen.wait_for_element_visibility(system_logs_screen.wait_time, SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    assert LogsScreenConstants.PageNumber.replace('{}', count) in system_logs_screen.get_text(
        SystemLogsScreenLocators.PAGE_NUMBER), f"Page Number is not as expected. " \
                                               f"Actual:{system_logs_screen.get_text(SystemLogsScreenLocators.PAGE_NUMBER)} Expected:Page 2 "


@then(cfparse('User validates the page "{count}" logs are displayed and the scroll is up'))
def validate_first_screen(count, system_logs_screen: LogsScreen):
    system_logs_screen.wait_till_element_is_invisible(SystemLogsScreenLocators.BACK_PAGE_AVAILABLE, system_logs_screen.wait_time)
    system_logs_screen.wait_for_element_visibility(system_logs_screen.wait_time, SystemLogsScreenLocators.FIRST_LOG_ENTRY)
    page_number_text = system_logs_screen.get_text(SystemLogsScreenLocators.PAGE_NUMBER)
    assert LogsScreenConstants.PageNumber.replace('{}', count) in page_number_text, f"Page Number is not as expected. Actual:{page_number_text} Expected:Page 2"
    assert system_logs_screen.is_displayed(SystemLogsScreenLocators.FIRST_LOG_ENTRY), "The Scroll bar is not in the first entry"


@then('User validates the simple filter was applied and logs are filtered')
def validate_data(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    try:
        system_logs_screen.find_element(SystemLogsScreenLocators.FIRST_LOG_ENTRY)
        log_table = system_logs_screen.get_table_entries()
        if context['date_range_option'] == '1 Month':
            days_before = get_date_with_days_delta(30)
        elif context['date_range_option'] == '1 Week':
            days_before = get_date_with_days_delta(7)
        else:
            days_before = "All"
        for data in log_table:
            if context['content_filter_option'] != "All":
                assert context['content_filter_option'] in data[
                    'Category'], f"Expected filter not found. Expected:[{context['content_filter_option']}] Actual:[{data['Category']}]"
            if days_before != "All":
                assert is_past_event(data['Date and Time'],
                                     days_before), f"Time is not in order. {data['Date and Time']} time is expected to be before {days_before}"
    except NoSuchElementException:
        logger.info(
            f"No events were found for the following combination of data range {context['date_range_option']} and filter {context['content_filter_option']}")


@then(cfparse('User validates the "{date_range_option}" and "{content_filter_option}" are displayed'))
def validate_filter(date_range_option, content_filter_option, system_logs_screen: LogsScreen):
    assert system_logs_screen.get_text(
        SystemLogsScreenLocators.RANGE_FILTER_LABEL) == date_range_option, f"Data range is not as expected. " \
                                                                           f"Expected:[{date_range_option}] Actual:[{system_logs_screen.get_text(SystemLogsScreenLocators.RANGE_FILTER_LABEL)}] "
    assert system_logs_screen.get_text(
        SystemLogsScreenLocators.CONTENT_FILTER_LABEL) == content_filter_option, f"Content Filter is not as expected. " \
                                                                                 f"Expected:[{content_filter_option}] Actual:[{system_logs_screen.get_text(SystemLogsScreenLocators.CONTENT_FILTER_LABEL)}] "


@then('User validates that maximum 100 characters can be defined')
def validate_max_limit(system_logs_screen: LogsScreen):
    max_allowed_characters = system_logs_screen.get_text(SystemLogsScreenLocators.MAX_CHAR)
    assert max_allowed_characters == LogsScreenConstants.MaxCharAllowedLabel, f"The max allowed character is incorrect. Expected:[{LogsScreenConstants.MaxCharAllowedLabel}] Actual:[{max_allowed_characters}]"


@then('User validates the new entry is not added in the entry logs')
def validate_no_entry_added(context, system_logs_screen: LogsScreen):
    system_logs_screen.validate_system_logs_screen()
    log_table = system_logs_screen.get_table_entries()
    log_entry = log_table[0]

    assert log_entry[LogTableHeaders.date_and_time] == context['initial_date_time'], (
        f'Log entry "{LogTableHeaders.date_and_time}" is unexpected. Expected: {context["date_time"]}. Actual date: {log_entry[LogTableHeaders.date_and_time]}')

    assert log_entry[LogTableHeaders.category] == context['category'], (
        f'Log entry "{LogTableHeaders.category}" is unexpected. Expected: {context["category"]}. Actual date: {log_entry[LogTableHeaders.category]}')

    assert log_entry[LogTableHeaders.source] == context['source'], (
        f'Log entry "{LogTableHeaders.source}" is unexpected. Expected: {context["source"]}. Actual date: {log_entry[LogsScreenConstants.Source]}')


@when('User navigates from log screen back to dashboard')
@then('User navigates from log screen back to dashboard')
def navigate_dashboard_screen(dashboard_screen_page: DashBoardScreen, system_logs_screen: LogsScreen):
    system_logs_screen.tap(SystemLogsScreenLocators.TOP_BACK_BUTTON)
    dashboard_screen_page.tap_home()
