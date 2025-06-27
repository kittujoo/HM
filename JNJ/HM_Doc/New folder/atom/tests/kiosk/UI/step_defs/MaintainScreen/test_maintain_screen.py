import time
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse
from utilities.logger import Logger
from web_framework.kiosk.pages.Maintain.maintain_screen import MaintainScreen

if __name__ == Path(__file__).stem:
    scenarios('../../features/MaintainScreen/maintain_screen.feature')
logger = Logger("test_maintain_screen")


@when(cfparse('User taps the "{navigation_panel}"'))
def test(maintain_screen_page: MaintainScreen, navigation_panel):
    maintain_screen_page.validate_maintain_screen()
    maintain_screen_page.tap_panel(navigation_panel)


@then('User confirms the changes')
def confirm_changes(maintain_screen_page: MaintainScreen):
    maintain_screen_page.tap_done_button()


@then('User cancels the changes')
def cancel_changes(maintain_screen_page: MaintainScreen):
    # sleep due to individual panel screens not having elements to create validate function yet
    time.sleep(2)
    maintain_screen_page.tap_cancel_button()
