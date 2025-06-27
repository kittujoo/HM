@kiosk @ALIST-228 @kiosk_valve_position_feature
Feature: Kiosk | Valve position condition card

  @real @weekly
  Scenario: To verify the valve position displayed is a valid position

    Given User navigates to the sample manager screen
    When User obtains the current valve position
    Then User validates that the current valve position is one of expected:
      | Allowed_positions |
      | Blocked           |
      | Load              |
      | Inject            |