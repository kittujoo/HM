from datetime import datetime, timedelta
from typing import List

from pytest_bdd import then
from pytest_bdd.parsers import cfparse
from selenium.webdriver.support.color import Color

from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.System.Log.logs_screen import LogsScreen


@then(cfparse('log entries have one with current date, "{category}" category and "{source}" source details'))
def validate_log_screen_details(category, source, context, system_logs_screen: LogsScreen):
    actual_entries: List[dict] = system_logs_screen.get_table_entries()

    for entry in actual_entries:
        entry['Date and Time'] = datetime.strptime(entry['Date and Time'], '%m/%d/%Y %H:%M')

    expected_error_time = context.get("alarm_set_time", datetime.now())

    matched_entries = filter(
        lambda item: (category in item['Category']) and (source in item['Source'] and (expected_error_time - entry['Date and Time'] < timedelta(minutes=1))),
        actual_entries)

    assert matched_entries, f"Log has no entries matched given criteria: Category contains [{category}], Source contains [{source}], date is a current date"


@then(cfparse('User validates the top issue resolution is red color'))
def validate_active_issues_color(instrument_diagnostic_page: InstrumentDiagnosticScreen):
    issue = instrument_diagnostic_page.get_issue_items()[0]
    expected_border_color = Color(red=255, green=82, blue=82, alpha=1)

    # Assertions for color components
    assert issue.border_color == expected_border_color, f"Error border color is not as expected"
