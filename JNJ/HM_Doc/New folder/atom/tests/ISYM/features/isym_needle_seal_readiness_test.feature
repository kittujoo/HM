  """
  Desc: Feature to validate iSym Needle Seal Readiness Workflow.
  """

@isym @isym_needle_seal_readiness_feature
Feature: iSym | Needle Seal Readiness Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_seal_readiness_workflow @quarantine @defect:INSISYM-4698
  Scenario: Needle seal readiness test workflow - run to completion
    When a needle seal readiness test is started
    Then the system state changes to Busy
    And the needle seal readiness test completes
    And the needle seal readiness test status will be passed
    And the system state changes to Idle


  @isym_workflows_abort @isym_seal_readiness_abort
  Scenario: Needle seal readiness test workflow - abort execution
    When a needle seal readiness test is started
    Then the system state changes to Busy

    When the system stop command is requested
    Then the system state changes to Idle


  @isym_workflows_completion @isym_seal_readiness_workflow @quarantine @defect:INSISYM-4698
  Scenario Outline: FlowRateTargetMlPerMin valid value tests
    When payload set with flow rate target value = "<value>"
    And the needle seal readiness test is started
    Then the system state changes to Busy
    And the needle seal readiness test completes
    And the needle seal readiness test status will be passed
    And the system state changes to Idle

    Examples:
      | value |
      | 0.0   | # minimum
      | 10.0  | # maximum
      | 5.0   | # intermediate


  @isym_seal_readiness_invalid_property
  Scenario Outline: FlowRateTargetMlPerMin invalid value tests
    When payload set with flow rate target value = "<value>"
    And the needle seal readiness test is started
    Then the response status code is "409"

    Examples:
      | value |
      | -1.0  | # below min
      | 11.0  | # above max

  @isym_workflows_completion @isym_seal_readiness_workflow @quarantine @defect:INSISYM-4698
  Scenario Outline: Solvent Composition Tests
    When the needle seal readiness test is started with given data:
      | flowRateTargetMlPerMin | <flowRateTargetMlPerMin> |
      | solventAPct            | <solventAPct>            |
      | solventBPct            | <solventBPct>            |
      | solventCPct            | <solventCPct>            |
      | solventDPct            | <solventDPct>            |
    Then the response status code is "200"
    And the system state changes to Busy
    And the needle seal readiness test completes
    And the needle seal readiness test status will be passed
    And the system state changes to Idle

    Examples:
      | flowRateTargetMlPerMin | solventAPct | solventBPct | solventCPct | solventDPct |
      | 0.0                    | 0.0         | 0.0         | 0.0         | 0.0         | # Zero Solvent Compositions
      | 1.2                    | 23.0        | 24.0        | 25.0        | 19.0        | # Non-Default Valid Values
      | 0.0                    | 25.0        | 25.0        | 25.0        | 25.0        | # Mixed Solvent Compositions
      | 0.0                    | 50.0        | 50.0        | 0.0         | 0.0         | # Mixed Solvent Compositions
      | 0.0                    | 100.0       | 0.0         | 0.0         | 0.0         | # Mixed Solvent Compositions
      | 0.0                    | 100.0       | 100.0       | 100.0       | 100.0       | # Maximum Solvent Compositions

  @isym_seal_readiness_invalid_structure
  Scenario: Additional properties test
    When payload set with key additional property
    And the needle seal readiness test is started
    Then the response status code is "409"


  @isym_seal_readiness_invalid_structure
  Scenario Outline: Required Fields Tests
    When payload set with omitting property "<property_name>"
    And the needle seal readiness test is started
    Then the response status code is "409"

    Examples:
      | property_name          |
      | flowRateTargetMlPerMin |
      | solventAPct            |


  @isym_seal_readiness_invalid_structure
  Scenario Outline: Test With Invalid Type Values - String
    When payload set with key "<property_name>" value as "waters"
    And the needle seal readiness test is started
    Then the response status code is "409"

    Examples:
      | property_name          |
      | flowRateTargetMlPerMin |
      | solventAPct            |
