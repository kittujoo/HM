  """
  Desc: Feature to validate isym system commands
  """

@isym @isym_system_commands_feature
Feature: iSym | System Commands Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_scan_column_workflow
  Scenario: Scan Column Tag
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the scan column tag is requested
    Then the scan column tag activity completed successfully

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_completion @isym_autozero_workflow
  Scenario: AutoZero workflow
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle
    And the autozero offsets values are collected

    When the autozero activity is requested
    Then the autozero activity started successfully
    And the updated autozero offsets values were measured

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_completion @isym_leak_sensors_workflow
  Scenario: Get Leak Sensors
    When the enable system leak sensor configuration is requested
    And the system leak sensor check is requested
    Then no leak status was observed in response
