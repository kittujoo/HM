import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.seperation.leak_sensor_request import LeakSensorConfig
from isym_test_api.rest_api.drivers.seperation.chc_leak_sensor_driver import CHCLeakSensorDriver
from utilities.logger import Logger
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_chc_leak_sensor_configuration.feature')


@when(cfparse('the CHC leak sensor is "{status}"'))
def set_configuration(context, status: str, chc_leak_sensor_rest_api_driver: CHCLeakSensorDriver):
    status = True if status == 'enabled' else False
    payload = LeakSensorConfig(enabled=status)
    context['api_response'] = chc_leak_sensor_rest_api_driver.set_chc_leak_sensor_configuration(payload=payload)


@then(cfparse('the status of CHC leak sensor will be "{status}"'))
def check_status(status, chc_leak_sensor_rest_api_driver: CHCLeakSensorDriver):
    assert chc_leak_sensor_rest_api_driver.get_chc_leak_sensor_configuration().data.enabled == str_to_bool(status), "The CHC leak sensor status was not as expected"
