  """
  Desc: Feature to validate ISYM SetMethod.

  """

@isym @isym_setmethod_feature
Feature: iSym | Set Method Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_setmethod_test
  Scenario: SetMethod Test with correct method data
    When the correct method data is sent
    Then the system state changes to Busy
    And the system state changes to Idle


  @isym_workflows_completion @isym_workflows_payload_invalid
  Scenario: SetMethod Test - incorrect method data
    When the incorrect method data is sent
    Then the system state changes to Error


  @isym_workflows_completion @isym_workflows_payload_invalid
  Scenario: SetMethod Test - incorrect method data then correct method data
    When the incorrect method data is sent
    Then the system state changes to Error

    When the system reset command is requested
    Then the system state changes to Idle

    When the correct method data is sent
    Then the system state changes to Busy
    And the system state changes to Idle
