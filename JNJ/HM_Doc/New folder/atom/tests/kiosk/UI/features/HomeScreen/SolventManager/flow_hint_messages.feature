@flow @simulation @kiosk @ALIST-228
Feature: Kiosk | Solvent composition condition hint messages

  Scenario:  To validate the hint messages in the solvent flow edit field through flow
    When User navigates to the flow control screen
    And The user enters the "2.00"
    Then User validates the hint messages for the flow

  Scenario:  To validate the hint messages in the solvent composition edit field through flow

    When User navigates to the flow control screen
    Then User validates the hint messages for "<line_1>" "<line_2>" "<line_3>" "<line_4>" in the condition card

    Examples:
      | line_1     | line_2     | line_3    | line_4    |
      | A,False,45 | B,False,45 | C,False,5 | D,False 5 |

  Scenario:  To validate the empty hint messages in the solvent flow edit field

    When User navigates to the flow control screen
    And The user enters the "<flow_rate>"
    Then User validates the hint messages for the empty flow edit field

    Examples:
      | flow_rate |
      |           |


