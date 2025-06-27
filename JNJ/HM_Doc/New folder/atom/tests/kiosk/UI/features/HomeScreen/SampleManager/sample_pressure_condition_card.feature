@kiosk @ALIST-228
Feature: Kiosk | Sample pressure condition card

  Background:
    Given User navigates to the sample pressure settings screen


  @real @daily
  Scenario Outline: To verify that when the pressure unit is changed, all display locations are changed to that unit/value

    When User changes the unit to "<sample_pressure_unit>"
    And  User confirms the unit change
    Then User validates "<expected_pressure_unit>" in the sample pressure conditional card
    And  User validates "<expected_pressure_unit>" info in the sample manager card reader

    Examples:
      | sample_pressure_unit | expected_pressure_unit |
      | bar                  | bar                    |
      | kPa                  | kPa                    |
      | psi                  | psi                    |
      | MPa                  | MPa                    |


  @real @daily
  Scenario: To verify when the pressure unit is changed but cancelled, all display locations of unit/value are unchanged

    When User changes the unit to "psi"
    And User confirms the unit change
    And User goes back to the sample pressure settings screen
    And User checks the currently selected unit
    And User changes the unit to "bar"
    And User cancels the unit change
    Then User validates "psi" in the sample pressure conditional card

    