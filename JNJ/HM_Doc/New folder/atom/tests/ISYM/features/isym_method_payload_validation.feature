  """
  Desc: Feature to validate ISYM Method Payload.
  """


@isym @isym_method_payload_validation
Feature: iSym | Validate Method Payload

  Background:
    Given the system state is Idle
    When the Exclusive Idle system state is requested
    Then the system state changes to Exclusive Idle

  @isym_workflows_valid_payload
  Scenario: Runs To Completion With Non Default Property Values
    When the gradient method data is sent with non default values
    Then the response status code is "200"
    And the system state changes to Setting Method


  @isym_workflows_invalid_payload @quarantine
  Scenario: Solvent Percentages With Zero Composition
    When the method data is sent with next properties:
      | acquisition.qsm1.gradient.segments.-1.solventAPct | 0.0 |
      | acquisition.qsm1.gradient.segments.-1.solventBPct | 0.0 |
      | acquisition.qsm1.gradient.segments.-1.solventCPct | 0.0 |
      | acquisition.qsm1.gradient.segments.-1.solventDPct | 0.0 |
    Then the response status code is "500"
    And the system state changes to Exclusive Fail


  @isym_workflows_invalid_payload @quarantine
  Scenario: Solvent Percentages With Max Composition
    When the method data is sent with next properties:
      | acquisition.qsm1.gradient.segments.-1.solventAPct | 100.0 |
      | acquisition.qsm1.gradient.segments.-1.solventBPct | 100.0 |
      | acquisition.qsm1.gradient.segments.-1.solventCPct | 100.0 |
      | acquisition.qsm1.gradient.segments.-1.solventDPct | 100.0 |
    Then the response status code is "500"
    And the system state changes to Exclusive Fail


  @isym_workflows_valid_payload
  Scenario: Solvent Percentages With Mixed Composition
    When the method data is sent with next properties:
      | acquisition.qsm1.gradient.segments.-1.solventAPct | 25.0 |
      | acquisition.qsm1.gradient.segments.-1.solventBPct | 25.0 |
      | acquisition.qsm1.gradient.segments.-1.solventCPct | 25.0 |
      | acquisition.qsm1.gradient.segments.-1.solventDPct | 25.0 |
    Then the response status code is "200"
    And the system state changes to Setting Method


  @isym_workflows_invalid_payload
  Scenario: Empty Segment Property For Payload
    When the method data is sent with missing properties:
      | acquisition.qsm1.gradient.segments.-1.timeMin          |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin |
      | acquisition.qsm1.gradient.segments.-1.curve            |
      | acquisition.qsm1.gradient.segments.-1.solventAPct      |
      | acquisition.qsm1.gradient.segments.-1.solventBPct      |
      | acquisition.qsm1.gradient.segments.-1.solventCPct      |
      | acquisition.qsm1.gradient.segments.-1.solventDPct      |
    Then the response status code is "500"
    And the system state changes to Exclusive Fail


  @isym_workflows_valid_payload
  Scenario: Multiple Segments For Payload
    When the gradient method data is sent with "200" segment data
    Then the response status code is "200"
    And the system state changes to Setting Method


  @isym_workflows_invalid_payload
  Scenario: Multiple Segments For Invalid Payload
    When the gradient method data is sent with "201" segment data
    Then the response status code is "500"
    And the system state changes to Exclusive Fail


  @isym_workflows_invalid_payload
  Scenario Outline: Send method data with absent property values
    When the method data is sent with missing "<property_name>" property
    Then the response status code is "500"
    And the system state changes to Exclusive Fail

    Examples:
      | property_name                                                                               |
      | systemMethodHeader.dataModelRevision                                                        |
      | systemMethodHeader.methodType                                                               |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 |
      | acquisition.qsm1.gradient.offsetVolumeUl                                                    |
      | acquisition.qsm1.gradient.offsetType                                                        |
      | acquisition.gwy.diagChannels                                                                |
      | acquisition.qsm1.diagChannels.compositionDChannelEnable                                     |
      | acquisition.qsm1.flowRampPeriodMin                                                          |
      | acquisition.qsm1.solvents.solventLineA                                                      |
      | acquisition.qsm1.solvents                                                                   |
      | acquisition.qsm1.sealWashPeriodMin                                                          |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                                |
      | acquisition.tuv1.deviceType                                                                 |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthMode                                     |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                                        |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                                        |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec             |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnInjectStart      |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnWavelengthChange |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.filterBehavior             |
      | acquisition.tuv1.dataAcquisitionSettings.timedEvents                                        |
      | acquisition.tuv1.lampOn                                                                     |
      | acquisition.chc1.deviceType                                                                 |
      | acquisition.chc1.diagChannels                                                               |
      | acquisition.chc1.columnTemperature                                                          |
      | acquisition.chc1.columnTemperatureThresholdEnable                                           |
      | acquisition.chc1.columnTemperatureThresholdDegC                                             |
      | acquisition.chc1.columnType                                                                 |
      | acquisition.ftn1.deviceType                                                                 |
      | acquisition.ftn1.diagChannels                                                               |
      | acquisition.ftn1.needleWashSec                                                              |
      | acquisition.ftn1.drawRateULPerMin                                                           |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                               |
      | acquisition.ftn1.vialAndWellBottomSense                                                     |
      | acquisition.ftn1.sampleTemperature                                                          |
      | acquisition.ftn1.sampleTemperatureThresholdEnable                                           |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                             |
      | acquisition.ftn1.solvents                                                                   |


  @isym_workflows_valid_payload
  Scenario Outline: Validate boundary values for method set request
    When the method data is sent with "<property_name>" = "<value>" property
    Then the response status code is "200"
    And the system state changes to Setting Method

    Examples:
      | property_name                                                                   | value    |
      | acquisition.qsm1.flowRampPeriodMin                                              | 0.066667 |
      | acquisition.qsm1.flowRampPeriodMin                                              | 0.5      |
      | acquisition.qsm1.flowRampPeriodMin                                              | 0.25     |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                             | 0.0      |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                             | 10000.0  |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                             | 5000.0   |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                            | 0.0      |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                            | 5000.0   |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                            | 10000.0  |
      | acquisition.qsm1.sealWashPeriodMin                                              | 0.0167   |
      | acquisition.qsm1.sealWashPeriodMin                                              | 30.0     |
      | acquisition.qsm1.sealWashPeriodMin                                              | 60.0     |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                    | 66.0     |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                    | 90.0     |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                    | 132.0    |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                          | 0.0      |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                          | 10.0     |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                          | 5.0      |
      | acquisition.qsm1.gradient.offsetVolumeUl                                        | 0.0      |
      | acquisition.qsm1.gradient.offsetVolumeUl                                        | 2000.0   |
      | acquisition.qsm1.gradient.offsetVolumeUl                                        | 1000.0   |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                            | 190.0    |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                            | 700.0    |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                            | 300.0    |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                            | 190.0    |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                            | 700.0    |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                            | 300.0    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec | 0.0      |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec | 5.0      |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec | 2.5      |
      | acquisition.chc1.columnTemperature.columnTemperature.targetTemperatureDegC      | 4.0      |
      | acquisition.chc1.columnTemperature.columnTemperature.targetTemperatureDegC      | 90.0     |
      | acquisition.chc1.columnTemperature.columnTemperature.targetTemperatureDegC      | 45.0     |
      | acquisition.chc1.columnTemperatureThresholdDegC                                 | 1.0      |
      | acquisition.chc1.columnTemperatureThresholdDegC                                 | 10.0     |
      | acquisition.chc1.columnTemperatureThresholdDegC                                 | 5.0      |
      | acquisition.ftn1.needleWashSec                                                  | 4.0      |
      | acquisition.ftn1.needleWashSec                                                  | 10.0     |
      | acquisition.ftn1.needleWashSec                                                  | 120.0    |
      | acquisition.ftn1.drawRateULPerMin                                               | 10.0     |
      | acquisition.ftn1.drawRateULPerMin                                               | 50.0     |
      | acquisition.ftn1.drawRateULPerMin                                               | 1000.0   |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                   | 0.0      |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                   | 20.0     |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                   | 30.0     |
      | acquisition.ftn1.sampleTemperature.sampleTemperature.targetTemperatureDegC      | 4.0      |
      | acquisition.ftn1.sampleTemperature.sampleTemperature.targetTemperatureDegC      | 30.0     |
      | acquisition.ftn1.sampleTemperature.sampleTemperature.targetTemperatureDegC      | 40.0     |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                 | 0.5      |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                 | 2.0      |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                 | 10.0     |


  @isym_workflows_invalid_payload
  Scenario Outline: Validate invalid boundary values for method set request
    When the method data is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"
    And the system state changes to Exclusive Fail

    Examples:
      | property_name                                                                   | value   |
      | acquisition.qsm1.flowRampPeriodMin                                              | -1.0    |
      | acquisition.qsm1.flowRampPeriodMin                                              | 0.6     |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                             | -1.0    |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                             | 12000.0 |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                            | -1.0    |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                            | 12000.0 |
      | acquisition.qsm1.sealWashPeriodMin                                              | -1.0    |
      | acquisition.qsm1.sealWashPeriodMin                                              | 61.0    |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                    | 65.0    |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                    | 133.0   |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                          | -1.0    |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                          | 11.0    |
      | acquisition.qsm1.gradient.offsetVolumeUl                                        | -1.0    |
      | acquisition.qsm1.gradient.offsetVolumeUl                                        | 2001.0  |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                            | 189.0   |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                            | 701.0   |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                            | 189.0   |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                            | 701.0   |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec | -1.0    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec | 6       |
      | acquisition.chc1.targetTemperatureDegC                                          | -4.0    |
      | acquisition.chc1.targetTemperatureDegC                                          | 91.0    |
      | acquisition.chc1.columnTemperatureThresholdDegC                                 | -1.0    |
      | acquisition.chc1.columnTemperatureThresholdDegC                                 | 11.0    |
      | acquisition.ftn1.needleWashSec                                                  | 3.0     |
      | acquisition.ftn1.needleWashSec                                                  | 121.0   |
      | acquisition.ftn1.drawRateULPerMin                                               | 9.0     |
      | acquisition.ftn1.drawRateULPerMin                                               | 1001.0  |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                   | -1.0    |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                   | 31.0    |
      | acquisition.ftn1.targetTemperatureDegC                                          | 3.0     |
      | acquisition.ftn1.targetTemperatureDegC                                          | 41.0    |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                 | 0       |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                 | 11.0    |


  @isym_workflows_valid_payload
  Scenario Outline: Validate Valid enum values for method set request
    When the method data is sent with "<property_name>" = "<value>" property
    Then the response status code is "200"
    And the system state changes to Setting Method

    Examples:
      | property_name                                                                               | value                                            |
      | acquisition.qsm1.gradient.offsetType                                                        | GradientStartInjectionOffsetType_ATINJECTION     |
      | acquisition.qsm1.gradient.offsetType                                                        | GradientStartInjectionOffsetType_BEFOREINJECTION |
      | acquisition.qsm1.gradient.offsetType                                                        | GradientStartInjectionOffsetType_AFTERINJECTION  |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE1                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE2                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE3                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE4                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE5                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE6                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE7                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE8                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE9                             |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE10                            |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE11                            |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthMode                                     | WavelengthMode_SINGLE                            |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthMode                                     | WavelengthMode_DUAL                              |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_1HZ                                     |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_2HZ                                     |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_5HZ                                     |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_10HZ                                    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_20HZ                                    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_40HZ                                    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_80HZ                                    |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | DataRate_160HZ                                   |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnWavelengthChange | AutoZeroBehavior_NOOPERATIONAUTOZERO             |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnWavelengthChange | AutoZeroBehavior_OFFSETTOZERO                    |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnWavelengthChange | AutoZeroBehavior_MAINTAINBASELINE                |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.filterBehavior             | FilterBehavior_NOOPERATIONFILTER                 |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.filterBehavior             | FilterBehavior_LEGACYHAMMINGFILTER               |

  @isym_workflows_invalid_payload
  Scenario Outline: Send method data with invalid property values
    When the method data is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"
    And the system state changes to Exclusive Fail

    Examples:
      | property_name                                                                               | value                                         |
      | acquisition.qsm1.flowRampPeriodMin                                                          | test                                          |
      | acquisition.qsm1.pressureLimits.lowPressureLimitPsi                                         | test                                          |
      | acquisition.qsm1.pressureLimits.highPressureLimitPsi                                        | test                                          |
      | acquisition.qsm1.sealWashPeriodMin                                                          | test                                          |
      | acquisition.qsm1.strokeVolume.strokeVolumeUL                                                | test                                          |
      | acquisition.qsm1.gradient.segments.-1.flowRateMlPerMin                                      | test                                          |
      | acquisition.qsm1.gradient.offsetVolumeUl                                                    | test                                          |
      | acquisition.qsm1.gradient.offsetType                                                        | GradientStartInjectionOffsetType_NONINJECTION |
      | acquisition.qsm1.gradient.segments.-1.curve                                                 | GradientCurve_CURVE53                         |
      | acquisition.qsm1.gradient.segments.-1.solventAPct                                           | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthMode                                     | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthA                                        | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.wavelengthB                                        | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.dataRateHz                        | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.filterParameters.filterTimeConstantSec             | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnInjectStart      | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.autoZeroOnWavelengthChange | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.dataProcessingBehaviors.filterBehavior             | test                                          |
      | acquisition.tuv1.dataAcquisitionSettings.timedEvents                                        | test                                          |
      | acquisition.tuv1.lampOn                                                                     | test                                          |
      | acquisition.gwy.diagChannels                                                                | test                                          |
      | acquisition.chc1.columnTemperatureChannelEnable                                             | test                                          |
      | acquisition.chc1.targetTemperatureDegC                                                      | test                                          |
      | acquisition.chc1.temperatureControlled                                                      | test                                          |
      | acquisition.chc1.columnTemperatureThresholdEnable                                           | test                                          |
      | acquisition.chc1.columnTemperatureThresholdDegC                                             | test                                          |
      | acquisition.ftn1.diagChannels                                                               | abcd                                          |
      | acquisition.ftn1.needleWashSec                                                              | abcd                                          |
      | acquisition.ftn1.drawRateULPerMin                                                           | abcd                                          |
      | acquisition.ftn1.aspirationDistanceFromSampleLocationBottomMM                               | abcd                                          |
      | acquisition.ftn1.vialAndWellBottomSense                                                     | abcd                                          |
      | acquisition.ftn1.sampleTemperature                                                          | abcd                                          |
      | acquisition.ftn1.sampleTemperatureThresholdEnable                                           | abcd                                          |
      | acquisition.ftn1.sampleTemperatureThresholdDegC                                             | abcd                                          |
      | acquisition.ftn1.solvents                                                                   | abcd                                          |


  @isym_workflows_invalid_payload
  Scenario Outline: Addition Of Property
    When the method data is sent with "<property_name>" = "<property_val>" property
    Then the response status code is "500"
    And the system state changes to Exclusive Fail

    Examples:
      | property_name                                      | property_val |
      | acquisition.qsm1.gradient.segments.-1.cycle_rate   | default      |
      | acquisition.qsm1.gradient.temporary_flow           | fast         |
      | acquisition.tuv1.dataAcquisitionSettings.wave_flow | linear       |
      | acquisition.tuv1.lampColor                         | red          |
      | acquisition.gwy.Channels                           | analog       |
      | acquisition.chc1.column_rate                       | generic      |
      | acquisition.chc1.temperature_value                 | slow         |
      | acquisition.ftn1.unknown_property                  | default      |
      | acquisition.ftn1.unknown_value                     | 100.0        |
