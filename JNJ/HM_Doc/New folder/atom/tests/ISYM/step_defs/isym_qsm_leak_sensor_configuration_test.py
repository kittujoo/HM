import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.solvent_management.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.drivers.solvent_management.qsm_flow_driver import QSMFlowDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_qsm_leak_sensor_configuration_test.feature')


@when(cfparse('the qsm leak sensor is "{status}"'))
def set_configuration(context, status, qsm_flow_rest_api_driver: QSMFlowDriver):
    payload = LeakSensorConfig()
    status = True if status == 'enabled' else False
    payload.enabled = status
    context['api_response'] = qsm_flow_rest_api_driver.set_qsm_leak_sensor_configuration(payload=payload)


@then(cfparse('the status of qsm leak sensor will be "{status}"'))
def check_status(status, qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: qsm_flow_rest_api_driver.get_qsm_leak_sensor_configuration().enabled, str_to_bool(status),
                             "The leak sensor status was not as expected")
