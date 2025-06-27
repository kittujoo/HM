import json
import os
from typing import Dict, Optional, List

import pytest

from isym_test_api.rest_api.api.system.system_configuration_response import SystemConfigurationResponse
from isym_test_api.rest_api.drivers.system.system_configuration_driver import SystemConfigurationDriver
from utilities.configuration_models import EnvironmentType
from utilities.logger import Logger
from utilities.logs.ispp_log_collector import IsppLogCollector
from utilities.logs.isym_log_collector import IsymLogCollector
from utilities.logs.logs_collector_cds_env import LogsCollectorCDSEnv
from utilities.logs.logs_collector_instrument import LogsCollectorInstrument
from utilities.logs.logs_collector_interface import LogsCollectorInterface
from utilities.logs.logs_collector_simulator_env import LogsCollectorSimulatorEnv
from utilities.manifest.chromium_browser_manifest_collector import ChromiumBrowserManifestCollector
from utilities.manifest.common_data_manifest import CommonDataManifestCollector
from utilities.manifest.instrument_configuration_collector import InstrumentConfigurationCollector
from utilities.manifest.instrument_manifest_collector import InstrumentManifestCollector
from utilities.manifest.manifest_collector_cds_env import ManifestCollectorCdsEnv
from utilities.manifest.manifest_collector_interface import ManifestCollectorInterface
from utilities.manifest.manifest_collector_ispp import IsppManifestCollector
from utilities.manifest.manifest_collector_isym import IsymManifestCollector
from utilities.manifest.manifest_collector_isym_hardware import IsymHardwareManifestCollector
from utilities.ssh_connection import SSh
from utilities.universal_text_file_tool import SshTextFileTool

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def instrument_ports(components_config, isym_port_forwarder):
    instruments = {'chc', 'ftn', 'qsm', 'tuv'}

    ports = {}
    for instrument in instruments:
        config = components_config[instrument]
        ports[instrument] = isym_port_forwarder(config.hostname, 23)

    return ports


@pytest.fixture(scope='session')
def real_env_manifest_creators(components_config, instrument_ports, isym_linux_universal_tool, ispp_linux_universal_tool,
                               localhost_linux_universal_tool):
    """
    Generates proper manifest collectors for REAL env
    :param components_config: instruments hostnames, usernames and passwords for telnet connection
    :param instrument_ports: instruments ports provided by sshtunnel tool
    :param isym_linux_universal_tool: generic linux tool that could be used with ssh with isym credentials
    :param ispp_linux_universal_tool: generic linux tool that could be used with ssh with ispp credentials
    :param localhost_linux_universal_tool: generic linux tool that could be used on local host
    :return: List[ManifestCollectorInterface]
    """
    manifest_collectors = [IsppManifestCollector(ispp_linux_universal_tool),
                           IsymManifestCollector(isym_linux_universal_tool),
                           IsymHardwareManifestCollector(isym_linux_universal_tool),
                           ChromiumBrowserManifestCollector(localhost_linux_universal_tool)]

    for name, config in components_config.items():
        port = instrument_ports.get(name)
        manifest_collectors.append(InstrumentManifestCollector(instrument_name=name, hostname="localhost", username=config.username,
                                                               password=config.password, port=port))

    return manifest_collectors


@pytest.fixture(scope='session')
def system_configuration_details(system_configuration_driver: SystemConfigurationDriver) -> SystemConfigurationResponse:
    return system_configuration_driver.get_system_configuration()


@pytest.fixture(scope='session')
def cds_env_manifest_creators(registry_universal_tool, text_file_universal_tool, cmd_universal_tool, system_configuration_details):
    """
    Generates proper manifest collectors for CDS env
    :param registry_universal_tool: generic registry tool that could be used with ssh or localhost
    :param text_file_universal_tool: generic test file tool that could be used with ssh or localhost
    :param cmd_universal_tool: generic cmd tool that could be used with ssh or localhost
    :param system_configuration_details: details of current system configuration
    :return: List[ManifestCollectorInterface]
    """
    manifest_collectors = [ManifestCollectorCdsEnv(registry_universal_tool, text_file_universal_tool, cmd_universal_tool),
                           InstrumentConfigurationCollector(system_configuration_details)]
    return manifest_collectors


@pytest.fixture(scope='session')
def simulation_env_manifest_creators(ispp_linux_universal_tool, isym_linux_universal_tool, localhost_linux_universal_tool):
    """
    Generates proper manifest collectors for SIMULATION env
    :param isym_linux_universal_tool: generic linux tool that could be used with ssh with isym credentials
    :param ispp_linux_universal_tool: generic linux tool that could be used with ssh with ispp credentials
    :param localhost_linux_universal_tool: generic linux tool that could be used on local host
    :return: List[ManifestCollectorInterface]
    """
    manifest_collectors = [IsppManifestCollector(ispp_linux_universal_tool),
                           IsymManifestCollector(isym_linux_universal_tool),
                           ChromiumBrowserManifestCollector(localhost_linux_universal_tool)]
    return manifest_collectors


@pytest.fixture(scope='session', autouse=True)
def create_manifest(request, environment_type: EnvironmentType, results_folder):
    manifest_dict = {}
    manifest_collectors: List[ManifestCollectorInterface] = [CommonDataManifestCollector(environment_type)]

    if environment_type == EnvironmentType.REAL:
        real_env_manifest_collectors = try_get_fixture(request, 'real_env_manifest_creators', [])
        manifest_collectors.extend(real_env_manifest_collectors)
    elif environment_type == EnvironmentType.CDS:
        cds_env_manifest_collectors = try_get_fixture(request, 'cds_env_manifest_creators', [])
        manifest_collectors.extend(cds_env_manifest_collectors)
    elif environment_type == EnvironmentType.SIMULATION:
        simulation_env_manifest_collectors = try_get_fixture(request, 'simulation_env_manifest_creators', [])
        manifest_collectors.extend(simulation_env_manifest_collectors)
    else:
        logger.error(f"Unexpected environment type '{environment_type}'")

    for manifest_collector in manifest_collectors:
        try:
            manifest_collector.enrich_manifest(manifest_dict)
        except Exception as e:
            logger.error(f"Manifest collector: {manifest_collector} failed with error: {e}")

    with open(os.path.join(results_folder, "manifest.json"), "w+") as manifest:
        json.dump(manifest_dict, manifest, indent=4)


@pytest.fixture(scope='session')
def real_env_log_collectors(isym_config, ispp_config, results_folder, components_config, instrument_ports):
    log_collectors = {}
    path = os.path.join(results_folder, "instruments")

    for name, config in components_config.items():
        port = instrument_ports.get(name)
        log_collector = LogsCollectorInstrument(ip="localhost", port=port, username=config.username, password=config.password, instrument=name,
                                                results_folder=path)
        log_collectors[name] = log_collector

    isym_ssh = SSh(isym_config.hostname, isym_config.username, isym_config.password)
    ispp_ssh = SSh(ispp_config.hostname, ispp_config.username, ispp_config.password)
    isym_file_handler = SshTextFileTool(isym_ssh)
    log_collectors["IsymLogCollector"] = IsymLogCollector(file_handler=isym_file_handler, results_folder=results_folder)
    ispp_file_handler = SshTextFileTool(ispp_ssh)
    log_collectors["IsppLogCollector"] = IsppLogCollector(file_handler=ispp_file_handler, results_folder=results_folder)
    yield log_collectors


def try_get_fixture(request, fixture, default_value=None):
    try:
        return request.getfixturevalue(fixture)
    except Exception as e:
        logger.error(f"Failed to get fixture [{fixture}], error is [{e}")
        return default_value


@pytest.fixture(scope='session', autouse=True)
def start_logging(request, api_base_url, environment_type: EnvironmentType, isym_config, ispp_config, components_config, results_folder, ):
    """
    Called at the start of the session before performing collection and entering the run test loop.
    :return: None
    """
    log_collectors: Dict[str, Optional[LogsCollectorInterface]] = {}
    if environment_type == EnvironmentType.REAL:
        log_collectors = try_get_fixture(request, 'real_env_log_collectors', {})
    elif environment_type == EnvironmentType.CDS:
        log_collectors = {"LogsCollectorCDSEnv": LogsCollectorCDSEnv(results_folder)}
    elif environment_type == EnvironmentType.SIMULATION:
        log_collectors = {"LogsCollectorSimulatorEnv": LogsCollectorSimulatorEnv(results_folder)}
    else:
        logger.error(f"Unexpected environment type '{environment_type}'")

    for logger_name, log_collector in log_collectors.items():
        try:
            logger.debug(f"Starting log collector: [{logger_name}]")
            log_collector.start_logging()
        except Exception as e:
            log_collectors[logger_name] = None
            logger.error(f"Failed to start log collector [{logger_name}] with exception: [{e}]")

    yield

    for logger_name, log_collector in log_collectors.items():
        if log_collector is None:
            continue
        try:
            log_collector.stop_logging()
        except Exception as e:
            logger.error(f"Failed to stop log collector [{logger_name}] with exception: [{e}]")
