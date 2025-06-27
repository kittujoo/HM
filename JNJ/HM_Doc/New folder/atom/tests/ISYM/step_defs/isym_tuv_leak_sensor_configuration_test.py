import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.detection.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.drivers.detection.tuv_flow_driver import TUVFlowDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_tuv_leak_sensor_configuration_test.feature')


@when(cfparse('the tuv leak sensor is "{status}"'))
def set_configuration(context, status, tuv_flow_rest_api_driver: TUVFlowDriver):
    payload = LeakSensorConfig()
    status = True if status == 'enabled' else False
    payload.enabled = status
    context['api_response'] = tuv_flow_rest_api_driver.set_tuv_leak_sensor_configuration(payload=payload)


@then(cfparse('the status of tuv leak sensor will be "{status}"'))
def check_status(status, tuv_flow_rest_api_driver: TUVFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: tuv_flow_rest_api_driver.get_tuv_leak_sensor_configuration().enabled, str_to_bool(status),
                             "The leak sensor status was not as expected")
