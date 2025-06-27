  """
  Desc: Feature to validate ISYM System Noise And Drift workflow.
  """

@isym @isym_system_noise_and_drift_feature
Feature: iSym | System Noise And Drift Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_system_noise_drift_workflow
  Scenario: System noise and drift test
    When a system noise and drift test is started
    Then the system state changes to Busy
    And the system noise and drift test completes
    And the system noise and drift test status will be passed
    And the system state changes to Idle


  @isym_workflows_abort @isym_system_noise_drift_abort
  Scenario: System noise and drift test abort
    When a system noise and drift test is started
    Then the system state changes to Busy

    When the system stop command is requested
    Then the system state changes to Idle


  @isym_workflows_valid_payload
  Scenario: Runs To Completion With Non Default Property Values
    When a system noise and drift test is set with non default values
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_invalid_payload
  Scenario: Missing flowRateTargetMlPerMin Property For Payload
    When a system noise and drift test is set with "qsm1.flowRateTargetMlPerMin" property removed
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Missing wavelengthA Property For Payload
    When a system noise and drift test is set with "tuv1.wavelengthA" property removed
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Flow Rate Target Minimum Value
    When a system noise and drift test started with "qsm1.flowRateTargetMlPerMin" = "-1.0"
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Flow Rate Target Maximum Value
    When a system noise and drift test started with "qsm1.flowRateTargetMlPerMin" = "-1.0"
    Then the response status code is "409"


  @isym_workflows_valid_payload
  Scenario: Solvent Percentages With Zero Composition
    When a system noise and drift test started with data:
      | qsm1.solventAPct | 0.0 |
      | qsm1.solventBPct | 0.0 |
      | qsm1.solventCPct | 0.0 |
      | qsm1.solventDPct | 0.0 |
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: Solvent Percentages With Max Composition
    When a system noise and drift test started with data:
      | qsm1.solventAPct | 100.0 |
      | qsm1.solventBPct | 100.0 |
      | qsm1.solventCPct | 100.0 |
      | qsm1.solventDPct | 100.0 |
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: Solvent Percentages With Mixed Composition
    When a system noise and drift test started with data:
      | qsm1.solventAPct | 25.0 |
      | qsm1.solventBPct | 25.0 |
      | qsm1.solventCPct | 25.0 |
      | qsm1.solventDPct | 25.0 |
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: WavelengthA Minimum Value
    When a system noise and drift test started with "tuv1.wavelengthA" = "190.0"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: WavelengthA Maximum Value
    When a system noise and drift test started with "tuv1.wavelengthA" = "700.0"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: WavelengthA Intermediate Value
    When a system noise and drift test started with "tuv1.wavelengthA" = "300.0"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_invalid_payload
  Scenario: WavelengthA Out of Range Value
    When a system noise and drift test started with "tuv1.wavelengthA" = "180.0"
    Then the response status code is "409"


  @isym_workflows_valid_payload
  Scenario Outline: Data Rate Variants Valid Value
    When a system noise and drift test started with "<property_name>" = "<property_value>"
    Then the response status code is "200"
    And the system state changes to Busy

    Examples:
      | property_name                    | property_value |
      | tuv1.filterParameters.dataRateHz | DataRate_1HZ   |
      | tuv1.filterParameters.dataRateHz | DataRate_2HZ   |
      | tuv1.filterParameters.dataRateHz | DataRate_5HZ   |
      | tuv1.filterParameters.dataRateHz | DataRate_10HZ  |
      | tuv1.filterParameters.dataRateHz | DataRate_20HZ  |
      | tuv1.filterParameters.dataRateHz | DataRate_40HZ  |
      | tuv1.filterParameters.dataRateHz | DataRate_80HZ  |
      | tuv1.filterParameters.dataRateHz | DataRate_160HZ |


  @isym_workflows_valid_payload
  Scenario: FilterTimeConstantSec Minimum Value
    When a system noise and drift test started with "tuv1.filterParameters.filterTimeConstantSec" = "0.2"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: FilterTimeConstantSec Maximum Value
    When a system noise and drift test started with "tuv1.filterParameters.filterTimeConstantSec" = "5.0"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario: FilterTimeConstantSec Intermediate Value
    When a system noise and drift test started with "tuv1.filterParameters.filterTimeConstantSec" = "1.0"
    Then the response status code is "200"
    And the system state changes to Busy


  @isym_workflows_valid_payload
  Scenario Outline: FilterBehaviour Variants Valid Value
    When a system noise and drift test started with "<property_name>" = "<property_value>"
    Then the response status code is "200"
    And the system state changes to Busy
    Examples:
      | property_name                      | property_value                     |
      | tuv1.filterBehavior.filterBehavior | FilterBehavior_NOOPERATIONFILTER   |
      | tuv1.filterBehavior.filterBehavior | FilterBehavior_LEGACYHAMMINGFILTER |


  @isym_workflows_invalid_payload
  Scenario: Additional Property For qsm1 Payload
    When a system noise and drift test started with "qsm1.cycle_rate" = "default"
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Payload With Invalid Type For dataRateHz
    When a system noise and drift test started with "tuv1.filterParameters.dataRateHz" = "INVALID_TYPE"
    Then the response status code is "409"


  @isym_workflows_invalid_payload
  Scenario: Payload With Invalid Type For wavelengthA
    When a system noise and drift test started with "tuv1.wavelengthA" = "invalid_value"
    Then the response status code is "409"
