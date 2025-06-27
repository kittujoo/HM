  """
  Desc: Feature to validate isym system events
  """


@isym @isym_system_events_feature
Feature: iSym | System Events Test

  Background:
    Given the system state is Idle

  @isym_workflows_valid_payload @isym_subscribe_unsubscribe_event_workflow
  Scenario: Subscribe and unsubscribe events
    When the available events are requested
    Then the current events list is retrieved

    When subscribing event from an available events list
    Then the subscribed events list is retrieved with the correct event

    When the available event is unsubscribed
    Then the subscribed events list will be empty


  @isym_workflows_valid_payload @isym_subscribe_single_event_workflow
  Scenario: Subscribe to an event
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event


  @isym_workflows_valid_payload @isym_subscribe_multiple_events_workflow
  Scenario: Subscribe to multiple events
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When subscribing for "TuvLampStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "TuvLampStatus" event


  @isym_workflows_valid_payload @isym_subscribe_unsubscribe_single_event_workflow
  Scenario: Subscribe to one event and UnSubscribe
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When unsubscribed "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list should not contain "FlowControlStatus" event


  @isym_workflows_valid_payload @isym_subscribe_unsubscribe_multiple_events_workflow
  Scenario: Subscribe to multiple events and unsubscribe from all events
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When subscribing for "TuvLampStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "TuvLampStatus" event

    When unsubscribed "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list should not contain "FlowControlStatus" event

    When unsubscribed "TuvLampStatus" event
    Then the response status code is "200"
    And the subscribed events list will be empty


  @isym_workflows_valid_payload @isym_subscribe_multiple_unsubscribe_one_events_workflow
  Scenario: Subscribe to multiple events and unsubscribe from one event
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When subscribing for "ColumnTemperatureStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "ColumnTemperatureStatus" event

    When unsubscribed "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list should not contain "FlowControlStatus" event


  @isym_workflows_invalid_payload @isym_subscribe_invalid_event_workflow @quarantine @defect:INSISYM-4718
  Scenario: Subscribe to invalid event
    When subscribing for "SystemBehaviourStatus" event
    Then the response status code is "500"
    And the subscribed events list should not contain "SystemBehaviourStatus" event


  @isym_workflows_invalid_payload @isym_subscribe_multiple_one_invalid_event_workflow @quarantine @defect:INSISYM-4718
  Scenario: Subscribe to multiple events with one invalid event
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When subscribing for "TuvLampStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "TuvLampStatus" event

    When subscribing for "SystemBehaviourStatus" event
    Then the response status code is "500"
    And the subscribed events list should not contain "SystemBehaviourStatus" event


  @isym_workflows_invalid_payload @isym_subscribe_multiple_unsubscribe_one_invalid_event_workflow
  Scenario: Subscribe to multiple events and unsubscribe from one invalid event
    When subscribing for "FlowControlStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "FlowControlStatus" event

    When subscribing for "TuvLampStatus" event
    Then the response status code is "200"
    And the subscribed events list contains "TuvLampStatus" event

    When unsubscribed "SystemBehaviourStatus" event
    Then the response status code is "200"
    And the subscribed events list should not contain "SystemBehaviourStatus" event
