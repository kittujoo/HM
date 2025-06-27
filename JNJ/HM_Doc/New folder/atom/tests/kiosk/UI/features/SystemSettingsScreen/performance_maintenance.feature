@kiosk @ALIST-228 @performance_maintenance_screen_feature
Feature: Kiosk | performance maintenance screen

  Background:
    Given User navigates to the administration screen
    When User navigates to the performance maintenance screen

  @real @daily
  Scenario Outline: To verify the toggle button for set performance maintenance  is functional and being saved
    When User sets the toggle component to "<toggle_status>"
    And User confirms the changes
    And User navigates to the performance maintenance screen
    Then User validates the toggle button is saved to "<toggle_status>"

    Examples:
      | toggle_status |
      | False         |
      | True          |

  @real @daily
  Scenario Outline: To validate the user is able to change and save the next performance maintenance expiration date
    When User sets the toggle component to "True"
    And User sets next performance maintenance to "<actual_months>"
    And User confirms the changes
    Then User validats the performance maintenance expiration date is displayed under the performance tab
    When User navigates to the performance maintenance screen
    Then User validates the performance maintenance expiration date as "<expected_months>"

    Examples:
      | actual_months | expected_months |
      | 1             | 1               |
      | 5             | 5               |
      | 9             | 9               |
      | 12            | 12              |

  @real @daily
  Scenario Outline: To verify the toggle status is not updated when the user taps the cancel button
    When User sets the toggle component to "<actual_toggle_status>"
    And User confirms the changes
    And User navigates to the performance maintenance screen
    Then User validates the toggle button is saved to "<actual_toggle_status>"
    When User sets the toggle component to "<toggle_status>"
    And User cancels the setting
    And User navigates to the performance maintenance screen
    Then User validates the toggle button is saved to "<expected_toggle_status>"

    Examples:
      | actual_toggle_status | toggle_status | expected_toggle_status |
      | False                | True          | False                  |
      | True                 | False         | True                   |

  @real @daily
  Scenario Outline: To verify the qualification expires value is not updated when the user taps the cancel button
    When User sets the toggle component to "True"
    And User sets next performance maintenance to "<expected_months>"
    And User confirms the changes
    And User navigates to the performance maintenance screen
    Then User validates the performance maintenance expiration date as "<expected_months>"
    When User sets next performance maintenance to "<desired_maintenance_expires>"
    And User cancels the setting
    And User navigates to the performance maintenance screen
    Then User validates the performance maintenance expiration date as "<expected_months>"

    Examples:
      | expected_months | desired_maintenance_expires |
      | 5               | 7                           |
      | 12              | 3                           |

  @real @daily
  Scenario: User validate the default button sets the default performance maintenance date
    When User sets the toggle component to "True"
    And User sets next performance maintenance to "10"
    And User taps the default button
    And User confirms the changes
    And User navigates to the performance maintenance screen
    Then User validate the maintenance expires date is set to default as "12"

  @simulation @weekly 
  Scenario Outline: To verify note is allowed to have maximum 14 characters
    When User taps the note tab
    And User enters text to the "<note>"
    Then User validates the comment card shows correct numbers with "<expected_length>" characters

    Examples:
      | note           | expected_length |
      | abcdefghijklmn | 14              |
      | abcdefghij12   | 12              |
      | abcde12345     | 10              |
      | q              | 1               |
