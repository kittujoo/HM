from pathlib import Path
from pytest_bdd import when, then, scenarios
from pytest_bdd.parsers import cfparse

from tests.constants.wait_time_constants import WaitTimeConstants
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver
from web_framework.empower.pages.run_samples.run_samples_main_page import SingleInjectionRunStatus

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_sample_set_single_injection_test.feature')


@when(cfparse('the sample name field "{sample_name}" is entered'))
def enter_sample_name(sample_name: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.validate_opened()
    run_samples_driver.run_samples_tabs.single_injection_tab.set_sample_name(sample_name)


@when(cfparse('the entry from the dropdown menu for function "{function}" is selected'))
def select_function_from_dropdown(function: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.select_function(function)


@when(cfparse('the entry from dropdown menu for method set "{method_set}" is selected'))
def select_method_set_from_dropdown(method_set: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.select_method(method_set)


@when(cfparse('the plate position "{plate}" is added'))
def select_plate_position(plate: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.set_plate(plate)


@when(cfparse('injection volume "{injection_volume}" is added'))
def select_injection_volume(injection_volume: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.set_injection_volume(injection_volume)


@when(cfparse('run time "{run_time}" is added'))
def add_run_time(run_time: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.single_injection_tab.set_run_time(run_time)


@when('injection is started')
def start_injection(run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_single_injection()


@then('the acquisition starts')
def validate_acquisition_start(run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_single_injection_run_status(SingleInjectionRunStatus.INJECTION_RUNNING, WaitTimeConstants.SmallWait)


@then(cfparse('the sample set acquisition completes with state "{status}"'))
def validate_sample_set_status(status: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_intermediate_run_status(status)
