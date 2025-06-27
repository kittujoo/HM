@kiosk @pumpMaintenanceWorkflow @FCS
Feature: Kiosk | Pump Maintenance workflow functionality

  Background:
    Given User navigates to the replace components HUB area

  @ignore
  Scenario Outline: To test the screens and features within the pump maintenance workflow
    When User taps the pump maintenance panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User validates the context in the procedure screen
    And User sets the flush duration time as "<flush_duration>"
    And User selects a "<solvent>"
    And User validates the "<flush_duration>"  in summary details
      # TODO: workflow is not completed, more steps when they are added into workflow
      #      And User validates the flush process completes
      #      Then User XYZ

    Examples:
      | flush_duration | solvent |
      | 5.00           | B       |
      | 3.75           | C       |


  Scenario Outline: To test the flush duration field functions
    When User taps the pump maintenance panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User validates the context in the procedure screen
    And User sets the flush duration time as "<flush_duration>"
    Then User validates the flush duration field is in error state
    And User sets the field to the default value
    And User validates the "<default_value>"  has been set

    Examples:
      | flush_duration | default_value |
      | 99             | 2.00          |
