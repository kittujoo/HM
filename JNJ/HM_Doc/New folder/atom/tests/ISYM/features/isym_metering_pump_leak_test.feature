  """
  Desc: Feature to validate ISYM Metering Pump Leak workflow.

  """

@isym @isym_metering_pump_leak_feature
Feature: iSym | Metering Pump Leak Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_metering_pump_leak_workflow
  Scenario: Metering pump leak
    When a metering pump leak test is started for solvent_a with the metering pump primed
    Then the stored leak test configuration is as expected
    And the system state changes to Busy
    And the metering pump leak test completes with no leaks
    And the leak test status will be passed
    And the system state changes to Idle

  @isym_workflows_abort @isym_metering_pump_leak_abort
  Scenario: Metering pump leak abort
    When a metering pump leak test is started for solvent_a with the metering pump primed
    And the system stop command is requested
    Then the stored leak test configuration is as expected
    And the system state changes to Idle

  @isym_workflows_non_default_valid_values @isym_metering_pump_leak_non_default_valid_values
  Scenario: Metering pump leak non-default valid values
    When a metering pump leak test is started for non-default valid values
    Then the stored leak test configuration is as expected
    And the system state changes to Busy
    And the metering pump leak test completes with no leaks
    And the leak test status will be passed
    And the system state changes to Idle

  @isym_workflows_missing_required_field @isym_metering_pump_leak_missing_required_field
  Scenario: Metering pump leak missing required field
    When a metering pump leak test is started with property "includePrime" missing
    Then the response status code is "409"

  @isym_workflows_min_pressure @isym_metering_pump_leak_min_pressure
  Scenario: Metering pump leak min pressure
    When a metering pump leak test is started with minimum pressure
    Then the stored leak test configuration is as expected
    And the system state changes to Busy
    And the metering pump leak test completes with no leaks
    And the leak test status will be passed
    And the system state changes to Idle

  @isym_workflows_max_pressure @isym_metering_pump_leak_max_pressure
  Scenario: Metering pump leak max pressure
    When a metering pump leak test is started with maximum pressure
    Then the stored leak test configuration is as expected
    And the system state changes to Busy
    And the metering pump leak test completes with no leaks
    And the leak test status will be passed
    And the system state changes to Idle

  @isym_workflows_edge_min_pressure @isym_metering_pump_leak_edge_min_pressure
  Scenario: Metering pump leak edge minimum pressure
    When a metering pump leak test is started just below minimum pressure
    Then the response status code is "409"

  @isym_workflows_edge_max_pressure @isym_metering_pump_leak_edge_max_pressure
  Scenario: Metering pump leak edge maximum pressure
    When a metering pump leak test is started just above maximum pressure
    Then the response status code is "409"

  @isym_workflows_additional_property @isym_metering_pump_leak_additional_property
  Scenario: Metering pump leak additional property
    When a metering pump leak test is started with an additional property "additionalProperty" with a value "additionalValue"
    Then the response status code is "409"
