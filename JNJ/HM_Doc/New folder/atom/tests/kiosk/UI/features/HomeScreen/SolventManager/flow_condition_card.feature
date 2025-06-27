@kiosk @ALIST-228
Feature: Kiosk | Flow condition card


  Background:
    Given User navigates to the flow control screen


  @simulation @weekly
  Scenario Outline:  To verify user able to set the flow after tapping the done button

    When The user enters the "<flow_rate>"
    And User enters the acceleration time "<time_value>"
    And User adds the solvent composition for solvent line "A,True,45", "B,False,45", "C,True,5", "D,True,5"
    And The user confirms the selection
    Then The User validates "<expected_flow_rate>" info in the sm home screen
    And The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | flow_rate | expected_flow_rate | time_value |
      | 2         | 2                  | 0.06667    |
      | 1.8       | 1.8                | 0.067      |

  @simulation @weekly
  Scenario Outline: To verify able to set the flow after tapping done button

    When The user enters the "<flow_rate>"
    And  User adds the solvent composition for solvent line "A,True,45", "B,False,45", "C,True,5", "D,True,5"
    And The user confirms the selection
    Then The User validates "<expected_flow_rate>" info in the sm home screen
    Then The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | flow_rate | expected_flow_rate |
      | 2         | 2                  |


  @simulation @weekly
  Scenario: To verify there should not be any change in the flow rate when user taps the cancel button

    When User adds the solvent composition for solvent line "A,True,45", "B,False,45", "C,True,5", "D,True,5"
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
  Scenario Outline:  To verify different flow rate options
    When  User adds the solvent composition for solvent line "A,True,45", "B,False,45", "C,True,5", "D,True,5"
    And User navigates to the flow rate control screen
    And The user confirms the selection
    Then The User validates the solvent composition "A,True,45" "B,False,45" "C,True,5" "D,True,5" in the condition card
    And The User validates "<expected_flow_rate>" info in the sm home screen
    Then The user validates the schematic icon for the flow rate
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader

    Examples:
      | expected_flow_rate |
      | 0.1                |

  @simulation @weekly
  Scenario Outline: To verify the flow is off when toggle button is switched off

    When The user enters the "<flow_rate>"
    And User adds the solvent composition for solvent line "A,True,45", "B,False,45", "C,True,5", "D,True,5"
    And User navigates to the flow rate control screen
    And Tap the toggle button to turn off the flow
    And The user confirms the selection
    Then The user validate the flow is turned OFF
    And The user validates "<expected_flow_rate>" info in the solvent manager card reader
    And Tap the toggle button to turn on the flow

    Examples:
      | flow_rate | expected_flow_rate |
      | 2         | OFF                |
