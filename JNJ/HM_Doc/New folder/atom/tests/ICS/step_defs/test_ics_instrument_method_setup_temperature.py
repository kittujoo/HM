from pathlib import Path
from pytest_bdd import when, then, scenarios, given
from pytest_bdd.parsers import cfparse

from web_framework.empower.drivers.console_driver import ConsoleDriver
from web_framework.empower.drivers.instrument_method_editor_driver import InstrumentMethodEditorDriver
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_instrument_method_setup_temperature.feature')


@given('the instrument method editor window is opened')
def select_instrument_method(run_samples_driver: RunSamplesDriver):
    run_samples_driver.instrument_method.click_edit_button()


@given(cfparse('instrument method has column temperature parameter "{column_value}"'))
def set_column_temperature(column_value: str, instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.set_column_temperature(column_value)


@given(cfparse('instrument method has sample temperature parameter "{sample_value}"'))
def set_sample_temperature(sample_value: str, instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.set_sample_temperature(sample_value)


@given(cfparse('instrument method is saved with name "{instrument_method}"'))
def save(instrument_method: str, instrument_method_editor_driver: InstrumentMethodEditorDriver):
    instrument_method_editor_driver.save_method(instrument_method, 'method comment')


@given(cfparse('entry from drop down instrument method is selected "{instrument_method}"'))
def select_instrument_method(instrument_method: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.select_instrument_method_from_dialog(instrument_method)


@when('Setup run section is selected')
def run_setup(run_samples_driver: RunSamplesDriver):
    run_samples_driver.instrument_method.click_setup_button()


@then(cfparse('Setup run goes to "{state}" state'))
def validate_state(state: str, run_samples_driver: RunSamplesDriver):
    run_samples_driver.validate_intermediate_run_status(state, wait_time=WaitTimeConstants.SmallWait)


@then(cfparse('Console sample temperature shows "{sample_value}"'))
def validate_sample_temperature_in_control_panel(sample_value: str, console_driver: ConsoleDriver):
    console_driver.validate_sample_temperature(sample_value)


@then(cfparse('Console column temperature shows "{column_value}"'))
def validate_column_temperature_in_control_panel(column_value: str, console_driver: ConsoleDriver):
    console_driver.validate_column_temperature(column_value)
