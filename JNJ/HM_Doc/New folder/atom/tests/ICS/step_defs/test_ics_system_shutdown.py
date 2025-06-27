from pytest_bdd import when, then, scenarios
from pytest_bdd.parsers import cfparse

from web_framework.empower.drivers.console_driver import ConsoleDriver

scenarios('../features/ics_system_shutdown.feature')


@when('Shutdown section is selected')
def select_shutdown_option(console_driver: ConsoleDriver):
    console_driver.select_shutdown_option()


@then(cfparse('Shutdown section text is "{shutdown_text}"'))
def check_shutdown_button_clickable(shutdown_text: str, console_driver: ConsoleDriver):
    console_driver.validate_active_text(shutdown_text)
