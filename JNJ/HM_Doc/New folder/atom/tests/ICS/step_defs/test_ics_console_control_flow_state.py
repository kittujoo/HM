import os

from pathlib import Path
from pytest_bdd import when, then, given, scenarios
from pytest_bdd.parsers import cfparse

from utilities.datatables.converters import CONVERTERS
from utilities.logger import Logger
from web_framework.empower.drivers.console_driver import ConsoleDriver
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_console_control_flow_state.feature')


@when(cfparse('set flow to "{flow_state:bool}"', CONVERTERS))
def set_control_flow(flow_state: bool, console_driver: ConsoleDriver):
    console_driver.set_flow(flow_state)


@given(cfparse('flow is "{flow_state:bool}"', CONVERTERS))
def given_system_flow(flow_state: bool, console_driver: ConsoleDriver):
    console_driver.console_base_page.open_commands_tab()
    console_driver.validate_commands_tab_opened()
    console_driver.set_flow(flow_state)


@then(cfparse('Console Commands page shows flow status as "{flow_state}"', CONVERTERS))
def validate_flow_in_commands_page(flow_state: str, console_driver: ConsoleDriver):
    console_driver.validate_control_flow_state_equal_to(flow_state)


@then(cfparse('Control Panel shows flow "{flow_state:bool}"', CONVERTERS))
def validate_control_panel_flow_rate(flow_state: bool, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_control_panel_flow_rate_equal_to(
        "0.000") if not flow_state else run_samples_driver.validate_control_panel_flow_not_equal_to("0.000")
