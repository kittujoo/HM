import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.solvent_management.flow_request import generate_default_flow_request
from isym_test_api.rest_api.drivers.solvent_management.qsm_flow_driver import QSMFlowDriver
from isym_test_api.rest_api.drivers.system.command.system_command_driver import SystemCommandDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.datatables.headless_datatable import headlesstable, HeadlessDataTable
from utilities.glom_utilities import assign_many, assert_dicts_equal
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_emergency_stop_test.feature')


@when(headlesstable("flow started with given data:"))
def modify_property_value(context, table, qsm_flow_rest_api_driver: QSMFlowDriver):
    payload = as_dict(generate_default_flow_request())
    assign_many(payload, table.as_dict(convert=True))
    context['payload'] = payload
    context['api_response'] = qsm_flow_rest_api_driver.start_flow(payload=payload)


@when('Emergency Stop command is sent')
def send_emergency_stop(context, system_command_rest_api_driver: SystemCommandDriver):
    context['api_response'] = system_command_rest_api_driver.system_emergency_stop()


@then(headlesstable("flow status result has next data:"))
def check_flow_response(table: HeadlessDataTable, qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.wait_no_exception(lambda: (assert_dicts_equal(as_dict(qsm_flow_rest_api_driver.get_flow_status()), table.as_dict(convert=True))),
                                     message="Invalid data for flow status result",
                                     polling_period_in_seconds=WaitTimeConstants.LittleWait)


@then(cfparse('the flowRateCurrentMlPerMin changes to "{expected_value:f}"'))
def check_current_flow_response(expected_value: float, qsm_flow_rest_api_driver: QSMFlowDriver, assert_timeout: AssertTimeout):
    assert_timeout.are_equal(lambda: qsm_flow_rest_api_driver.get_flow_status().flowRateCurrentMlPerMin, expected_value,
                             "The Current Flow value did not increase to the expected value")
