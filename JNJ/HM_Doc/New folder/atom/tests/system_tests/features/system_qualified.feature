@system @ALIST-231
Feature: System | System Qualification

  Background:
    Given User navigates to Administration - System Qualification screen

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: An acquisition can be run if the System Qualification is not expired
    Given Pre-Run Checks window is opened
    And System is qualified toggle button is "<toggle_state>"
    And User validates in Console on Acquisition tab, Pre-run checks that System is qualified is "<state>"
    When User navigates to System Qualification screen
    And User set the System Qualification to "<toggle_button>"
    And the System Qulification date is not expired
    And User starts an aquisition
    Then User validates the acquisition is successfully started

    Examples
      | toggle_state | state | toggle_button |
      | Enabled      | ON    | ON            |
      | Disabled     | OFF   | OFF           |
      | Disabled     | OFF   | ON            |
      | Enabled      | ON    | OFF           |

  @real_or_simulation @weekly @new @ignore
  Scenario: An acquisition cannot be run if the System Qualification is expired
    Given An instrument system with the system qualification date expired
    And Pre-Run Checks window is opened
    And System is qualified toggle button is enabled
    And User navigates to System Qualification screen
    And User validates the System Qulification date is expired
    And User starts an aquisition
    Then User validates the acquisition is not started
    And Users validates in Message Center a message is displayed