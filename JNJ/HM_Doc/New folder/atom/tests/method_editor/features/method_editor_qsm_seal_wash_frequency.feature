@method_editor @ALIST-230 @simulation @daily @pda @tuv_bio @pda_bio @method_editor_seal_wash_frequency @new @ignore
Feature: Method Editor | QSM Seal Wash Frequency
  The QSM controls the seal wash time frequency.

  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Seal Wash Frequency menu is opened

      ### Scenario testing labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Seal Wash Frequency menu title is "Seal Wash Frequency"
    And the setting group title is "Seal Wash Frequency"
    And the setting group summary text is "Every 0.02 minutes"
    And the Seal Wash Frequency setting title is "Seal Wash Frequency (min)"
    And the Seal Wash Frequency setting summary is "Number of minutes between seal wash cycles"

      ### Scenarios testing favorites and filtering ###

  Scenario: Seal Wash Frequency can be set as Favorite
    When the Seal Wash Frequency setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Seal Wash Frequency" menu title is available

      ### Works only for Seal at the moment and returns 3 options  ###

  Scenario Outline: Seal Wash Frequency setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Seal Wash Frequency setting group is displayed
    And the "Pump" menu is highlighted

    Examples:
      | Search Text         |
      | Seal                |
      | Seal Wash           |
      | Seal Wash Frequency |


      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default setting is correct
    Then the "Pump" menu is highlighted
    And the "Seal Wash Frequency" menu is highlighted
    And the Seal Wash Frequency input has value set to "0.02"
    And the Seal Wash Frequency summary menu value is "Every 0.02 min"

  Scenario Outline: Seal Wash Frequency valid value is accepted
    When the Seal Wash Frequency input is set to "<value>"
    Then the Seal Wash Frequency input is not in error
    And no issue is raised
    And the Seal Wash Frequency summary menu value is "Every <value> min"

    Examples:
      | value |
      | 0.02  |
      | 60.00 |


      ### Scenario testing the mechanism for validation issues ###

  Scenario Outline: An issue is raised when the Wash Time is out of range
    When the Seal Wash Frequency input is set to an out of range value "<value>"
    Then the Seal Wash Frequency input is in error
    And the Seal Wash Frequency summary menu value is "Every <summary_menu_value> min"
    And an issue is raised
    And the issue has title "Seal Wash Frequency" and description "Invalid Range"

    Examples:
      | value  | summary_menu_value |
      | 60.01  | 60.01              |
      | 120.00 | 120.00             |


  Scenario: Hint text changes when Seal Wash Frequency input is empty
    When the Seal Wash Frequency input is set to "empty string"
    Then the Seal Wash Frequency input is in error
    And an issue is raised
    And the issue has title "Seal Wash Frequency" and description "Invalid Range"
    And the Seal Wash Frequency setting input hint text is "Required"


  Scenario: A Seal Wash Frequency issue can be clicked to navigate to the Seal Wash Frequency section
    Given the Seal Wash Frequency input is in error
    And the System menu is opened
    When the "Seal Wash Frequency" issue indicator is selected
    Then the Seal Wash Frequency setting group is displayed

  Scenario: Seal Wash Frequency validation issue is cleared when a valid value is entered
    Given the Seal Wash Frequency input is in error
    When the Seal Wash Frequency input is set to valid value "30"
    Then the Seal Wash Frequency input has value set to "30"
    And the Seal Wash Frequency input is not in error
    And no issues are present


      ### Scenarios for saving methods ###

  Scenario: Settings are saved and restored
    Given the Seal Wash Frequency input is set to "15"
    When the method is saved
    And the method is closed and reopened
    Then the Seal Wash Frequency input is set to "15"


  Scenario: Seal Wash Frequency validation issue persists through saving and no other issues are raised
    Given the Seal Wash Frequency is in error
    And a single issue is raised
    When the method is saved
    And the method is closed and reopened
    Then there is still a single issue raised