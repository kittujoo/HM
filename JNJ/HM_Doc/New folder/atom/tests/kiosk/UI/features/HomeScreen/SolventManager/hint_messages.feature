@hintMessages @simulation @kiosk
Feature: Kiosk | Solvent composition condition hint messages


  Scenario Outline: To validate the hint messages in the solvent composition edit field
    When User navigates to the solvent composition settings screen
    Then User validates the hint messages for "<line_1>" "<line_2>" "<line_3>" "<line_4>" in the condition card
    Examples:
      | line_1       | line_2       | line_3      | line_4       |
      | A,False,45.0 | B,False,45.0 | C,False,5.0 | D,False, 5.0 |


  Scenario Outline: To validate the hint messages in the solvent flow edit field
    When User navigates to the solvent composition settings screen
    When User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    Then User validates the hint messages for the flow
    Examples:
      | flow_rate |
      | 2.00      |
      | 10.10     |


  Scenario: To validate the empty hint messages in the solvent flow edit field
    When User navigates to the solvent composition settings screen
    When User navigates to the flow rate control screen
    And The user leaves the flow_rate as empty
    Then User validates the hint messages for the empty flow edit field