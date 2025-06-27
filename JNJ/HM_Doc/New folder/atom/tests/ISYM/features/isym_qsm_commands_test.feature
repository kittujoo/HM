  """
  Desc: Feature to validate isym qsm commands
  """

@isym @isym_qsm_commands_feature
Feature: iSym | QSM Commands Test

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_flow_control_workflow
  Scenario: Flow Control
    When the flow control is turned "Off"
    Then the flow control status is turned "Off"

    When the flow control is turned "On"
    Then the flow control status is turned "On"
    And the system state changes to Idle


  @isym_workflows_completion @isym_full_flow_control_workflow
  Scenario: Full Flow Control configured
    When the flow control is turned "Off"
    Then the flow control status is turned "Off"

    When the full flow control activity is requested
    Then the full flow control activity started successfully
    And the full flow control activity completed successfully
    And the full flow control status match requested configuration
    And the system state changes to Idle


  @isym_workflows_completion @isym_prime_pump_workflow
  Scenario: Prime Pump workflow
    When the pump priming activity is requested
    Then the pump priming activity is started successfully
    And the pump priming activity is completed successfully
    And the system state changes to Idle


  @isym_workflows_completion @isym_flow_delta_pressure_workflow
  Scenario Outline: Flow Delta Pressure workflow
    When flow started with "<value>" flow target rate
    Then the response status code is "200"
    And flow status result reach to expected "<value>" flow target rate
    And delta pressure is verified with pressure limits

    Examples:
      | value |
      | 10.0  |
      | 0.001 |
      | 5.0   |
      | 1.0   |


  @isym_workflows_completion @isym_single_line_prime_solvent_workflow
  Scenario: Single Line Prime Solvent workflow
    When the workflow is started
    Then the response status code is "200"
    And the system state changes to Workflow

    When the single prime line start with default flow rate "5.0"
    Then the response status code is "200"
    And prime line status is Active
    And flow status result reach to expected "5.0" flow target rate
    And prime line status is Completed

    When the workflow is deleted
    Then the response status code is "200"
    And the system state is Workflow Recovering
    And prime line status is Inactive
    And the system state changes to Idle


  @isym_workflows_completion @isym_single_line_prime_solvent_abort_workflow
  Scenario: Single Line Prime Solvent Abort workflow
    When the workflow is started
    Then the response status code is "200"
    And the system state changes to Workflow

    When the single prime line start with default flow rate "10.0"
    Then the response status code is "200"
    And prime line status is Active

    When the system stop command is requested
    And the workflow is deleted
    Then the response status code is "200"
    And the system state is Workflow Recovering
    And prime line status is Inactive
    And the system state changes to Idle
