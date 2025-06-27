  """
  Desc: Feature to validate Isym Vent Valve workflow
  """

@isym @isym_vent_valve_feature
Feature: iSym | Vent Valve Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_valid_payload
  Scenario Outline: ISYM Vent Valve Test
    When the vent valve is requested for "<vent_valve_position>" position
    Then the response status code is "200"
    And the vent valve workflow is completed
    And the vent valve is positioned for "<vent_valve_position>"

    Examples:
      | vent_valve_position      |
      | VentValvePosition_WASTE  |
      | VentValvePosition_SYSTEM |


  @isym_workflows_invalid_payload
  Scenario: ISYM Vent Valve Unknown Position Test
    Given the vent valve is positioned for "VentValvePosition_SYSTEM" position
    When the vent valve is requested for "VentValvePosition_UNKNOWN" position
    Then the response status code is "500"
    And the vent valve workflow is completed
    And the vent valve is positioned for "VentValvePosition_SYSTEM"


  @isym_workflows_invalid_payload
  Scenario: ISYM Vent Valve Illegal Position Test
    Given the vent valve is positioned for "VentValvePosition_SYSTEM" position
    When the vent valve is requested for "VentValvePosition_ILLEGAL" position
    Then the response status code is "500"
    And the vent valve workflow is completed
    And the vent valve is positioned for "VentValvePosition_SYSTEM"


  @isym_workflows_valid_payload
  Scenario Outline: ISYM Vent Valve Pressure Or Flow Test
    When the vent valve "<vent_valve_position>" position is requested for "<property>" with "<value>"
    Then the response status code is "200"
    And the vent valve workflow is completed
    And the vent valve is positioned for "<vent_valve_position>"

    Examples:
      | vent_valve_position     | property             | value   |
      | VentValvePosition_WASTE | waitForPressure      | false   |
      | VentValvePosition_WASTE | waitForPressure      | true    |
      | VentValvePosition_WASTE | resumeFlow           | false   |
      | VentValvePosition_WASTE | resumeFlow           | true    |
      | VentValvePosition_WASTE | pressureThresholdPsi | 10.0    |
      | VentValvePosition_WASTE | pressureThresholdPsi | 10000.0 |


  @isym_workflows_invalid_payload
  Scenario Outline: ISYM Vent Valve Out Of Limit Pressure Threshold Test
    Given the vent valve is positioned for "VentValvePosition_SYSTEM" position
    When the vent valve "<vent_valve_position>" position is requested for "<property>" with "<value>"
    Then the response status code is "500"
    And the vent valve workflow is completed
    And the vent valve is positioned for "VentValvePosition_SYSTEM"

    Examples:
      | vent_valve_position     | property             | value   |
      | VentValvePosition_WASTE | pressureThresholdPsi | 9.0     |
      | VentValvePosition_WASTE | pressureThresholdPsi | 10001.0 |


  @isym_workflows_invalid_payload
  Scenario Outline: ISYM Vent Valve Missing Property Test
    Given the vent valve is positioned for "VentValvePosition_SYSTEM" position
    When the vent valve "<vent_valve_position>" position is requested without "<property>" property
    Then the response status code is "500"
    And the vent valve workflow is completed
    And the vent valve is positioned for "VentValvePosition_SYSTEM"

    Examples:
      | vent_valve_position     | property             |
      | VentValvePosition_WASTE | pressureThresholdPsi |
      | VentValvePosition_WASTE | waitForPressure      |
      | VentValvePosition_WASTE | resumeFlow           |
      | VentValvePosition_WASTE | valvePosition        |


  @isym_workflows_valid_payload
  Scenario Outline: ISYM Flow Control with the Vent Valve
    When the vent valve is requested for "<vent_valve_position>" position
    Then the response status code is "200"
    And the vent valve workflow is completed
    And the vent valve is positioned for "<vent_valve_position>"

    When the flow control is turned "On"
    Then the response status code is "200"
    And the flow control status is turned "On"
    And the system state changes to Idle

    Examples:
      | vent_valve_position      |
      | VentValvePosition_WASTE  |
      | VentValvePosition_SYSTEM |
