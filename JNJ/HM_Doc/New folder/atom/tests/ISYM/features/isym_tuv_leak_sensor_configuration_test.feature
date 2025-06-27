  """
  Desc: Feature to validate ISYM TUV Leak Sensor Test Configuration

  """

@isym @isym_tuv_leak_feature
Feature: iSym | Tuv Leak Sensor Configuration Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_tuv_leak_test_enabled_workflow
  Scenario: iSym Tuv Leak Sensor Configuration Test - Enabled
    When the tuv leak sensor is "enabled"
    Then the response status code is "200"
    And the status of tuv leak sensor will be "True"

  @isym_tuv_leak_test_workflow @isym_tuv_leak_test_disabled_workflow
  Scenario: iSym Tuv Leak Sensor Configuration Test - Disabled
    When the tuv leak sensor is "disabled"
    Then the response status code is "200"
    And the status of tuv leak sensor will be "False"
