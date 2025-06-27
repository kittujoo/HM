import os

from glom import assign, delete
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorState
from isym_test_api.rest_api.api.behavior.system_meta_tuv_wavelength_calibration_request import generate_calibrate_wavelength_request
from isym_test_api.rest_api.drivers.detection.tuv_command_driver import TuvCommandDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.convertion_utilities import parse_string_to_obj
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_calibrate_wavelength_test.feature')


# region When

@when('wavelength calibration is started')
def request_calibrate_wavelength(context, tuv_command_rest_api_driver: TuvCommandDriver):
    context['api_response'] = tuv_command_rest_api_driver.calibrate_wavelength(payload=generate_calibrate_wavelength_request(True, True))


@when(cfparse('the calibrate wavelength data "{property_name}" is set with "{value}"'))
def set_valid_calibrate_wavelength_data(context, property_name: str, value: str, tuv_command_rest_api_driver: TuvCommandDriver):
    payload = as_dict(generate_calibrate_wavelength_request(False, False))
    value = parse_string_to_obj(value.lower())
    assign(payload, property_name, value)
    context['calibrate_wavelength'] = payload
    context['api_response'] = tuv_command_rest_api_driver.calibrate_wavelength(payload=payload)


@when(cfparse('the calibrate wavelength data is set with missing "{property_name}" in payload'))
def set_missing_calibrate_wavelength_data(context, property_name: str, tuv_command_rest_api_driver: TuvCommandDriver):
    payload = as_dict(generate_calibrate_wavelength_request(False, False))
    delete(payload, property_name)
    context['calibrate_wavelength'] = payload
    context['api_response'] = tuv_command_rest_api_driver.calibrate_wavelength(payload=payload)


@when(cfparse('the calibrate wavelength data is set with missing "{property_name}" value in payload'))
def set_missing_value_calibrate_wavelength_data(context, property_name: str, tuv_command_rest_api_driver: TuvCommandDriver):
    payload = as_dict(generate_calibrate_wavelength_request(False, False))
    assign(payload, property_name, None)
    context['calibrate_wavelength'] = payload
    context['api_response'] = tuv_command_rest_api_driver.calibrate_wavelength(payload=payload)

# endregion When


# region Then

@then('the calibrate wavelength state is active')
def get_calibrate_wavelength_status_active(tuv_command_rest_api_driver: TuvCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: tuv_command_rest_api_driver.get_calibrate_wavelength_status().data.state, BehaviorState.BehaviorState_ACTIVE,
                            "Calibrate Wavelength state does not become active", timeout_in_seconds=WaitTimeConstants.LittleWait)


@then('the calibrate wavelength state is inactive')
def get_calibrate_wavelength_status_inactive(tuv_command_rest_api_driver: TuvCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: tuv_command_rest_api_driver.get_calibrate_wavelength_status().data.state, BehaviorState.BehaviorState_INACTIVE,
                            "Calibrate Wavelength state does not become inactive", timeout_in_seconds=WaitTimeConstants.ExtraWait)

# endregion Then
