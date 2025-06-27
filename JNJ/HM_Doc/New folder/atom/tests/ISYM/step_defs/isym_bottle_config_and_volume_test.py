from glom import delete, assign
from pathlib import Path
from pytest_bdd import scenarios, given, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.solvent_management.bottle_config_request import (generate_bottle_config_non_default_request,
                                                                                 generate_bottle_config_default_request)
from isym_test_api.rest_api.api.solvent_management.bottle_volume_request import (generate_bottle_volume_non_default_request, generate_bottle_volume_request)
from isym_test_api.rest_api.drivers.solvent_management.bottle_config_driver import BottleConfigurationDriver
from utilities.convertion_utilities import parse_string_to_obj
from utilities.glom_utilities import assert_dicts_equal
from utilities.json_utility import as_dict

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_bottle_config_and_volume_test.feature')


@given('bottle is configured')
def given_configure_bottle(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_config_default_request()
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload)
    assert as_dict(bottle_config_rest_api_driver.get_bottle_configuration().data) == as_dict(payload), "Bottle configuration is not as expected"


@given('bottle is configured with non-default properties')
def given_configure_bottle_non_default(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_config_non_default_request()
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload)
    assert as_dict(bottle_config_rest_api_driver.get_bottle_configuration().data) == as_dict(payload), "Bottle configuration is not as expected"


@when('bottle configuration is sent')
def configure_bottle_default(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_config_default_request()
    context['payload'] = payload
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload)


@when('bottle configuration is sent with non-default properties')
def configure_bottle_with_non_default_properties(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_config_non_default_request()
    context['payload'] = payload
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload)


@when(cfparse('bottle configuration is sent with the property "{property_name}" missing'))
def configure_bottle_with_missing_values(context, property_name, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload_as_dict = as_dict(generate_bottle_config_default_request())
    delete(payload_as_dict, property_name)
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload_as_dict)


@when(cfparse('bottle configuration is sent with "{property_name}" missing its value'))
def configure_bottle_with_missing_required_field(context, property_name, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload_as_dict = as_dict(generate_bottle_config_default_request())
    assign(payload_as_dict, property_name, None)
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload_as_dict)


@when(cfparse('bottle configuration is sent with "{property_name}" = "{value}" property'))
def configure_bottle_add_property(context, property_name, value, bottle_config_rest_api_driver: BottleConfigurationDriver):
    value = parse_string_to_obj(value)
    payload_as_dict = as_dict(generate_bottle_config_default_request())
    assign(payload_as_dict, property_name, value)
    context['payload'] = payload_as_dict
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_configuration(payload_as_dict)


@when('bottle volume is sent')
def set_bottle_volume(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_volume_request()
    context['payload'] = payload
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_volume(payload)


@when('bottle volume is sent with non-default properties')
def set_bottle_volume_with_non_default_properties(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload = generate_bottle_volume_non_default_request()
    context['payload'] = payload
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_volume(payload)


@when(cfparse('bottle volume is sent with the property "{property_name}" missing'))
def set_bottle__volume_with_missing_required_field(context, property_name, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload_as_dict = as_dict(generate_bottle_volume_request())
    delete(payload_as_dict, property_name)
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_volume(payload_as_dict)


@when(cfparse('bottle volume is sent with "{property_name}" missing its value'))
def set_bottle_volume_with_missing_values(context, property_name, bottle_config_rest_api_driver: BottleConfigurationDriver):
    payload_as_dict = as_dict(generate_bottle_volume_request())
    assign(payload_as_dict, property_name, None)
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_volume(payload_as_dict)


@when(cfparse('bottle volume is sent with "{property_name}" = "{value}" property'))
def bottle_volume_add_property(context, property_name, value, bottle_config_rest_api_driver: BottleConfigurationDriver):
    value = parse_string_to_obj(value)
    payload_as_dict = as_dict(generate_bottle_volume_request())
    assign(payload_as_dict, property_name, value)
    context['payload'] = payload_as_dict
    context['api_response'] = bottle_config_rest_api_driver.set_bottle_volume(payload_as_dict)


@then('bottle configuration is as expected')
def verify_bottle_configuration(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    expected_payload = context['payload'] if isinstance(context['payload'], dict) else as_dict(context['payload'])
    actual_payload = as_dict(bottle_config_rest_api_driver.get_bottle_configuration().data)
    assert_dicts_equal(actual_payload, expected_payload, ignored_keys=["dataModelType", "dataModelVersion"])


@then('bottle volume is as expected')
def verify_bottle_volume(context, bottle_config_rest_api_driver: BottleConfigurationDriver):
    if isinstance(context['payload'], dict):
        assert as_dict(bottle_config_rest_api_driver.get_bottle_volume().data) == context['payload'], "Bottle volume is not as expected"
    else:
        assert as_dict(bottle_config_rest_api_driver.get_bottle_volume().data) == as_dict(context['payload']), "Bottle volume is not as expected"
