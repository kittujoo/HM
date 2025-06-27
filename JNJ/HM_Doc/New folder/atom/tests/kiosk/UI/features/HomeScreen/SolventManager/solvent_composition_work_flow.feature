@kiosk @ALIST-228
Feature: Kiosk | Solvent composition condition card

  Background:
    Given User navigates to the solvent composition settings screen

  @simulation @weekly
  Scenario Outline:  To verify ability to set the flow after tapping the done button

    When User adds the solvent composition for solvent line "A,True,45.0", "B,True,45.0", "C,True,5.0", "D,True, 5.0"
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    And The user confirms the selection
    Then The User validates the solvent composition "A,True,45.0" "B,True,45.0" "C,True,5.0" "D,True, 5.0" in the condition card
    And The User validates "<expected_flow_rate>" info in the home screen
    And The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | flow_rate | expected_flow_rate |
      | 2.00      | 2                  |
      | 1.8       | 1.8                |


  @simulation @weekly
  Scenario Outline:  To verify there should not be any flow in pump when user sets out of range flow

    When  User adds the solvent composition for solvent line "A,True,45.0", "B,True,45.0", "C,True,5.0", "D,True, 5.0"
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    Then The system indicates the flow rate is out range and does not navigate to the condition card screen

    Examples:
      | flow_rate |
      | 10.1      |
      | 00000     |
      | 0.00      |

  @simulation @weekly
  Scenario: To verify there should not be any change in the flow rate when user taps the cancel button

    When User adds the solvent composition for solvent line "A,True,45.0", "B,True,45.0", "C,True,5.0", "D,True, 5.0"
    And User navigates to the flow rate control screen
    And The user enters the "0.1"
    And The user confirms the selection
    And User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "1.01"
    And The user cancels the selection
    Then validate the flow rate "0.1" is not altered
    And The user validates "0.1" info in the solvent manager card reader

  @simulation @weekly
  Scenario Outline:  To verify different flow rate options in the solvent composition settings screen

    When  User adds the solvent composition for solvent line "A,True,45.0", "B,True,45.0", "C,True,5.0", "D,True, 5.0"
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    And The user confirms the selection
    Then The User validates the solvent composition "A,True,45.0" "B,True,45.0" "C,True,5.0" "D,True, 5.0" in the condition card
    And The User validates "<expected_flow_rate>" info in the home screen
    And The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | flow_rate | expected_flow_rate |
      | 0.1       | 0.1                |

  @simulation @weekly
  Scenario Outline:  To verify ability to set the flow first and then solvent composition in the card

    When User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    And User navigates to the solvent composition screen
    And User adds the solvent composition for solvent line "A,True,45.0", "B,True,45.0", "C,True,5.0", "D,True, 5.0"
    And The user confirms the selection
    Then The User validates the solvent composition "A,True,45.0" "B,True,45.0" "C,True,5.0" "D,True, 5.0" in the condition card
    And The User validates "<expected_flow_rate>" info in the home screen
    And The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | flow_rate | expected_flow_rate |
      | 2.00      | 2                  |
      | 1.8       | 1.8                |