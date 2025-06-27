  """
  Issues raised:
  * Then the system state changes to Preparing. This step is commented because the state change is too fast.
  Preparing state will be tested using channel data in the future. Kept here for reference.
  """

@isym @isym_wash_needle_workflow_feature
Feature: iSym | Wash Needle Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_wash_needle_workflow
  Scenario: Wash Needle Test
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And the system state changes to At Method Conditions

    When the Wash Needle operation is requested to perform
#    Then the system state changes to Preparing
    Then the system state changes to Running
    And the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_abort @isym_wash_needle_abort
  Scenario: Wash Needle Abort
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And the system state changes to At Method Conditions

    When the Wash Needle operation is requested to perform
#    Then the system state changes to Preparing
    Then the system state changes to Running

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle
