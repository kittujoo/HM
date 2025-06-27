import os
import time

from pytest_bdd import given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.column_manager.temperature_request import ColumnTemperatureW
from isym_test_api.rest_api.api.sample_management.temperature_request import FtnSampleTemperatureW
from isym_test_api.rest_api.drivers.column_manager.column_manager_temperature_driver import ColumnManagerTemperatureDriver
from isym_test_api.rest_api.api.system.system_configuration_response import SystemConfigurationResponse
from isym_test_api.rest_api.drivers.sample_management.ftn_temperature_driver import FTNTemperatureDriver
from tests.ISYM.conftest import *
from utilities.assert_timeout import AssertTimeout
from utilities.datatables.converters import CONVERTERS
from utilities.empower_utility import EmpowerConfiguration
from utilities.logger import Logger
from utilities.windows_shell_utilities import is_application_installed
from web_framework.empower.drivers.console_driver import ConsoleDriver
from web_framework.empower.drivers.instrument_method_editor_driver import InstrumentMethodEditorDriver
from web_framework.empower.drivers.project_restore_driver import ProjectRestoreDriver
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver
from web_framework.empower.pages.run_samples.run_samples_main_page import SampleSetRunStatus, SampleRunMode
from web_framework.empower.pages.run_samples.samples_table import MethodFunctions

logger = Logger(os.path.basename(__file__))


# region Given

@given('the driver is already installed')
def check_driver_is_installed(empower_configuration: EmpowerConfiguration):
    ics_instrument_type = empower_configuration.ics_instrument_type
    assert is_application_installed(ics_instrument_type) is True, f"Was expecting ICS driver for '{ics_instrument_type}' to be installed"


@given(cfparse('the "{project_name}" project is available in Empower'))
def restore_project(project_name: str, project_restore_driver: ProjectRestoreDriver, context):
    context["empower_project"] = project_name
    logger.info(f"The test is using Empower project: '{project_name}'.")
    project_restore_driver.restore(project_name)


@given(cfparse('the "{project_name}" instrument version specific project is available in Empower'))
def restore_project(project_name: str, project_restore_driver: ProjectRestoreDriver, system_configuration_details: SystemConfigurationResponse, context):
    project_name += '_tuv_bio' if system_configuration_details.isBio else '_tuv'
    context["empower_project"] = project_name
    logger.info(f"The test is using Empower project: '{project_name}'.")
    project_restore_driver.restore(project_name)


@given('run samples application is open for the current project and system')
@then('run samples application is open for the current project and system')
def start_and_login_to_run_samples(run_samples_driver: RunSamplesDriver, empower_configuration: EmpowerConfiguration, context):
    project_name = context["empower_project"]
    run_samples_driver.login_to_project(project_name,
                                        empower_configuration.username, empower_configuration.password,
                                        empower_configuration.empower_system_name)


@then(cfparse('Control Panel shows "{state}" state'))
@given(cfparse('Control Panel shows "{state}" state'))
def validate_system_state_in_control_panel(state: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.control_panel.validate_system_state(state)


@when("Console is launched from Control Panel")
@given("Console is launched from Control Panel")
def open_console_from_control_panel(run_samples_driver: RunSamplesDriver, console_driver: ConsoleDriver):
    run_samples_driver.control_panel.open_console()
    console_driver.validate_console_opened()


@given(cfparse('Console page shows "{state}" state'))
def validate_system_state_in_console(state: str, console_driver: ConsoleDriver):
    console_driver.validate_system_state(state)


@given('method editor application is open for the current project and system')
@then('method editor application opens with the restored project')
def start_and_login_to_method_creation(instrument_method_editor_driver: InstrumentMethodEditorDriver,
                                       empower_configuration: EmpowerConfiguration,
                                       context):
    project_name = context["empower_project"]
    instrument_method_editor_driver.login_to_project(project_name,
                                                     empower_configuration.username,
                                                     empower_configuration.password,
                                                     empower_configuration.empower_system_name)


@given(cfparse('Lamp is turned "{lamp_state:bool}"', CONVERTERS))
@given(cfparse('Lamp is "{lamp_state:bool}"', CONVERTERS))
def given_lamp_state(lamp_state: bool, console_driver: ConsoleDriver):
    console_driver.console_base_page.open_commands_tab()
    console_driver.set_lamp_state(lamp_state)
    console_driver.validate_commands_page_lamp_state(lamp_state)


@given(cfparse('sample temperature initial state is set as "{current_sample_temp_state:bool}"', CONVERTERS))
def ftn_thermal_control_initial_state(current_sample_temp_state: bool, ftn_temperature_rest_api_driver: FTNTemperatureDriver, assert_timeout: AssertTimeout):
    initial_state = 'ThermalControlState_OFF' if not current_sample_temp_state else 'ThermalControlState_ON'
    ftn_temperature_rest_api_driver.set_temperature_control(initial_state)
    assert_timeout.are_equal(lambda: ftn_temperature_rest_api_driver.get_thermal_control_state(), initial_state,
                             f"Thermal control state is not as expected. "
                             f"Expected:[{initial_state}] Actual:[{ftn_temperature_rest_api_driver.get_thermal_control_state()}]")


@given(cfparse('column temperature initial state is set as "{current_column_temp_state:bool}"', CONVERTERS))
def column_control_initial_state(current_column_temp_state: bool, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver,
                                 assert_timeout: AssertTimeout):
    initial_state = 'ThermalControlState_OFF' if not current_column_temp_state else 'ThermalControlState_ON'
    column_manager_temperature_rest_api_driver.set_temperature_control(initial_state)
    assert_timeout.are_equal(lambda: column_manager_temperature_rest_api_driver.get_thermal_control_state(), initial_state,
                             f"Thermal control state is not as expected. "
                             f"Expected:[{initial_state}] Actual:[{column_manager_temperature_rest_api_driver.get_thermal_control_state()}]")


@given(cfparse('Flow rate is turned "{flow_rate:bool}"', CONVERTERS))
def given_system_flow(flow_rate: bool, console_driver: ConsoleDriver):
    console_driver.set_flow(flow_rate)
    console_driver.validate_commands_page_flow_state(flow_rate)


# endregion Given


# region When

@when(cfparse('the sample set "{sample_set_name}" is loaded'))
def load_sample_set(sample_set_name: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.load_created_sample_set(sample_set_name)


@when(cfparse('function "{function_name}" is selected'))
def select_function_from_table(function_name: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.samples_tab.select_method_function(1, MethodFunctions(function_name))


@when(cfparse('method set "{method_set}" is selected'))
def select_predefined_method_set_for_created_line(method_set: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.samples_tab.select_method_set(1, method_set)


@when('the acquisition starts')
def start_new_sample_set(run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_sample_set(SampleRunMode.RunOnly)


@when("system reset is selected from Console")
def open_console_from_control_panel(console_driver: ConsoleDriver):
    console_driver.reset_system()


@when('User selects Home from Console')
def select_setup(console_driver: ConsoleDriver):
    console_driver.console_base_page.open_home_tab()
    console_driver.validate_home_tab_opened()


@when("select Commands from Console")
def open_commands_from_console(console_driver: ConsoleDriver):
    console_driver.console_base_page.open_commands_tab()
    console_driver.validate_commands_tab_opened()


@given(cfparse('Column Temperature is "{temperature_value:f}"'))
def set_target_column_temperature(temperature_value: float, column_manager_temperature_rest_api_driver: ColumnManagerTemperatureDriver):
    set_temperature_request = ColumnTemperatureW(targetTemperatureDegC=temperature_value)
    column_manager_temperature_rest_api_driver.set_temperature(set_temperature_request)


@given(cfparse('Sample Temperature is "{temperature_value:f}"'))
def set_target_sample_temperature(temperature_value: float, ftn_temperature_rest_api_driver: FTNTemperatureDriver):
    set_temperature_request = FtnSampleTemperatureW(targetTemperatureDegC=temperature_value)
    ftn_temperature_rest_api_driver.set_temperature(set_temperature_request)


@when('User selects Setup from Console')
def select_setup(console_driver: ConsoleDriver):
    console_driver.console_base_page.open_setup_tab()
    console_driver.validate_setup_tab_opened()


# endregion When


# region Then

@then(cfparse('Console Home page shows flow "{flow_state:bool}"', CONVERTERS))
def validate_flow_in_console_home_page(flow_state: bool, console_driver: ConsoleDriver):
    console_driver.console_base_page.open_home_tab()
    console_driver.validate_control_flow_rate_equal_to("0.000 mL/min") if not flow_state else console_driver.validate_control_flow_not_equal_to(
        "0.000 mL/min")


@then('the sample set acquisition completes successfully')
def validate_sample_set_status(run_samples_driver: RunSamplesDriver):
    #TODO refactor this mechanism as when multiple injections need to run, the Preparing state occurs before each one
    running_timeout_buffer_in_seconds = 240
    run_samples_driver.validate_run_status(SampleSetRunStatus.COMPLETE.value, running_timeout_buffer_in_seconds)


@then(cfparse('Console page shows "{state}" state'))
def validate_system_state_in_console(state: str, console_driver: ConsoleDriver):
    console_driver.validate_system_state(state)


@then(cfparse('Console Home page shows lamp "{state:bool}"', CONVERTERS))
def validate_lamp_state(state: bool, console_driver: ConsoleDriver):
    time.sleep(5)  # physical wait for waiting home screen to load all elements in correct sequence
    console_driver.validate_lamp_state(state)


@then(cfparse('Control Panel shows Lamp "{lamp_state:bool}"', CONVERTERS))
def validate_lamp_state(lamp_state: bool, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_control_panel_lamp_state(lamp_state)


@then(cfparse('Console shows Flow rate set to "{flow_rate}"'))
def validate__lamp_state(flow_rate: str, console_driver: ConsoleDriver):
    console_driver.validate_control_flow_rate_equal_to(flow_rate)


@then(cfparse('Control Panel shows Column Temperature is "{temperature_value:f}"'))
def validate_column_temperature(temperature_value: float, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_column_temperature(temperature_value)


@then(cfparse('Control Panel shows Sample Temperature is "{temperature_value:f}"'))
def validate_sample_temperature(temperature_value: float, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_sample_temperature(temperature_value)


@then(cfparse('Control Panel shows Flow rate set to "{flow_rate}"'))
def validate_sample_temperature(flow_rate: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_control_panel_flow_rate_equal_to(flow_rate)


@then(cfparse('Console shows Sample Temperature state set to "{state:bool}"', CONVERTERS))
def validate_sample_temperature(state: bool, console_driver: ConsoleDriver):
    console_driver.validate_sample_temperature_state(state)


@then(cfparse('Console shows Column Temperature state set to "{state:bool}"', CONVERTERS))
def validate_sample_temperature(state: bool, console_driver: ConsoleDriver):
    console_driver.validate_column_temperature_state(state)
# endregion Then
