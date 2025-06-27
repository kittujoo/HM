@kiosk @ALIST-228 @system_leak_test_feature
Feature: Kiosk | System Leak Test Workflow

  @real @weekly
  Scenario Outline: To validate the leak workflow when user abort it with end point as vent valve
    Given User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    Then User validates the welcome context in the welcome screen
    And User validates the better results text in the welcome screen
    When User navigates to the next screen
    And User selects "<solvent_line>", "<acc_pressure>", primary_pressure will be automatically set 2000 psi less than acc pressure, "<end_point>", "<prime_option>"
    Then User validates the summary details for the leak test
    When User aborts the leak test workflow after "<stop_time>" seconds
    Then User validates the status screen for the leak test

    Examples:
      | solvent_line | acc_pressure | end_point  | prime_option | stop_time |
      | C            | 5000         | Vent Valve | Prime        | 5         |
      | D            | 6500         | Vent Valve | Don't Prime  | 15        |


  @daily @weekly @manual @ignore
  Scenario Outline: To validate the leak workflow when user abort it with end point as column
    Given User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    Then User validates the welcome context in the welcome screen
    And User validates the better results text in the welcome screen
    When User navigates to the next screen
    And User selects "<solvent_line>", "<acc_pressure>", primary_pressure will be automatically set 2000 psi less than acc pressure, "<end_point>", "<prime_option>"
    And User navigates to the next screen
    Then User validates the summary details for the leak test
    When User aborts the leak test workflow after "<stop_time>" seconds
    Then User validates the status screen for the leak test

    Examples:
      | solvent_line | acc_pressure | end_point | prime_option | stop_time |
      | C            | 5000         | Column    | Prime        | 30        |
      | D            | 6500         | Column    | Don't Prime  | 15        |


  @real @daily
  Scenario Outline: To validate the System leak test workflow when user abort it
    Given User sets pre-required date and time format
    And User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    Then User validates the welcome context in the welcome screen
    And User validates the better results text in the welcome screen
    When User navigates to the next screen
    And User selects "<solvent_line>", "<acc_pressure>", primary_pressure will be automatically set 2000 psi less than acc pressure, "<end_point>", "<prime_option>"
    Then User validates the summary details for the leak test
    When User aborts the leak test workflow after "<stop_time>" seconds
    Then User validates the status screen for the leak test
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | solvent_line | acc_pressure | end_point  | prime_option | stop_time |
      | A            | 5000         | Vent Valve | Prime        | 60        |
      | B            | 9500         | Vent Valve | Don't Prime  | 5         |


  @simulation @daily
  Scenario Outline: To validate user cannot enter out of range pressure
    Given User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    And User navigates to the next screen
    And User navigates to the next screen
    And The user enters the "<enter_pressure>"
    Then Validate the pressure edit field shows "<error_state>"

    Examples:
      | enter_pressure | error_state |
      | 4999           | True        |
      | 10010          | True        |
      | 5001           | False       |
      | 9500           | False       |
      | 9501           | True        |


  @real @weekly
  Scenario Outline: To validate the complete success of the workflow
    Given User sets pre-required date and time format
    And User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    Then User validates the welcome context in the welcome screen
    And User validates the better results text in the welcome screen
    When User navigates to the next screen
    And User selects "<solvent_line>", "<acc_pressure>", primary_pressure will be automatically set 2000 psi less than acc pressure, "<end_point>", "<prime_option>"
    Then User validates the summary details for the leak test
    And User validates the result screen for "<acc_pressure>" and "<primary_pressure>": Leak rate (nL/min), Maximum pressure (psi), Final Stroke (%), Compression attempts
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | solvent_line | acc_pressure | primary_pressure | end_point  | prime_option |
      | A            | 5000         | 3000             | Vent Valve | Prime        |
      | B            | 6000         | 4000             | Vent Valve | Don't Prime  |


  @real @daily
  Scenario Outline: To validate the System leak test workflow completes
    Given User sets pre-required date and time format
    And User navigates the troubleshoot tab
    When User navigates to the welcome screen in leak test workflow
    Then User validates the welcome context in the welcome screen
    And User validates the better results text in the welcome screen
    When User navigates to the next screen
    And User selects "<solvent_line>", "<acc_pressure>", primary_pressure will be automatically set 2000 psi less than acc pressure, "<end_point>", "<prime_option>"
    Then User validates the summary details for the leak test
    And User validates the result screen for "<acc_pressure>" and "<primary_pressure>": Leak rate (nL/min), Maximum pressure (psi), Final Stroke (%), Compression attempts
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | solvent_line | acc_pressure | primary_pressure | end_point  | prime_option |
      | C            | 6000         | 4000             | Vent Valve | Don't Prime  |
