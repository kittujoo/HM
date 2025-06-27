@kiosk @kiosk_prime_solvents_feature @ALIST_228
Feature: Kiosk | Prime Mobile Phase Solvents Workflow Functionality

  @real @weekly
  Scenario Outline: To validate the prime solvents workflow summary screen
    When User starts the workflow
    And User validates the welcome context in the welcome screen
    And User taps next
    And User validates the Caution text in the caution screen
    And User taps next
    And User sets the solvent toggle "<toggle_state>"
    And User sets "<prime_duration>" in "<unit>" for the "<solvent_lines>"
    And User taps next
    And User taps next
    And User sets the composition toggle "<toggle_state>"
    And User sets "<line_1>", "<line_2>", "<line_3>", "<line_4>" composition solvent lines
    And User taps next
    And User sets the "<com_duration>" for prime by composition
    And User taps next
    And User enters the "<flow_rate>" for "<eq_duration>" for composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User taps next
    Then User validate the summary screen details for solvent by line "<solvent_lines>", "<prime_duration>"
    And User validate the solvent by composition "<line_1>" "<line_2>" "<line_3>" "<line_4>", "<com_duration>"
    And User validates the final condition for "<line_1>" "<line_2>" "<line_3>" "<line_4>", "<flow_rate>", "<eq_duration>"
    And User validates the workflow is completed successfully

    Examples:
      | solvent_lines | prime_duration | unit | line_1    | line_2    | line_3   | line_4   | com_duration | flow_rate | eq_duration | toggle_state |
      | ABCD          | 2:00           | 30   | A,True,45 | B,True,45 | C,True,5 | D,True,5 | 2            | 0.5       | 3           | ON           |


  @real @weekly
  Scenario Outline: To validate the prime work flow when user abort it
    When User starts the workflow
    And User validates the welcome context in the welcome screen
    And User taps next
    And User validates the Caution text in the caution screen
    And User taps next
    And User sets the solvent toggle "<toggle_state>"
    And User sets "<prime_duration>" in "<unit>" for the "<solvent_lines>"
    And User taps next
    And User taps next
    And User sets the composition toggle "<toggle_state>"
    And User sets "<line_1>", "<line_2>", "<line_3>", "<line_4>" composition solvent lines
    And User taps next
    And User sets the "<com_duration>" for prime by composition
    And User taps next
    And User enters the "<flow_rate>" for "<eq_duration>" for composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User taps next
    Then User aborts the prime workflow
    And User validates the stopped status screen for the prime workflow

    Examples:
      | solvent_lines | prime_duration | unit | line_1    | line_2     | line_3   | line_4   | com_duration | flow_rate | eq_duration | toggle_state |
      | ABCD          | 2:00           | 30   | A,True,45 | B,False,45 | C,True,5 | D,True,5 | 3            | 0.001     | 10          | ON           |

  @real @weekly
  Scenario Outline: To validate prime solvents workflow with minimal options
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User taps next
    And User sets the composition toggle "<comp_toggle>"
    And User taps next
    And User enters the "<flow_rate>" for "<eq_duration>" for composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User taps next
    Then User validate the solvent by line is not enabled
    And User validate the solvent by composition is not enabled

    Examples:
      | solvent_toggle | comp_toggle | flow_rate | eq_duration | line_1    | line_2     | line_3   | line_4   |
      | OFF            | False       | 0.001     | 2           | A,True,45 | B,False,45 | C,True,5 | D,True,5 |

  @real @weekly
  Scenario Outline: To validate prime solvents workflow when using prime solvent options
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "ON"
    And User sets "<prime_duration>" in "<unit>" for the "<solvent_lines>"
    And User taps next
    And User taps next
    And User sets the composition toggle "<comp_toggle>"
    And User taps next
    And User enters the "<flow_rate>" for "<eq_duration>" for composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User taps next
    Then User validate the summary screen details for solvent by line "<solvent_lines>", "<prime_duration>"
    And User validate the solvent by composition is not enabled

    Examples:
      | solvent_lines | prime_duration | unit | comp_toggle | flow_rate | eq_duration | line_1    | line_2     | line_3   | line_4   |
      | ABCD          | 2:00           | 30   | OFF         | 0.001     | 2           | A,True,45 | B,False,45 | C,True,5 | D,True,5 |


  @real @weekly
  Scenario Outline: To validate prime solvents workflow when using prime composition options only
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User taps next
    And User sets the composition toggle "ON"
    And User sets "<line_1>", "<line_2>", "<line_3>", "<line_4>" composition solvent lines
    And User taps next
    And User sets the "<com_duration>" for prime by composition
    And User taps next
    And User enters the "<flow_rate>" for "<eq_duration>" for composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User taps next
    Then User validate the solvent by line is not enabled
    And User validate the solvent by composition "<line_1>" "<line_2>" "<line_3>" "<line_4>", "<com_duration>"
    And User validates the final condition for "<line_1>" "<line_2>" "<line_3>" "<line_4>", "<flow_rate>", "<eq_duration>"

    Examples:
      | solvent_toggle | com_duration | flow_rate | eq_duration | line_1    | line_2     | line_3   | line_4   |
      | OFF            | 3            | 0.001     | 2           | A,True,45 | B,False,45 | C,True,5 | D,True,5 |


  @real @weekly @quarantine @defect:INSISPP-8494
  Scenario Outline: To validate prime duration range
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User sets "<prime_duration>" in "<unit>" for the "ABCD"
    Then User validates the "<minus_button>" "<plus_button>" "<reset_button>" status

    Examples:
      | solvent_toggle | prime_duration | unit | minus_button | plus_button | reset_button |
      | ON             | 2:00           | 30   | Disable      | Enable      | Disable      |
      | ON             | 5:00           | 30   | Enable       | Enable      | Enable       |
      | ON             | 60:00          | 30   | Enable       | Disable     | Enable       |


  @real @weekly
  Scenario Outline: To validate prime by composition range
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User taps next
    And User sets the composition toggle "<comp_toggle>"
    And User taps next
    And User sets the "<com_duration>" for prime by composition
    Then User validates the "<next_button>" status

    Examples:
      | solvent_toggle | comp_toggle | com_duration | next_button |
      | OFF            | ON          | 2            | Enable      |
      | OFF            | ON          | 60           | Enable      |
      | OFF            | ON          | 10           | Enable      |
      | OFF            | ON          | 1            | Disable     |
      | OFF            | ON          | 60.51        | Disable     |


  @real @weekly
  Scenario Outline: To validate flow rate range
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User taps next
    And User sets the composition toggle "<comp_toggle>"
    And User taps next
    And User enters the flow rate to "<flow_rate>"
    Then User validates the "<next_button>" status

    Examples:
      | solvent_toggle | comp_toggle | flow_rate | next_button |
      | OFF            | OFF         | 0.001     | Enable      |
      | OFF            | OFF         | 10.000    | Enable      |
      | OFF            | OFF         | 2         | Enable      |
      | OFF            | OFF         | 0         | Disable     |
      | OFF            | OFF         | 10.100    | Disable     |

  @real @weekly
  Scenario Outline: To validate equilibration duration range
    When User starts the workflow
    And User taps next
    And User taps next
    And User sets the solvent toggle "<solvent_toggle>"
    And User taps next
    And User sets the composition toggle "<comp_toggle>"
    And User taps next
    And User enters the equilibration duration to "<eq_duration>"
    Then User validates the "<next_button>" status

    Examples:
      | solvent_toggle | comp_toggle | eq_duration | next_button |
      | OFF            | OFF         | 2           | Enable      |
      | OFF            | OFF         | 30          | Enable      |
      | OFF            | OFF         | 3           | Enable      |
      | OFF            | OFF         | 0           | Disable     |
      | OFF            | OFF         | 33          | Disable     |

