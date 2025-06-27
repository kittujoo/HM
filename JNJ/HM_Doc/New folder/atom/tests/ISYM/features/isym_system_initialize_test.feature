"""
  Desc: Feature to validate isym system initialize
  """

@isym @isym_system_initialize_feature
Feature: iSym | System Initialize Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_system_initialize_workflow
  Scenario: System Initialize
    When the system software initialize is requested
#    Then the system state changes to Initializing
    Then the system state changes to Resetting
    And the system state changes to Idle
