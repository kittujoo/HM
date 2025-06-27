@kiosk @replaceNeedle @FCS
Feature: Kiosk | Replace needle workflow functionality


  Scenario: To validate the the welcome and caution text in needle work flow

    When User taps the replace needle panel
    Then User validates the Welcome screen text
    Then User validates the Caution screen text


  Scenario: To validate the next button is enabled when the pre-conditions are met

    When User taps the replace needle panel
    And User navigates to the pre-conditions screen
    Then User confirms the preconditions
    And User validates the carriage is in the service position
    And User validates the replace needle procedure text
    And User runs the recommended tests


  Scenario: To validate the workflow stop executes when the user taps the close button

    When User taps the replace needle panel
    And User navigates to the pre-conditions screen
    Then User confirms the preconditions
    And User taps the stop button
    And User validates the workflow is stopped


  Scenario: To validate that user navigates to home screen when the worlflow is complete

    When User taps the replace needle panel
    And User navigates to the pre-conditions screen
    Then User confirms the preconditions
    And User validates the carriage is in the service position
    And User validates the replace needle procedure text
    And User taps the start icon
    And User taps the stop button
    And User validates the workflow is stopped