@kiosk @signout
Feature: Kiosk | Test for Sign Out Option

  Background:
    Given User navigates to the user profile screen


  Scenario: To verify dashboard is displayed after the lock timer
    When User taps the lock button
    Then User is redirected to dashboard screen after 30 seconds


  Scenario: To verify dashboard screen is displayed when sign out is tapped
    When User taps the lock button
    And User taps the confirm button
    Then User is redirected to dashboard screen


  Scenario: To verify user setting screen is displayed when cancel is tapped
    When User taps the lock button
    And User taps the cancel button
    Then User stays in the user setting screen