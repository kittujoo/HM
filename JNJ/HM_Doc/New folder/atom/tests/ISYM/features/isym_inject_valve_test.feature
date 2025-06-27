  """
  Desc: Feature to validate ISYM Inject Valve Test Workflow.

  """

@isym @isym_inject_valve_feature
Feature: iSym | Inject Valve Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_injection_workflow
  Scenario Outline: Inject Valve Test
    When inject valve is set to "<position_name>" position
    Then the response status code is "200"
    And the inject valve position is set to "<position_name>"

    Examples:
      | position_name              |
      | InjectValvePosition_BLOCK  |
      | InjectValvePosition_LOAD   |
      | InjectValvePosition_INJECT |
