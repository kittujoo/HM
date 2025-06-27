from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.dynamic_leak.dynamic_leak_request import SystemLeakTest
from isym_test_api.rest_api.drivers.behavior.dynamic_leak_driver import DynamicLeakDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.string_utility import str_to_bool


if __name__ == Path(__file__).stem:
    scenarios('../features/isym_dynamic_leak_test.feature')


@when(cfparse('Dynamic leak test started with property "{property_name}" is removed'))
def remove_dynamic_leak_test_property(context, property_name, dynamic_leak_driver_api_driver: DynamicLeakDriver):
    payload_as_dict = as_dict(SystemLeakTest())
    payload = payload_as_dict.pop(property_name)
    context["api_response"] = dynamic_leak_driver_api_driver.start_leak_test(payload)


@when(cfparse('Dynamic leak test started with new property "{property_name}" is added with value "{value}"'))
def add_dynamic_leak_test_property(context, property_name, value, dynamic_leak_driver_api_driver: DynamicLeakDriver):
    payload_as_dict = as_dict(SystemLeakTest())
    payload_as_dict[property_name] = value
    context["api_response"] = dynamic_leak_driver_api_driver.start_leak_test(payload_as_dict)


@when(cfparse('parameter "{parameter}" set as boolean "{value}" for Dynamic Leak test'))
def set_dynamic_leak_test_bool(context, parameter, value):
    payload = context.get('payload', SystemLeakTest())
    value = str_to_bool(value)
    setattr(payload, parameter, value)
    context['payload'] = payload


@when(cfparse('parameter "{parameter}" set as numeric "{value:f}" for Dynamic Leak test'))
def set_dynamic_leak_test_numeric(context, parameter, value):
    payload = context.get('payload', SystemLeakTest())
    setattr(payload, parameter, value)
    context['payload'] = payload


@when(cfparse('parameter "{parameter}" set as "{value}" for Dynamic Leak test'))
def set_dynamic_leak_test(context, parameter, value):
    payload = context.get('payload', SystemLeakTest())
    setattr(payload, parameter, value)
    context['payload'] = payload


@when('Dynamic leak test is started')
def start_dynamic_leak_test(context, dynamic_leak_driver_api_driver: DynamicLeakDriver):
    context["api_response"] = dynamic_leak_driver_api_driver.start_leak_test(payload=context['payload'])


@then('the dynamic leak test completes with no leaks')
def assert_dynamic_leak_test_result(context, dynamic_leak_driver_api_driver: DynamicLeakDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: dynamic_leak_driver_api_driver.get_status(),
                            "BehaviorState_INACTIVE", "Dynamic leak test status is not as expected", WaitTimeConstants.LongWait)
    result = dynamic_leak_driver_api_driver.get_result()
    context['dynamic_leak_test_result'] = result
    assert all(
        [leak_rate_result.compressResult == 'PressurizeAxisCompressResult_PASSED' and leak_rate_result.monitorResult == 'PressurizeAxisMonitorResult_PASSED' for
         leak_rate_result in result.results]), "Dynamic leak test results is not as expected"


@then('the leak test status will be passed')
def assert_dynamic_leak_test_result(context):
    result = context['dynamic_leak_test_result']
    assert all(
        [leak_rate_result.leakTestPassed for leak_rate_result in result.results]), "Dynamic leak test results 'leakTestPassed' statuses is not as expected"
