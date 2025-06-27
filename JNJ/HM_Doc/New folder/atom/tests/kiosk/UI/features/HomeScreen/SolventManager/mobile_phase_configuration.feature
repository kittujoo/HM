@kiosk @kiosk_mobile_phase_feature @ALIST-228
Feature: Kiosk | Mobile Phase Configuration
  # Notify on Low level Solvent and Notify when solvent is about to expire will be test at system level


  @real @weekly
  Scenario Outline:  To verify mobile phase configuration settings are being saved when changed
    When User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<toggle_status>"
    And User selects the "<bottle_volume>" volume for "<mobile_phase>"
    And User selects the "<line_color>" color for "<mobile_phase>"
    And User confirms the changes
    And User navigates to home screen
    Then User confirms the color of the "<mobile_phase>" bottle in the schematic icon home page is "<line_color>"
    When User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies "<bottle_volume>" and "<line_color>" were saved for "<mobile_phase>"

    Examples:
      | mobile_phase | toggle_status | bottle_volume | line_color |
      | A            | true          | 5L            | red        |
      | B            | true          | 4L            | pink       |
      | C            | true          | 2L            | blue       |
      | D            | true          | 4L            | green      |
      | Seal         | true          | 5L            | red        |

  @simulation @weekly
  Scenario Outline: To verify mobile phase configuration settings are not saving when cancelled
    When User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<toggle_status>"
    And User selects the "<bottle_volume>" volume for "<mobile_phase>"
    And User selects the "<line_color>" color for "<mobile_phase>"
    And User confirms the changes
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User selects the "<new_bottle_volume>" volume for "<mobile_phase>"
    Then User cancels the changes
    When User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    Then User verifies "<bottle_volume>" and "<line_color>" were not changed for "<mobile_phase>"

    Examples:
      | mobile_phase | toggle_status | bottle_volume | line_color | new_bottle_volume |
      | A            | true          | 4L            | pink       | 5L                |

  @simulation @weekly
  Scenario Outline: To verify the mobile phase badge status when toggling
    When  User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "<toggle_status>"
    Then User validates the "<mobile_phase>" and installation status "<installation_status>"
    When User confirms the changes
    And User navigates to home screen
    Then User validates the "<mobile_phase>" is "<configure_status>"

    Examples:
      | mobile_phase | toggle_status | installation_status | configure_status |
      | A            | false         | uninstalled         | not displayed    |
      | A            | true          | installed           | displayed        |
      | B            | false         | uninstalled         | not displayed    |
      | B            | true          | installed           | displayed        |
      | C            | false         | uninstalled         | not displayed    |
      | C            | true          | installed           | displayed        |
      | D            | false         | uninstalled         | not displayed    |
      | D            | true          | installed           | displayed        |
      | Seal         | false         | uninstalled         | not displayed    |
      | Seal         | true          | installed           | displayed        |
      | Needle       | false         | uninstalled         | not displayed    |
      | Needle       | true          | installed           | displayed        |


  @simulation @weekly
  Scenario Outline:  To validate the prime solvent process
    When  User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "true"
    And User confirms the changes
    And User taps the prime solvent panel
    And User sets the prime duration "<prime_duration>"
    And User starts the prime cycle
    Then User validates the prime cycle was completed within "<max_prime_time>"

    Examples:
      | mobile_phase | prime_duration | max_prime_time |
      | A            | 02:00          | 180            |
      | B            | 02:00          | 180            |
      | C            | 02:00          | 180            |
      | D            | 02:00          | 180            |
      | Seal         | 02:00          | 300            |
      | Needle       | 10 Cycle       | 300            |


  @simulation @weekly
  Scenario Outline: To validate the user can stop the prime in progress
    When User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "true"
    And User confirms the changes
    And User taps the prime solvent panel
    And User sets the prime duration "<prime_duration>"
    And User starts the prime cycle
    And User stops the prime cycle
    Then User validates the status screen after aborting

    Examples:
      | mobile_phase | prime_duration |
      | A            | 02:00          |
      | B            | 02:00          |
      | C            | 02:00          |
      | D            | 02:00          |
      | Seal         | 02:00          |
      | Needle       | 10 Cycle       |


  @simulation @weekly
  Scenario Outline: To validate the features of replacing a solvent
    Given User sets date and time format
    When User taps the mobile phase "<mobile_phase>" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "<mobile_phase>" tab
    And User toggles the "<mobile_phase>" toggle to "true"
    And User selects the "<bottle_volume>" volume for "<mobile_phase>"
    And User confirms the changes
    And User taps the replace solvent panel
    And User sets the solvent level "<solvent_level>"
    Then User validates the solvent level is set to "<solvent_level>"
    When User sets the "<solvent_expire_month>", "<solvent_expire_day>", and "<solvent_expire_year>"
    And User sets the prepared by name "<prepared_by_name>"
    And User sets the solvent name "<solvent_name>"
    And User enters the solvent note "<solvent_note>"
    And User taps the replace solvent panel
    Then User validates the following were saved: "<solvent_level>", "<solvent_expire_month>", "<solvent_expire_day>", "<solvent_expire_year>", "<prepared_by_name>", "<solvent_name>", and "<solvent_note>"
    And User validates the following in the solvent details screen: "<solvent_level>", "<solvent_expire_month>", "<solvent_expire_day>", "<solvent_expire_year>", "<prepared_by_name>", "<solvent_name>", and "<solvent_note>" for "<bottle_volume>"

    Examples:
      | mobile_phase | solvent_level | solvent_expire_month | solvent_expire_day | solvent_expire_year | prepared_by_name | solvent_name | solvent_note | bottle_volume |
      | A            | 3/8 Full      | October              | 15                 | 2024                | Analyst          | Buffer       | testnotes    | 5L            |
      | B            | 1/2 Full      | May                  | 20                 | 2024                | Analyst          | Phosphate    | note test    | 4L            |
      | C            | 3/4 Full      | December             | 6                  | 2024                | Analyst          | Ammonia      | notetest    | 2L            |
      | D            | Full          | December             | 27                 | 2024                | Analyst          | Buffer       | testdata     | 5L            |
      | Seal         | 3/8 Full      | December             | 10                 | 2024                | Analyst          | Buffer       | testdata     | 5L            |
      | Needle       | Empty         | December             | 27                 | 2024                | Analyst          | Buffer       | testdata     | 5L            |


  @simulation @weekly
  Scenario: To validate the features of adding/changing/deleting a new analyst name
    When User taps the mobile phase "A" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "A" tab
    And User toggles the "A" toggle to "true"
    And User confirms the changes
    And User taps the replace solvent panel
    And User taps the prepared by tab
    When User press the add button
    And User enters "Analyst 63"
    And User saves the changes
    Then the "Analyst 63" is displayed
    And the "Analyst 63" is updated
    When User press the edit button
    And User enters "Analyst 85"
    And User saves the changes
    Then the "Analyst 85" is displayed
    When User press the edit button
    And User enters "Testing is the important"
    Then User validates "14" is the max number of the characters that can be written
    When User saves the changes
    When User press the - button
    And User confirms deletion
    Then User Confirms the "Analyst 85" is deleted


  @simulation @weekly
  Scenario: To validate the features of adding/changing/deleting a new solvent name
    When User taps the mobile phase "B" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "B" tab
    And User toggles the "B" toggle to "true"
    And User confirms the changes
    And User taps the replace solvent panel
    And User taps the solvent name tab
    And User press the add solvent
    And User enters "Solvent 25"
    And User saves the changes
    Then the "Solvent 25" is displayed
    When User press the edit solvent button
    And User enters "Solvent 2024"
    And User saves the changes
    Then the "Solvent 2024" is displayed
    When User press the edit solvent button
    And User enters "Testing is the important"
    Then User validates "14" is the max number of the characters that can be written
    When User saves the changes
    And User press the - solvent button
    And User confirms deletion
    Then User Confirms the "Solvent 2024" is deleted


  @simulation @weekly
  Scenario: To validate the features of adding/changing note
    When User taps the mobile phase "Seal" condition card
    And User taps the configure solvent panel
    And User selects the mobile phase "Seal" tab
    And User toggles the "Seal" toggle to "true"
    And User confirms the changes
    And User taps the replace solvent panel
    And User taps the notes tab
    And User enters "Note 2025"
    And User saves the changes
    Then the "Note 2025" is displayed
    When User taps the notes tab
    And User enters "Each logged item shall include an optional detailed description. The log item detail view shall be displayed."
    Then User validates "100" is the max number of the characters that can be written