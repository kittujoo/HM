@simulation @flow @kiosk @ALIST-228
Feature: Kiosk | flow edit field feature


  Scenario Outline: The flow edit field shows different state for different range of flow
    When User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    Then Validate the flow edit field shows "<error_state>"

    Examples:
      | flow_rate | error_state |
      | 0.11      | False       |
      | 2.22      | False       |
      | 0.00      | True        |
      | 10.24     | True        |


  Scenario Outline: To validate flow rate when moving between solvent and flow screens
    When User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    And User navigates to the solvent composition screen
    And User navigates to the flow rate control screen
    Then The user validates "<expected_flow_rate>" in the settings screen

    Examples:
      | flow_rate | expected_flow_rate |
      | 2         | 2.0                |
      | .1        | 0.10               |
      | .2        | 0.2                |
      | 0.2       | 0.2                |
      | .0        | 0.0                |

  @sim3
  Scenario Outline: To verify validation is done in the edit field
    When User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    Then The user validates "<expected_flow_rate>" in the settings screen

    Examples:

      | flow_rate | expected_flow_rate |
      | 2         | 2                  |
      | 0000      | 0                  |
      | 0002      | 2                  |
      | 00.2      | 0.2                |
      | ..25      | 0.25               |
      | ...25     | 0.25               |
      | .0        | 0.0                |


  Scenario Outline: To validate the state of the flow rate default button with different values
    When User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    Then User validates the default button disabled is "<is_button_disabled>"

    Examples:
      | flow_rate | is_button_disabled |
      | 0.100     | True               |
      | 1.8       | False              |

  @real
  Scenario Outline: To validate using the flow rate default value button sets the flow rate to the default value
    When User navigates to the flow control screen
    And User navigates to the flow rate control screen
    And The user enters the "<flow_rate>"
    And User taps the default flow button
    Then The user validates "<expected_flow_rate>" in the settings screen

    Examples:
      | flow_rate | expected_flow_rate |
      | 1.8       | 0.100              |