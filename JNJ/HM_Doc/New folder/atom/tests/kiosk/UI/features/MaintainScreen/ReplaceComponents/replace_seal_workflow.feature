@kiosk @replaceSealWorkflow @FCS @ignore #INS-27842 & INS-27844
Feature: Kiosk | Replace seal workflow functionality

  Background:
    Given User navigates to the replace components HUB area

  Scenario: To test the screens and features within the replace seal workflow
    When User taps the replace seal panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User validates the preconditions are in a passing state
    And User validates the carriage service process completes
    And User validates the context in the first procedure screen
      #    And User validates the context in the second procedure screen
      #    Then User validates the needle seal readiness test completes
