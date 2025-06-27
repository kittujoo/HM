  """

Feature to validate plate layout

  """

@ics @simulation @daily @ics_plate_layout_feature @new @ignore
Feature: Select plate layout for Alliance iS

  Background:
    Given the window for define plates for sample set method section layout is already open

  Scenario Outline: Selecting different types of plate type plate position
    Given the system is configured with "<Plate type>"
    And the define plates for sample set method section window is open

    When the define plates position "<Plate position>" is selected
    Then the plate position is active

    When the dropdown menu from position "<Plate position>" is selected
    And the entry from the dropdown menu "<Plate type>" is selected
    And the vial position "<Vial position>" is selected
    Then vial "<Vial position>" position is active for plate position "<Plate position>"

    When the define plates for sample set method window is closed with "Ok"
    Then the plate and vial position should be available in the sample set window

    Examples:
      | Plate position | Plate type           | Vial position |
      | 1              | ANSI-48Vial2mLHolder | A,1           |
      | 2              | ANSI-384well100ul    | A,1           |
      | 3              | ANSI-96well2mL       | A,1           |
      | 1              | ANSI-48Vial2mLHolder | F,8           |
      | 2              | ANSI-384well100ul    | F,8           |
      | 3              | ANSI-96well2mL       | F,8           |

  Scenario Outline: Fixed vial positions
    Given the define plates for sample set method section window is open

    When the fixed vial position "<Fixed vial position>" is selected
    Then the fixed vial position is active

    When the define plates for sample set method window is closed with "Ok"
    Then the fixed vial position should be available in the sample set window

    Examples:
      | Fixed vial position |
      | V:1                 |
      | V:6                 |
      | V:10                |