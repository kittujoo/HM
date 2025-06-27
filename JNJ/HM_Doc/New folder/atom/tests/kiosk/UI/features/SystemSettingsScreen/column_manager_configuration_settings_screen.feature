@kiosk @ALIST-228
Feature: Kiosk | Column manager configuration settings screen

  
  @real @weekly
  Scenario Outline: To verify the toggle components are functional and being saved
    Given User navigates to the CHC module configuration screen
    And CHC leak configuration was set "<initial_state>" state    
    When User navigates to the column configuration settings screen
    Then User validates the CHC leak sensor configuration state is "<expected_state>"
    And User cancels the changes

    Examples:
      | initial_state |expected_state|
      | OFF           |    OFF       |
      | ON            |    ON        |


  @real @daily
  Scenario Outline: To verify the toggle status is not updated when the user taps the cancel button
    Given User navigates to the CHC module configuration screen
    And CHC leak configuration was set "<initial_state>" state
    When User navigates to the column configuration settings screen    
    Then User validates the CHC leak sensor configuration state is "<expected_state>"
    And User sets the toggle button to "<toggle_status>"
    And User cancels the changes
    And User navigates to the column configuration settings screen
    Then User validates the CHC leak sensor configuration state is "<expected_state>"

    Examples:
      | initial_state | expected_state |toggle_status|
      | OFF           | OFF            |    True     |
      

  @real @weekly
  Scenario Outline: To verify turning ON/OFF CHC leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    And CHC leak sensor was set "<initial_state>" state
    When User switches the CHC leak sensor to "<expected_state>" state
    And User navigates to the column configuration settings screen
    Then User validates the CHC leak sensor configuration state is "<expected_state>"

    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |


  @real @weekly
  Scenario Outline: To verify turning ON/OFF CHC leak sensor from Module Configuration Tab
    Given User navigates to the CHC module configuration screen
    And CHC leak configuration was set "<initial_state>" state
    When User switches the CHC leak configuration sensor to "<expected_state>" state
    And User navigates to the leak sensor screen
    Then User validates the CHC leak sensor state is "<expected_state>"

    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |

