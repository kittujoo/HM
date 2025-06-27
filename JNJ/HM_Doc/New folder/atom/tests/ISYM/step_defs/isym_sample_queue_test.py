import os

from glom import assign, delete
from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.system.system_sample_queue_request import generate_default_set_system_sample_queue_request
from isym_test_api.rest_api.drivers.system.data_system_acquisition_driver import DatasystemAcquisitionDriver
from utilities.convertion_utilities import parse_string_to_obj
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_sample_queue_test.feature')

# region When


@when('the sample queue data is set')
def set_default_sample_queue_data(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = generate_default_set_system_sample_queue_request()
    context['set_sample_queue'] = as_dict(payload)
    context['api_response'] = data_system_acquisition_rest_api_driver.set_sample_queue(payload=payload)


@when(cfparse('the sample queue data "{property_name}" is set with "{value}"'))
def set_valid_sample_queue_data(context, property_name: str, value: str, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_set_system_sample_queue_request())
    value = parse_string_to_obj(value)
    assign(payload, property_name, value)
    context['set_sample_queue'] = payload
    context['api_response'] = data_system_acquisition_rest_api_driver.set_sample_queue(payload=payload)


@when(cfparse('the sample queue data is set with missing "{property_name}" in payload'))
def set_missing_sample_queue_data(context, property_name: str, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_set_system_sample_queue_request())
    delete(payload, property_name)
    context['set_sample_queue'] = payload
    context['api_response'] = data_system_acquisition_rest_api_driver.set_sample_queue(payload=payload)


@when(cfparse('the sample queue data is set with missing "{property_name}" value in payload'))
def set_missing_value_sample_queue_data(context, property_name: str, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    payload = as_dict(generate_default_set_system_sample_queue_request())
    value = None
    assign(payload, property_name, value)
    context['set_sample_queue'] = payload
    context['api_response'] = data_system_acquisition_rest_api_driver.set_sample_queue(payload=payload)


@when('the sample queue data is requested')
def get_sample_queue_data(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    context['api_response'] = data_system_acquisition_rest_api_driver.get_sample_queue()
    context['sample_queue'] = as_dict(context['api_response'].data)

# endregion When
# region Then


@then('requested sample queue data is matched with registered sample queue data')
def compare_request_response_data(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    assert context['set_sample_queue'] == context['sample_queue'], f"Unexpected sample queue data: {context['sample_queue']}"


@then('requested sample queue data does not match with registered sample queue data')
def compare_request_response_data_unmatch(context, data_system_acquisition_rest_api_driver: DatasystemAcquisitionDriver):
    assert context['set_sample_queue'] != context['sample_queue'], f"Equal sample queue data: {context['sample_queue']}"

# endregion Then
