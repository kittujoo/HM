import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorState
from isym_test_api.rest_api.api.sample_management.wash_needle_request import FTNWashNeedleRequest
from isym_test_api.rest_api.api.sample_management.wash_needle_request import generate_default_prime_cycle_request, generate_default_wash_needle_request
from isym_test_api.rest_api.drivers.sample_management.ftn_wash_needle_driver import FtnWashNeedleDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_needle_wash_workflow_test.feature')


@when(cfparse('the wash needle operation requested with washDurationSec = "{value:d}" seconds'))
def request_wash_needle_operation(context, value, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_wash_needle_request(payload=FTNWashNeedleRequest(washDurationSec=value))


@then(cfparse('the wash needle state is active for "{value:d}" seconds'))
def get_wash_needle_status_active(value, wash_needle_rest_api_driver: FtnWashNeedleDriver, assert_timeout: AssertTimeout):
    assert_timeout.value_remains_same(lambda: wash_needle_rest_api_driver.get_wash_needle_status().data.state, BehaviorState.BehaviorState_ACTIVE,
                                      message="Wash needle states changed",
                                      timeout_in_seconds=value)


@then(cfparse('the wash needle state becomes inactive'))
def get_wash_needle_status_inactive(wash_needle_rest_api_driver: FtnWashNeedleDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: wash_needle_rest_api_driver.get_wash_needle_status().data.state, BehaviorState.BehaviorState_INACTIVE,
                             "the wash needle status was not inactive", timeout_in_seconds=WaitTimeConstants.LittleWait)


@then(cfparse('the last wash needle request was stored as "{value:d}"'))
def get_wash_needle_store(value, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    assert wash_needle_rest_api_driver.get_wash_needle_store().data.washDurationSec == value, "the last wash needle request was not stored as expected"


@when(cfparse('the wash needle operation requested without washDurationSec property'))
def request_wash_needle_with_empty_payload(context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_wash_needle_request({})


@when(cfparse('the wash needle operation requested with washDurationSec as string'))
def request_wash_needle_with_string_value(context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_wash_needle_request(payload=FTNWashNeedleRequest(washDurationSec="Invalid"))


@when(cfparse('the wash needle operation requested with primeCycles'))
def request_wash_needle_with_prime_cycles(context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_wash_needle_request(generate_default_prime_cycle_request())


@when(cfparse('the wash needle operation requested with additional property duration as {value:d}'))
def request_wash_needle_with_prime_cycles(context, value: int, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    payload_as_dict = as_dict(FTNWashNeedleRequest())
    payload_as_dict["duration"] = value
    context['api_response'] = wash_needle_rest_api_driver.send_wash_needle_request(payload_as_dict)


@when(cfparse('the needle wash operation requested'))
def request_needle_wash_operation(context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_needle_wash_request({})


@then(cfparse('the needle wash state is active'))
def get_needle_wash_status_active(wash_needle_rest_api_driver: FtnWashNeedleDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: wash_needle_rest_api_driver.get_needle_wash_status().data.state, BehaviorState.BehaviorState_ACTIVE,
                             "wash needle state does not become active", timeout_in_seconds=WaitTimeConstants.LittleWait)


@then(cfparse('the needle wash state becomes inactive'))
def get_needle_wash_status_inactive(wash_needle_rest_api_driver: FtnWashNeedleDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: wash_needle_rest_api_driver.get_needle_wash_status().data.state, BehaviorState.BehaviorState_INACTIVE,
                             "wash needle state does not become inactive", timeout_in_seconds=WaitTimeConstants.LittleWait)


@when(cfparse('the needle wash operation requested with payload as string'))
def request_needle_wash_random(context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    context['api_response'] = wash_needle_rest_api_driver.send_needle_wash_request("Invalid")


@when(cfparse('the needle wash operation requested with payload "{property_name}"'))
def request_needle_wash_prime(property_name, context, wash_needle_rest_api_driver: FtnWashNeedleDriver):
    payload = generate_default_prime_cycle_request() if property_name == "primeCycles" else generate_default_wash_needle_request()
    context['api_response'] = wash_needle_rest_api_driver.send_needle_wash_request(payload)
