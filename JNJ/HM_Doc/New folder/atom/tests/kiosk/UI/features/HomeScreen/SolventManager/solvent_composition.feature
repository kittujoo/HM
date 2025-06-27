@kiosk @ALIST-228
Feature: Kiosk | Solvent condition card

  Background:
    Given User navigates to the flow control screen

  @simulation @weekly
  Scenario Outline:  To verify user adds different solvent composition for a specific flow rate using the flow condition card

    When The user enters the "1.5"
    And User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    Then Validate the solvent line for "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And Validate the total composition is "<total_composition>"


    Examples:
      | line_1      | line_2      | line_3       | line_4        | total_composition |
      | A,True,45   | B,True,45   | C,True,5     | D,True, 5     | 100               |
      | A,True,25.2 | B,True,24.3 | C,True,24.50 | D,True, 26.00 | 100               |


  @simulation @weekly
  Scenario Outline: To verify validation is done in the edit field

    When User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User navigates to the flow rate control screen
    And User navigates to the solvent composition screen
    And User validates the "<line_1>" is highlighted
    And User adds the solvent "<actual_composition>" for solvent A only
    Then User validates the "<expected_composition>" for solvent line

    Examples:
      | line_1   | line_2 | line_3 | line_4 | actual_composition | expected_composition |
      | A,True,0 | ""     | ""     | ""     | 000000             | 0                    |
      | A,True,0 | ""     | ""     | ""     | 0005               | 5                    |
      | A,True,0 | ""     | ""     | ""     | 0.2                | 0.2                  |
      | A,True,0 | ""     | ""     | ""     | .0                 | 0.0                  |
      | A,True,0 | ""     | ""     | ""     | ..2                | 0.2                  |
      | A,True,0 | ""     | ""     | ""     | 2                  | 2                    |

  @simulation @weekly
  Scenario Outline: To verify formatting is done  when the focus is lost

    When User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User navigates to the flow rate control screen
    And User navigates to the solvent composition screen
    And User validates the "<line_1>" is highlighted
    And User adds the solvent "<actual_composition>" for solvent A only
    And User navigates to the flow rate control screen
    And User navigates to the solvent composition screen
    Then User validates the "<expected_composition>" for solvent line

    Examples:
      | line_1    | line_2 | line_3 | line_4 | actual_composition | expected_composition |
      | A,True,0  | ""     | ""     | ""     | 000000             | 0.00                 |
      | A,True,0  | ""     | ""     | ""     | 0005               | 5.00                 |
      | A,True,0  | ""     | ""     | ""     | 00.2               | 0.2                  |
      | A,True,0  | ""     | ""     | ""     | .0                 | 0.00                 |
      | A,True,0  | ""     | ""     | ""     | ..25               | 0.2                  |
      | A, True,0 | ""     | ""     | ""     | 2                  | 2.00                 |
