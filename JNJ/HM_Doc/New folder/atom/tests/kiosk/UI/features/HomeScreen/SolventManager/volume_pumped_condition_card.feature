@kiosk @volumnPumped
Feature: Kiosk | Volume pumped condition card

  Background:
    Given User navigates to the third solvent manager page


  Scenario Outline: To set the volume pump threshold value

    When User sets the threshold volume to "<threshold_volume>"
    And User confirms the settings for threshold volume
    Then User validates the system displays readback message when the threshold volume is meet


    Examples:
      | threshold_volume |
      | 10               |


  Scenario Outline: To validate the edit field does not allow values that are out of range

    When User sets the threshold volume to "<threshold_volume>"
    Then User validate the edit field state "<is_error_state>"

    Examples:
      | threshold_volume | is_error_state |
      | 100              | False          |
      | 110              | True           |
      | 0.9              | True           |


  @ignore #INS-30472
  Scenario Outline: To validate the edit field read back message when no data is entered

    When User sets the threshold volume to "<threshold_volume>"
    Then User validates the hint messages for the empty flow edit field

    Examples:
      | threshold_volume |
      |                  |


  Scenario Outline: To validate the edit field read back message when data is entered

    When User sets the threshold volume to "<threshold_volume>"
    Then User validates the hint messages for the flow edit field

    Examples:
      | threshold_volume |
      | 99               |
      | 110              |
