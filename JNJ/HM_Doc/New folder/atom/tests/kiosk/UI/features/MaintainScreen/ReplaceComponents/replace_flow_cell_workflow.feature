@kiosk @replaceFlowCellWorkflow @FCS
Feature: Kiosk | Replace flow cell workflow functionality

  Background:
    Given User navigates to the replace components HUB area

  Scenario Outline: To test the screens and features within the replace flow cell workflow
    When User taps the replace flow cell panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User starts the preconditions process validating the conditions
    And User validates the context in the removal screen
    And User validates the context in the first installation screen screen
    And User validates the context in the second installation screen screen
    And User enters the "<flow_rate>" and "<flow_duration>"
    And User taps next
    And User selects the "<solvent>"
    Then User validates the flow cell conditioning process
    And User validates the finish screen
    And User taps done
    And User navigates back to dashboard

    Examples:
      | flow_rate | flow_duration | solvent |
      | 5.000     | 60.0          | B       |
      | 1.000     | 30.0          | A       |

  Scenario Outline: To test the flow settings error condition
    When User taps the replace flow cell panel
    And User taps next
    And User taps next
    And User starts the preconditions process validating the conditions
    And User taps next
    And User taps next
    And User taps next
    And User enters the "<flow_rate>" and "<flow_duration>"
    Then User validates that flow settings screen is in error state
    And User taps cancel
    And User navigates back to dashboard

    Examples:
      | flow_rate | flow_duration |
      | 99        | 999           |
