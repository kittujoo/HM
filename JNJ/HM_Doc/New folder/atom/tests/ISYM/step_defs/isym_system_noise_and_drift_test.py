import os

from glom import assign, delete
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.behavior.system_noise_and_drift.system_noise_and_drift_request import (generate_default_system_tuv_noid_and_drift_request,
                                                                                                       DataRate, FilterBehavior)
from isym_test_api.rest_api.drivers.behavior.system_noise_and_drift_driver import SystemNoiseAndDriftDriver
from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.convertion_utilities import parse_string_to_obj
from utilities.datatables.headless_datatable import headlesstable
from utilities.glom_utilities import assign_many
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_noise_and_drift_test.feature')


@when('a system noise and drift test is started')
def start_system_noise_and_drift_test(context, system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver):
    payload = generate_default_system_tuv_noid_and_drift_request()
    context['api_response'] = system_noise_and_drift_rest_api_driver.start_test(payload)


@when('the system stop command is sent')
def stop_system_noise_and_drift_test(system_command_rest_api_driver: SystemCommandDriver):
    system_command_rest_api_driver.system_stop()


@when('a system noise and drift test is set with non default values')
def noise_and_drift_flowRateMlPerMin_property(context, system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver):
    payload = generate_default_system_tuv_noid_and_drift_request()
    payload.qsm1.flowRateTargetMlPerMin = 5.0
    payload.qsm1.solventAPct = 0.0
    payload.qsm1.solventBPct = 0.0
    payload.qsm1.solventCPct = 50.0
    payload.qsm1.solventDPct = 50.0
    payload.tuv1.wavelengthA = 300.0
    payload.tuv1.filterParameters.dataRateHz = DataRate.DataRate_10HZ
    payload.tuv1.filterParameters.filterTimeConstantSec = 1.0
    payload.tuv1.filterBehavior.filterBehavior = FilterBehavior.FilterBehavior_LEGACYHAMMINGFILTER
    context['api_response'] = system_noise_and_drift_rest_api_driver.start_test(payload)


@when(cfparse('a system noise and drift test is set with "{property_name}" property removed'))
def remove_flowRateTargetMlPerMin_property(context, property_name, system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver):
    payload = as_dict(generate_default_system_tuv_noid_and_drift_request())
    delete(payload, property_name)
    context['api_response'] = system_noise_and_drift_rest_api_driver.start_test(payload=payload)


@when(headlesstable('a system noise and drift test started with data:'))
def modify_solvent_property(table, context, system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver):
    payload = as_dict(generate_default_system_tuv_noid_and_drift_request())
    assign_many(payload, table.as_dict(convert=True))
    context['api_response'] = system_noise_and_drift_rest_api_driver.start_test(payload)


@when(cfparse('a system noise and drift test started with "{property_name}" = "{property_value}"'))
def noise_and_drift_wavelengthA_property(property_name, property_value, context, system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver):
    payload = as_dict(generate_default_system_tuv_noid_and_drift_request())
    property_value = parse_string_to_obj(property_value)
    assign(payload, property_name, property_value)
    context['api_response'] = system_noise_and_drift_rest_api_driver.start_test(payload)


@then('the system noise and drift test completes')
def assert_system_noise_and_drift_test_completes(system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: str(system_noise_and_drift_rest_api_driver.get_status().state),
                             "BehaviorState_ACTIVE", "SystemNoiseAndDrift test is not running/completed",
                             WaitTimeConstants.MidWait)
    assert_timeout.are_equal(lambda: str(system_noise_and_drift_rest_api_driver.get_status().state),
                             "BehaviorState_INACTIVE", "SystemNoiseAndDrift test is not running/completed",
                             WaitTimeConstants.MidWait)


@then('the system noise and drift test status will be passed')
def verify_system_noise_and_drift_test_results(system_noise_and_drift_rest_api_driver: SystemNoiseAndDriftDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: type(system_noise_and_drift_rest_api_driver.get_result().noise), float,
                             "SystemNoiseAndDriftResult test is not Completed", WaitTimeConstants.MidWait)
    assert_timeout.are_equal(lambda: type(system_noise_and_drift_rest_api_driver.get_result().drift), float,
                             "SystemNoiseAndDriftResult test is not Completed", WaitTimeConstants.MidWait)
