import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.sample_management.inject_valve_request import generate_default_inject_valve_request
from isym_test_api.rest_api.drivers.sample_management.ftn_inject_valve_driver import FtnInjectValveDriver
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_inject_valve_test.feature')


@when(cfparse('inject valve is set to "{position_name}" position'))
def request_inject_valve_position(context, position_name: str, inject_valve_rest_api_driver: FtnInjectValveDriver):
    context['api_response'] = inject_valve_rest_api_driver.set_inject_valve(payload=generate_default_inject_valve_request(position_name))


@then(cfparse('the inject valve position is set to "{position_name}"'))
def verify_inject_valve_position(context, position_name: str, inject_valve_rest_api_driver: FtnInjectValveDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: inject_valve_rest_api_driver.get_inject_valve().position.name,
                             position_name, "Inject Valve Position is not as expected")
