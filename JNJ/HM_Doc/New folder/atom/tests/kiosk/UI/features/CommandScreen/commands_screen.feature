@kiosk @ALIST-228 @command_screen_feature
Feature: Kiosk | Commands Screen functionality


  @real @daily
  Scenario Outline: To verify user able to turn ON or OFF the flow
    When Flow is "<current_flow_control>"
    And User taps the flow button to set flow to "<new_flow_control>"
    Then Kiosk Commands page shows flow control "<new_flow_control>"
    And User verifies the "<flowing_state>"

    Examples:
      | current_flow_control | new_flow_control | flowing_state |
      | OFF                  | ON               | True          |
      | ON                   | OFF              | False         |

  @real @weekly
  Scenario Outline: To verify UV lamp turn ON or OFF command card functionality of the system
    When Detector lamp is "<current_lamp_state>"
    And User taps the detector lamp button to set lamp to "<new_lamp_state>"
    Then Kiosk Commands page shows detector lamp "<new_lamp_state>"
    And User Verifies the UV lamp is "<new_lamp_state>" on the dashboard

    Examples:
      | current_lamp_state | new_lamp_state |
      | OFF                | ON             |
      | ON                 | OFF            |

  @real @daily
  Scenario Outline: Detector lamp state doesn't change after reset card
    When Detector lamp is "<current_lamp_state>"
    And User taps the reset button
    And User taps the commands page button
    Then Kiosk Commands page shows detector lamp "<new_lamp_state>"

    Examples:
      | current_lamp_state | new_lamp_state |
      | OFF                | OFF            |
      | ON                 | ON             |

  @simulation @daily
  Scenario: To verify user able to stop the flow using the emergency stop card
    When User taps the flow button to turn on the flow
    And User verifies the flowing state is True
    And User taps the emergency stop button
    Then User verifies the flowing state is False

  @simulation @daily
  Scenario: To verify when the reset card is interacted with, the machine reset occurs
    When User taps the reset button
    Then User verify the system is reset

  @real @weekly @negative @ignore #need to find a way to trigger an alarm through isym
  Scenario: To validate the reset card when user trigger an error
    When User raises an alarm on the instrument system (e.g. leak)
    And User taps the reset button
    Then User verify the system is reset
    And User validates Kiosk page shows IDLE state
