import json
import os
import threading

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from allure_commons.types import AttachmentType
from pytest_bdd.parser import Scenario

from fixtures_win_app_driver import WinAppDriverHandler
from isym_test_api.rest_api.api.base_response import ServerRestApiException
from isym_test_api.rest_api.api.system.event_log_entry_request import EventLogMultipleEntries
from isym_test_api.rest_api.api.system.event_log_response import EventLogMultipleResponse
from isym_test_api.rest_api.api.system.system_state_response import SystemStateEnum
from isym_test_api.rest_api.asserts.assert_system_state import AssertSystemState
from isym_test_api.rest_api.drivers.system.event_log_driver import EventLogDriver
from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.empower_utility import EmpowerConfiguration
from utilities.json_utility import as_dict
from utilities.logger import Logger
from utilities.logs.logs_collector_cds_env import LogsCollectorCDSEnv
from web_framework.empower.drivers.message_center_driver import MessageCenterDriver

logger = Logger(os.path.basename(__file__))


def get_scenario_full_name(request, scenario):
    params = {}
    if hasattr(request.node, "callspec"):
        params = request.node.callspec.params["_pytest_bdd_example"]

    params_str = ""
    if params:
        params_str = f" - [{', '.join(params.values())}]"

    return f"[{scenario.name} - [{params_str}]"


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    logger.info(f"======= Feature: [{feature.name}] =======")

    scenario_full_name = get_scenario_full_name(request, scenario)
    logger.info(f"======= Started scenario: {scenario_full_name} =======")

    store_event_log_id(request)
    system_reset(request)


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_before_step_call(request: FixtureRequest, feature, scenario, step, step_func, step_func_args):
    step_name = step.name
    for key, value in step_func_args.items():
        if key in step.params:
            step_name = step_name.replace(f"<{key}>", f"{key}({value})")
    logger.info(f"===== Started step: [{step_name}] =====")


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_step(request: FixtureRequest, feature, scenario, step, step_func, step_func_args):
    step_name = step.name
    for key, value in step_func_args.items():
        if key in step.params:
            step_name = step_name.replace(f"<{key}>", f"{key}({value})")
    logger.info(f"===== Finished step: [{step_name}] =====")


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_step_error(request, step, exception):
    logger.info(f"===== Failed step: [{step.name}] with error: [{str(exception).strip()}] =====")

    # TODO refactor this part cos in case of running kiosk test on CDS env - no screenshot will be attached
    # need to check also for system tests when both Kiosk and Empower are used within the same scenario. perhaps the winappdriver screenshot should be used
    thread_local = threading.current_thread()
    driver = getattr(thread_local, 'web_driver', None)

    if driver:
        allure.attach(driver.get_screenshot_as_png(), name=step.name + " (kiosk)", attachment_type=AttachmentType.PNG)

    driver = getattr(thread_local, 'win_app_driver', None)
    if driver:
        allure.attach(driver.get_screenshot_as_png(), name=step.name + " (empower)", attachment_type=AttachmentType.PNG)


def pytest_bdd_apply_tag(tag, function):
    """
    This pytest_bdd_apply_tag hook helps skip the test that is tagged as "ignore"
    We are adding the ignore tag for two reasons:
    Defects as you mention
    Feature not fully implemented

    """
    if tag == 'ignore':
        marker = pytest.mark.skip(reason="failing due to defects")
        marker(function)
        return True
    else:
        # Fall back to pytest-bdd's default behavior
        return None


@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_scenario(request, feature, scenario: Scenario):
    scenario_full_name = get_scenario_full_name(request, scenario)
    logger.info(f"======= Finished scenario: [{scenario_full_name}] =======")

    if 'copy_temp_logs' in scenario.tags:
        results_folder: str = request.getfixturevalue('results_folder')
        logs_collector = LogsCollectorCDSEnv(results_folder)
        logs_collector.collect_temp_logs()

    if 'collect_message_center_log' in scenario.tags:
        message_center_driver: MessageCenterDriver = request.getfixturevalue('message_center_driver')
        message_center_driver.login_to_project()
        message_center_driver.get_log()

    save_event_log(request, scenario)
    system_reset(request)


@allure.step
def system_reset(request):
    """
    This function verifies if system is on state different from IDLE
    If so, resets system, setting it to IDLE state, using API call
    """

    system_state_rest_api_driver: SystemStateDriver = request.getfixturevalue("system_state_rest_api_driver")
    actual_system_state = system_state_rest_api_driver.get_system_state().state

    if actual_system_state != SystemStateEnum.SystemStateEnum_IDLE:
        logger.info(f"System is not in idle state: '{actual_system_state}' -> Reset requested.")
        request.getfixturevalue("system_command_rest_api_driver").system_reset()
        assert_system_state: AssertSystemState = request.getfixturevalue("assert_system_state")
        assert_system_state.state_is_idle(WaitTimeConstants.MidWait)
        logger.info("System reset completed.")


@allure.step
def store_event_log_id(request):
    """
        This function stores the latest Event Log ID that was used
    """
    event_log_rest_api_driver: EventLogDriver = request.getfixturevalue("event_log_rest_api_driver")
    context: dict = request.getfixturevalue("context")
    try:
        response = event_log_rest_api_driver.get_all_event_log_entry(payload=EventLogMultipleEntries())
        context['log_id_before_test'] = response.data.events.events[0].id
    except ServerRestApiException:
        logger.info("No logs were found so setting the log_id as 0")
        context['log_id_before_test'] = 0


def write_event_to_file(log_file, scenario_name, events_to_log):
    """
        This function writes the events to the file
    """
    with open(log_file, "a") as event_log_file:
        event_log_file.write(f"======= Started {scenario_name} =======\n\n")
        lines_to_log = [json.dumps(as_dict(event), indent=4) for event in events_to_log]
        event_log_file.writelines(lines_to_log)
        event_log_file.writelines('\n')
        event_log_file.write(f"======= Finished {scenario_name} =======\n\n")


def save_event_log(request, scenario: Scenario):
    """
        This function saves the newly generated events to a file
    """
    event_log_rest_api_driver: EventLogDriver = request.getfixturevalue("event_log_rest_api_driver")
    target_dir: str = os.path.join(request.getfixturevalue('results_folder'), "event-log")
    os.makedirs(target_dir, exist_ok=True)
    context: dict = request.getfixturevalue("context")
    try:
        event_log = event_log_rest_api_driver.get_all_event_log_entry(payload=EventLogMultipleEntries()).data
    except ServerRestApiException:
        logger.info("No logs found")
        return
    initial_id = context['log_id_before_test']
    events_to_log = [event for event in event_log.events.events if event.id > initial_id]
    if events_to_log:
        log_file = os.path.join(target_dir, f"{scenario.feature.name.replace('/', '_').replace('|', '_')}.log")
        scenario_name = get_scenario_full_name(request, scenario)
        write_event_to_file(log_file, scenario_name, events_to_log)
