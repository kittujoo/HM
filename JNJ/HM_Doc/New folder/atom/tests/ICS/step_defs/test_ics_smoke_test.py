import os
import uuid
from os.path import exists, getsize

from pathlib import Path
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import cfparse

from tests.constants.wait_time_constants import WaitTimeConstants
from utilities.assert_timeout import AssertTimeout
from utilities.empower_utility import EmpowerConfiguration
from utilities.logger import Logger
from utilities.windows_shell_utilities import is_application_installed, uninstall_application
from web_framework.empower.drivers.configuration_manager_driver import ConfigurationManagerDriver
from web_framework.empower.drivers.instrument_method_editor_driver import InstrumentMethodEditorDriver
from web_framework.empower.drivers.project_driver import ProjectDriver, TableColumnNames
from web_framework.empower.drivers.report_publisher_driver import ReportPublisherDriver, FileType
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver
from web_framework.empower.pages.run_samples.run_samples_main_page import SingleInjectionPreparationStatus, SingleInjectionRunStatus, SampleRunMode


if __name__ == Path(__file__).stem:
    scenarios('../features/ics_smoke_test.feature')

logger = Logger(__name__)

node_name = 'Desktop-b84fll0'
instrument_method_name = 'atom_beta_default_method'
sample_set_name = 'atom_beta_sample_set_3'  # part of the Empower VM template


@when('the uninstaller is executed')
def execute_uninstaller(empower_configuration: EmpowerConfiguration):
    ics_instrument_type = empower_configuration.ics_instrument_type
    assert uninstall_application(ics_instrument_type), f"Failed to uninstall ICS driver '{ics_instrument_type}'"


@then('the software is removed')
def validate_software_was_removed(empower_configuration: EmpowerConfiguration, assert_timeout: AssertTimeout):
    ics_instrument_type = empower_configuration.ics_instrument_type
    assert_timeout.is_false(lambda: is_application_installed(ics_instrument_type), f"Failed to uninstall '{ics_instrument_type}'")


@given('configuration manager application is open')
def start_and_login_to_configuration_manager(configuration_manager_driver: ConfigurationManagerDriver, empower_configuration: EmpowerConfiguration):
    configuration_manager_driver.login_to_project(empower_configuration.username, empower_configuration.password)


@when('a system is created')
def create_system(configuration_manager_driver: ConfigurationManagerDriver, empower_configuration: EmpowerConfiguration):
    system_name_to_use = empower_configuration.ics_instrument_type + "#" + empower_configuration.hardware_system_name
    configuration_manager_driver.create_new_system(empower_configuration.empower_system_name, system_name_to_use)


@then('the system is successfully brought online')
def validate_system_online(configuration_manager_driver: ConfigurationManagerDriver):
    pass


@when('a method editor window is opened')
def method_editor_is_opened(instrument_method_editor_driver: InstrumentMethodEditorDriver, empower_configuration: EmpowerConfiguration, context):
    instrument_method_editor_driver.method_editor_page.validate_opened()


@when('a method is saved with the default values')
def save_instrument_method(instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.save_method(instrument_method_name, 'method comment')


@when('a new sample set method is created')
def create_new_sample_set_method(run_samples_driver: RunSamplesDriver):
    run_samples_driver.create_new_sample_set()
    run_samples_driver.select_new_sample_method_creation()


@when('sample set method and dissolution types are selected')
def select_sample_set_method_and_dissolution_types(run_samples_driver: RunSamplesDriver):
    sample_set_method_type = 'LC or PDA/MS'
    dissolution_type = 'No Dissolution'
    run_samples_driver.select_sample_method_type(sample_set_method_type, dissolution_type)


@when('the standard injections location is selected')
def select_location_of_standard_injections(run_samples_driver: RunSamplesDriver):
    standard_injections_location = 'No standards'
    run_samples_driver.select_location_of_standard_injections(standard_injections_location)


@when('the sample description is defined')
def sample_description_definition(run_samples_driver: RunSamplesDriver):
    samples_number = 1
    injections_number = 1
    injection_volume = 1
    run_time = 1
    run_samples_driver.describe_samples(samples_number, injections_number, injection_volume, run_time)


@when('the instrument method is selected')
def select_instrument_method(run_samples_driver: RunSamplesDriver):
    run_samples_driver.select_instrument_method()


@when('the standards identification is defined')
def set_standards_identification(run_samples_driver: RunSamplesDriver):
    run_samples_driver.identify_standards()


@when('the runtime option is selected')
def select_runtime_options(run_samples_driver: RunSamplesDriver):
    run_mode = 'Run only'
    run_samples_driver.select_runtime_option(run_mode)


@when('the set method summary is confirmed')
def confirm_set_method_summary(run_samples_driver: RunSamplesDriver):
    run_samples_driver.confirm_sample_set_method_summary()


@when('the component editor is confirmed')
def confirm_component_editor(run_samples_driver: RunSamplesDriver):
    run_samples_driver.confirm_component_editor()


@when('the sample set is executed')
def start_new_sample_set(run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_sample_set(SampleRunMode.RunOnly, sample_set_name=sample_set_name)


@when("single injection tab is opened")
def open_single_tab_injection_tab(run_samples_driver: RunSamplesDriver):
    _ = run_samples_driver.run_samples_tabs.single_injection_tab


@when('a single injection configuration is set')
def create_single_injection(run_samples_driver: RunSamplesDriver):
    function_type = 'Inject Samples'
    plate = '1:A,1'
    injection_volume = 1
    run_time = 1
    run_samples_driver.create_new_single_injection(sample_set_name, function_type, plate, injection_volume, run_time)


@when('an instrument method is created')
def create_method(run_samples_driver: RunSamplesDriver):
    run_samples_driver.create_instrument_method()


@when('method editor data channels are turned on')
def turn_on_data_channels(instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.setup_instrument_method()
    instrument_method_editor_driver.method_editor_page.save_page_source()


@when('an instrument method is saved and exported')
def save_export_instrument_method(context, results_folder, instrument_method_editor_driver: InstrumentMethodEditorDriver):
    target_path = os.path.join(results_folder, f"data_{uuid.uuid4()}.json")
    context["instrument_method_path"] = target_path
    instrument_method_editor_driver.save_method(instrument_method_name, 'method comment')
    instrument_method_editor_driver.export_to_json(target_path)


@when('the preparation is completed')
def click_prepare(run_samples_driver: RunSamplesDriver):
    preparation_timeout_in_seconds = 120
    run_samples_driver.prepare_single_injection()
    run_samples_driver.validate_single_injection_preparation_status(SingleInjectionPreparationStatus.PRESS_INJECT_BUTTON.value, preparation_timeout_in_seconds)


@when('the single injection is completed')
def single_injection_completed(run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_single_injection()
    run_samples_driver.validate_single_injection_run_status(SingleInjectionRunStatus.COMPLETE, WaitTimeConstants.SmallWait)


@when('the report publisher system is opened')
def open_report_publisher(project_driver: ProjectDriver, empower_configuration: EmpowerConfiguration, context):
    project_name = context["empower_project"]
    project_driver.login_to_project(empower_configuration.username, empower_configuration.password, project_name)
    project_driver.open_preview_publisher(1, TableColumnNames.SAMPLE_NAME)


@when('the report is selected')
def select_report(report_publisher_driver: ReportPublisherDriver, context):
    report_publisher_driver.open_report_method()


@when('the Instrument Method report is saved')
def print_report_pdf(report_publisher_driver: ReportPublisherDriver):
    report_publisher_driver.save_report('Instrument Methods', 'Instrument Method Group')


@when(cfparse("the Instrument Method report is exported as {file_type} file"))
def save_report_pdf(file_type: str, context, results_folder: str, report_publisher_driver: ReportPublisherDriver, assert_timeout: AssertTimeout):
    file_type = FileType(file_type)
    report_file_path = os.path.join(results_folder, f"Instrument_Method_{uuid.uuid4()}.pdf")
    context["instrument_method_report_path"] = report_file_path
    report_publisher_driver.save_report_as(report_file_path, file_type)
    assert_timeout.is_true(lambda: exists(report_file_path) and getsize(report_file_path) > 0,
                           message=f"Instrument Method report file [{report_file_path}] does not exist or is empty",
                           timeout_in_seconds=5, polling_period_in_seconds=1)


@then('the Instrument Method report is validated')
def validate_report(context):
    report_file_name = context["instrument_method_report_path"]
    report_key = "Ambient Temperature Data Channel Enabled"
    json_file_name = context["instrument_method_path"]
    json_key = "ambientTemperatureChannelEnable"
    ReportPublisherDriver.validate_report(json_file_name, json_key, report_file_name, report_key)
