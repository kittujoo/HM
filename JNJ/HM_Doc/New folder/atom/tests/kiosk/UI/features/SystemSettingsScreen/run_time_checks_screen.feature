@kiosk @ALIST-228 @run_time_checks_feature @weekly
Feature: Kiosk | run time checks settings screen


  Background:
    Given User navigates to system screen
    And User navigates to the Solvents system settings


  @simulation
  Scenario: To verify the default settings for toggle buttons
    When User configures the mobile phase and wash solvent
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    Then User validates the status of the mobile phase, wash solvent, leak detected, and vial missing toggles
    And User validates leak is detected and vial is missing toggle buttons are not editable
    And User validates the low solvent limits is 10%


  @simulation
  Scenario: To verify when all mobile phases are not configured, the mobile phase toggle button is not editable
    When User unconfigures all Mobile Phase solvent lines
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    Then User validates the mobile phase toggle button is disabled and not editable


  @real
  Scenario Outline: To verify when at least one mobile phase is configured, the mobile phase toggle button is editable
    When User configures "<solvent_line_a_toggle>", "<solvent_line_b_toggle>", "<solvent_line_c_toggle>", "<solvent_line_d_toggle>" Mobile Phase solvent lines
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    Then User validates the mobile phase toggle button is enabled

    Examples:
      | solvent_line_a_toggle | solvent_line_b_toggle | solvent_line_c_toggle | solvent_line_d_toggle |
      | True                  | False                 | False                 | False                 |
      | True                  | True                  | False                 | False                 |
      | True                  | True                  | True                  | False                 |
      | True                  | True                  | True                  | True                  |


  @simulation
  Scenario: To verify Done saves the changes
    When User configures the mobile phase and wash solvent
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    And User sets the mobile phase and wash solvent toggles to the opposite configuration
    And User confirms the changes
    And User navigates to Run Time Checks tab
    Then User confirms the mobile phase and wash solvent toggle button changes did save


  @simulation
  Scenario: To verify when data is changed but canceled, the changes are not saved
    When User configures the mobile phase and wash solvent
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    And User sets the mobile phase and wash solvent toggles to the opposite configuration
    And User cancels the changes
    And User navigates to Run Time Checks tab
    Then User confirms the mobile phase and wash solvent toggle button changes did not save


  @simulation
  Scenario: To verify when wash solvent level is low, the wash solvent toggle button is not editable
    When User unconfigures the seal wash and needle wash
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    Then User validates wash solvent toggle button is disabled and not editable


  @real
  Scenario Outline: To verify when the seal wash and/or needle wash is/are configured, the wash solvent toggle button is editable
    When User configures "<seal_wash_toggle>" and "<needle_wash_toggle>"
    And User navigates to the Administration tab
    And User navigates to the Acquisition checks tab
    And User navigates to Run Time Checks tab
    Then User validates the wash solvent toggle button is enabled

    Examples:
      | seal_wash_toggle | needle_wash_toggle |
      | True             | False              |
      | False            | True               |
      | True             | True               |
