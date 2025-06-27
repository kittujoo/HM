@kiosk @ALIST-228 @kiosk_column_temperature_condition_card_feature
Feature: Kiosk | Column temperature condition card


  Background:
    Given Navigate to the column temperature setting screen

  @simulation @weekly
  Scenario Outline:  To verify the condition card displays same temperature that was set by the user in the column temperature setting screen
    Given Column manager temperature was set as "<actual_temperature>"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "<expected_temperature>"
    And User taps the DONE button
    Then Validate the status changes to "SETPOINT REACHED"
    And Validate the temperature is "<expected_temperature>"
    When User navigates to home screen
    Then The user validates "<expected_temperature>" info in the column manager card reader

    Examples:
      | actual_temperature | expected_temperature |
      | 4                  | 6                    |
      | 6                  | 8                    |
      | 8                  | 10                   |
      | 10                 | 13                   |


  @real @weekly
  Scenario: The temperature shown in the condition card remains the same when user taps the cancel button
    Given Column manager temperature was set as "13"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "15"
    And Tap the CANCEL button
    Then Validate the temperature is "13"

  @simulation @weekly
  Scenario: To validate the user cannot set the column temperature when the temperature control is off

    When User taps the toggle button to turn off the temperature control
    Then User validates the user cannot set the temperature


  @simulation @weekly
  Scenario: To validate the setpoint temperature is off when the toggle button is switched off
    When User taps the toggle button to turn off the temperature control
    And User taps the DONE button
    Then Validate the temperature setpoint is OFF

  @simulation @weekly
  Scenario: To validate the user able to change the temperature when the current column temperature is rising
    Given Column manager temperature was set as "13"
    When Navigate to the column temperature setting screen
    When Set column manager temperature as "18"
    And User taps the DONE button
    Then Validate the temperature is "16"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "20"
    And User taps the DONE button
    Then Validate the temperature is "20"
    When User navigates to home screen
    Then The user validates "20" info in the column manager card reader

  @simulation @weekly
  Scenario: To validate the user able to change the temperature when the current column temperature is decreasing
    When Set column manager temperature as "20"
    And User taps the DONE button
    Then Validate the temperature is "20"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "15"
    And User taps the DONE button
    Then Validate the temperature is "17"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "20"
    And User taps the DONE button
    Then Validate the temperature is "20"
    When User navigates to home screen
    Then The user validates "20" info in the column manager card reader

  @simulation @weekly
  Scenario: To validate the user can switch off the toggle button when the temperature is rising
    Given Column manager temperature was set as "20"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "28"
    And User taps the DONE button
    Then Validate the temperature is "23"
    When Navigate to the column temperature setting screen
    And User taps the toggle button to turn off the temperature control
    And User taps the DONE button
    Then Validate the temperature setpoint is OFF

  @simulation @weekly
  Scenario: To validate the user can switch off the toggle button when the temperature is decreasing
    Given Column manager temperature was set as "23"
    When Navigate to the column temperature setting screen
    And Set column manager temperature as "15"
    And User taps the DONE button
    Then Validate the temperature is "18"
    When Navigate to the column temperature setting screen
    And User taps the toggle button to turn off the temperature control
    And User taps the DONE button
    Then Validate the temperature setpoint is OFF


  @simulation @weekly
  Scenario: To validate the spinner component is stay loaded when the toggle button on
    When User taps the toggle button to turn on the temperature control
    And User taps the DONE button
    Then Validate the setpoint temperature is not OFF
    When Navigate to the column temperature setting screen
    Then Validate the spinner component is visible
