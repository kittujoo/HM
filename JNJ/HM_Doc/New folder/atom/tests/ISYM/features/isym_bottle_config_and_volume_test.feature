  """
  Desc: Feature to validate ISYM bottle configuration and volume workflow.
  """

@isym @isym_bottle_config_and_volume_feature
Feature: iSym | Bottle Configuration and Volume Workflow

  Background:
    Given the system state is Idle


  @isym_workflows_completion @isym_bottle_config
  Scenario: Bottle configuration
    When bottle configuration is sent
    Then bottle configuration is as expected
    And the response status code is "200"


  @isym_workflows_completion @isym_bottle_config_non_default
  Scenario: Bottle configuration non-default properties
    When bottle configuration is sent with non-default properties
    Then bottle configuration is as expected
    And the response status code is "200"


      #ALIST-104 - allows for missing properties instead of rejecting the request
  @isym_workflows_completion @isym_bottle_config_missing_required_property @quarantine
  Scenario Outline: Bottle configuration missing required property
    When bottle configuration is sent with the property "<property_name>" missing
    Then the response status code is "500"

    Examples:
      | property_name                                 |
      | solventBottle.0.id                            |
      | solventBottle.0.displayName                   |
      | solventBottle.0.solventType.id                |
      | solventBottle.0.solventType.name              |
      | solventBottle.0.sizeMl                        |
      | solventBottle.0.lowVolumeWarningLevelMl       |
      | solventBottle.0.raiseLowVolumeWarning         |
      | solventBottle.0.lowVolumeErrorLevelMl         |
      | solventBottle.0.raiseLowVolumeError           |
      | solventBottle.0.solventExpirationDate         |
      | solventBottle.0.raiseSolventExpirationWarning |
      | solventBottle.0.raiseSolventExpirationError   |
      | solventBottle.0.solventLines.0                |


      #ALIST-104 - allows for missing values instead of rejecting the request
  @isym_workflows_completion @isym_bottle_config_missing_values @quarantine
  Scenario Outline: Bottle configuration missing values
    When bottle configuration is sent with "<property_name>" missing its value
    Then the response status code is "500"

    Examples:
      | property_name                                 |
      | solventBottle.0.id                            |
      | solventBottle.0.displayName                   |
      | solventBottle.0.solventType.id                |
      | solventBottle.0.solventType.name              |
      | solventBottle.0.sizeMl                        |
      | solventBottle.0.lowVolumeWarningLevelMl       |
      | solventBottle.0.raiseLowVolumeWarning         |
      | solventBottle.0.lowVolumeErrorLevelMl         |
      | solventBottle.0.raiseLowVolumeError           |
      | solventBottle.0.solventExpirationDate         |
      | solventBottle.0.raiseSolventExpirationWarning |
      | solventBottle.0.raiseSolventExpirationError   |
      | solventBottle.0.solventLines.0                |


  @isym_workflows_completion @isym_bottle_config_boundary_values
  Scenario Outline: Bottle configuration using minimum and maximum values
    When bottle configuration is sent with "<property_name>" = "<value>" property
    Then bottle configuration is as expected
    And the response status code is "200"

    Examples:
      | property_name                           | value |
      | solventBottle.0.sizeMl                  | 0     |
      | solventBottle.0.sizeMl                  | 99999 |
      | solventBottle.0.lowVolumeWarningLevelMl | 0     |
      | solventBottle.0.lowVolumeWarningLevelMl | 99999 |
      | solventBottle.0.lowVolumeErrorLevelMl   | 0     |
      | solventBottle.0.lowVolumeErrorLevelMl   | 99999 |


      #ALIST-104 - allows for values to be above max, limit for sizeMl, lowVolumeWarningMl, and highVolumeWarningMl is 99999 but accepts 100000
  @isym_workflows_completion @isym_bottle_config_out_of_boundary_values @quarantine
  Scenario Outline: Bottle configuration using below minimum and above maximum values
    When bottle configuration is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                           | value  |
      | solventBottle.0.sizeMl                  | -1     |
      | solventBottle.0.sizeMl                  | 100000 |
      | solventBottle.0.lowVolumeWarningLevelMl | -1     |
      | solventBottle.0.lowVolumeWarningLevelMl | 100000 |
      | solventBottle.0.lowVolumeErrorLevelMl   | -1     |
      | solventBottle.0.lowVolumeErrorLevelMl   | 100000 |


  @isym_workflows_completion @isym_bottle_config_invalid_types
  Scenario Outline: Bottle configuration using invalid types
    When bottle configuration is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                                 | value           |
      | solventBottle.0.id                            | 1               |
      | solventBottle.0.displayName                   | 1               |
      | solventBottle.0.solventType.id                | 1               |
      | solventBottle.0.solventType.name              | 1               |
      | solventBottle.0.sizeMl                        | test            |
      | solventBottle.0.lowVolumeWarningLevelMl       | test            |
      | solventBottle.0.raiseLowVolumeWarning         | test            |
      | solventBottle.0.lowVolumeErrorLevelMl         | test            |
      | solventBottle.0.raiseLowVolumeError           | test            |
      | solventBottle.0.solventExpirationDate         | 1               |
      | solventBottle.0.raiseSolventExpirationWarning | test            |
      | solventBottle.0.raiseSolventExpirationError   | test            |
      | solventBottle.0.solventLines.0                | SolventLine_XYZ |


  @isym_workflows_completion @isym_bottle_config_additional_property
  Scenario Outline: Bottle configuration with additional property
    When bottle configuration is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                      | value           |
      | solventBottle.0.additionalProperty | additionalValue |


  @isym_workflows_completion @isym_bottle_volume
  Scenario: Bottle volume setting
    Given bottle is configured
    When bottle volume is sent
    Then bottle volume is as expected
    And the response status code is "200"


  @isym_workflows_completion @isym_bottle_volume_non_default
  Scenario: Bottle volume setting with non-default properties
    Given bottle is configured with non-default properties
    When bottle volume is sent with non-default properties
    Then bottle volume is as expected
    And the response status code is "200"


      #ALIST-104 - allows for missing properties instead of rejecting the request
  @isym_workflows_completion @isym_bottle_volume_missing_required_property @quarantine
  Scenario Outline: Bottle volume setting missing required property
    Given bottle is configured
    When bottle volume is sent with the property "<property_name>" missing
    Then the response status code is "500"

    Examples:
      | property_name                  |
      | solventBottleVolume.0.id       |
      | solventBottleVolume.0.volumeMl |


      #ALIST-104 - allows for missing values instead of rejecting the request
  @isym_workflows_completion @isym_bottle_volume_missing_values @quarantine
  Scenario Outline: Bottle volume setting missing values
    Given bottle is configured
    When bottle volume is sent with "<property_name>" missing its value
    Then the response status code is "500"

    Examples:
      | property_name                  |
      | solventBottleVolume.0.id       |
      | solventBottleVolume.0.volumeMl |


  @isym_workflows_completion @isym_bottle_volume_boundary_values
  Scenario Outline: Bottle volume using minimum and maximum values
    Given bottle is configured
    When bottle volume is sent with "<property_name>" = "<value>" property
    Then bottle volume is as expected
    And the response status code is "200"

    Examples:
      | property_name                  | value |
      | solventBottleVolume.0.volumeMl | 0     |
      | solventBottleVolume.0.volumeMl | 99999 |


      #ALIST-104 - allows for values to be above max, limit for volumeMl is 99999 but accepts 100000
  @isym_workflows_completion @isym_bottle_volume_out_of_boundary_values @quarantine
  Scenario Outline: Bottle volume setting using below minimum and above maximum values
    Given bottle is configured
    When bottle volume is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                  | value  |
      | solventBottleVolume.0.volumeMl | -1     |
      | solventBottleVolume.0.volumeMl | 100000 |


  @isym_workflows_completion @isym_bottle_volume_invalid_types
  Scenario Outline: Bottle volume setting using invalid types
    Given bottle is configured
    When bottle volume is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                  | value |
      | solventBottleVolume.0.id       | 1     |
      | solventBottleVolume.0.volumeMl | test  |


  @isym_workflows_completion @isym_bottle_volume_additional_property
  Scenario Outline: Bottle volume setting with additional property
    Given bottle is configured
    When bottle volume is sent with "<property_name>" = "<value>" property
    Then the response status code is "500"

    Examples:
      | property_name                            | value           |
      | solventBottleVolume.0.additionalProperty | additionalValue |
