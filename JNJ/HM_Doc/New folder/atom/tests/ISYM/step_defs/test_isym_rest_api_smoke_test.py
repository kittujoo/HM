import os
from dataclasses import asdict

from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.api.system.system_state_response import SystemStateEnum
from isym_test_api.rest_api.drivers.routes_api_driver import RoutesApiDriver
from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from utilities.assert_timeout import AssertTimeout
from utilities.assertions import assert_object_equal
from utilities.json_utility import read_json_file
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_rest_api_smoke_test.feature')


@when('a command to get the instrument state is sent via HTTP request')
def get_instrument_state_via_http(context, system_state_rest_api_driver: SystemStateDriver):
    context['api_response'] = system_state_rest_api_driver.get_system_state()


@then('the HTTP reply returns the current state of the instrument')
def assert_http_reply_returns_a_system_state(context, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: context['api_response'].state in SystemStateEnum, "api_response doesn't contain current system state")


@when('instrument routes are requested')
def get_instrument_api_routes(context, routes_api_driver: RoutesApiDriver):
    context['api_routes'] = routes_api_driver.get_endpoint_routes()


@then('the routes returns a list of endpoints')
def assert_returned_api_routes_list(context):
    actual_api_routes = context['api_routes'].endpoints
    assert actual_api_routes, "Returned endpoints list is absent"


@then('the endpoints returned are not changed')
def assert_returned_api_routes_string(context, test_data_dir):
    actual_api_routes = asdict(context['api_routes'])
    expected_endpoints_json = os.path.join(test_data_dir, "routes", "isym_endpoints.json")
    expected_api_routes = read_json_file(expected_endpoints_json)
    assert_object_equal(actual_api_routes, expected_api_routes)
