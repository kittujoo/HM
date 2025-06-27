  """
  Desc: Feature to validate ISYM FTN Leak Sensor Configuration
  """

@isym @isym_ftn_leak_sensor_feature
Feature: iSym | FTN Leak Sensor Configuration Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_ftn_leak_sensor_enabled_workflow
  Scenario: iSym FTN Leak Sensor Configuration - Enabled
    When the FTN leak sensor is "enabled"
    Then the response status code is "200"
    And the status of FTN leak sensor will be "True"

  @isym_workflows_completion @isym_ftn_leak_sensor_disabled_workflow
  Scenario: iSym FTN Leak Sensor Configuration - Disabled
    When the FTN leak sensor is "disabled"
    Then the response status code is "200"
    And the status of FTN leak sensor will be "False"
