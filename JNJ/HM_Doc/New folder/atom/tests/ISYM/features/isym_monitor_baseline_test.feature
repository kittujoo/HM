"""
  Issues raised:
  * Then the system state changes to Preparing/Running. This steps are commented because the state change is too fast.
  Preparing/Running state will be tested using channel data in the future. Kept here for reference.
  """
@isym @isym_monitor_baseline_feature
Feature: iSym | Monitor Baseline Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_monitor_baseline_workflow
  Scenario: Monitor Baseline test workflow - run to completion
    When the correct method data is sent
    Then the system state changes to Busy
    And the system state changes to Idle

    When the monitor baseline operation is started
    #Then the system state changes to Preparing
    #Then the system state changes to Running
    Then the system state changes to Busy

    When the system stop command is requested
    Then the system state changes to Idle
