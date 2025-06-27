@ALIST-230 @method_editor @simulation @daily @pda @method_editor_stroke_volume @new @ignore
Feature: Method Editor | QSM Stroke volume
  The Stroke volume is the volume of mobile phase pumped between two consecutive moves of the plunger.
  The stroke volume can be set between a minimum and a maximum value

  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Stroke Volume menu is opened

      ### Scenario Testing Labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Stroke Volume menu title is "Stroke Volume"
    And the setting group title text is "Stroke Volume"
    And the Stroke Volume setting title is "Stroke Volume (µL)"
    And the Stroke Volume hint text is "66.00 to 132.00 µL"


      ### Scenarios testing favorites and filtering ###

  Scenario: Stroke Volume can be set as Favorite
    When the Stroke Volume setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Stroke Volume" menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Stoke Volume setting group is displayed
    And the "Pump" menu is highlighted

    Examples:
      | Search Text   |
      | Stroke        |
      | Stroke Volume |


      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "Pump" menu is highlighted
    And the "Stroke Volume" menu is highlighted
    And the Stroke Volume input has value set to "132.00"

  Scenario Outline: Stroke Volume valid value is accepted
    When the Stroke Volume input is set to valid value "<value>"
    Then the Stroke Volume input is not in error
    And no issue is raised

    Examples:
      | value  |
      | 66.00  |
      | 132.00 |

      # Potential defect #
  Scenario Outline: An issue is raised when the Stroke Volume is out of range
    When the Stroke Volume input is set to out of range value "<value>"
    Then the Stroke volume hint text is "66.00 to 132.00 µL"
    And the Stroke Volume input is in error
    And an issue is raised
    And the issue has title "Stroke Volume" and description "Invalid Range"

    Examples:
      | value    |
      | -5       |
      | 65.9999  |
      | 65.99    |
      | 132.0001 |
      | 132.01   |


      # Scenarios testing the mechanism for raising validation issues #

  Scenario: Stroke Volume validation issue is cleared when a valid value is entered
    Given the Stroke Volume input is in error
    When the Stroke Volume input is set to valid value "100.00"
    Then no issues are present

  Scenario: A Stroke Volume issue can be clicked to navigate to the Stroke Volume section
    Given the Stroke Volume input is in error
    And the System menu is opened
    When the "Stroke Volume" issue indicator is selected
    Then the Stroke Volume setting group is displayed


      ### Scenarios for testing the input fields ###

  Scenario Outline: Stroke Volume input does not accept unexpected input
    When the Stroke Volume input is set to "<value>"
    Then the Stroke Volume input is in error
    And the Stroke Volume input is empty
    And the Stroke Volume input hint text is "Required"
    And an issue is raised
    And the issue has title "Stroke Volume" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | !$%&        |
      | empty input |

      # Check if the value should be rounded_value in the input field

  Scenario Outline: Stroke Volume rounding when too many decimal places are entered
    When the Stroke Volume input is set to "<value>"
    Then the Stroke Volume summary text has value set to "<rounded_value>"
    And the Stroke Volume input has value set to "<rounded_value>"

    Examples:
      | value        | rounded_value |
      | 68.99999999  | 69.00         |
      | 70.651111111 | 70.65         |
      | 109.2581     | 109.26        |


      ### Scenario for Saving methods ###

  Scenario: Settings are saved and restored
    Given the Stroke Volume input is set to "100.00"
    When the method is saved
    Then there are no issues raised
    And the method is closed and reopened
    Then the Stroke Volume input is set to "100.00"
    And there are no issues raised

      # Potential defect. When saving the method an extra issue is raised which cannot be cleared
  Scenario: Stroke Volume input validation issue persists when method is reloaded
    Given the Stroke Volume input is in error
    Then a single issue is raised
    When the method is saved
    Then there is still a single issue raised
    And the method is closed and reopened
    Then there is still a single issue raised
