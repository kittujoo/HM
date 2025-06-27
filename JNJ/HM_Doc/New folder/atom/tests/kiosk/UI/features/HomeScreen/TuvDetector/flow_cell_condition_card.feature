@kiosk @ALIST-228 @kiosk_flow_cell_condition_card_feature @ignore #INSISPP-3947 Flow cell card was temporarily removed from Dashboard
Feature: Kiosk | Flow Cell Condition Card

  @ignore #INSISPP-3947 Flow cell card was temporarily removed from Dashboard
  Scenario: To verify flow cell details
    Given User is at the flow cell settings screen
    Then User validates the flow cell details information

  @ignore #INSISPP-3947 Flow cell card was temporarily removed from Dashboard
  Scenario: To verify flow cell actions
    Given User is at the flow cell settings screen
    When User navigates to the actions tab
      # And User taps replace flow cell panel TODO: This panel is currently nonfunctional [INS-27989]
