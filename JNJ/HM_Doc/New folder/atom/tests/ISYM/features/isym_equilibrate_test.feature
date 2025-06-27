  """
  Desc: Feature to validate ISYM Equilibrate Test
  """

@isym @isym_equilibrate_feature
Feature: iSym | Equilibrate Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_equilibrate_test_workflow @quarantine
  Scenario: iSym Equilibrate Test - run to completion
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And the system state changes to At Method Conditions

    When a equilibrating test is started
#    Then the system state changes to Preparing
    Then the system state changes to Running
    And the system state changes to Exclusive Idle
    And the post run report is available

    When the Exclusive Idle system state is released
    Then the system state changes to Idle
