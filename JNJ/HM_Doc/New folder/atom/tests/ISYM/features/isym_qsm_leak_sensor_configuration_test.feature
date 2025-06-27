  """
  Desc: Feature to validate ISYM QSM Leak Sensor Test

  """

@isym @isym_qsm_leak_feature
Feature: iSym | Qsm Leak Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_qsm_leak_test_enabled_workflow
  Scenario: iSym Qsm Leak Configuration Test - Enabled
    When the qsm leak sensor is "enabled"
    Then the response status code is "200"
    And the status of qsm leak sensor will be "True"

  @isym_qsm_leak_test_workflow @isym_qsm_leak_test_disabled_workflow
  Scenario: iSym Qsm Leak Configuration Test - Disabled
    When the qsm leak sensor is "disabled"
    Then the response status code is "200"
    And the status of qsm leak sensor will be "False"