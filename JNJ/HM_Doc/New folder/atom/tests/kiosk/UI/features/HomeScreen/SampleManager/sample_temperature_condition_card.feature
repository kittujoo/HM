@kiosk @ALIST-228 @kiosk_sample_temperature_condition_card
Feature: Kiosk | Sample temperature condition card

  Background:
    Given Navigate to the sample temperature settings screen


  @real @weekly 
  Scenario Outline: To verify the condition card displays same temperature that was set by the user in the sample temperature setting screen
    Given Sample manager temperature was set as "<actual_temperature>"
    And The temperature is "<actual_temperature>"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "<expected_temperature>"
    And Tap the DONE button
    Then Validate the status changes to "SETPOINT REACHED"
    And Validate the temperature is "<expected_temperature>"
    When User navigates to home screen
    Then The user validates "<expected_temperature>" info in the sample manager card reader

    Examples:
      | actual_temperature | expected_temperature |
      | 8.0                | 12.0                 |
      | 13.0               | 17.0                 |


  @real @weekly 
  Scenario: To verify the condition card displays the correct temperature when the sample compartment is in cooling state
    Given Sample manager temperature was set as "17.0"
    And The temperature is "17.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "13.0"
    And Tap the DONE button
    Then Validate the status changes to "COOLING IS ON"
    And Validate the status changes to "SETPOINT REACHED"
    And Validate the temperature is "13.0"
    When User navigates to home screen
    Then The user validates "13.0" info in the sample manager card reader


  @real @weekly 
  Scenario: The temperature shown in the condition card remains the same when user taps the cancel button
    Given Sample manager temperature was set as "13.0"
    And The temperature is "13.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "40.0"
    And Tap the CANCEL button
    Then Validate the temperature is "13.0"


  @simulation @daily 
  Scenario: To validate the user cannot set the sample temperature when the temperature control is off

    When Tap the toggle button to turn off the temperature control
    Then Validate the user cannot set the temperature

  @real @weekly 
  Scenario: To validate the setpoint temperature is off when the toggle button is switched off
    When Tap the toggle button to turn off the temperature control
    And Tap the DONE button
    Then Validate the temperature setpoint is OFF


  @real @weekly 
  Scenario: To validate the user able to change the temperature when the current sample temperature is rising
    Given Sample manager temperature was set as "13.0"
    And The temperature is "13.0"
    When User navigate to the sample temperature settings screen
    When Set sample manager temperature as "20.0"
    And Tap the DONE button
    Then Validate the temperature is "16.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "22.0"
    And Tap the DONE button
    Then Validate the temperature is "22.0"
    When User navigates to home screen
    Then The user validates "22.0" info in the sample manager card reader


  @real @weekly 
  Scenario: To validate the user can switch off the toggle button when the temperature is rising
    Given Sample manager temperature was set as "22.0"
    And The temperature is "22.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "28.0"
    And Tap the DONE button
    Then Validate the temperature is "25.0"
    When User navigate to the sample temperature settings screen
    And Tap the toggle button to turn off the temperature control
    And Tap the DONE button
    Then Validate the temperature setpoint is OFF


  @simulation @weekly 
  Scenario: To validate the temperature edit field is not changed after turning sample temperature ON/OFF
    When Set sample manager temperature as "25.0"
    And Tap the DONE button
    Then Validate the temperature is "25.0"
    When User navigate to the sample temperature settings screen
    And Tap the toggle button to turn off the temperature control
    And Tap the toggle button to turn on the temperature control
    Then Validate the input "25.0" should not be affected by the hide/show of the edit field


  @real @weekly 
  Scenario Outline: To verify the temperature subtitle changes when the user makes a temperature selection

    When Set sample manager temperature as "<temperature_to_set>"
    Then User validates the temperature option is "<temperature_to_set>"
    Examples:
      | temperature_to_set |
      | 28.0               |
      | 38.0               |
      | 40.0               |
      | 15.0               |


  @real @weekly 
  Scenario: To validate the user able to change the temperature when the current sample temperature is decreasing
    When Set sample manager temperature as "25.0"
    And Tap the DONE button
    Then Validate the temperature is "25.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "20.0"
    And Tap the DONE button
    Then Validate the temperature is "22.0"
    When User navigate to the sample temperature settings screen
    And Set sample manager temperature as "28.0"
    And Tap the DONE button
    Then Validate the temperature is "28.0"
    When User navigates to home screen
    Then The user validates "28.0" info in the sample manager card reader


  @simulation @daily 
  Scenario: To validate the spinner component is stay loaded when the toggle button on

    When Tap the toggle button to turn on the temperature control
    And Tap the DONE button
    Then Validate the setpoint temperature is not OFF
    When User navigate to the sample temperature settings screen
    Then Validate the spinner component is visible
