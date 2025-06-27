  """
  Desc: Feature to validate ISYM Column Temperature Set/Control Test.
  """

@isym @isym_column_temp_set_control_feature
Feature: iSym | Column Temperature Set/Control Test

  @isym_workflows_completion
  Scenario Outline: Column thermal control can be changed with valid values
    Given the column thermal control state is "<initial_state>"
    When the column thermal control state is changed to "<new_state>"
    Then the column thermal control state updates to "<new_state>"

    Examples:
      | initial_state           | new_state               |
      | ThermalControlState_ON  | ThermalControlState_OFF |
      | ThermalControlState_OFF | ThermalControlState_ON  |


  @isym_workflows_invalid_payload
  Scenario Outline: Column thermal control can't be changed with invalid values
    Given the column thermal control state is "<initial_state>"
    When the column thermal control state is changed to "<new_state>"
    Then the response status code is "500"

    Examples:
      | initial_state           | new_state                   |
      | ThermalControlState_ON  | Thermal_State_ON            |
      | ThermalControlState_ON  | 10000                       |
      | ThermalControlState_OFF | ThermalControlState_ILLEGAL |


  @isym_workflows_invalid_payload
  Scenario: Column thermal control can't be changed with property removed
    Given the column thermal control state is "ThermalControlState_ON"
    When the column thermal control state is changed with property thermalControlState removed
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: Column thermal control can't be changed with additional property
    Given the column thermal control state is "ThermalControlState_ON"
    When the column thermal control is changed with additional property "targetABCD" and value "10000"
    Then the response status code is "500"


  @isym_workflows_valid_payload
  Scenario Outline: Column temperature can be changed with valid values
    Given the column thermal control state is "ThermalControlState_ON"
    When the column target temperature is set to "<temperature>"
    Then the column current temperature updates to "<temperature>" degrees

    Examples:
      | temperature |
      # minimum
      | 4.0         |
      # intermediate
      | 50.0        |
      # maximum
      | 90.0        |


  @isym_workflows_valid_payload
  Scenario: Column temperature can be increased
    Given the column thermal control state is "ThermalControlState_ON"
    When the target temperature is increased by 2.0 degrees
    Then the target temperature updates to the changed value


  @isym_workflows_valid_payload
  Scenario: Column temperature can be decreased
    Given the column thermal control state is "ThermalControlState_ON"
    When the target temperature is decreased by 2.0 degrees
    Then the target temperature updates to the changed value


  @isym_workflows_invalid_payload
  Scenario Outline: Column temperature can't be changed with invalid values
    Given the column thermal control state is "ThermalControlState_ON"
    When the column target temperature is set to "<temperature>"
    Then the response status code is "500"

    Examples:
      | temperature |
      # below_minimum
      | 3.9         |
      # above_maximum
      | 90.1        |


  @isym_workflows_invalid_payload
  Scenario: Column temperature can't be changed with property removed
    Given the column thermal control state is "ThermalControlState_ON"
    When the target temperature is changed with property targetTemperatureDegC removed
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: Column temperature can't be changed with additional property
    Given the column thermal control state is "ThermalControlState_ON"
    When the target temperature is changed with additional property "thermal_ABCD" and value "10000"
    Then the response status code is "500"


  @isym_workflows_invalid_payload
  Scenario: Column temperature can't be changed with string values
    Given the column thermal control state is "ThermalControlState_ON"
    When column set target temperature request sent with "targetTemperatureDegC" = "ABCDEFG"
    Then the response status code is "500"


  @isym_workflows_valid_payload
  Scenario Outline: Column temperature can't be changed with thermal state off
    Given the column thermal control state is "ThermalControlState_OFF"
    When the column target temperature is set to "<temperature>"
    Then the current temperature should not update to given degrees
    Examples:
      | temperature |
      | 30.0        |

