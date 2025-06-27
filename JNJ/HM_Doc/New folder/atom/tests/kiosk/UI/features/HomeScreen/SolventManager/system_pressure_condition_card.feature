@kiosk @ALIST-228 @system_pressure_condition_card
Feature: Kiosk | System pressure condition card


  Background:
    Given User navigates to the system pressure settings screen


  @simulation @weekly
  Scenario Outline: To verify that when the pressure unit is changed, all display locations are changed to that unit/value
    When User changes the unit to "<system_pressure_unit>"
    And User confirms the unit change
    Then User validates "<expected_system_pressure_unit>" in the system pressure conditional card
    And User validates "<expected_system_pressure_unit>" in the solvent manager card reader
    And User validates the "<expected_system_pressure_unit>" in the system leak test
    And User validates the "<expected_system_pressure_unit>" in the sample metering pump leak test
    And User validates the "<expected_system_pressure_unit>" in the needle seal readiness test
    And User validates the "<expected_system_pressure_unit>" in the system settings

    Examples:
      | system_pressure_unit | expected_system_pressure_unit |
      | bar                  | bar                           |
      | kPa                  | kPa                           |
      | MPa                  | MPa                           |


  @real @weekly
  Scenario Outline: To verify that when the pressure unit psi is changed, all display locations are changed to that psi unit/value
    When User changes the unit to "<system_pressure_unit>"
    And User confirms the unit change
    Then User validates "<expected_system_pressure_unit>" in the system pressure conditional card
    And User validates "<expected_system_pressure_unit>" in the solvent manager card reader
    And User validates the "<expected_system_pressure_unit>" in the system leak test
    And User validates the "<expected_system_pressure_unit>" in the sample metering pump leak test
    And User validates the "<expected_system_pressure_unit>" in the needle seal readiness test
    And User validates the "<expected_system_pressure_unit>" in the system settings

    Examples:
      | system_pressure_unit | expected_system_pressure_unit |
      | psi                  | psi                           |



  @simulation @weekly
  Scenario Outline: To verify when the pressure unit is changed but cancelled, all display locations of unit/value are unchanged
    When User changes the unit to "psi"
    And User confirms the unit change
    And User goes back to the system pressure settings screen
    And User checks the currently selected unit
    And User changes the unit to "bar"
    And User cancels the unit change
    Then User validates "<expected_system_pressure_unit>" in the system pressure conditional card
    And User validates "<expected_system_pressure_unit>" in the solvent manager card reader
    And User validates the "<expected_system_pressure_unit>" in the system leak test
    And User validates the "<expected_system_pressure_unit>" in the sample metering pump leak test
    And User validates the "<expected_system_pressure_unit>" in the needle seal readiness test
    And User validates the "<expected_system_pressure_unit>" in the system settings

    Examples:
      | expected_system_pressure_unit |
      | psi                           |
