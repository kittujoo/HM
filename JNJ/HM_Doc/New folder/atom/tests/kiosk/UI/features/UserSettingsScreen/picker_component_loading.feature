@kiosk @ALIST-228
Feature: Kiosk | Picker component on user preferences settings screen


  Background:
    Given User navigates to the user preferences screen

  @simulation @weekly
  Scenario: To verify the Date picker component is visible on page load
    When User taps the Date and Time format tab
    Then User validates the time zone picker is displayed
    When User taps the Date and Time format tab
    Then User validates the date picker is displayed
