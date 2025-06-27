import os

from pathlib import Path
from pytest_bdd import scenarios, when, given, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.system.start_column_request import StartColumnRequest
from isym_test_api.rest_api.drivers.system.command.start_column_driver import StartColumnDriver
from utilities.json_utility import as_dict
from utilities.logger import Logger
from utilities.string_utility import str_to_bool

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_condition_column_test.feature')


def start_conditioning(start_column_rest_api_driver: StartColumnDriver, payload: StartColumnRequest):
    start_column_rest_api_driver.set_start_column(payload)


@when(cfparse('condition column is started with a runtime set to "{runtime:f}" minutes'))
def start_conditioning_valid(start_column_rest_api_driver: StartColumnDriver, runtime: float):
    payload = StartColumnRequest(runTimeMin=runtime)
    start_conditioning(start_column_rest_api_driver, payload)


@when(cfparse('condition column is started with a runtime set to "{runtime}" minutes with string type value'))
def start_conditioning_string_type(start_column_rest_api_driver: StartColumnDriver, runtime: str):
    payload = StartColumnRequest(runTimeMin=runtime)
    start_conditioning(start_column_rest_api_driver, payload)


@when(cfparse('condition column is started with a boolean type value as "{value}"'))
def start_conditioning_bool_type(start_column_rest_api_driver: StartColumnDriver, value):
    payload = StartColumnRequest(runTimeMin=str_to_bool(value))
    start_conditioning(start_column_rest_api_driver, payload)


@when(cfparse('condition column is started with a runtime set to "{runtime}" minutes with array type value'))
def start_conditioning_array_type(start_column_rest_api_driver: StartColumnDriver, runtime: list):
    payload = StartColumnRequest(runTimeMin=list(runtime))
    start_conditioning(start_column_rest_api_driver, payload)


@when('condition column is started with a runtime as Object type value')
def start_conditioning_object_type(start_column_rest_api_driver: StartColumnDriver):
    payload = StartColumnRequest(runTimeMin={"a": 1})
    start_conditioning(start_column_rest_api_driver, payload)


@when('column condition is started with a runtime set to null value')
def start_conditioning_null_value(start_column_rest_api_driver: StartColumnDriver):
    payload = StartColumnRequest(runTimeMin=None)
    start_conditioning(start_column_rest_api_driver, payload)


@when(cfparse('condition column is started with "{additional_property}" as "{value}"'))
def start_conditioning_additional_properties(start_column_rest_api_driver: StartColumnDriver, additional_property, value):
    payload = as_dict(StartColumnRequest())
    payload[additional_property] = value
    start_conditioning(start_column_rest_api_driver, payload)


@when('condition column is started with a missing runtime')
@when('condition column is started with a empty payload')
def start_conditioning_empty_payload(start_column_rest_api_driver: StartColumnDriver):
    start_conditioning(start_column_rest_api_driver, {})
