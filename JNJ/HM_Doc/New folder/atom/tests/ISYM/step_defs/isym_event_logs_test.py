import os

from pathlib import Path
from pytest_bdd import scenarios, when, then, given
from glom import assign, delete, glom
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.base_response import ServerRestApiException
from isym_test_api.rest_api.api.system.event_log_response import EventLogMultipleResponse
from isym_test_api.rest_api.drivers.system.event_log_driver import EventLogDriver
from isym_test_api.rest_api.api.behavior.system_meta_report_response import CommonMetaEventMetadata
from isym_test_api.rest_api.api.system.event_log_request import EventLogConfiguration, EventLogEnum
from isym_test_api.rest_api.api.system.event_log_entry_request import EventLogSingleEntry, EventLogMultipleEntries
from utilities.convertion_utilities import parse_string_to_obj
from utilities.datatables.vertical_list import verticallist
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_event_logs.feature')


@given('the event log entry is added manually')
def add_entry(event_log_rest_api_driver: EventLogDriver):
    event_log_rest_api_driver.add_event_log_entry(payload=EventLogConfiguration())


@given('the latest log id is stored')
def store_id(context, event_log_rest_api_driver: EventLogDriver):
    try:
        log_entry_id = event_log_rest_api_driver.get_all_event_log_entry(payload=EventLogMultipleEntries()).data.events.events[0].id
    except ServerRestApiException:
        log_entry_id = 0
    context['log_id_before_test'] = log_entry_id


@when('the single event log information is requested')
def get_single_entry(context, event_log_rest_api_driver: EventLogDriver):
    log_id = context['log_id_before_test'] + 1
    context['event_log'] = event_log_rest_api_driver.get_single_event_log_entry(
        payload=EventLogSingleEntry(id=log_id)).data


@when('all the event log information are requested')
def get_multiple_entry(context, event_log_rest_api_driver: EventLogDriver):
    context['event_log'] = event_log_rest_api_driver.get_all_event_log_entry(payload=EventLogMultipleEntries()).data.events.events[0]


@when('the event log entry is added with non-default values')
def add_entry_non_default(context, event_log_rest_api_driver: EventLogDriver):
    context['api_response'] = event_log_rest_api_driver.add_event_log_entry(
        payload=EventLogConfiguration(user="root", eventtype=EventLogEnum.AuditEventType_HARDWARE, comments="test"))


@when('the single event log entry is requested with non-default values')
def get_single_entry_non_default(context, event_log_rest_api_driver: EventLogDriver):
    context['api_response'] = event_log_rest_api_driver.get_single_event_log_entry(payload=EventLogSingleEntry(id=context['log_id_before_test']))


@when('multiple event log entries are requested with non-default values')
def get_multiple_entries_non_default(context, event_log_rest_api_driver: EventLogDriver):
    context['api_response']: EventLogMultipleResponse = event_log_rest_api_driver.get_all_event_log_entry(
        payload=EventLogMultipleEntries(pageNumber=2, eventsPerPage=30, earliestDate="2023-01-01T00:00:00.000000Z", latestDate="2023-01-01T00:00:00.000000Z"))


@when('the event log entry is added with "<property_name>" = "<property_value>"')
@when(cfparse('the event log entry is added with "{property_name}" = "{property_value}"'))
def set_value_to_add(context, property_name, property_value, event_log_rest_api_driver: EventLogDriver):
    property_value = parse_string_to_obj(property_value)
    payload_as_dict = as_dict(EventLogConfiguration())
    assign(payload_as_dict, property_name, property_value)
    context['api_response'] = event_log_rest_api_driver.add_event_log_entry(payload=payload_as_dict)


@when('multiple event log entries are requested with "<property_name>" = "<property_value>"')
@when(cfparse('multiple event log entries are requested with "{property_name}" = "{property_value}"'))
def set_value_multiple_entry(context, property_name, property_value, event_log_rest_api_driver: EventLogDriver):
    property_value = parse_string_to_obj(property_value)
    payload_as_dict = as_dict(EventLogMultipleEntries())
    assign(payload_as_dict, property_name, property_value)
    context['api_response'] = event_log_rest_api_driver.get_all_event_log_entry(payload=payload_as_dict)


@when('the single event log entry is requested with "<property_name>" = "<property_value>"')
@when(cfparse('the single event log entry is requested with "{property_name}" = "{property_value}"'))
def set_value_single_entry(context, property_name, property_value, event_log_rest_api_driver: EventLogDriver):
    property_value = parse_string_to_obj(property_value)
    payload_as_dict = as_dict(EventLogSingleEntry())
    assign(payload_as_dict, property_name, property_value)
    context['api_response']: CommonMetaEventMetadata = event_log_rest_api_driver.get_single_event_log_entry(
        payload=payload_as_dict)


@when(verticallist('the event log entry is added with missing properties:'))
def missing_value_add_entry(context, table, event_log_rest_api_driver: EventLogDriver):
    payload_as_dict = as_dict(EventLogConfiguration())
    for prop in table.data:
        delete(payload_as_dict, prop)
    context['api_response'] = event_log_rest_api_driver.add_event_log_entry(payload=payload_as_dict)


@when(cfparse('multiple event log entries are requested with "{property_name}" missing'))
def missing_value_multiple_entry(context, property_name, event_log_rest_api_driver: EventLogDriver):
    payload_as_dict = as_dict(EventLogMultipleEntries())
    delete(payload_as_dict, property_name)
    context['api_response'] = event_log_rest_api_driver.get_all_event_log_entry(payload=payload_as_dict)


@when(cfparse('the single event log entry is requested with "{property_name}" missing'))
def missing_value_single_entry(context, property_name, event_log_rest_api_driver: EventLogDriver):
    payload_as_dict = as_dict(EventLogSingleEntry())
    delete(payload_as_dict, property_name)
    context['api_response']: CommonMetaEventMetadata = event_log_rest_api_driver.get_single_event_log_entry(
        payload=payload_as_dict)


@then('the event log information is available')
def validate_event_information(context):
    assert "admin" in context['event_log'].detail.data, "Expected User Data Not Found In Event Log"
    assert "AuditEventType_GENERIC" in context['event_log'].detail.data, "Expected eventtype Data Not Found In Event Log"
    assert "manually added" in context['event_log'].detail.data, "Expected comments Data Not Found In Event Log"
