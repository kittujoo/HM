@kiosk @ALIST-228 @kiosk_system_qualification_feature
Feature: Kiosk | System Qualification screen

  Background:
    Given User navigates to the administration - system qualification screen


  @simulation @daily
  Scenario Outline: To verify the toggle button is functional and being saved
    When User sets the toggle component to "<toggle_state>"
    And User confirms the changes
    And User navigates to the system qualification screen
    Then User validates the toggle state is "<toggle_state>"

    Examples:
      | toggle_state |
      | False        |
      | True         |


  @simulation @daily
  Scenario Outline: To validate the user is able to change and save the qualification expiration date
    When User sets the toggle component to "True"
    And User sets the qualification expire to "<qualification_expiry>"
    And User confirms the changes
    And User navigates to the system qualification screen
    Then the qualification expiration date is "<qualification_expiry>"

    Examples:
      | qualification_expiry |
      | 1                    |
      | 5                    |
      | 9                    |
      | 11                   |


  @simulation @daily
  Scenario Outline: To verify the toggle state is not saved when the user taps the cancel button
    When User sets the toggle button as "<initial_toggle_status>"
    And User confirms the changes
    And User navigates to the system qualification screen
    Then User validates the toggle button is saved as "<initial_toggle_status>"
    When User sets the toggle as "<new_toggle_status>"
    And User cancels the setting
    Then User validates the toggle button gets saved to "<initial_toggle_status>"

    Examples:
      | new_toggle_status | initial_toggle_status |
      | True              | False                 |
      | False             | True                  |


  @simulation @daily
  Scenario Outline: To verify the qualification expires value is not updated when the user taps the cancel button
    When User sets the toggle button as enable
    And User set qualification expires as "<actual_qualification_expires>"
    And User navigates to the system qualification screen
    Then qualification expires value is "<actual_qualification_expires>"
    When User sets qualification expires as "<desired_qualification_expires>"
    And User cancels the setting
    And User navigates to the system qualification screen
    Then qualification expires value is "<actual_qualification_expires>"

    Examples:
      | actual_qualification_expires | desired_qualification_expires |
      | 5                            | 12                            |
      | 12                           | 5                             |


  @simulation @daily
  Scenario: User validate the default button sets the default expiration date
    When User taps the default button
    Then User validate the qualification expires date is set to default
