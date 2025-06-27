import os

import pytest
from glom import assign
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.column_manager.temperature_control_request import ChcThermalControlState, ThermalControlState
from isym_test_api.rest_api.api.column_manager.temperature_request import ColumnTemperatureW
from isym_test_api.rest_api.drivers.column_manager.column_manager_temperature_driver import ColumnManagerTemperatureDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.convertion_utilities import parse_string_to_obj
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_column_temperature_set_control_test.feature')


@pytest.fixture
def initial_system_state(context, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, assert_timeout: AssertTimeout):
    context['initial_temperature'] = 20.0
    set_temperature_request = ColumnTemperatureW(targetTemperatureDegC=context['initial_temperature'])
    column_manager_temperature_rest_api_driver.set_temperature(set_temperature_request)
    assert_timeout.value_is_within_tolerance(lambda: column_manager_temperature_rest_api_driver.get_current_temperature(), context['initial_temperature'],
                                             tolerance=0.5,
                                             message="Column current temperature is not as expected",
                                             timeout_in_seconds=WaitTimeConstants.SmallWait)


@given(cfparse('the column thermal control state is "{initial_state}"'))
def column_thermal_control_initial_state(initial_state: ThermalControlState, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver,
                                         assert_timeout: AssertTimeout):
    column_manager_temperature_rest_api_driver.set_temperature_control(initial_state)
    assert_timeout.are_equal(lambda: column_manager_temperature_rest_api_driver.get_thermal_control_state(),
                             initial_state, "Thermal control state is not as expected")


@when(cfparse('the column thermal control state is changed to "{new_state}"'))
def column_change_thermal_control(context, new_state, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature_control(new_state)


@when(cfparse('the column target temperature is set to "{temperature:f}"'))
def set_target_temperature(context, temperature: float, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, initial_system_state):
    set_temperature_request = ColumnTemperatureW(targetTemperatureDegC=temperature)
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when('the target temperature is changed with property targetTemperatureDegC removed')
def remove_temperature_control_property(context, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    payload_as_dict = {}
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature_control(payload_as_dict)


@when(cfparse('the target temperature is changed with additional property "{property_name}" and value "{value}"'))
def add_column_temperature_property(context, property_name, value, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    payload_as_dict = as_dict(ColumnTemperatureW())
    payload_as_dict[property_name] = value
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('column set target temperature request sent with "{property_name}" = "{value}"'))
def set_target_temperature_string(property_name, value, context, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    payload = as_dict(ColumnTemperatureW())
    value = parse_string_to_obj(value)
    assign(payload, property_name, value)
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature(payload)


@when('the column thermal control state is changed with property thermalControlState removed')
def remove_column_thermal_control_property(context, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    payload_as_dict = {}
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('the column thermal control is changed with additional property "{property_name}" and value "{value}"'))
def add_column_thermal_control_property(context, property_name, value, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    payload_as_dict = as_dict(ChcThermalControlState())
    payload_as_dict[property_name] = value
    context['api_response'] = column_manager_temperature_rest_api_driver.set_temperature(payload_as_dict)


@when(cfparse('the target temperature is increased by {temperature:f} degrees'))
def increase_temperature(temperature: float, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, context, initial_system_state):
    current_temperature = column_manager_temperature_rest_api_driver.get_current_temperature()
    context["target_temperature"] = round(current_temperature + temperature, 2)
    set_temperature_request = ColumnTemperatureW(targetTemperatureDegC=context["target_temperature"])
    column_manager_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when(cfparse('the target temperature is decreased by {temperature:f} degrees'))
def decrease_temperature(temperature: float, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, context, initial_system_state):
    current_temperature = column_manager_temperature_rest_api_driver.get_current_temperature()
    context["target_temperature"] = round(current_temperature - temperature, 2)
    set_temperature_request = ColumnTemperatureW(targetTemperatureDegC=context["target_temperature"])
    column_manager_temperature_rest_api_driver.set_temperature(set_temperature_request)


@then('the target temperature updates to the changed value')
def temperature_updates(column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, context, initial_system_state,
                        assert_timeout: AssertTimeout):
    new_temperature = context["target_temperature"]
    assert_timeout.value_is_within_tolerance(lambda: column_manager_temperature_rest_api_driver.get_current_temperature(),
                                             new_temperature, tolerance=0.5, message="Column current temperature is not as expected",
                                             timeout_in_seconds=WaitTimeConstants.SmallWait)


@then('the current temperature should not update to given degrees')
def set_target_temperature_invalid(context, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.value_is_not_within_tolerance(lambda: column_manager_temperature_rest_api_driver.get_current_temperature(),
                                                 context['initial_temperature'], tolerance=0.5,
                                                 message="Current temperature was changed", timeout_in_seconds=WaitTimeConstants.SmallWait)


@then(cfparse('the column thermal control state updates to "{new_state}"'))
def column_assert_thermal_control(new_state, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: column_manager_temperature_rest_api_driver.get_thermal_control_state(),
                             new_state, "Thermal control state is not as expected")


@then(cfparse('the column current temperature updates to "{temperature:f}" degrees'))
def get_current_temperature(temperature: float, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver, assert_timeout: AssertTimeout):
    assert_timeout.value_is_within_tolerance(lambda: column_manager_temperature_rest_api_driver.get_current_temperature(),
                                             temperature, tolerance=0.5,
                                             message="Column current temperature is not as expected", timeout_in_seconds=WaitTimeConstants.SmallWait)
