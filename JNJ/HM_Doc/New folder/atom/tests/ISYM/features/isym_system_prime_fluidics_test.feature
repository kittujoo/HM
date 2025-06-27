  """
  Desc: Feature to validate System Prime Fluidics workflow
  """

@isym @isym_system_prime_fluidics_feature
Feature: iSym | System Prime Fluidics Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_system_prime_fluidics_workflow
  Scenario: System Prime Fluidics
    When system prime fluidics test is started
    Then the system state changes to Busy
    And system prime fluidics test completes
    And the system state changes to Idle


  @isym_workflows_abort @isym_system_prime_fluidics_abort
  Scenario: System Prime Fluidics Abort
    When system prime fluidics test is started
    Then the system state changes to Busy

    When the system stop command is requested
    Then the system state changes to Idle
