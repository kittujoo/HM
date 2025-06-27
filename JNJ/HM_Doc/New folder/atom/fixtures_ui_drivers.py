import pytest

from web_framework.kiosk.drivers.commands_driver import CommandsDriver
from web_framework.kiosk.drivers.health_check_driver import HealthCheckDriver
from web_framework.kiosk.drivers.sample_manager_driver import SampleManagerDriver
from web_framework.kiosk.drivers.sample_metering_pump_workflow_driver import SampleMeteringPumpWorkflowDriver
from web_framework.kiosk.drivers.solvent_manager_driver import SolventManagerDriver
from web_framework.kiosk.drivers.startup_workflow_driver import StartUpWorkFlowDriver


@pytest.fixture
def health_check_driver(page_builder):
    return HealthCheckDriver(page_builder)


@pytest.fixture
def sample_metering_pump_workflow_driver(page_builder):
    return SampleMeteringPumpWorkflowDriver(page_builder)


@pytest.fixture
def sample_manager_ui_driver(page_builder):
    """
    Fixture to construct the Sample Manager UI driver.
    :return: SampleManagerDriver
    """
    return SampleManagerDriver(page_builder)


@pytest.fixture
def solvent_manager_ui_driver(page_builder):
    """
    Fixture to construct the Solvent Manager UI driver.
    :return: SolventManagerDriver
    """
    return SolventManagerDriver(page_builder)


@pytest.fixture
def startup_workflow_ui_driver(page_builder):
    """
    Fixture to construct the Startup Workflow UI driver.
    :return: StartUpWorkFlowDriver
    """
    return StartUpWorkFlowDriver(page_builder)


@pytest.fixture
def commands_ui_driver(page_builder):
    """
    Fixture to construct the Commands Actions UI driver.
    :return: CommandsDriver
    """
    return CommandsDriver(page_builder)
