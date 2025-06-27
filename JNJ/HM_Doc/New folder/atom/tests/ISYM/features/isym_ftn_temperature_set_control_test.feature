  """
  Desc: Feature to validate ISYM FTN temperature set/control Test.
  """

@isym @isym_ftn_temp_set_control_feature
Feature: iSym | FTN temperature set/control test

  @isym_workflows_valid_payload
  Scenario Outline: FTN thermal control can be changed with valid values
    Given the FTN thermal control state is "<initial_state>"
    When the FTN thermal control state is changed to "<new_state>"
    Then the FTN thermal control state updates to "<new_state>"

    Examples:
      | initial_state           | new_state               |
      | ThermalControlState_ON  | ThermalControlState_OFF |
      | ThermalControlState_OFF | ThermalControlState_ON  |


  @isym_workflows_invalid_payload
  Scenario Outline: FTN thermal control can't be changed with invalid values
    Given the FTN thermal control state is "<initial_state>"
    When the FTN thermal control state is changed to "<new_state>"
    Then the response status code is "500"

    Examples:
      | initial_state           | new_state                   |
      | ThermalControlState_ON  | Thermal_State_ON            |
      | ThermalControlState_ON  | 10000                       |
      | ThermalControlState_OFF | ThermalControlState_ILLEGAL |


  @isym_workflows_invalid_payload
  Scenario: FTN thermal control can't be changed with property removed
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN thermal control state is changed with property thermalControlState removed
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: FTN thermal control can't be changed with additional property
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN thermal control is changed with additional property "targetABCD" and value "10000"
    Then the response status code is "500"


  @isym_workflows_valid_payload
  Scenario Outline: FTN temperature can be changed with valid values
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is changed to "<temperature>"
    Then the FTN sample temperature updates to "<temperature>" degrees

    Examples:
      | temperature |
      | 4.0         | # minimum
      | 20.0        | # intermediate
      | 40.0        | # maximum


  @isym_workflows_valid_payload
  Scenario: FTN temperature can be increased
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is increased by 2.0 degrees
    Then the FTN sample temperature updates to the changed value


  @isym_workflows_valid_payload
  Scenario: FTN temperature can be decreased
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is decreased by 2.0 degrees
    Then the FTN sample temperature updates to the changed value


  @isym_workflows_invalid_payload
  Scenario Outline: FTN temperature can't be changed with invalid values
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is changed to "<temperature>"
    Then the response status code is "500"

    Examples:
      | temperature |
      | 3.9         | # below_minimum
      | 40.1        | # above_maximum


  @isym_workflows_invalid_payload
  Scenario: FTN temperature can't be changed with property removed
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is changed with property targetTemperatureDegC removed
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: FTN temperature can't be changed with additional property
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is changed with additional property "thermal_ABCD" and value "10000"
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: FTN temperature can't be changed with string values
    Given the FTN thermal control state is "ThermalControlState_ON"
    When the FTN sample temperature is changed with string "ABCDEFG"
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: FTN temperature can't be changed with thermal state off
    Given the FTN thermal control state is "ThermalControlState_OFF"
    When the FTN sample temperature is changed to "30.0"
    Then the FTN sample temperature should not update to given degrees
