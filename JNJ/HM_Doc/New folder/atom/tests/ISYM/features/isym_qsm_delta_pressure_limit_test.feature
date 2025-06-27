  """
  Desc: Feature to validate ISYM Qsm Delta Pressure Limit workflow
  """

@isym @isym_qsm_delta_pressure_limit_feature
Feature: iSym | Qsm Delta Pressure Limit Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_valid_payload @isym_delta_pressure_limit_allowed_values_workflow
  Scenario Outline: ISYM Qsm Delta Pressure Limit allowed values workflow
    When solvent management delta pressure limit is set to "<value>"
    Then the response status code is "200"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "<value>"

    Examples:
      | value |
      | 5.0   |
      | 100.0 |


  @isym_workflows_invalid_payload @isym_delta_pressure_limit_missing_property_workflow
  Scenario: ISYM Qsm Delta Pressure Limit missing mandatory property workflow
    When solvent management delta pressure limit is set to "5.0"
    Then solvent management delta pressure limit received as "5.0"

    When solvent management delta pressure limit is set with missing "deltaPressureLimitPsi" in payload
    Then the response status code is "500"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "5.0"


  @isym_workflows_invalid_payload @isym_delta_pressure_limit_missing_values_workflow
  Scenario: ISYM Qsm Delta Pressure Limit missing values workflow
    When solvent management delta pressure limit is set to "5.0"
    Then solvent management delta pressure limit received as "5.0"

    When solvent management delta pressure limit is set with missing "deltaPressureLimitPsi" value in payload
    Then the response status code is "500"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "5.0"


  @isym_workflows_invalid_payload @isym_delta_pressure_limit_outside_allowed_boundaries_workflow
  Scenario Outline: ISYM Qsm Delta Pressure Limit using values outside allowed boundaries workflow
    When solvent management delta pressure limit is set to "5.0"
    Then solvent management delta pressure limit received as "5.0"

    When solvent management delta pressure limit is set to "<value>"
    Then the response status code is "500"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "5.0"

    Examples:
      | value |
      | 4.9   |
      | 100.1 |


  @isym_workflows_invalid_payload @isym_delta_pressure_limit_invalid_values_workflow
  Scenario: ISYM Qsm Delta Pressure Limit invalid types of property values workflow
    When solvent management delta pressure limit is set to "5.0"
    Then solvent management delta pressure limit received as "5.0"

    When solvent management delta pressure limit is set to "abcd"
    Then the response status code is "500"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "5.0"


  @isym_workflows_invalid_payload @isym_delta_pressure_limit_with_additional_property_workflow
  Scenario: ISYM Qsm Delta Pressure Limit with additional property workflow
    When solvent management delta pressure limit is set to "5.0"
    Then solvent management delta pressure limit received as "5.0"

    When solvent management delta pressure limit sets an additional property "currentPressureLimitPsi" with "7.0" in payload
    Then the response status code is "500"
    And the system state changes to Idle
    And solvent management delta pressure limit received as "5.0"
