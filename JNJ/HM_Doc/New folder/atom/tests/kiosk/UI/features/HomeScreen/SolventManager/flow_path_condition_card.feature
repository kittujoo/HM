@flowPathConditionCard @reg @ignore #flow_path unresponsive
Feature: Kiosk | Flow path condition card


  Background:
    Given User navigates to the third solvent manager page

  @real @weekly
  Scenario Outline: To verify that when the flow path is changed, all display locations are changed to that flow path
    When User navigates to the flow path settings screen
    And User change the the "<flow_path>" at isym level
    Then User validates the "<flow_path>" was changed on kiosk
    And User returns to the solvent manager home screen

    Examples:
      | flow_path |
      | Blocked   |
      | Mixer     |
      | Vent      |


  Scenario Outline: To verify when the flow path is changed but cancelled, all display locations of the flow path are unchanged
    When User navigates to the flow path settings screen
    And User taps the "<flow_path>"
    And User cancels the flow path change
    Then User validates the "<expected_flow_path>" is unchanged
    And User returns to the solvent manager home screen


    Examples:
      | flow_path | expected_flow_path |
      | Blocked   | Vent               |
