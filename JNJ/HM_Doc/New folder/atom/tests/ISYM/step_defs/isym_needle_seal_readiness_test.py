from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorState
from isym_test_api.rest_api.api.behavior.needle_seal_readiness.needle_seal_readiness_request import generate_default_needle_seal_readiness_request
from isym_test_api.rest_api.drivers.behavior.needle_seal_readiness_driver import NeedleSealReadinessDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.datatables.headless_datatable import headlesstable
from utilities.glom_utilities import assign_many
from utilities.json_utility import as_dict

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_needle_seal_readiness_test.feature')


@when('a needle seal readiness test is started')
def start_needle_seal_readiness_test(context, needle_seal_readiness_rest_api_driver: NeedleSealReadinessDriver):
    payload = generate_default_needle_seal_readiness_request()
    context['api_response'] = needle_seal_readiness_rest_api_driver.start_test(payload)


@then('the needle seal readiness test status will be passed')
def verify_needle_seal_readiness_test_results(needle_seal_readiness_rest_api_driver: NeedleSealReadinessDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: str(needle_seal_readiness_rest_api_driver.get_result().result), "System_RESULTPASS",
                             "Needle seal readiness test failed", WaitTimeConstants.SmallWait)


@when(cfparse('payload set with flow rate target value = "{value:f}"'))
def set_flow_rate_property(context, value):
    context['payload'] = as_dict(generate_default_needle_seal_readiness_request(value))


@when(headlesstable('the needle seal readiness test is started with given data:'))
def modify_property_value(table, context, needle_seal_readiness_rest_api_driver: NeedleSealReadinessDriver):
    payload = as_dict(generate_default_needle_seal_readiness_request())
    assign_many(payload, table.as_dict(convert=True))
    context['api_response'] = needle_seal_readiness_rest_api_driver.start_test(payload)


@when('the needle seal readiness test is started')
def send_custom_method_payload(context, needle_seal_readiness_rest_api_driver: NeedleSealReadinessDriver):
    context['api_response'] = needle_seal_readiness_rest_api_driver.start_test(payload=context['payload'])


@then('the needle seal readiness test completes')
def assert_needle_seal_readiness_test_completes(needle_seal_readiness_rest_api_driver: NeedleSealReadinessDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: needle_seal_readiness_rest_api_driver.get_status().state,
                             BehaviorState.BehaviorState_ACTIVE, "Needle seal readiness test does not started.", WaitTimeConstants.MidWait)
    assert_timeout.are_equal(lambda: needle_seal_readiness_rest_api_driver.get_status().state,
                             BehaviorState.BehaviorState_INACTIVE, "Needle seal readiness test does not stopped.", WaitTimeConstants.MidWait)


@when('payload set with omitting property "<property_name>"')
@when(cfparse('payload set with omitting property "{property_name}"'))
def needle_seal_readiness_remove_property(context, property_name):
    payload_as_dict = as_dict(generate_default_needle_seal_readiness_request())
    payload_as_dict.pop(property_name)
    context['payload'] = payload_as_dict


@when('payload set with key additional property')
def needle_seal_readiness_remove_property(context):
    payload_as_dict = as_dict(generate_default_needle_seal_readiness_request())
    payload_as_dict["additionalProperties"] = False
    context['payload'] = payload_as_dict


@when(cfparse('payload set with key "{property_name}" value as "{property_value}"'))
def needle_seal_readiness_invalid_type_property(context, property_name: str, property_value: str):
    payload = as_dict(generate_default_needle_seal_readiness_request())
    payload[property_name] = property_value
    context['payload'] = payload
