import os
from dataclasses import dataclass
from typing import Dict

import pytest

from argument_constants import ENVIRONMENT, RUN_ON_LOCAL, HEADLESS, ISPP_HOSTNAME, PATH_TO_TEMP_CONFIG
from config.settings import get_settings
from utilities.alarms.instrument_alarm_utility import InstrumentAlarmUtility
from utilities.configuration_models import ComponentConfiguration, EnvironmentType
from utilities.empower_utility import EmpowerConfiguration
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def environment_type(request):
    env = request.config.getoption(ENVIRONMENT)
    return EnvironmentType.from_string(env)


@pytest.fixture(scope='session')
def settings(environment_type):
    settings = get_settings(environment_type, extra_configs=[PATH_TO_TEMP_CONFIG])
    logger.info(f"Executions settings: {settings.as_dict()}")
    return settings


@pytest.fixture(scope='session')
def run_on_local(request, settings):
    return request.config.getoption(RUN_ON_LOCAL)


@pytest.fixture(scope='session')
def api_base_url(request, run_on_local, environment_type, settings):
    if run_on_local and environment_type == EnvironmentType.CDS:
        empower_settings: EmpowerConfiguration = request.getfixturevalue('empower_configuration')
        system_type = empower_settings.ics_instrument_type.replace(" ", "").replace("#", "")
        system_name = empower_settings.hardware_system_name.replace(" ", "").replace("#", "")
        url = f"http://{settings.host}/{system_type}{system_name}/isymRest/"
        return url
    return settings.ispp_api_url


@pytest.fixture(scope='session')
def kiosk_base_url(request, settings, environment_type):
    if environment_type == EnvironmentType.CDS:
        empower_settings: EmpowerConfiguration = request.getfixturevalue('empower_configuration')
        system_type = empower_settings.ics_instrument_type.replace(" ", "").replace("#", "")
        system_name = empower_settings.hardware_system_name.replace(" ", "").replace("#", "")
        url = f"http://{settings.host}/{system_type}{system_name}/kiosk-app/?dn='ICS'"
        return url
    return settings.kiosk_url


@pytest.fixture(scope='session')
def ispp_config(request, settings) -> ComponentConfiguration:
    ispp_hostname = settings.get(ISPP_HOSTNAME, request.config.getoption(ISPP_HOSTNAME))
    ispp_username = settings.ispp_username
    ispp_password = settings.ispp_password
    return ComponentConfiguration(
        hostname=ispp_hostname,
        username=ispp_username,
        password=ispp_password
    )


@pytest.fixture(scope='session')
def isym_config(settings) -> ComponentConfiguration:
    isym_hostname = settings.isym_hostname
    isym_username = settings.isym_username
    isym_password = settings.isym_password
    return ComponentConfiguration(
        hostname=isym_hostname,
        username=isym_username,
        password=isym_password
    )


@pytest.fixture(scope='session')
def components_config(settings) -> Dict[str, ComponentConfiguration]:
    username = settings.isym_username
    password = settings.isym_password
    return {
        "chc": ComponentConfiguration(
            hostname=settings.chc_hostname,
            username=username,
            password=password
        ),
        "ftn": ComponentConfiguration(
            hostname=settings.ftn_hostname,
            username=username,
            password=password
        ),
        "qsm": ComponentConfiguration(
            hostname=settings.qsm_hostname,
            username=username,
            password=password
        ),
        "tuv": ComponentConfiguration(
            hostname=settings.tuv_hostname,
            username=username,
            password=password
        )
    }


@pytest.fixture(scope='session')
def empower_configuration(settings):
    return EmpowerConfiguration(
        ics_executable_name=settings.ics_executable_name,
        ics_instrument_type=settings.ics_instrument_type,
        empower_system_name=settings.empower_system_name,
        ics_installer_path=settings.ics_installer_path,
        ics_download_url=settings.ics_download_url,
        ics_version=settings.ics_version,
        reg_key=settings.empower_reg_key,
        username=settings.empower_username,
        password=settings.empower_password,
        hardware_system_name=settings.hardware_system_name
    )


@pytest.fixture(scope='session')
def instrument_alarm_utility_config(settings, components_config):
    return InstrumentAlarmUtility(
        hostname=settings.host,
        username=settings.instrument_username,
        password=settings.instrument_password,
        jump_server_username=settings.host_username,
        jump_server_password=settings.host_password,
        ispp_hostname=settings.ispp_hostname,
        isym_hostname=settings.isym_hostname,
        # Telnet uses the same credentials as Empower login
        telnet_username=settings.empower_username,
        telnet_password=settings.empower_password,
        components_config=components_config
    )


@pytest.fixture(scope='session')
def default_api_timeout_in_seconds(settings):
    return settings.default_assert_timeout_in_seconds


@dataclass
class BrowserConfiguration:
    headless: bool
    results_folder: str


@pytest.fixture(scope='session')
def browser_config(request, results_folder, settings):
    headless = settings.get(HEADLESS, request.config.getoption("headless"), cast="@bool")
    return BrowserConfiguration(headless=headless, results_folder=results_folder)


@pytest.fixture(scope='session')
def executing_host(settings) -> ComponentConfiguration:
    return ComponentConfiguration(hostname=settings.host, username=settings.host_username, password=settings.host_password)


@pytest.fixture(scope='session')
def atom_root_dir() -> str:
    return os.path.dirname(__file__)


@pytest.fixture(scope='session')
def test_data_dir(atom_root_dir) -> str:
    return os.path.join(atom_root_dir, "tests", "data")
