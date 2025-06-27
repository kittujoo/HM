@kiosk @ALIST-228 @kiosk_column_condition_card_feature
Feature: Kiosk | Column condition card

  Background:
    Given Navigate to the column settings screen


  Scenario Outline: To verify the edit field is visible depending on toggle state

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    Then The user validate the injection count edit field is "<edit_field_displayed_state>"

    Examples:
      | warning_toggle_button_state | edit_field_displayed_state |
      | True                        | True                       |
      | False                       | False                      |


  Scenario Outline: To verify the maximum temperature button is enabled when the temperature set is less than 90 degree celcius

    When The user navigates to the temperature control screen
    And The user sets the maximum warning temperature as "<maximum_warning_temperature>"
    Then Validate the enabled state of the maximum temperature button "<is_button_disabled>"

    Examples:
      | maximum_warning_temperature | is_button_disabled |
      | 88.0                        | False              |
#      | 87.0                        | False              |
#      | 90.0                        | True               |


  Scenario Outline: To verify the user not able to navigate to the condition card when an out of range injection count is entered and "Done" button is tapped

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as "<monitor_injection_count>"
    Then The user validates the done button is disabled
    And Validate the injection count  edit field shows "<error_state>"

    Examples:
      | warning_toggle_button_state | monitor_injection_count | error_state |
      | True                        |                         | True        |
      | True                        | 10001                   | True        |
      | True                        | 0                       | True        |


  Scenario Outline: To verify monitor injection count info is not updated when the user taps the cancel button

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as 300
    And The user navigates to the temperature control screen
    And The user sets the maximum warning temperature as "<maximum_warning_temperature>"
    And The user confirms the monitor injection count
    And Navigate to the column settings screen
    And User validates the monitor injection count as "<expected_monitor_injection_count>"
    And Navigate to the column settings screen
    And The user navigates to the temperature control screen
    And User validates the maximum temperature as 85
    And The user confirms the monitor injection count
    And The user navigates to the monitor injection count settings screen
    And The user enter the monitor injection count as 200
    And The user navigates to the temperature control screen
    And The user sets the maximum warning temperature as 75.0
    And The user cancels the monitor injection count
    And Navigate to the column settings screen
    Then User validates the monitor injection count as "<expected_monitor_injection_count>"
    And Navigate to the column settings screen
    And The user navigates to the temperature control screen
    And User validates the maximum temperature as 85

    Examples:
      | warning_toggle_button_state | maximum_warning_temperature | expected_monitor_injection_count |
      | True                        | 85.0                        | 300                              |


  Scenario Outline: To verify monitor injection count is not altered when users taps the action icons

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as 300
    And The user navigates to the temperature control screen
    And The user sets the maximum warning temperature as 85.0
    And The user navigates to the info screen
    And The user navigates to the settings screen
    And The user navigates to the monitor injection count screen
    And User validates the monitor injection count as "<expected_monitor_injection_count>"
    And Navigate to the column settings screen
    And The user navigates to the temperature control screen
    And User validates the maximum temperature as 85

    Examples:
      | warning_toggle_button_state | expected_monitor_injection_count |
      | True                        | 300                              |


  Scenario Outline: To verify the monitor injection edit field stays in error state when user taps the info icon

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as "<monitor_injection_count>"
    And The user navigates to the info screen
    Then The user validates the done button is disabled
    And Validate the injection count  edit field shows "<error_state>"

    Examples:
      | warning_toggle_button_state | monitor_injection_count | error_state |
      | True                        |                         | True        |
      | True                        | 10001                   | True        |
      | True                        | 0                       | True        |


  Scenario Outline: The comments enter should be saved when user enters the temperature tab

    When User taps the monitor injection count tab
    And User taps the comments tab
    And User enters "<comments>" in the comments tab
    And The user navigates to the temperature control screen
    And User taps the comments tab
    Then Validates the text enter as "<comments>"

    Examples:
      | comments        |
      | Column Comments |


  Scenario Outline: The comments entered should be saved when user enters the injection tab

    When User taps the monitor injection count tab
    And User taps the comments tab
    And User enters "<comments>" in the comments tab
    And User taps the monitor injection count tab
    And User taps the comments tab
    Then Validates the text enter as "<comments>"

    Examples:
      | comments        |
      | Column Comments |


  Scenario Outline: The comments enter should be saved after tapping the done button

    When User taps the comments tab
    And User enters "<comments>" in the comments tab
    And The user confirms the monitor injection count
    And The user navigates to the monitor injection count settings screen
    And User taps the comments tab
    Then Validates the text enter as "<comments>"

    Examples:
      | comments        |
      | Column Comments |


  Scenario Outline: Ability to set the injection limit and maximum temperature for the column

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as "<monitor_injection_count>"
    And The user navigates to the temperature control screen
    And The user sets the maximum warning temperature as "<maximum_warning_temperature>"
    And The user confirms the monitor injection count

    Examples:

      | warning_toggle_button_state | monitor_injection_count | maximum_warning_temperature |
      | True                        | 200                     | 85.0                        |


  Scenario Outline: Verify the edit field value when the value is set invalid

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as "<monitor_injection_count>"
    When The user sets False for the set injection warning toggle button
    When The user sets True for the set injection warning toggle button
    And The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    Then The user validates the value in the edit field is 2000

    Examples:

      | warning_toggle_button_state | monitor_injection_count |
      | True                        | 20000                   |


  Scenario Outline: Verify the edit field value when the value is set None

    When The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    And The user enter the monitor injection count as 2
    And The user confirms the monitor injection count
    And The user navigates to the monitor injection count settings screen
    And The user enter the monitor injection count as "<monitor_injection_count>"
    When The user sets False for the set injection warning toggle button
    When The user sets True for the set injection warning toggle button
    And The user sets "<warning_toggle_button_state>" for the set injection warning toggle button
    Then The user validates the value in the edit field is 2

    Examples:

      | warning_toggle_button_state | monitor_injection_count |
      | True                        |                         |


  @real @weekly
  Scenario: Verify the read icon displays the details of the column

    When The user taps the read icon
    Then The user validates the information text
    And The users validates the column information