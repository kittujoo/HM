import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.metering_pump_leak.metering_pump_leak_request import (
    generate_start_metering_pump_leak_test_non_default,
    generate_start_metering_pump_leak_test_minimum_pressure,
    generate_start_metering_pump_leak_test_maximum_pressure,
    SystemMeteringPumpLeakTest,
    generate_start_metering_pump_leak_test_below_min_pressure,
    generate_start_metering_pump_leak_test_above_max_pressure)
from isym_test_api.rest_api.drivers.behavior.metering_pump_leak_driver import MeteringPumpLeakDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_metering_pump_leak_test.feature')


# region When

@when('a metering pump leak test is started for solvent_a with the metering pump primed')
def start_metering_pump_leak_test(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = SystemMeteringPumpLeakTest()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when('a metering pump leak test is started for non-default valid values')
def start_metering_pump_leak_test_non_default(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = generate_start_metering_pump_leak_test_non_default()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when(cfparse('a metering pump leak test is started with property "{property_name}" missing'))
def start_metering_pump_leak_test_missing_required_field(context, property_name, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload_as_dict = as_dict(SystemMeteringPumpLeakTest())
    payload = payload_as_dict.pop(property_name)
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when('a metering pump leak test is started with minimum pressure')
def start_metering_pump_leak_test_minimum_pressure(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = generate_start_metering_pump_leak_test_minimum_pressure()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when('a metering pump leak test is started with maximum pressure')
def start_metering_pump_leak_test_maximum_pressure(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = generate_start_metering_pump_leak_test_maximum_pressure()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when('a metering pump leak test is started just below minimum pressure')
def start_metering_pump_leak_test_below_minimum_pressure(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = generate_start_metering_pump_leak_test_below_min_pressure()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when('a metering pump leak test is started just above maximum pressure')
def start_metering_pump_leak_test_above_maximum_pressure(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload = generate_start_metering_pump_leak_test_above_max_pressure()
    context['payload'] = payload
    context['api_response'] = metering_pump_leak_rest_api_driver.start_test(payload)


@when(cfparse('a metering pump leak test is started with an additional property "{property_name}" with a value "{value}"'))
def start_metering_pump_leak_test_additional_property(context, property_name, value, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    payload_as_dict = as_dict(SystemMeteringPumpLeakTest())
    payload_as_dict[property_name] = value
    context["api_response"] = metering_pump_leak_rest_api_driver.start_test(payload_as_dict)


# endregion When


# region Then

@then('the metering pump leak test completes with no leaks')
def assert_metering_pump_leak_test_result(metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: metering_pump_leak_rest_api_driver.get_status().data.state,
                             "BehaviorState_INACTIVE", "Metering pump leak test status is not as expected", WaitTimeConstants.MidWait)
    assert_timeout.value_is_within_tolerance(lambda: float(metering_pump_leak_rest_api_driver.get_result().data.leakRateulPerMin), expected=0, tolerance=0.5,
                                             message="Metering pump leak rate is not as expected")


@then('the leak test status will be passed')
def assert_metering_pump_leak_test_status(metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: metering_pump_leak_rest_api_driver.get_result().data.leakTestPassed, True,
                             "Metering pump leak test 'leakTestPassed' status is not as expected", WaitTimeConstants.MidWait)


@then('the stored leak test configuration is as expected')
def verify_leak_test_configuration(context, metering_pump_leak_rest_api_driver: MeteringPumpLeakDriver):
    expected_data = as_dict(context['payload'])
    assert as_dict(metering_pump_leak_rest_api_driver.get_store().data) == expected_data, "Metering pump leak test store is not as expected"

# endregion Then
