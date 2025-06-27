@method_editor @ALIST-230 @simulation @daily @pda @tuv_bio @pda_bio @method_editor_wash_time_feature
Feature: Method Editor | FTN Wash Time
  The Sample Manager controls the needle wash time between injections.
  JIRA corresponding requirement: SRS-1404

  Background:
    Given an acquisition method that contains default settings is open
    And the Sample Manager menu is opened
    And the Wash Time menu is open

  Scenario: Titles and descriptions are displayed - default view
    Then the Wash Time menu title is "Wash Time"
    And the setting group title is "Wash Time"
    And the Wash Time setting title is "Wash Time (s)"
    And the Wash Time setting summary is "Specify time for additional needle washing between injections"
    And the Wash Time setting input hint text is "4.0 to 120.0 s"

  Scenario: Wash Time can be set as Favorite
    When the Wash Time setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Wash Time" menu title is displayed

  @quarantine @defect:INSSYS-299
  Scenario Outline: Wash Time setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Wash Time setting group is displayed
    And the "Sample Manager" menu is highlighted

    Examples:
      | Search Text |
      | Wash        |
      | Wash Time   |

  Scenario: Default setting is correct
    Then the "Sample Manager" menu is highlighted
    And the "Wash Time" menu is highlighted
    And the Wash Time input has value set to "6"
    And the Wash Time summary menu value is "6.0 s"


  Scenario Outline: Wash Time valid min and max value is accepted
    When the Wash Time input is set to "<value>"
    Then the Wash Time input is not in error
    And no issue is raised
    And the Wash Time summary menu value is "<value> s"

    Examples:
      | value |
      | 4.0   |
      | 120.0 |

  Scenario Outline: An issue is raised when the Wash Time is out of range
    When the Wash Time input is set to an out of range value "<value>"
    Then the Wash Time input is in error
    And the Wash Time summary menu value is "<summary_menu_value> s"
    And an issue is raised
    And the issue has title "Wash Time" and description "Invalid Range"

    Examples:
      | value | summary_menu_value |
      | -     | 0.0                |
      | 3.9   | 3.9                |
      | 120.1 | 120.1              |

  Scenario Outline: When the Wash Time input value has more than one decimal it is removed
    When the Wash Time input is set to "<value>"
    Then the Wash Time input is not in error
    And no issue is raised
    And the Wash Time summary menu value is "<summary_menu_value> s"
    And the Wash Time input has value set to "<summary_menu_value>"

    Examples:
      | value  | summary_menu_value |
      | 5.99   | 5.9                |
      | 112.22 | 112.2              |

  Scenario: A Wash Time issue can be clicked to navigate to the Wash Time section
    Given the Wash Time input is in error
    And the System menu is opened
    When the "Wash Time" issue indicator is selected
    Then the Wash Time setting group is displayed


  Scenario: Wash Time validation issue is cleared when a valid value is entered
    Given the Wash Time input is in error
    When the Wash Time input is set to "7"
    Then the Wash Time input has value set to "7"
    And the Wash Time input is not in error
    And no issues are present

  Scenario Outline: Wash time rounding when too many decimal places are entered
    When the Wash Time input is set to "<value>"
    Then the Wash Time input has value set to "<rounded_value>"
    And the Wash Time menu summary is rounded to 1 decimal place showing "<rounded_value> s"

    Examples:
      | value  | rounded_value |
      | 5.99   | 5.9           |
      | 10.585 | 10.5          |

  Scenario Outline: Wash Time does not accept unexpected input
    When the Wash Time input is set to "<value>"
    Then the Wash Time input is in error
    And the Wash Time input is empty
    And the Wash Time setting input hint text is "Required"
    And the Wash Time summary menu value is "0.0 s"
    And an issue is raised
    And the issue has title "Wash Time" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

  Scenario: Settings are saved and restored
    Given the Wash Time input is set to "15.0"
    When the method is saved
    And the method is closed and reopened
    And the Sample Manager menu is opened
    And the Wash Time menu is open
    Then the Wash Time summary menu value is "15.0 s"
    And the Wash Time input has value set to "15"

  @defect:INSSYS-299
  Scenario: Wash Time validation issue raised when reopening a method with parameters out of range
    Given the Wash Time input is in error
    When the method is saved
    And the method is closed and reopened
    Then an issue is still raised
