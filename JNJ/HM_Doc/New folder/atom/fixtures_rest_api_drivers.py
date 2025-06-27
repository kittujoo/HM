import os

import pytest

from isym_test_api.rest_api.api.system.session_models import SessionCredentials
from isym_test_api.rest_api.drivers.behavior.dynamic_leak_driver import DynamicLeakDriver
from isym_test_api.rest_api.drivers.behavior.metering_pump_leak_driver import MeteringPumpLeakDriver
from isym_test_api.rest_api.drivers.behavior.needle_seal_readiness_driver import NeedleSealReadinessDriver
from isym_test_api.rest_api.drivers.behavior.system_noise_and_drift_driver import SystemNoiseAndDriftDriver
from isym_test_api.rest_api.drivers.column_manager.chc_command_driver import ChcCommandDriver
from isym_test_api.rest_api.drivers.column_manager.column_manager_temperature_driver import ColumnManagerTemperatureDriver
from isym_test_api.rest_api.drivers.detection.tuv_command_driver import TuvCommandDriver
from isym_test_api.rest_api.drivers.detection.tuv_flow_driver import TUVFlowDriver
from isym_test_api.rest_api.drivers.detection.tuv_lamp_driver import TuvLampDriver
from isym_test_api.rest_api.drivers.meta_setting.meta_setting_driver import MetaSettingDriver
from isym_test_api.rest_api.drivers.rest_api_driver import RestAPIDriver
from isym_test_api.rest_api.drivers.routes_api_driver import RoutesApiDriver
from isym_test_api.rest_api.drivers.sample_management.ftn_inject_valve_driver import FtnInjectValveDriver
from isym_test_api.rest_api.drivers.sample_management.ftn_leak_sensor_driver import FTNLeakSensorDriver
from isym_test_api.rest_api.drivers.sample_management.ftn_temperature_driver import FTNTemperatureDriver
from isym_test_api.rest_api.drivers.sample_management.ftn_wash_needle_driver import FtnWashNeedleDriver
from isym_test_api.rest_api.drivers.seperation.chc_leak_sensor_driver import CHCLeakSensorDriver
from isym_test_api.rest_api.drivers.solvent_management.bottle_config_driver import BottleConfigurationDriver
from isym_test_api.rest_api.drivers.solvent_management.qsm_command_driver import QsmCommandDriver
from isym_test_api.rest_api.drivers.solvent_management.qsm_flow_driver import QSMFlowDriver
from isym_test_api.rest_api.drivers.solvent_management.qsm_vent_valve_driver import QsmVentValveDriver
from isym_test_api.rest_api.drivers.system.ambient_temperature_driver import AmbientTemperatureDriver
from isym_test_api.rest_api.drivers.system.command.start_column_driver import StartColumnDriver
from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from isym_test_api.rest_api.drivers.system.event_log_driver import EventLogDriver
from isym_test_api.rest_api.drivers.system.exclusive_mode_driver import ExclusiveModeDriver
from isym_test_api.rest_api.drivers.system.leak_sensors_driver import LeakSensorsDriver
from isym_test_api.rest_api.drivers.system.session_driver import SessionDriver
from isym_test_api.rest_api.drivers.system.system_configuration_driver import SystemConfigurationDriver
from isym_test_api.rest_api.drivers.system.system_event_driver import SystemEventDriver
from isym_test_api.rest_api.drivers.system.system_prime_fluidics_driver import PrimeFluidicsDriver
from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.rest_client import rest_session

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='session')
def auth_rest_api_driver(session_driver: SessionDriver) -> RestAPIDriver:
    session = rest_session()
    response = session_driver.create_session(SessionCredentials(applicationContext="TestSession"))
    if response.is_failed():
        message = f"Failed to create session with status code {response.status_code}, response was [{response.message}]"
        logger.error(message)
        raise ValueError(message)
    if not response.data.sessionId:
        message = f"Failed to obtain session id, response was [{response.message}]"
        logger.error(message)
        raise ValueError(message)
    session.headers.update({'sessionid': response.data.sessionId})
    driver = RestAPIDriver(session)
    yield driver
    response = session_driver.delete_session(response.data)
    if response.is_failed():
        message = f"Deletion of session failed with status code {response.status_code} with body: {response.message}"
        logger.error(message)
        raise ValueError(message)


@pytest.fixture(scope='session')
def rest_api_driver():
    session = rest_session()
    return RestAPIDriver(session)


@pytest.fixture(scope='session')
def qsm_flow_rest_api_driver(rest_api_driver, api_base_url):
    """
    Fixture to construct the QSM flow rest api driver.
    :return: QSMFlowDriver
    """
    driver = QSMFlowDriver(rest_api_driver, api_base_url)
    return driver


@pytest.fixture(scope='session')
def tuv_flow_rest_api_driver(rest_api_driver, api_base_url):
    """
    Fixture to construct the TUV flow rest api driver.
    :return: TUVFlowDriver
    """
    driver = TUVFlowDriver(rest_api_driver, api_base_url)
    return driver


# will be handled via ATOM-474
# @pytest.fixture(scope='session', autouse=True)
#     yield driver
#     try:
#         flow_state = driver.get_flow_status()
#         if not flow_state:
#             logger.info("Session finish - Flow was OFF.")
#             return
#         driver.set_flow_control(False)
#         assert_timeout.are_equal(lambda: driver.get_flow_status(), False
#                                 , "Flow was not turned off.")
#         logger.info("Session finish - Flow was turned off")
#     except Exception as e:
#         logger.error(f"Exception raised while turning flow off: {e}")


@pytest.fixture(scope='session')
def ftn_temperature_rest_api_driver(rest_api_driver, api_base_url, assert_timeout: AssertTimeout):
    driver = FTNTemperatureDriver(rest_api_driver, api_base_url, assert_timeout)
    yield driver
    driver.cleanup()


@pytest.fixture(scope='session')
def column_manager_temperature_rest_api_driver(rest_api_driver, api_base_url, assert_timeout: AssertTimeout):
    driver = ColumnManagerTemperatureDriver(rest_api_driver, api_base_url, assert_timeout)
    yield driver
    driver.cleanup()


@pytest.fixture(scope='session')
def metering_pump_leak_rest_api_driver(rest_api_driver, api_base_url):
    return MeteringPumpLeakDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def system_state_rest_api_driver(rest_api_driver, api_base_url):
    return SystemStateDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def exclusive_mode_rest_api_driver(rest_api_driver, api_base_url):
    return ExclusiveModeDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def system_command_rest_api_driver(rest_api_driver, api_base_url):
    return SystemCommandDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def routes_api_driver(rest_api_driver, api_base_url):
    return RoutesApiDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def data_system_acquisition_rest_api_driver(rest_api_driver, api_base_url):
    return DatasystemAcquisitionDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def start_column_rest_api_driver(rest_api_driver, api_base_url):
    return StartColumnDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def dynamic_leak_driver_api_driver(rest_api_driver, api_base_url):
    return DynamicLeakDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def system_noise_and_drift_rest_api_driver(rest_api_driver, api_base_url):
    return SystemNoiseAndDriftDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def meta_setting_rest_api_driver(rest_api_driver, api_base_url):
    return MetaSettingDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def needle_seal_readiness_rest_api_driver(rest_api_driver, api_base_url):
    return NeedleSealReadinessDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def prime_fluidics_rest_api_driver(rest_api_driver, api_base_url):
    return PrimeFluidicsDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def system_events_rest_api_driver(auth_rest_api_driver, api_base_url):
    return SystemEventDriver(auth_rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def inject_valve_rest_api_driver(rest_api_driver, api_base_url):
    return FtnInjectValveDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def ambient_temperature_rest_api_driver(rest_api_driver, api_base_url):
    return AmbientTemperatureDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def vent_valve_rest_api_driver(rest_api_driver, api_base_url):
    return QsmVentValveDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def session_driver(rest_api_driver, api_base_url) -> SessionDriver:
    return SessionDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def system_configuration_driver(rest_api_driver, api_base_url) -> SystemConfigurationDriver:
    return SystemConfigurationDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def tuv_lamp_rest_api_driver(rest_api_driver, api_base_url) -> TuvLampDriver:
    return TuvLampDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def chc_leak_sensor_rest_api_driver(rest_api_driver, api_base_url):
    return CHCLeakSensorDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def tuv_command_rest_api_driver(rest_api_driver, api_base_url):
    return TuvCommandDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def chc_command_rest_api_driver(rest_api_driver, api_base_url):
    return ChcCommandDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def qsm_command_rest_api_driver(rest_api_driver, api_base_url):
    return QsmCommandDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def leak_sensors_rest_api_driver(rest_api_driver, api_base_url):
    return LeakSensorsDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def wash_needle_rest_api_driver(rest_api_driver, api_base_url):
    return FtnWashNeedleDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def ftn_leak_sensor_rest_api_driver(rest_api_driver, api_base_url):
    return FTNLeakSensorDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def bottle_config_rest_api_driver(rest_api_driver, api_base_url):
    return BottleConfigurationDriver(rest_api_driver, api_base_url)


@pytest.fixture(scope='session')
def event_log_rest_api_driver(rest_api_driver, api_base_url):
    return EventLogDriver(rest_api_driver, api_base_url)
