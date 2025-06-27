import os

from glom import assign, delete
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.solvent_management.delta_pressure_limit_request import generate_delta_pressure_limit_request
from isym_test_api.rest_api.drivers.solvent_management.qsm_command_driver import QsmCommandDriver
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_qsm_delta_pressure_limit_test.feature')

# region When


@when(cfparse('solvent management delta pressure limit is set to "{value}"'))
def set_delta_pressure_limit(context, value: str, qsm_command_rest_api_driver: QsmCommandDriver):
    value_data = float(value) if value.replace('.', '', 1).isdigit() else value
    payload = generate_delta_pressure_limit_request(value_data)
    context['api_response'] = qsm_command_rest_api_driver.set_delta_pressure_limit(payload=payload)


@when(cfparse('solvent management delta pressure limit is set with missing "{property_name}" in payload'))
def set_missing_delta_pressure_limit_data(context, property_name: str, qsm_command_rest_api_driver: QsmCommandDriver):
    payload = as_dict(generate_delta_pressure_limit_request())
    delete(payload, property_name)
    context['api_response'] = qsm_command_rest_api_driver.set_delta_pressure_limit(payload=payload)


@when(cfparse('solvent management delta pressure limit is set with missing "{property_name}" value in payload'))
def set_missing_value_delta_pressure_limit_data(context, property_name: str, qsm_command_rest_api_driver: QsmCommandDriver):
    payload = as_dict(generate_delta_pressure_limit_request())
    assign(payload, property_name, None)
    context['api_response'] = qsm_command_rest_api_driver.set_delta_pressure_limit(payload=payload)


@when(cfparse('solvent management delta pressure limit sets an additional property "{property_name}" with "{value}" in payload'))
def set_additional_delta_pressure_limit_data(context, property_name: str, value: str, qsm_command_rest_api_driver: QsmCommandDriver):
    value_data = float(value) if value.replace('.', '', 1).isdigit() else value
    payload = as_dict(generate_delta_pressure_limit_request())
    assign(payload, property_name, value_data)
    context['api_response'] = qsm_command_rest_api_driver.set_delta_pressure_limit(payload=payload)

# endregion When
# region Then


@then(cfparse('solvent management delta pressure limit received as "{value}"'))
def verify_delta_pressure_limit(context, value: str, qsm_command_rest_api_driver: QsmCommandDriver):
    context['api_response'] = qsm_command_rest_api_driver.get_delta_pressure_limit()
    response = context['api_response'].data
    assert float(value) == response.deltaPressureLimitPsi, f"Delta Pressure Limit differs : {response}"

# endregion Then