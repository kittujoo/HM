@kiosk @ALIST-228
Feature: Kiosk | Solvent composition

  Background:
    Given User navigates to the solvent composition settings screen

  @simulation @weekly
  Scenario Outline:  To verify field focus within the solvent composition settings screen
    When  User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    Then User validates the "<focused_field>" is "<is_focused>"

    Examples:
      | line_1     | line_2   | line_3   | line_4   | focused_field | is_focused |
      | A,True, 85 | B,True,5 | C,True,5 | D,True,5 | D             | True       |

  @simulation @weekly
  Scenario Outline: To verify when user cancels changes in solvent settings, the field focus is reset
    When  User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And The user cancels the selection
    And User navigates to the solvent composition settings screen
    Then User validates the "<focused_field>" is "<is_focused>"

    Examples:
      | line_1    | line_2   | line_3   | line_4   | focused_field | is_focused |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |

  @simulation @weekly
  Scenario Outline: To verify when user confirms changes in solvent settings, the field focus is not reset
    When  User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And The user confirms the selection
    And User navigates to the solvent composition settings screen
    Then User validates the "<focused_field>" is "<is_focused>"

    Examples:
      | line_1    | line_2   | line_3   | line_4   | focused_field | is_focused |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |


  @simulation @weekly
  Scenario Outline: To verify field focus is not lost when taking flow condition card path to solvent settings
    When  User adds the solvent composition for solvent line "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And The user confirms the selection
    And User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And User navigates to the solvent composition screen
    Then User validates the "<focused_field>" is "<is_focused>"

    Examples:
      | line_1    | line_2   | line_3   | line_4   | focused_field | is_focused |
      | A,True,85 | B,True,5 | C,True,5 | D,True,5 | A             | True       |