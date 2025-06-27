@kiosk @replaceColumnWorkflow @FCS
Feature: Kiosk | Replace column workflow functionality

  Background:
    Given User navigates to the replace components HUB area

  Scenario Outline: To test the screens and features within the replace column workflow
    When User taps the replace column panel
    And User validates the context in the welcome screen
    And User validates the context in the caution screen
    And User toggles the flush column option to "<flush_option>"
    And User sets the "<flow_rate>"
    And User sets the "<flow_duration>"
    And User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User validates the flush column summary screen details, "<flow_rate>" "<expected_line_1>" "<expected_line_2>" "<expected_line_3>" "<expected_line_4>"
    And User runs and validates the flush column test is completed
    And User checks the conditions within the preconditions screen
      # TODO: Remove and Install screens have the wrong text copy [INS-28315]
    And User validates the context in the remove screen
    And User validates the context in the install screen
    And User validates the new column information
      # new column (radio selection, prime is disabled)
      # Prime Instrument Screens?
    And User taps next
    And User toggles the condition flow option to "<condition_flow_option>"
    And User sets the "<condition_flow_rate>"
    And User adds the condition solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User sets the "<condition_duration>"
      # summary TODO: [INS-27737] Summary screen is getting a re-work
    And User validates the information in the summary screen
    Then User validates the column condition process

      # TODO: Vertical grid should be converted back to typical examples grid due to this being deprecated in later gherkin versions
    Examples:
      | flush_option | flow_rate | flow_duration | line_1    | line_2     | line_3   | line_4   | expected_line_1 | expected_line_2 | expected_line_3 | expected_line_4 | condition_flow_option | condition_flow_rate | condition_duration |
      | true         | 2.00      | 05:00         | A,True,45 | B,False,45 | C,True,5 | D,True,5 | 45              | 45              | 5               | 5               | true                  | 2.00                | 05:00              |