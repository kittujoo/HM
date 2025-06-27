@kiosk @ALIST-228 @uv_lamp_condition_card_feature
Feature: Kiosk | UV Lamp Condition Card

  @real @weekly
  Scenario: To verify UV lamp details
    Given User sets pre-required date and time format
    And User is at the UV lamp settings screen
    Then User validates the UV lamp details information

  @real @weekly
  Scenario: To validate the lamp hours used is displayed same in all the screens
    Given User is at the UV lamp settings screen
    When User get the lamp hours used info from the lamp details
    Then User validates the lamp hours info in the condition card
    Then User validates the lamp hours used info in the card reader
    Then User validates the lamp hours info in the performance counters screen
