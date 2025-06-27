import os

import pytest
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.sample_management.temperature_control_request import FtnThermalControlState, ThermalControlState
from isym_test_api.rest_api.api.sample_management.temperature_request import FtnSampleTemperatureW
from isym_test_api.rest_api.drivers.sample_management.ftn_temperature_driver import FTNTemperatureDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_ftn_temperature_set_control_test.feature')


@pytest.fixture
def initial_system_state(context, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    context['initial_temperature'] = 20.0
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=context['initial_temperature'])
    ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)
    assert_timeout.value_is_within_tolerance(lambda: ftn_temperature_rest_api_driver.get_current_temperature(), context['initial_temperature'],
                                             tolerance=0.5,
                                             message="Ftn current temperature is not as expected",
                                             timeout_in_seconds=WaitTimeConstants.SmallWait)


@given(cfparse('the FTN thermal control state is "{initial_state}"'))
def ftn_thermal_control_initial_state(initial_state: ThermalControlState, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    ftn_temperature_rest_api_driver.set_temperature_control(initial_state)
    assert_timeout.are_equal(lambda: ftn_temperature_rest_api_driver.get_thermal_control_state(), initial_state, "Thermal control state is not as expected")


@when(cfparse('the FTN thermal control state is changed to "{new_state}"'))
def ftn_change_thermal_control(context, new_state, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature_control(new_state)


@when(cfparse('the FTN sample temperature is changed to "{temperature:f}"'))
def set_target_temperature(context, temperature: float, ftn_temperature_rest_api_driver: FTNTemperatureDriver, initial_system_state):
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=temperature)
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when('the FTN sample temperature is changed with property targetTemperatureDegC removed')
def remove_ftn_temperature_property(context, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    payload_as_dict = {}
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature_control(payload_as_dict)


@when(cfparse('the FTN sample temperature is changed with additional property "{property_name}" and value "{value}"'))
def add_ftn_temperature_property(context, property_name, value, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    payload_as_dict = as_dict(FtnSampleTemperatureW())
    payload_as_dict[property_name] = value
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('the FTN sample temperature is changed with string "{temperature}"'))
def set_ftn_target_temperature_string(context, temperature, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=temperature)
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when('the FTN thermal control state is changed with property thermalControlState removed')
def remove_ftn_thermal_control_property(context, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    payload_as_dict = {}
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('the FTN thermal control is changed with additional property "{property_name}" and value "{value}"'))
def add_ftn_thermal_control_property(context, property_name, value, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    payload_as_dict = as_dict(FtnThermalControlState())
    payload_as_dict[property_name] = value
    context['api_response'] = ftn_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('the FTN sample temperature is increased by {temperature:f} degrees'))
def increase_temperature(temperature: float, ftn_temperature_rest_api_driver: FTNTemperatureDriver, context, initial_system_state):
    current_temperature = ftn_temperature_rest_api_driver.get_current_temperature()
    context["ftn_sample_temperature"] = round(current_temperature + temperature, 2)
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=context["ftn_sample_temperature"])
    ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when(cfparse('the FTN sample temperature is decreased by {temperature:f} degrees'))
def decrease_temperature(temperature: float, ftn_temperature_rest_api_driver: FTNTemperatureDriver, context, initial_system_state):
    current_temperature = ftn_temperature_rest_api_driver.get_current_temperature()
    context["ftn_sample_temperature"] = round(current_temperature - temperature, 2)
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=context["ftn_sample_temperature"])
    ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)


@then('the FTN sample temperature updates to the changed value')
def temperature_updates(ftn_temperature_rest_api_driver: FTNTemperatureDriver, context, initial_system_state, assert_timeout: AssertTimeout):
    new_temperature = context["ftn_sample_temperature"]
    assert_timeout.value_is_within_tolerance(lambda: ftn_temperature_rest_api_driver.get_current_temperature(),
                                             new_temperature, tolerance=0.5, message="Ftn current temperature is not as expected",
                                             timeout_in_seconds=WaitTimeConstants.SmallWait)


@then('the FTN sample temperature should not update to given degrees')
def set_ftn_target_temperature_invalid(context, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.value_is_not_within_tolerance(lambda: ftn_temperature_rest_api_driver.get_current_temperature(),
                                                 context['initial_temperature'], tolerance=0.5, message="FTN temperature was changed",
                                                 timeout_in_seconds=WaitTimeConstants.SmallWait)


@then(cfparse('the FTN thermal control state updates to "{new_state}"'))
def assert_ftn_thermal_control(new_state, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: ftn_temperature_rest_api_driver.get_thermal_control_state(), new_state, "Thermal control state is not as expected")


@then(cfparse('the FTN sample temperature updates to "{temperature:f}" degrees'))
def get_ftn_current_temperature(temperature: float, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.value_is_within_tolerance(lambda: ftn_temperature_rest_api_driver.get_current_temperature(),
                                             temperature, tolerance=0.5, message="Ftn current temperature is not as expected",
                                             timeout_in_seconds=WaitTimeConstants.SmallWait)
