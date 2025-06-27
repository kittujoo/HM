@kiosk @replaceLampWorkflow @FCS
Feature: Kiosk | Replace lamp workflow functionality

  Background:
    Given User navigates to the replace components HUB area

  Scenario: To test the screens and features within the replace lamp workflow
    When User taps the replace lamp panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User validates the context and conditions in the preconditions screen
    And User validates the context in the removal screen
    And User validates the context in the first installation screen
    And User validates the context in the second installation screen
    Then User validates the lamp hours in the finalization screen