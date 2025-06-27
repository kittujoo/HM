@system @ALIST-231 @system_pressure_consistency_feature
Feature: System | Pressure value workflow

  @real_or_simulation @daily @new @ignore
  Scenario Outline: Pressure value are updated correctly across all applications when flow is started from Console
    When user start "<flow>" flow from Console
    Then user confirms the "<pressure_value>" with "<tolerance>" for system pressure in Console
    And user confirms the "<pressure_value>" with "<tolerance>" for system pressure in Control panel
    And User confirms the "<pressure_value>" with "<tolerance>" for system pressure in Kiosk

    Examples:
      | flow | pressure_value | tolerance |
      | 1.0  | 1556           | 10        |


  @real_or_simulation @daily @new @ignore
  Scenario Outline: Pressure value are updated correctly across all applications when flow is setting from Kiosk app
    When user start "<flow>" flow from kiosk - Home - Solvent Bottle - Flow condition card
    Then user confirms the "<pressure_value>" with "<tolerance>" for system pressure in Console
    And user confirms the "<pressure_value>" with "<tolerance>" for system pressure in Control panel
    And User confirms the "<pressure_value>" with "<tolerance>" for system pressure in Kiosk

    Examples:
      | flow | pressure_value | tolerance |
      | 1.8  | 2820           | 10        |