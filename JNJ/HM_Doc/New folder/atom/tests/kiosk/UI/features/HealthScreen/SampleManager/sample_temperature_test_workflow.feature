@kiosk @ALIST-228 @sampleTempTest
Feature: Kiosk | Sample Temperature Test Workflow functionality

  Background:
    Given User sets pre-required date and time format
    And User navigates to sample manager section within health troubleshoot area
    When User taps sample temperature test panel


  @real @weekly
  Scenario: To validate the screens and features within the sample temperature test workflow when the door is closed
    Then User validates the welcome context in the welcome screen
    And User validates the preconditions
    And User validates the Next button is disabled
    When User checks the confirmation check box
    Then User confirms the Next button is enabled
    When User taps Next button
    Then User validates the summary screen information
    When User taps Start
    Then User validates the sample temperature test process
    And User validates the results screen information with ambient temperature, target temperature and measured temperature
    And User validates the test passes if the measured change is greater than 2C
    When User enters the log screen
    Then User verifies the sample temperature test log is generated


  @real @weekly
  Scenario: To validate the sample temperature workflow aborts successfully
    When User taps Next button
    And User validates the preconditions
    And User validates the summary screen information
    And User aborts the sample temperature workflow after 3 seconds
    Then User validates the status stopped for the sample temperature workflow
    When User enters the log screen
    Then User verifies the sample temperature test log is generated


  @monthly @manual @ignore
  Scenario: To validate the screens and features within the sample temperature test workflow when the door is open
    Then User validates the welcome context in the welcome screen
    And User open the compartment door
    And User validates the status of compartment door precondition is open
    And User validates the Next and Start buttons are disabled


