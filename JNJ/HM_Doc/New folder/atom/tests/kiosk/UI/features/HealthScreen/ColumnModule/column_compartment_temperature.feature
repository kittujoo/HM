@kiosk @ALIST-228 @columnTest
Feature: Kiosk | Column Compartment Temperature Test Workflow functionality

  Background:
    Given User sets pre-required date and time format
    And User navigates to column section within health troubleshoot area
    When User taps column compartment temperature test panel


  @real @weekly
  Scenario: To validate the screens and features within the column compartment temperature test workflow when the door is closed
    Then User validates the welcome context in the welcome screen
    And User validates the preconditions
    And User validates the Next button is disabled
    When User checks the confirmation check box
    Then User confirms the Next button is enabled
    When User validates the summary screen information
    And User taps Start
    Then User validates the column compartment temperature test process
    And User validates the results screen information with ambient temperature, target temperature and measured temperature
    And User validates the test passes if the measured change is greater than 6 degree Celsius
    When User enters the log screen
    Then User verifies the column compartment temperature test log is generated


  @real @weekly
  Scenario: To validate the column compartment temperature workflow aborts successfully
    When User validates the preconditions
    And User validates the summary screen information
    And User aborts the column compartment temperature workflow after 3 seconds
    Then User validates the status stopped for the column compartment temperature workflow
    When User enters the log screen
    Then User verifies the column compartment temperature test log is generated


  @monthly  @manual @ignore
  Scenario: To validate the screens and features within the column compartment temperature test workflow when the door is open
    Then User validates the welcome context in the welcome screen
    And User open the compartment door
    And User validates the status of compartment door precondition is open
    And User validates the Next and Start buttons are disabled
