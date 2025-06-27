import os

from pathlib import Path
from pytest_bdd import when, then, scenarios, given
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.empower.drivers.console_driver import ConsoleDriver

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_console_control_lamp_state.feature')


@when(cfparse('set lamp to "{state:bool}"', CONVERTERS))
def set_lamp_state(state: bool, console_driver: ConsoleDriver):
    console_driver.set_lamp_state(state)


@then(cfparse('Console Commands page shows lamp "{state:bool}"', CONVERTERS))
def validate_lamp_state(state: bool, console_driver: ConsoleDriver):
    console_driver.validate_commands_page_lamp_state(state)
