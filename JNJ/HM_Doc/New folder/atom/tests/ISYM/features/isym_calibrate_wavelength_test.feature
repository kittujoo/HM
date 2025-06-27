  """
  Desc: Feature to validate Isym Calibrate Wavelength workflow
  """

@isym @isym_calibrate_wavelength_feature
Feature: iSym | Calibrate Wavelength Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_valid_payload @long
  Scenario: ISYM Calibrate Wavelength Test - Default values
    When wavelength calibration is started
    Then the response status code is "200"
    And the system state changes to Busy
    And the calibrate wavelength state is active
    And the calibrate wavelength state is inactive
    And the system state changes to Idle


  @isym_workflows_invalid_payload @isym_calibrate_wavelength_missing_property_workflow
  Scenario Outline: Calibrate Wavelength missing mandatory property workflow
    When the calibrate wavelength data is set with missing "<property_name>" in payload
    Then the response status code is "409"
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name                            |
      | preflush.enabled                         |
      | preflush.flowRate.flowRateTargetMlPerMin |
      | preflush.flowRate.solventAPct            |
      | preflush.flowRate.solventBPct            |
      | preflush.flowRate.solventCPct            |
      | preflush.flowRate.solventDPct            |
      | preflush.duration                        |
      | preflush                                 |
      | flush.enabled                            |
      | flush.flowRate.flowRateTargetMlPerMin    |
      | flush.flowRate.solventAPct               |
      | flush.flowRate.solventBPct               |
      | flush.flowRate.solventCPct               |
      | flush.flowRate.solventDPct               |
      | flush.duration                           |
      | flush                                    |


  @isym_workflows_invalid_payload @isym_calibrate_wavelength_missing_values_workflow
  Scenario Outline: Calibrate Wavelength missing values workflow
    When the calibrate wavelength data is set with missing "<property_name>" value in payload
    Then the response status code is "409"
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name                            |
      | preflush.enabled                         |
      | preflush.flowRate.flowRateTargetMlPerMin |
      | preflush.flowRate.solventAPct            |
      | preflush.flowRate.solventBPct            |
      | preflush.flowRate.solventCPct            |
      | preflush.flowRate.solventDPct            |
      | preflush.duration                        |
      | preflush                                 |
      | flush.enabled                            |
      | flush.flowRate.flowRateTargetMlPerMin    |
      | flush.flowRate.solventAPct               |
      | flush.flowRate.solventBPct               |
      | flush.flowRate.solventCPct               |
      | flush.flowRate.solventDPct               |
      | flush.duration                           |
      | flush                                    |


  @isym_workflows_valid_payload @isym_calibrate_wavelength_allowed_values_workflow
  Scenario Outline: Calibrate Wavelength allowed values workflow
    When the calibrate wavelength data "<property_name>" is set with "<value>"
    Then the response status code is "200"
    And the system state changes to Busy
    And the calibrate wavelength state is active
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name                            | value |
      | preflush.enabled                         | True  | # @long
      | preflush.enabled                         | False |
      | preflush.flowRate.flowRateTargetMlPerMin | 0.0   |
      | preflush.flowRate.flowRateTargetMlPerMin | 10.0  |
      | preflush.flowRate.solventAPct            | 0.0   |
      | preflush.flowRate.solventAPct            | 100.0 |
      | preflush.flowRate.solventBPct            | 0.0   |
      | preflush.flowRate.solventBPct            | 100.0 |
      | preflush.flowRate.solventCPct            | 0.0   |
      | preflush.flowRate.solventCPct            | 100.0 |
      | preflush.flowRate.solventDPct            | 0.0   |
      | preflush.flowRate.solventDPct            | 100.0 |
      | preflush.duration                        | 0.1   |
      | preflush.duration                        | 60.0  |
      | flush.enabled                            | True  | # @long
      | flush.enabled                            | False |
      | flush.flowRate.flowRateTargetMlPerMin    | 0.0   |
      | flush.flowRate.flowRateTargetMlPerMin    | 10.0  |
      | flush.flowRate.solventAPct               | 0.0   |
      | flush.flowRate.solventAPct               | 100.0 |
      | flush.flowRate.solventBPct               | 0.0   |
      | flush.flowRate.solventBPct               | 100.0 |
      | flush.flowRate.solventCPct               | 0.0   |
      | flush.flowRate.solventCPct               | 100.0 |
      | flush.flowRate.solventDPct               | 0.0   |
      | flush.flowRate.solventDPct               | 100.0 |
      | flush.duration                           | 0.1   |
      | flush.duration                           | 60.0  |


  @isym_workflows_invalid_payload @isym_calibrate_wavelength_outside_allowed_boundaries_workflow
  Scenario Outline: Calibrate Wavelength using values outside allowed boundaries workflow
    When the calibrate wavelength data "<property_name>" is set with "<value>"
    Then the response status code is "409"
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name                            | value |
      | preflush.flowRate.flowRateTargetMlPerMin | -1.0  |
      | preflush.flowRate.flowRateTargetMlPerMin | 11.0  |
      | preflush.flowRate.solventAPct            | -1.0  |
      | preflush.flowRate.solventAPct            | 101.0 |
      | preflush.flowRate.solventBPct            | -1.0  |
      | preflush.flowRate.solventBPct            | 101.0 |
      | preflush.flowRate.solventCPct            | -1.0  |
      | preflush.flowRate.solventCPct            | 101.0 |
      | preflush.flowRate.solventDPct            | -1.0  |
      | preflush.flowRate.solventDPct            | 101.0 |
      | preflush.duration                        | 0.0   |
      | preflush.duration                        | 61.0  |
      | flush.flowRate.flowRateTargetMlPerMin    | -1.0  |
      | flush.flowRate.flowRateTargetMlPerMin    | 11.0  |
      | flush.flowRate.solventAPct               | -1.0  |
      | flush.flowRate.solventAPct               | 101.0 |
      | flush.flowRate.solventBPct               | -1.0  |
      | flush.flowRate.solventBPct               | 101.0 |
      | flush.flowRate.solventCPct               | -1.0  |
      | flush.flowRate.solventCPct               | 101.0 |
      | flush.flowRate.solventDPct               | -1.0  |
      | flush.flowRate.solventDPct               | 101.0 |
      | flush.duration                           | 0.0   |
      | flush.duration                           | 61.0  |


  @isym_workflows_invalid_payload @isym_calibrate_wavelength_invalid_values_workflow
  Scenario Outline: Calibrate Wavelength invalid types of property values workflow
    When the calibrate wavelength data "<property_name>" is set with "abcd"
    Then the response status code is "409"
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name                            |
      | preflush.enabled                         |
      | preflush.flowRate.flowRateTargetMlPerMin |
      | preflush.flowRate.solventAPct            |
      | preflush.flowRate.solventBPct            |
      | preflush.flowRate.solventCPct            |
      | preflush.flowRate.solventDPct            |
      | preflush.duration                        |
      | flush.enabled                            |
      | flush.flowRate.flowRateTargetMlPerMin    |
      | flush.flowRate.solventAPct               |
      | flush.flowRate.solventBPct               |
      | flush.flowRate.solventCPct               |
      | flush.flowRate.solventDPct               |
      | flush.duration                           |


  @isym_workflows_invalid_payload @isym_calibrate_wavelength_with_additional_property_workflow
  Scenario Outline: Calibrate Wavelength with additional property workflow
    When the calibrate wavelength data "<property_name>" is set with "<value>"
    Then the response status code is "409"
    And the calibrate wavelength state is inactive
    And the system state changes to Idle

    Examples:
      | property_name       | value |
      | preflush.flowStatus | True  |
      | flush.flowStatus    | True  |
      | flowStatus          | True  |
