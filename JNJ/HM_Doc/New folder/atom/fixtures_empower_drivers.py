from typing import Callable

import pytest

from fixtures_win_app_driver import WinAppDriverHandler
from isym_test_api.rest_api.rest_client.rest import RestClient
from utilities.assert_timeout import AssertTimeout
from utilities.empower_utility import EmpowerConfiguration
from utilities.ps_exec_tool import PsExecRemoteTool, PsExecLocalTool
from utilities.ssh_connection import SSh
from web_framework.empower.drivers.configuration_manager_driver import ConfigurationManagerDriver
from web_framework.empower.drivers.console_driver import ConsoleDriver
from web_framework.empower.drivers.instrument_method_editor_driver import InstrumentMethodEditorDriver
from web_framework.empower.drivers.message_center_driver import MessageCenterDriver
from web_framework.empower.drivers.project_driver import ProjectDriver
from web_framework.empower.drivers.project_restore_driver import ProjectRestoreDriver
from web_framework.empower.drivers.report_publisher_driver import ReportPublisherDriver
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient


@pytest.fixture
def message_center_driver(win_app_driver_handler, results_folder, empower_configuration: EmpowerConfiguration):
    driver = MessageCenterDriver(win_app_driver_handler=win_app_driver_handler,
                                 username=empower_configuration.username,
                                 password=empower_configuration.password,
                                 results_folder=results_folder)
    return driver


@pytest.fixture
def run_samples_driver(win_app_driver_handler, miltest_rest_client_creator, assert_timeout: AssertTimeout) -> RunSamplesDriver:
    driver = RunSamplesDriver(win_app_driver_handler, miltest_rest_client_creator, assert_timeout)
    return driver


@pytest.fixture
def instrument_method_editor_driver(win_app_driver_handler) -> InstrumentMethodEditorDriver:
    driver = InstrumentMethodEditorDriver(win_app_driver_handler)
    return driver


@pytest.fixture
def configuration_manager_driver(win_app_driver_handler) -> ConfigurationManagerDriver:
    driver = ConfigurationManagerDriver(win_app_driver_handler)
    return driver


@pytest.fixture(scope='session')
def project_restore_driver(empower_configuration: EmpowerConfiguration, test_data_dir: str):
    return ProjectRestoreDriver(empower_configuration.username, empower_configuration.password, test_data_dir)


@pytest.fixture
def miltest_rest_client_creator(settings) -> Callable[[str], MiltestRestClient]:
    def creator(handle: str):
        host = settings.empower_hostname
        port = settings.miltest_rest_client_port
        base_url = f"http://{host}:{port}"
        rest_client = RestClient(base_url, session_headers={"handle": handle})
        return MiltestRestClient(rest_client=rest_client)

    return creator


@pytest.fixture
def console_driver(win_app_driver_handler: WinAppDriverHandler, assert_timeout: AssertTimeout):
    return ConsoleDriver(win_app_driver_handler, assert_timeout)


@pytest.fixture
def project_driver(win_app_driver_handler, miltest_rest_client_creator) -> ProjectDriver:
    driver = ProjectDriver(win_app_driver_handler, miltest_rest_client_creator)
    return driver


@pytest.fixture
def report_publisher_driver(win_app_driver_handler) -> ReportPublisherDriver:
    driver = ReportPublisherDriver(win_app_driver_handler)
    return driver


@pytest.fixture(scope='session')
def ps_exec_tool(run_on_local, settings):
    if run_on_local:
        ssh = SSh(settings.empower_hostname, settings.host_username, settings.host_password)
        return PsExecRemoteTool(ssh, settings.host_username, settings.host_password)
    else:
        return PsExecLocalTool(settings.host_username, settings.host_password)
