from datetime import datetime
from pathlib import Path
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import cfparse
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_sample_set_special_functions.feature')


@given("new line is added in sample set")
def create_new_line_in_sample_table(run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.samples_tab.add_new_sample_table_line()


@when(cfparse('run time "{run_time}" is added'))
def add_run_time(run_time: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.set_sample_runtime(1, run_time)


@when('the sample set is saved')
def save_sample_set(run_samples_driver: RunSamplesDriver):
    start_time_string = format(datetime.now(), "%Y-%m-%d_%H_%M_%S")
    file_name = f"sample_set_{start_time_string}"
    run_samples_driver.save_sample_set_method(file_name, 'method comment')


@when(cfparse('sample prep "{value:d}" is added'))
def set_sample_prep_value(value: int, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_tabs.samples_tab.set_sample_prep(1, value)


@then(cfparse('the sample set acquisition completes with state "{status}"'))
@then(cfparse('the sample set status is set to "{status}"'))
def validate_sample_set_running_status(status: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_intermediate_run_status(status)
