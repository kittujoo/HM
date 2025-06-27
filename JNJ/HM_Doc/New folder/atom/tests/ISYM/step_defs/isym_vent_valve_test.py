import os

from glom import delete
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.solvent_management.vent_valve_request import generate_default_vent_valve_request
from isym_test_api.rest_api.api.solvent_management.vent_valve_response import QsmVentValveR
from isym_test_api.rest_api.drivers.solvent_management.qsm_vent_valve_driver import QsmVentValveDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.convertion_utilities import parse_string_to_obj
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_vent_valve_test.feature')


# region Given

@given(cfparse('the vent valve is positioned for "{vent_valve_position}" position'))
def identify_vent_valve(context, vent_valve_position: str, vent_valve_rest_api_driver: QsmVentValveDriver, assert_timeout: AssertTimeout):
    context['api_response'] = vent_valve_rest_api_driver.set_vent_valve(payload=generate_default_vent_valve_request(vent_valve_position))
    assert_timeout.is_true(lambda: vent_valve_rest_api_driver.is_vent_valve_complete(),
                           "Vent Valve did not positioned", WaitTimeConstants.SmallWait)
    response: QsmVentValveR = vent_valve_rest_api_driver.get_vent_valve().data
    assert response.position.name == vent_valve_position, "Vent Valve position is incorrect"


# endregion Given


# region When

@when(cfparse('the vent valve is requested for "{vent_valve_position}" position'))
def request_vent_valve(context, vent_valve_position: str, vent_valve_rest_api_driver: QsmVentValveDriver):
    context['api_response'] = vent_valve_rest_api_driver.set_vent_valve(payload=generate_default_vent_valve_request(vent_valve_position))


@when(cfparse('the vent valve "{vent_valve_position}" position is requested for "{property_name}" with "{value}"'))
def request_out_of_limit_threshold_vent_valve(context, vent_valve_position: str, property_name: str, value: str,
                                              vent_valve_rest_api_driver: QsmVentValveDriver):
    payload = as_dict(generate_default_vent_valve_request(vent_valve_position))
    payload[property_name] = parse_string_to_obj(value)
    context['api_response'] = vent_valve_rest_api_driver.set_vent_valve(payload=payload)


@when(cfparse('the vent valve "{vent_valve_position}" position is requested without "{property_name}" property'))
def request_missing_property_vent_valve(context, vent_valve_position: str, property_name: str, vent_valve_rest_api_driver: QsmVentValveDriver):
    payload = as_dict(generate_default_vent_valve_request(vent_valve_position))
    delete(payload, property_name)
    context['api_response'] = vent_valve_rest_api_driver.set_vent_valve(payload=payload)


# endregion When


# region Then

@then(cfparse('the vent valve is positioned for "{vent_valve_position}"'))
def verify_vent_valve_position(vent_valve_position: str, vent_valve_rest_api_driver: QsmVentValveDriver):
    response: QsmVentValveR = vent_valve_rest_api_driver.get_vent_valve().data
    assert response.position.name == vent_valve_position, "Vent Valve position is incorrect"


@then('the vent valve workflow is completed')
def vent_valve_status(vent_valve_rest_api_driver: QsmVentValveDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: vent_valve_rest_api_driver.is_vent_valve_complete(),
                           "Vent Valve test did not complete", WaitTimeConstants.SmallWait)

# endregion Then
