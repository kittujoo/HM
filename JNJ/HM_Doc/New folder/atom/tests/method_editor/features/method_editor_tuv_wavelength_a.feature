@method_editor @ALIST-230 @simulation @daily @tuv @tuv_bio @method_editor_tuv_wavelength_a @new @ignore
Feature: Method Editor | TUV Detector Wavelength A
  The TUV detector can collect data for the specified wavelength.
  JIRA corresponding requirement: SRS-1290, SR-1695, SRS-1385.

  Background:
    Given an acquisition method that contains default settings is opened
    And the TUV Detector menu is opened
    And the Wavelength A menu is opened

      ### Scenario testing labels ###

  Scenario: Titles and descriptions are displayed
    Then the Wavelength A menu title is "Wavelength A"
    And the setting group title is "Wavelength A"
    And the Wavelength setting title is "Wavelength (nm)"
    And the Wavelength setting hint text is "190 to 700 nm"

      ### Scenarios testing favorites and filering ###

  Scenario: Wavelength A can be set as Favorite
    When the Wavelength A setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Wavelength A" menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "Search Text" is entered into the search bar
    Then the Wavelength A setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text  |
      | Wavelength   |
      | Wavelength A |

      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "TUV Detector" menu is highlighted
    And the "Wavelength A" menu is highlighted
    And the Wavelength A input has value set to "254"
    And the Wavelength A menu summary is "254 nm"

  Scenario Outline: Wavelength A valid value is accepted
    When the Wavelength A input is set to "<value>"
    Then the Wavelength A input is not in error
    And no issue is raised
    And the Wavelength A menu summary is "<value> nm"

    Examples:
      | value |
      | 190   |
      | 700   |

      ### Scenario testing that Wavelength A value is kept when Wavelength Mode is toggled ###

  Scenario: Wavelength A value is kept when switching to Dual Wavelength Mode
    Given the Wavelength Mode selector is set to "Single"
    And the Wavelength A input has value set to "205"
    When the Wavelength Mode selector is set to "Dual"
    Then the Wavelength A input has value still set to "205"
    When the Wavelength Mode selector is set back to "Single"
    Then the Wavelength A input has value "205"

      ### Scenarios testing the mechanism for raising validation issues ###

  Scenario Outline: An issue is raised when the Wavelength A value is out of range
    When the Wavelength A input is set to an out of range value "<value>"
    Then the Wavelength A input is in error
    And an issue is raised
    And the issue has title "Wavelength A" and description "Invalid Range"

    Examples:
      | value |
      | 189   |
      | 700.1 |

  Scenario: Wavelength A validation issue is kept when Wavelength mode is changed to Dual
    Given the Wavelength Mode selector is set to "Single"
    And the Wavelength A input is in error
    When the Wavelength Mode selector is set to "Dual"
    Then the Wavelength A input is still in error
    And the Wavelength A issue is still raised

  Scenario: Wavelength valiation issue is cleared when a valid value is entered
    Given the Wavelength A input is in error
    When the Wavelength A value is set to valid value "500"
    Then the Wavelength A input has value set to "500"
    And the Wavelength A input is not in error
    And no issues are present

  Scenario: A Wavelength A issue can be clicked to navigate to the Wavelength A section
    Given the Wavelength A input is in error
    And the System menu is opened
    When the "Wavelength A" issues indicator is selected
    Then the Wavelength A setting group is displayed

      ### Scenario testing the input fields ###

  Scenario Outline: Wavelength A does not accept unexpected input
    When the Wavelength A input is set to "<value>"
    Then the Wavelength A input is in error
    And the Wavelength A input is empty
    And the Wavelength A setting input hint text is "Required"
    And an issue is raised
    And the issue has title "Wavelength A" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

      ### Scenarios for saving methods ###

  Scenario: Settings are saved and restored
    Given the Wavelength A input is set to valid value "300"
    When the method is saved
    And the method is closed and reopened
    Then the Wavelength A input is set to "300"

  Scenario: Wavelength A input valiation issue is kept when method is reloaded
    Given the Wavelength A input is in error
    Then an issue is raised
    When the method is saved
    Then there is still a single issue raised
    When the method is closed and reopened
    Then there is still a single issue raised