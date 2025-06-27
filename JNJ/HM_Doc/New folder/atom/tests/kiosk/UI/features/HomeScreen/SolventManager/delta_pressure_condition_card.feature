@kiosk
Feature: Kiosk | Delta pressure condition card


  Background:
    Given User navigates to the delta pressure settings screen


  Scenario: To verify when the pressure monitor is toggled on, the other features become available
    When User toggles the pressure monitor on
    And User saves the changes
    And User navigates back to the delta pressure settings
    Then User validates the pressure monitor features are available
    And User navigates back to the solvent manager home screen


  Scenario: To verify when the pressure monitor is off, the other features are unavailable
    When User toggles the pressure monitor off
    And User saves the changes
    And User navigates back to the delta pressure settings
    Then User validates the pressure monitor features are not available
    And User navigates back to the solvent manager home screen


  Scenario Outline: To verify when a valid target pressure range is set, it can be saved
    When User toggles the pressure monitor on
    And User sets target pressure to "<target_pressure_value>"
    And User saves the changes
    And User navigates back to the delta pressure settings
    Then User validates the "<target_pressure_value>" was saved
    And User navigates back to the solvent manager home screen

    Examples:
      | target_pressure_value |
      | 7.5                   |


  Scenario Outline: To validate the indicator messages in the delta pressure condition card1

    When User toggles the pressure monitor on
    And User sets target pressure to "<target_pressure_value>"
    And User saves the changes
    Then Validate the read back message in the condition card for "<target_pressure_value>"

    Examples:
      | target_pressure_value |
      | 7.5                   |
      | 20.0                  |


  Scenario: To validate the indicator messages in the delta pressure condition card

    When User toggles the pressure monitor off
    And User saves the changes
    Then Validate the indicator bar in the condition card grey out
