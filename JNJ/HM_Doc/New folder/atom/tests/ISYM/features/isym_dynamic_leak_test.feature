  """
  Desc: Feature to validate ISYM Dynamic Leak workflow.

  """

@isym @isym_dynamic_leak_feature
Feature: iSym | Dynamic Leak Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_dynamic_leak_workflow
  Scenario: Dynamic leak
    When parameter "solventLine" set as "SolventLine_A" for Dynamic Leak test
    And parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy
    And the dynamic leak test completes with no leaks
    And the leak test status will be passed
    And the system state changes to Idle

  @isym_workflows_abort  @isym_dynamic_leak_abort
  Scenario: Dynamic leak abort
    When parameter "solventLine" set as "SolventLine_A" for Dynamic Leak test
    And parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    And the system stop command is requested
    Then the system state changes to Idle

  @isym_workflows_completion
  Scenario: Dynamic leak test with TargetPressurePsi minimum valid values
    When parameter "accumulatorTargetPressurePsi" set as numeric "3500.0" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as numeric "3000.0" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_completion
  Scenario: Dynamic leak test with TargetPressurePsi maximum valid values
    When parameter "accumulatorTargetPressurePsi" set as numeric "9500.0" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as numeric "7500.0" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_completion
  Scenario: Dynamic leak test for enum valid case 1
    When parameter "solventLine" set as "SolventLine_A" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_completion
  Scenario: Dynamic leak test for enum valid case 2
    When parameter "solventLine" set as "SolventLine_B" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test for enum invalid value
    When parameter "solventLine" set as "SolventLine_XYZ" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"


  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean value as true for parameters
    When parameter "testAccumulator" set as boolean "true" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "true" for Dynamic Leak test
    And parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "true" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test for boolean value as false for parameters
    When parameter "testAccumulator" set as boolean "false" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "false" for Dynamic Leak test
    And parameter "includePrime" set as boolean "false" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "false" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test with TargetPressurePsi below minimum values
    When parameter "accumulatorTargetPressurePsi" set as numeric "2999.0" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as numeric "2999.0" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 1
    When parameter "testAccumulator" set as boolean "true" for Dynamic Leak test
    And parameter "accumulatorTargetPressurePsi" set as numeric "3000.0" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 2
    When parameter "testAccumulator" set as boolean "false" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "true" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as numeric "3000.0" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test with TargetPressurePsi above maximum values
    When parameter "accumulatorTargetPressurePsi" set as numeric "9501.0" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as numeric "7501.0" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test with TargetPressurePsi with invalid type values
    When parameter "accumulatorTargetPressurePsi" set as "XYZ" for Dynamic Leak test
    And parameter "primaryTargetPressurePsi" set as "ABCD" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 3
    When parameter "testAccumulator" set as boolean "false" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 4
    When parameter "testAccumulator" set as boolean "true" for Dynamic Leak test
    And parameter "testPrimary" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 5
    When parameter "includePrime" set as boolean "false" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "false" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 6
    When parameter "includePrime" set as boolean "false" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "false" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test for boolean values case 7
    When parameter "includePrime" set as boolean "false" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "true" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"


  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 8
    When parameter "includePrime" set as boolean "false" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "true" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 9
    When parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "false" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 10
    When parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "false" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the system state changes to Busy


  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test for boolean values case 11
    When parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "true" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "false" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "409"

  @isym_workflows_completion
  Scenario: Dynamic leak test for boolean values case 12
    When parameter "includePrime" set as boolean "true" for Dynamic Leak test
    And parameter "includeNeedleAndSeal" set as boolean "true" for Dynamic Leak test
    And parameter "includeColumn" set as boolean "true" for Dynamic Leak test
    And Dynamic leak test is started
    Then the response status code is "200"


  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test with removed property
    When Dynamic leak test started with property "testAccumulator" is removed
    Then the response status code is "409"

  @isym_workflows_invalid_payload
  Scenario: Dynamic leak test with extra property
    When Dynamic leak test started with new property "testABCD" is added with value "1000.0"
    Then the response status code is "409"
