@kiosk @ALIST-228 @kiosk_sample_metering_pump_feature
Feature: Kiosk | Sample Metering Pump Workflow functionality

  @simulation @weekly
  Scenario: To validate the sample metering pump workflow welcome screen
    Given User navigates to sample manager section within health troubleshoot area
    When User taps sample metering pump leak test start panel
    Then User validates welcome context in the welcome screen


  @simulation @daily
  Scenario Outline: To validate the target pressure edit field validation
    Given User navigates to sample manager section within health troubleshoot area
    When User taps sample metering pump leak test start panel
    And User navigates to the target pressure screen
    And User enters the "<pressure_value>" details
    Then User validates the "<error_state>"

    Examples:
      | pressure_value | error_state |
      | 100            | False       |
      | 500            | False       |
      | 10000          | False       |
      | 99             | True        |
      | 10001          | True        |


  @real @weekly
  Scenario Outline: To validate the screens and features within the sample metering pump workflow
    Given User sets pre-required date and time format
    And User navigates to sample manager section within health troubleshoot area
    When User taps sample metering pump leak test start panel
    And User taps next
    And User enters the solvent details "<line_1>", "<line_2>", "<line_3>", "<line_4>" for Setup
    Then User validates the total composition is "<total_composition>"
    When User taps next
    And User enters the "<pressure_value>" details
    And User chooses the prime "<toggle_position>"
    Then User validates the summary screen details for "<line_1>", "<line_2>", "<line_3>", "<line_4>", "<toggle_position>" and "<pressure_value>"
    When User taps start
    Then User verifies the results screen details with optional leak rate in uL/min
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | line_1    | line_2     | line_3    | line_4    | total_composition | toggle_position | pressure_value |
      | A,True,25 | B,True,25  | C,True,25 | D,True,25 | 100.0             | True            | 10000          |
      | A,True,45 | B,True,20  | C,False,0 | D,True,35 | 100.0             | True            | 5000           |
      | A,True,25 | B,False,25 | C,True,25 | D,True,25 | 100.0             | False           | 500            |
      

  @real @daily
  Scenario Outline: To validate the screens and features within the sample metering pump workflow
    Given User sets pre-required date and time format
    And User navigates to sample manager section within health troubleshoot area
    When User taps sample metering pump leak test start panel
    And User taps next
    And User enters the solvent details "<line_1>", "<line_2>", "<line_3>", "<line_4>" for Setup
    Then User validates the total composition is "<total_composition>"
    When User taps next
    And User enters the "<pressure_value>" details
    And User chooses the prime "<toggle_position>"
    Then User validates the summary screen details for "<line_1>", "<line_2>", "<line_3>", "<line_4>", "<toggle_position>" and "<pressure_value>"
    When User taps start
    Then User verifies the results screen details with optional leak rate in uL/min
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | line_1    | line_2     | line_3    | line_4    | total_composition | toggle_position | pressure_value |      
      | A,True,45 | B,True,20  | C,False,0 | D,True,35 | 100.0             | False           | 2500           |


  @real @weekly
  Scenario Outline: To validate the process of terminating the workflow
    Given User sets pre-required date and time format
    And User navigates to sample manager section within health troubleshoot area
    When User taps sample metering pump leak test start panel
    And User taps next
    And User enters the solvent details "<line_1>", "<line_2>", "<line_3>", "<line_4>" for Setup
    And User taps next
    And User chooses the prime "<toggle_position>"
    And User starts and then aborts the sample metering pump workflow at different "<stop_time>"
    Then User validates status screen after aborting
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | line_1    | line_2    | line_3    | line_4    | toggle_position | stop_time |
      | A,True,25 | B,True,25 | C,True,25 | D,True,25 | False           | 10        |
      | A,True,25 | B,True,25 | C,True,25 | D,True,25 | False           | 30        |
      | A,True,25 | B,True,25 | C,True,25 | D,True,25 | True            | 10        |
      | A,True,25 | B,True,25 | C,True,25 | D,True,25 | True            | 120       |
