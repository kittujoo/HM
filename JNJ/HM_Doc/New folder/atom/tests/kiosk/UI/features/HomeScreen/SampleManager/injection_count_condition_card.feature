@kiosk @ALIST-228 @injection_count_condition_card_feature
Feature: Kiosk | Injection count condition card


  Background:
    Given User navigates to the system - performance counters screen

  @real @monthly
  Scenario: To verify that when the total injection is reset, it is reset to zero
    When User taps to reset the total injection count
    Then User validates the total injection count was reset
    And User validates the sample injections was reset in the card reader
    And User validates the injection count was reset in the condition card
