import os

from pathlib import Path
from pytest_bdd import scenarios, when, then
from pytest_bdd.parsers import cfparse

from isym_test_api.rest_api.api.system.event_map_response import EventMap, EventDict
from isym_test_api.rest_api.drivers.system.system_event_driver import SystemEventDriver
from utilities.json_utility import as_dict
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/isym_system_events_test.feature')

isym_event_dict = {
    'FlowControlStatus': EventDict(publicTopic='/solventmanagement/qsm/flowcontrol', internalTopic='Status:Instrument:Qsm#.*:FlowControlStatus'),
    'TuvLampStatus': EventDict(publicTopic='/detection/tuv/lamp', internalTopic='Status:Instrument:Tuv#.*:LampStatus'),
    'ColumnTemperatureStatus': EventDict(publicTopic='/separation/cm/chamber1/temperature', internalTopic='Status:Instrument:Chc#.*:ColumnTemperatureStatus'),
    'FtnWashNeedle': EventDict(publicTopic='/samplemanagement/sm-ftn/behavior/washneedle/status', internalTopic='Status:Activity:FtnWashNeedle:*'),
    'SystemBehaviourStatus': EventDict(publicTopic='/kettle', internalTopic='brough:SystemBehaviourState:*')
}


# region When


@when('the available events are requested')
def request_available_events(context, system_events_rest_api_driver: SystemEventDriver):
    context['api_response'] = system_events_rest_api_driver.get_events()
    context['events'] = context['api_response'].data


@when('subscribing event from an available events list')
def request_event_subscription(context, system_events_rest_api_driver: SystemEventDriver):
    payload = EventMap([context['selected_event']])
    context['subscribe_event_payload'] = payload
    context['api_response'] = system_events_rest_api_driver.set_events_subscriptions(payload)


@when('the available event is unsubscribed')
def request_event_unsubscription(context, system_events_rest_api_driver: SystemEventDriver):
    payload = context['subscribe_event_payload']
    context['api_response'] = system_events_rest_api_driver.delete_events_subscriptions(payload).data


@when(cfparse('subscribing for "{value}" event'))
def request_event_to_subscribe(value, context, system_events_rest_api_driver: SystemEventDriver):
    event_query = isym_event_dict[value]
    context['selected_event'] = event_query
    context['subscribe_event_payload'] = EventMap([event_query])
    context['api_response'] = system_events_rest_api_driver.set_events_subscriptions(context['subscribe_event_payload'])
    context['subscribe_event_list'] = context['api_response'].data


@when(cfparse('unsubscribed "{value}" event'))
def request_event_unsubscription(value: str, context, system_events_rest_api_driver: SystemEventDriver):
    event_query = isym_event_dict[value]
    context['selected_event'] = event_query
    payload = EventMap([event_query])
    context['api_response'] = system_events_rest_api_driver.delete_events_subscriptions(payload)
    context['subscribe_event_list'] = context['api_response'].data


# endregion When
# region Then


@then('the subscribed events list is retrieved with the correct event')
def verify_subscribe_event_list(context, system_events_rest_api_driver: SystemEventDriver):
    payload = context['subscribe_event_payload']
    response: EventMap = system_events_rest_api_driver.get_events_subscriptions().data
    assert all(event in response.events for event in payload.events), f"Event is not subscribed: {payload}"


@then('the current events list is retrieved')
def verify_event_list(context):
    response: EventMap = context['events']
    assert response, "Events were not retrieved from the events list"
    assert response.events, "Events were not retrieved from the events list"
    context['selected_event'] = response.events[0]


@then('the subscribed events list will be empty')
def verify_empty_event_list(system_events_rest_api_driver: SystemEventDriver):
    response = system_events_rest_api_driver.get_events_subscriptions().data
    assert response is None, f"Subscribe events list is not empty: {response}"


@then(cfparse('the subscribed events list contains "{value}" event'))
def verify_subscribe_event_list_event(context, value: str, system_events_rest_api_driver: SystemEventDriver):
    payload = isym_event_dict[value]
    assert payload in context['subscribe_event_list'].events, f"Event is not subscribed: {context['subscribe_event_list']}"


@then(cfparse('the subscribed events list should not contain "{value}" event'))
def verify_subscribe_event_list_event(context, value: str, system_events_rest_api_driver: SystemEventDriver):
    payload = as_dict(isym_event_dict[value])
    response = context['subscribe_event_list']['events'] if bool(context['subscribe_event_list']) else []
    assert payload not in response, f"Unexpected events subscription list: {response}"


@then(cfparse('the subscribed events list should not contains "{value}" event'))
def verify_subscribe_event_list_incorrect_event(value: str, system_events_rest_api_driver: SystemEventDriver):
    payload = isym_event_dict[value]
    response: EventMap = system_events_rest_api_driver.get_events_subscriptions().data
    assert payload not in response.events, "Incorrect Event is subscribed"

# endregion Then
