import math
import os

from glom import assign
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.behavior_status_response import BehaviorStatus, BehaviorState
from isym_test_api.rest_api.api.solvent_management.delta_pressure_response import QsmDeltaPressure
from isym_test_api.rest_api.api.solvent_management.full_flow_control_request import generate_default_full_flow_control_request
from isym_test_api.rest_api.api.solvent_management.full_flow_control_response import SolvFullFlowControlR
from isym_test_api.rest_api.api.solvent_management.prime_pump_request import generate_default_prime_pump_request
from isym_test_api.rest_api.drivers.solvent_management.qsm_command_driver import QsmCommandDriver
from isym_test_api.rest_api.drivers.solvent_management.qsm_flow_driver import QSMFlowDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_qsm_commands_test.feature')

resource_list = ["Res-Activity-Qsm-QsmStopFlow",
                 "Res-Activity-Qsm-SetVentValveToWaste",
                 "Res-Activity-Qsm-QsmStopFlow",
                 "Res-Activity-Qsm-QsmChangeFlowRateAndComposition",
                 "Res-Activity-Qsm-WaitForPrimeToComplete",
                 "Res-Activity-Qsm-QsmStopFlow",
                 "Res-Activity-Qsm-SetVentValveToSystem",
                 "Res-Activity-QsmChangeFlowRateAndComposition-QsmChangeFlowRateAndComposition"]

# region When


@when('the full flow control activity is requested')
def request_full_flow_control(qsm_flow_rest_api_driver: QSMFlowDriver):
    qsm_flow_rest_api_driver.set_full_flow_control(payload=generate_default_full_flow_control_request())


@when('the pump priming activity is requested')
def request_prime_pump_test(qsm_command_rest_api_driver: QsmCommandDriver):
    qsm_command_rest_api_driver.start_prime_pump(payload=generate_default_prime_pump_request())


@when(cfparse('the single prime line start with default flow rate "{value:f}"'))
def request_solvent_prime_line(context, value: float, qsm_command_rest_api_driver: QsmCommandDriver):
    payload = as_dict(generate_default_prime_pump_request())
    logger.info(f"\npayload: {payload['steps']}\n")
    assign(payload, 'steps.0.flowRateMlPerMin', value)
    return qsm_command_rest_api_driver.set_single_prime_line(payload=payload)

# endregion When
# region Then


@then('the pump priming activity is started successfully')
def verify_pump_prime_started(qsm_command_rest_api_driver: QsmCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: qsm_command_rest_api_driver.is_prime_pump_test_started(),
                           "Pump Priming test did not started",
                           WaitTimeConstants.SmallWait)


@then('the pump priming activity is completed successfully')
def verify_pump_prime_completed(qsm_command_rest_api_driver: QsmCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: qsm_command_rest_api_driver.is_prime_pump_test_complete(),
                           "Pump Priming test did not completed",
                           WaitTimeConstants.MidWait)


@then('the full flow control activity started successfully')
def verify_full_flow_control_started(qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: qsm_flow_rest_api_driver.is_full_flow_control_started(),
                           "Full Flow Control did not started",
                           WaitTimeConstants.SmallWait)


@then('the full flow control activity completed successfully')
def verify_full_flow_control_completed(qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: qsm_flow_rest_api_driver.is_full_flow_control_complete(),
                           "Full Flow Control did not completed",
                           WaitTimeConstants.MidWait)


@then('the full flow control status match requested configuration')
def verify_full_flow_control_status(qsm_flow_rest_api_driver: QSMFlowDriver):
    response: SolvFullFlowControlR = qsm_flow_rest_api_driver.get_full_flow_control().data
    payload = generate_default_full_flow_control_request()  # Native payload requested for full control configuration
    assert response.flowOn, "Full Flow Control - flow was not turned on"
    assert round(response.flowRateCurrentMlPerMin, 2) == payload.flowRateTargetMlPerMin, "Full Flow Control - requested flow rate is not achieved"
    assert round(response.solventAPct, 2) == payload.solventAPct, "Full Flow Control - Solvent A requested flow rate did not reached"
    assert round(response.solventBPct, 2) == payload.solventBPct, "Full Flow Control - Solvent B requested flow rate did not reached"
    assert round(response.solventCPct, 2) == payload.solventCPct, "Full Flow Control - Solvent C requested flow rate did not reached"
    assert round(response.solventDPct, 2) == payload.solventDPct, "Full Flow Control - Solvent D requested flow rate did not reached"
    assert round(response.flowRampRateMlPerMinPerSec, 2) == payload.flowRampRateMlPerMinPerSec, "Full Flow Control - Flow Ramp rate requested wa not received"


@then('delta pressure is verified with pressure limits')
def verify_delta_pressure(qsm_command_rest_api_driver: QsmCommandDriver):
    response: QsmDeltaPressure = qsm_command_rest_api_driver.get_delta_pressure().data
    assert math.isclose(response.deltaMaxPressurePsi - response.deltaMinPressurePsi, response.deltaPressurePsi, abs_tol=0.00001), \
                        f"Delta Pressure was differing in limits: {response}"


@then('prime line status is Active')
def verify_single_prime_line_active(context, qsm_command_rest_api_driver: QsmCommandDriver):
    response: BehaviorStatus = qsm_command_rest_api_driver.get_single_prime_line_status().data
    assert response.state == BehaviorState.BehaviorState_ACTIVE, f"Unexpected Single Prime Line Active response: {response}"


@then('prime line status is Completed')
def verify_single_prime_line_complete(context, qsm_command_rest_api_driver: QsmCommandDriver, assert_timeout: AssertTimeout):
    assert_timeout.is_true(lambda: qsm_command_rest_api_driver.is_single_prime_line_complete(), "Unexpected Single Prime Line Active response",
                             WaitTimeConstants.MidWait)
    response: BehaviorStatus = qsm_command_rest_api_driver.get_single_prime_line_status().data
    for res in range(len(response.operationStatus)):
        assert response.operationStatus[res].resourceKey in resource_list[res] and response.operationStatus[res].state == BehaviorState.BehaviorState_COMPLETE,\
                f"Unexpected Prime Line response\n- res name: {response.operationStatus[res].resourceKey}\n- res state: {response.operationStatus[res].state}"


@then('prime line status is Inactive')
def verify_single_prime_line_inactive(context, qsm_command_rest_api_driver: QsmCommandDriver):
    response: BehaviorStatus = qsm_command_rest_api_driver.get_single_prime_line_status().data
    assert response.state == BehaviorState.BehaviorState_INACTIVE, f"Unexpected Single Prime Line Active response: {response}"

# endregion Then
