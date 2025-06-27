  """
  Desc: Feature to validate ISYM Sample Queue Test.
  """

@isym @isym_sample_queue_feature
Feature: iSym | Sample Queue Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_valid_payload @isym_sample_queue_workflow
  Scenario: Sample Queue Test - Default values
    When the sample queue data is set
    Then the response status code is "200"

    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data is matched with registered sample queue data


  @isym_workflows_invalid_payload @isym_sample_queue_missing_property_workflow @quarantine @defect:INSISYM-4784
  Scenario Outline: Sample Queue missing mandatory property workflow
    When the sample queue data is set with missing "<property_name>" in payload
    Then the response status code is "500"

    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data does not match with registered sample queue data

    Examples:
      | property_name                      |
      | sampleInjections.-1.injections     |
      | sampleInjections.-1.sampleLocation |
      | sampleInjections.-1.sampleVolumeUl |
      | sampleInjections                   |
      | samplesRemainingInSampleSet        |
      | samplesRemainingInQueue            |
      | injectionsRemainingInSampleSet     |
      | injectionsRemainingInQueue         |
      | additionalInfo                     |


  @isym_workflows_valid_payload @isym_sample_queue_allowed_values_workflow
  Scenario Outline: Sample Queue allowed values workflow
    When the sample queue data "<property_name>" is set with "<value>"
    Then the response status code is "200"
    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data is matched with registered sample queue data

    Examples:
      | property_name                      | value  |
      | sampleInjections.-1.injections     | 1      |
      | sampleInjections.-1.injections     | 32767  |
      | sampleInjections.-1.sampleLocation | ""     |
      | sampleInjections.-1.sampleLocation | "abcd" |
      | sampleInjections.-1.sampleVolumeUl | 0.0    |
      | sampleInjections.-1.sampleVolumeUl | 1000.0 |
      | samplesRemainingInSampleSet        | 0      |
      | samplesRemainingInSampleSet        | 32767  |
      | samplesRemainingInQueue            | 0      |
      | samplesRemainingInQueue            | 32767  |
      | injectionsRemainingInSampleSet     | 0      |
      | injectionsRemainingInSampleSet     | 32767  |
      | injectionsRemainingInQueue         | 0      |
      | injectionsRemainingInQueue         | 32767  |
      | additionalInfo                     | true   |
      | timeRemainingInSampleSet           | 1001.0 |
      | timeRemainingInQueue               | 1001.0 |
      | injectionsCompletedInQueue         | 0      |
      | injectionsCompletedInQueue         | 32767  |


  @isym_workflows_invalid_payload @isym_sample_queue_outside_allowed_boundaries_workflow @quarantine @defect:INSISYM-4784
  Scenario Outline: Sample Queue using values outside allowed boundaries workflow
    When the sample queue data "<property_name>" is set with "<value>"
    Then the response status code is "500"
    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data does not match with registered sample queue data

    Examples:
      | property_name                      | value        |
      | sampleInjections.-1.injections     | 0            |
      | sampleInjections.-1.injections     | 32768        |
      | sampleInjections.-1.sampleLocation | ""           |
      | sampleInjections.-1.sampleLocation | "0000000000" |
      | sampleInjections.-1.sampleVolumeUl | -1.0         |
      | sampleInjections.-1.sampleVolumeUl | 1001.0       |
      | samplesRemainingInSampleSet        | -1           |
      | samplesRemainingInSampleSet        | 32768        |
      | samplesRemainingInQueue            | -1           |
      | samplesRemainingInQueue            | 32768        |
      | injectionsRemainingInSampleSet     | -1           |
      | injectionsRemainingInSampleSet     | 32768        |
      | injectionsRemainingInQueue         | -1           |
      | injectionsRemainingInQueue         | 32768        |
      | additionalInfo                     | false        |
      | timeRemainingInSampleSet           | -1.0         |
      | timeRemainingInSampleSet           | 12345678.0   |
      | timeRemainingInQueue               | -1.0         |
      | timeRemainingInQueue               | 12345678.0   |
      | injectionsCompletedInQueue         | -1           |
      | injectionsCompletedInQueue         | 32768        |


  @quarantine @ignore # returns 502 bad gateway html string
  Scenario Outline: Sample Queue missing values workflow
    When the sample queue data is set with missing "<property_name>" value in payload
    Then the response status code is "502"

    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data does not match with registered sample queue data

    Examples:
      | property_name                      |
      | sampleInjections.-1.injections     |
      | sampleInjections.-1.sampleLocation |
      | sampleInjections.-1.sampleVolumeUl |
      | samplesRemainingInSampleSet        |
      | samplesRemainingInQueue            |
      | injectionsRemainingInSampleSet     |
      | injectionsRemainingInQueue         |
      | additionalInfo                     |
      | timeRemainingInSampleSet           |
      | timeRemainingInQueue               |
      | injectionsCompletedInQueue         |


  @quarantine @ignore # returns 502 bad gateway html string
  Scenario Outline: Sample Queue invalid types of property values workflow
    When the sample queue data "<property_name>" is set with "<value>"
    Then the response status code is "502"

    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data does not match with registered sample queue data

    Examples:
      | property_name                      | value  |
      | sampleInjections.-1.injections     | "abcd" |
      | sampleInjections.-1.sampleLocation | 4      |
      | sampleInjections.-1.sampleVolumeUl | "abcd" |
      | samplesRemainingInSampleSet        | "abcd" |
      | samplesRemainingInQueue            | "abcd" |
      | injectionsRemainingInSampleSet     | "abcd" |
      | injectionsRemainingInQueue         | "abcd" |
      | additionalInfo                     | "abcd" |
      | timeRemainingInSampleSet           | "abcd" |
      | timeRemainingInQueue               | "abcd" |
      | injectionsCompletedInQueue         | "abcd" |


  @quarantine @ignore # returns 502 bad gateway html string
  Scenario Outline: Sample Queue additional property workflow
    When the sample queue data "<property_name>" is set with "<value>"
    Then the response status code is "502"

    When the sample queue data is requested
    Then the response status code is "200"
    And requested sample queue data does not match with registered sample queue data

    Examples:
      | property_name                        | value |
      | sampleInjections.-1.injectionpending | 2     |
      | injectionsCompleted                  | 2     |
