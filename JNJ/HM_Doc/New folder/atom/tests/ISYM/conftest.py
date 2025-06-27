import os

from glom import assign
from pytest_bdd import given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.system_meta_method_request import generate_default_system_meta_method_request
from isym_test_api.rest_api.api.solvent_management.flow_request import generate_default_flow_request
from isym_test_api.rest_api.api.system.system_reset_request import generate_stopping_activity_with_initialization_system_reset_request
from isym_test_api.rest_api.api.system.workflow_request import generate_default_system_workflow_request
from isym_test_api.rest_api.asserts.assert_system_state import AssertSystemState
from isym_test_api.rest_api.drivers.solvent_management.qsm_flow_driver import QSMFlowDriver
from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from isym_test_api.rest_api.drivers.system.exclusive_mode_driver import ExclusiveModeDriver
from isym_test_api.rest_api.drivers.meta_setting.meta_setting_driver import MetaSettingDriver
from isym_test_api.rest_api.api.meta_setting.meta_setting_request import (generate_prerun_checks_request, generate_run_checks_request)
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


# region Given

@given('the system state is Idle')
def identify_instrument_idle(assert_system_state: AssertSystemState):
    assert_system_state.state_is_idle(WaitTimeConstants.MidWait)


@given('the Exclusive Idle system state is set')
def request_exclusive_idle_and_validate(exclusive_mode_rest_api_driver: ExclusiveModeDriver, assert_system_state: AssertSystemState):
    exclusive_mode_rest_api_driver.set_exclusive_mode(True, "system")
    assert_system_state.state_is_exclusive_idle(WaitTimeConstants.LittleWait)


@given('pre-run checks for sample set validation acquisition are disabled')
def pre_run_checks_disabled_for_acquisition(meta_setting_rest_api_driver: MetaSettingDriver):
    meta_setting_rest_api_driver.set_meta_checks(generate_prerun_checks_request())


@given('run checks for sample set validation acquisition are disabled')
def run_checks_disabled_for_acquisition(meta_setting_rest_api_driver: MetaSettingDriver):
    meta_setting_rest_api_driver.set_meta_checks(generate_run_checks_request())


# endregion Given


# region When

@when('the system software reset is requested')
def request_system_reset(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_reset()


@when('stopping activities and initialization is requested with system reset')
def request_system_hard_reset(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_reset_request(generate_stopping_activity_with_initialization_system_reset_request())


@when('the Exclusive Idle system state is requested')
def request_exclusive_idle(exclusive_mode_rest_api_driver: ExclusiveModeDriver):
    exclusive_mode_rest_api_driver.set_exclusive_mode(True, "system")


@when('the Exclusive Idle system state is released')
def release_exclusive_idle(exclusive_mode_rest_api_driver: ExclusiveModeDriver):
    exclusive_mode_rest_api_driver.set_exclusive_mode(False, "system")


@when('the system stop command is requested')
def request_system_stop(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_stop()


@when('the system reset command is requested')
def request_system_stop(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_reset()


@when('the correct method data is sent')
def request_method_conditioning(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    context['device_type'] = data_system_acquisition_rest_api_driver.set_method_tuv(payload=generate_default_system_meta_method_request())


@when(cfparse('the flow control is turned "{status}"'))
def request_flow_control_turned_onoff(context, status: str, qsm_flow_rest_api_driver: QSMFlowDriver):
    value = True if status.lower() == "on" else False
    context['api_response'] = qsm_flow_rest_api_driver.set_flow_control(value)


@when(cfparse('flow started with "{value:f}" flow target rate'))
def request_flow_rate(context, value: float, qsm_flow_rest_api_driver: QSMFlowDriver):
    payload = as_dict(generate_default_flow_request())
    assign(payload, "flowRateTargetMlPerMin", value)
    context['payload'] = payload
    context['api_response'] = qsm_flow_rest_api_driver.start_flow(payload=payload)


@when('the workflow is started')
def request_workflow_start(context, system_command_rest_api_driver: SystemCommandDriver):
    context['api_response'] = system_command_rest_api_driver.system_workflow_start(payload=generate_default_system_workflow_request())


@when('the workflow is deleted')
def request_workflow_delete(context, system_command_rest_api_driver: SystemCommandDriver):
    context['api_response'] = system_command_rest_api_driver.system_workflow_delete()


# endregion When

# region Then

@then('the system state changes to Busy')
def assert_busy_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_busy(WaitTimeConstants.MidWait)


@given('the system state changes to Idle')
@then('the system state changes to Idle')
def assert_idle_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_idle(WaitTimeConstants.MidWait)


@then('the system state changes to Exclusive Idle')
def assert_exclusive_idle_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_exclusive_idle(WaitTimeConstants.LongWait)


@then('the system state changes to Setting Method')
def assert_setting_method_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_setting_method(WaitTimeConstants.MidWait)


@then('the system state changes to At Method Conditions')
def assert_at_method_condition_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_at_method_conditions(WaitTimeConstants.MidWait)


@then('the system state changes to Preparing')
def assert_preparing_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_preparing(WaitTimeConstants.LittleWait)


@then('the system state changes to Halted')
def assert_halted_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_halted(WaitTimeConstants.LittleWait)


@then('the system state changes to Running')
def assert_at_running_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_running(WaitTimeConstants.MidWait)


@then('the system state changes to Exclusive Fail')
def assert_exclusivefail_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_exclusivefail(WaitTimeConstants.LittleWait)


@then('the system state changes to Error')
def assert_at_error_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_error(WaitTimeConstants.MidWait)


@then('the system state changes to Resetting')
def assert_resetting_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_resetting(WaitTimeConstants.LittleWait)


@then('the system state changes to Workflow')
def assert_workflow_active_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_workflow(WaitTimeConstants.LittleWait)


@then('the system state is Workflow Recovering')
def assert_workflow_closure_state(assert_system_state: AssertSystemState):
    assert_system_state.state_is_workflow_recovering(WaitTimeConstants.MidWait)


@then('the system state changes to Initializing')
def assert_initializing_state(assert_system_state: AssertSystemState, system_command_rest_api_driver: SystemCommandDriver):
    assert_system_state.state_is_initializing(WaitTimeConstants.LittleWait)
    assert system_command_rest_api_driver.get_system_initialize_status().uniqueName == "Initializing", "System behavior state is not Initializing"


@then('the post run report is available')
def verify_post_run_report(data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    response = data_system_acquisition_rest_api_driver.get_post_run_report()
    assert response, f"Post run report was empty"


@then(cfparse('the response status code is "{expected_status_code:d}"'))
def verify_status_code(context, expected_status_code: int):
    actual_status = context['api_response'].status_code
    assert actual_status == expected_status_code, f"Unexpected response status code. Actual: [{actual_status}], Expected: [{expected_status_code}]"


@then(cfparse('the flow control status is turned "{status}"'))
def verify_flow_control_status(status: str, qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    value = True if status.lower() == "on" else False
    assert_timeout.are_equal(lambda: qsm_flow_rest_api_driver.get_flow_control_status(), value, f"Flow was not turned {status}", \
                             WaitTimeConstants.MidWait, 2)


@then(cfparse('flow status result reach to expected "{value:f}" flow target rate'))
def verify_flow_rate(value: float, qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: round(qsm_flow_rest_api_driver.get_flow_status().flowRateCurrentMlPerMin, 3), value, \
                             "The Current Flow value did not increase to the expected value", WaitTimeConstants.MidWait)

# endregion Then
