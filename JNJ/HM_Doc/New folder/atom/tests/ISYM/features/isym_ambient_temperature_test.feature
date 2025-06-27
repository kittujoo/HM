  """
  Desc: Feature to validate ISYM Ambient Temperature Test.
  """

@isym @isym_ambient_temperature_feature
Feature: iSym | Ambient Temperature Test

  Scenario: Retrieve Ambient Temperature
    When the system ambient temperature is requested
    Then the current ambient temperature in Celsius degrees is returned
