import os

from pathlib import Path
from pytest_bdd import scenarios, when, then

from isym_test_api.rest_api.api.system.leak_sensors_configuration_request import \
    generate_default_enable_leak_sensors_configuration_request, generate_disable_leak_sensors_configuration_request
from isym_test_api.rest_api.api.system.leak_sensors_response import LeakSensorsStatus, LeakState
from isym_test_api.rest_api.drivers.column_manager.chc_command_driver import ChcCommandDriver
from isym_test_api.rest_api.drivers.detection.tuv_command_driver import TuvCommandDriver
from isym_test_api.rest_api.drivers.system.leak_sensors_driver import LeakSensorsDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_commands_test.feature')


# region When

@when('the scan column tag is requested')
def request_scan_column_tag_chc(chc_command_rest_api_driver: ChcCommandDriver):
    chc_command_rest_api_driver.start_scan_column_tag()


@when('the autozero activity is requested')
def request_auto_zero(tuv_command_rest_api_driver: TuvCommandDriver):
    tuv_command_rest_api_driver.set_auto_zero()


@when('the disable system leak sensor configuration is requested')
def request_set_leak_sensors_configuration(leak_sensors_rest_api_driver: LeakSensorsDriver):
    leak_sensors_rest_api_driver.set_leak_sensors_config(payload=generate_disable_leak_sensors_configuration_request())


@when('the enable system leak sensor configuration is requested')
def request_set_leak_sensors_configuration(leak_sensors_rest_api_driver: LeakSensorsDriver):
    leak_sensors_rest_api_driver.set_leak_sensors_config(payload=generate_default_enable_leak_sensors_configuration_request())


@when('the system leak sensor check is requested')
def request_get_leak_sensors(context, leak_sensors_rest_api_driver: LeakSensorsDriver):
    context['leak_sensors'] = leak_sensors_rest_api_driver.get_leak_sensors()


# endregion When


# region Then

@then('no leak status was observed in response')
def verify_no_leak(context):
    received_data: LeakSensorsStatus = context['leak_sensors']
    for leaksensor in received_data.leakSensors:
        assert leaksensor.state != LeakState.LeakState_LEAK, f"Leak observed in {leaksensor.deviceId} module: {leaksensor}"


@then('the autozero offsets values are collected')
def verify_auto_zero_offsets_values_stored(context, tuv_command_rest_api_driver: TuvCommandDriver):
    context['autozero_offset_before'] = tuv_command_rest_api_driver.get_auto_zero_offsets_value()


@then('the updated autozero offsets values were measured')
def verify_updated_auto_zero_offsets_values(context, tuv_command_rest_api_driver: TuvCommandDriver):
    response = tuv_command_rest_api_driver.get_auto_zero_offsets_value()
    assert response.autoZeroOffsetA != context['autozero_offset_before'].autoZeroOffsetA, "AutoZero was ideal on autoZeroOffsetA"
    assert response.autoZeroOffsetB != context['autozero_offset_before'].autoZeroOffsetB, "AutoZero was ideal on autoZeroOffsetB"


@then('the autozero activity started successfully')
def verify_autozero_status(tuv_command_rest_api_driver: TuvCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: tuv_command_rest_api_driver.is_auto_zero_status_complete(),
                           "AutZero did not completed",
                           WaitTimeConstants.SmallWait)
    response = tuv_command_rest_api_driver.get_auto_zero_status()
    assert response.uniqueName == "TuvAutoZero", "Tuv AutoZero did not operated"


@then('the scan column tag activity completed successfully')
def verify_scan_column_tag_completed(chc_command_rest_api_driver: ChcCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: chc_command_rest_api_driver.is_scan_column_tag_status_complete(),
                           "Scan Column Tag did not completed",
                           WaitTimeConstants.SmallWait)
    response = chc_command_rest_api_driver.get_scan_column_tag_status()
    assert response.uniqueName == "ChcScanColumnTag", "Chc Scan Column Tag did not operated"

# endregion Then
