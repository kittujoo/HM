@kiosk @ALIST-228 @kiosk_mobile_phase_wash_solvent_feature
Feature: Kiosk | Mobile phase/Wash solvent configuration screen

  @real @weekly
  Scenario Outline:  To verify mobile phase configuration settings are being saved when changed
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<toggle_status>"
    And User selects the "<bottle_volume>" volume for "<mobile_phase>"
    And User selects the "<line_color>" color for "<mobile_phase>"
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies "<bottle_volume>" and "<line_color>" were saved for "<mobile_phase>"

    Examples:
      | toggle_status | mobile_phase | bottle_volume | line_color |
      | true          | A            | 5L            | green      |


  @real @weekly
  Scenario Outline:  To verify mobile phase configuration settings are being saved when toggle is off
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<toggle_status>"
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies the "<mobile_phase>" toggle is "<toggle_status>"

    Examples:
      | toggle_status | mobile_phase |
      | false         | A            |
      | false         | D            |


  @real @weekly
  Scenario Outline: To verify the <toggle_status> is not updated when the user taps the cancel button
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<initial_toggle_state>"
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies the "<mobile_phase>" toggle is "<initial_toggle_state>"
    When User toggles the "<mobile_phase>" toggle to "<set_toggle_state>"
    And User cancels the setting
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies the "<mobile_phase>" toggle is "<initial_toggle_state>"

    Examples:
      | mobile_phase | initial_toggle_state | set_toggle_state |
      | A            | False                | True             |
      | B            | True                 | False            |
      | C            | False                | True             |
      | D            | True                 | False            |


  @real @weekly
  Scenario Outline: To verify mobile phase configuration settings are not updated when the user taps the cancel button
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "True"
    And User selects the "<actual_bottle_volume>" volume for "<mobile_phase>"
    And User selects the "<actual_line_color>" color for "<mobile_phase>"
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "True"
    And User selects the "<desired_bottle_volume>" volume for "<mobile_phase>"
    And User selects the "<desired_line_color>" color for "<mobile_phase>"
    And User cancels the setting
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies "<actual_bottle_volume>" and "<actual_line_color>" were saved for "<mobile_phase>"

    Examples:
      | mobile_phase | actual_bottle_volume | actual_line_color | desired_bottle_volume | desired_line_color |
      | A            | 5L                   | green             | 2L                    | red                |
      | A            | 2L                   | red               | 4L                    | blue               |
      | B            | 4L                   | blue              | 5L                    | pink               |
      | C            | 5L                   | pink              | 4L                    | green              |
      | D            | 2L                   | green             | 5L                    | pink               |


  @real @weekly
  Scenario: User validate the default color for mobile phase line color sets the default colors for all mobile phases
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects the mobile phase "A" tab
    And User toggles the "A" toggle to "True"
    And User taps set all to default color
    And User taps Reset button
    Then User validate the "A" line color was set to "yellow"


  @real @weekly @quarantine @defect:INSISPP-8164
  Scenario: User validate the default colors for mobile phase will keep the colors for wash solvent configuration
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects "red" color for all solvent phases
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "A" tab
    And User toggles the "A" toggle to "True"
    And User taps set all to default color
    And User taps Reset button
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    Then User validates the solvent line colors "red"


  @real @weekly
  Scenario: User validate the default button for mobile phase line colors do not sets the default colors when user taps cancel
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects "red" color for all mobile phases
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    And User selects the mobile phase "A" tab
    And User toggles the "A" toggle to "True"
    And User taps set all to default color
    And User cancels the setting to default
    Then User validates the line colors "red"


  @real @weekly
  Scenario Outline:  To verify wash solvent configuration settings are being saved when changed
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    And User toggles the solvent "<wash_solvent>" toggle to "<toggle_status>"
    And User selects the solvent "<bottle_volume>" volume for "<wash_solvent>"
    And User selects the solvent "<line_color>" color for "<wash_solvent>"
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    When User selects the "<wash_solvent>" tab
    Then User verifies "<bottle_volume>" and "<line_color>" were saved for solvent "<wash_solvent>"

    Examples:
      | toggle_status | wash_solvent | bottle_volume | line_color |
      | true          | Needle_Wash  | 5L            | blue       |
      | true          | Needle_Wash  | 2L            | pink       |
      | true          | Seal_Wash    | 4L            | green      |
      | true          | Seal_Wash    | 5L            | red        |
      | true          | Seal_Wash    | 2L            | blue       |


  @real @weekly
  Scenario Outline: To verify the <toggle_status> for Wash Solvents
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    And User toggles the solvent "<wash_solvent>" toggle to "<toggle_status>"
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    Then User verifies the solvent "<wash_solvent>" toggle is "<toggle_status>"
    Examples:
      | wash_solvent | toggle_status |
      | Needle_Wash  | false         |
      | Seal_Wash    | false         |


  @real @weekly
  Scenario Outline: To verify the <toggle_status> for Wash Solvents is not updated when the user taps the cancel button
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    And User toggles the solvent "<wash_solvent>" toggle to "<initial_toggle_state>"
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    Then User verifies the solvent "<wash_solvent>" toggle is "<initial_toggle_state>"
    When User toggles the solvent "<wash_solvent>" toggle to "<set_toggle_state>"
    And User cancels the setting
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    Then User verifies the solvent "<wash_solvent>" toggle is "<initial_toggle_state>"

    Examples:
      | wash_solvent | initial_toggle_state | set_toggle_state |
      | Needle_Wash  | False                | True             |
      | Seal_Wash    | True                 | False            |


  @real @daily
  Scenario Outline: To verify Wash Solvent configuration settings are not updated when the user taps the cancel button
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    And User toggles the solvent "<wash_solvent>" toggle to "true"
    And User selects the solvent "<actual_bottle_volume>" volume for "<wash_solvent>"
    And User selects the solvent "<actual_line_color>" color for "<wash_solvent>"
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    And User selects the solvent "<desired_bottle_volume>" volume for "<wash_solvent>"
    And User selects the solvent "<desired_line_color>" color for "<wash_solvent>"
    And User cancels the setting
    And User taps Wash Solvent Configuration screen
    And User selects the "<wash_solvent>" tab
    Then User verifies "<actual_bottle_volume>" and "<actual_line_color>" were saved for solvent "<wash_solvent>"

    Examples:
      | wash_solvent | actual_bottle_volume | actual_line_color | desired_bottle_volume | desired_line_color |
      | Needle_Wash  | 5L                   | green             | 2L                    | blue               |
      | Needle_Wash  | 2L                   | red               | 4L                    | pink               |
      | Seal_Wash    | 4L                   | pink              | 5L                    | red                |
      | Seal_Wash    | 5L                   | blue              | 4L                    | red                |


  @real @weekly
  Scenario: User validate the default color for wash solvent line color sets the default colors
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects the "Needle_Wash" tab
    And User toggles the solvent "Needle_Wash" toggle to "true"
    And User taps set all to default solvent color
    And User taps Reset button
    Then User validate the solvent "Needle_Wash" line color was set to "white"


  @real @weekly  @quarantine @defect:INSISPP-8164
  Scenario: User validate the default colors for wash solvent will keep the colors for mobile phase configuration color
    When User taps System - Module Configuration - Solvents
    And User taps Mobile Phase Configuration screen
    And User selects "red" color for all mobile phases
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    And User selects the "Needle_Wash" tab
    And User toggles the solvent "Needle_Wash" toggle to "true"
    And User taps set all to default solvent color
    And User taps Reset button
    Then User confirms the changes
    When User taps Mobile Phase Configuration screen
    Then User validates the line colors "red"


  @real @weekly
  Scenario: User validate the default button for wash solvent line colors do not sets the default colors when user taps cancel
    When User taps System - Module Configuration - Solvents
    And User taps Wash Solvent Configuration screen
    And User selects "red" color for all solvent phases
    Then User confirms the changes
    When User taps Wash Solvent Configuration screen
    And User selects the "Needle_Wash" tab
    And User toggles the solvent "Needle_Wash" toggle to "true"
    And User taps set all to default solvent color
    And User cancels the setting to default
    Then User validates the solvent line colors "red"
