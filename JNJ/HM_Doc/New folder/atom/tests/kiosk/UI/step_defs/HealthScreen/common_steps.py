from pytest_bdd import then, when
from pytest_bdd.parsers import cfparse

from web_framework.kiosk.pages.DashBoard.dash_board_screen import DashBoardScreen
from web_framework.kiosk.pages.Health.instrument_diagnostic_screen import InstrumentDiagnosticScreen
from web_framework.kiosk.pages.Locators.Health.instrument_diagnostic_locators import InstrumentDiagnosticLocators


@when('User navigates to issue resolution screen')
def navigate_to_issue_resolution_screen(dashboard_screen_page: DashBoardScreen,
                                        instrument_diagnostic_page: InstrumentDiagnosticScreen):
    dashboard_screen_page.tap_diagnose()
    instrument_diagnostic_page.validate_instrument_diagnostic_screen()
    instrument_diagnostic_page.tap(InstrumentDiagnosticLocators.ISSUE_RESOLUTION_PANEL)


@then(cfparse('User validates the "{issue}" is displayed in issue resolution field'))
def validate_active_issues(issue, instrument_diagnostic_page: InstrumentDiagnosticScreen):

    issue_text: str = instrument_diagnostic_page.get_first_active_error_text()
    active_issue_text: str = issue_text.split('\n')[0].strip()
    assert active_issue_text == issue, f"The Issue description is not as expected. Expected {issue}: 'error'. Actual issue: {active_issue_text}"
