  """
  Desc: Feature to validate isym system reset
  """

@isym @isym_system_reset_feature
Feature: iSym | System Reset Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_system_reset_workflow
  Scenario: System Reset - Stop Activity and Initialized
    When the system software reset is requested
    Then the system state changes to Resetting
    And the system state changes to Idle


  @isym_workflows_completion @isym_stopping_activity_system_reset_workflow
  Scenario: Stopping Activity and Uninitialized System Reset
    When stopping activities is requested with system reset
    Then the system state changes to Resetting
    And the system state changes to Idle


  @isym_workflows_completion @isym_stopping_activity_system_reset_workflow
  Scenario: Not Stopping Activity and only initialized System Reset
    When only initialized is requested with system reset
#    Then the system state changes to Initializing
    Then the system state changes to Resetting
    And the system state changes to Idle


  @isym_workflows_completion @isym_stopping_activity_initialization_system_reset_workflow
  Scenario: Stopping Activity and Initialized System Reset
    When stopping activities and initialization is requested with system reset
#    Then the system state changes to Initializing
    Then the system state changes to Resetting
    And the system state changes to Idle
