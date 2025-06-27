  """
  Desc: Feature to validate ISYM Injection workflow.

  """

@isym @isym_injection_feature
Feature: iSym | Injection Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_injection_workflow
  Scenario: Single injection
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And the system state changes to At Method Conditions

    When the acquisition channels are requested
    Then the acquisition channels information is returned
    And the expected acquisition channel type is returned

    When injection activity is started
    Then the system state changes to Preparing
    And the system state changes to Running
    And the system state changes to Exclusive Idle
    Then the post run report is available

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_abort @isym_injection_setting_abort
  Scenario: Single injection abort while at setting method
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_abort @isym_injection_method_condition_abort
  Scenario: Single injection abort while at method conditions state
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And the system state changes to At Method Conditions

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_abort @isym_injection_preparing_abort @quarantine @defect:INSISYM-4548
  Scenario: Single injection abort while at preparing state
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And  the system state changes to At Method Conditions

    When injection activity is started
    Then the system state changes to Preparing

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows_abort @isym_injection_running_abort
  Scenario: Single injection abort while at running state
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

    When the correct method data is sent
    Then the system state changes to Setting Method
    And  the system state changes to At Method Conditions

    When injection activity is started
    Then the system state changes to Preparing
    And  the system state changes to Running

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle
