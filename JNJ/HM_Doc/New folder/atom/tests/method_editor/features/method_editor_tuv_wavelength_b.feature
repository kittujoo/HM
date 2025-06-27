@method_editor @ALIST-230 @simulation @daily @tuv @tuv_bio @method_editor_tuv_wavelength_b @new @ignore
Feature: Method Editor | TUV Detector Wavelength B
  The TUV detector can collect data for the specified wavelength.
  JIRA corresponding requirement: SRS-1290, SR-1695, SRS-1385.

  Background:
    Given an acquisition method that contains default settings is opened
    And the TUV Detector menu is opened
    And the Wavelength Mode selector is set to "Dual"
    And the Wavelength B menu is opened

      ### Scenario testing labels ###

  Scenario: Titles and descriptions are displayed
    Then the Wavelength B menu title is "Wavelength B"
    And the setting group title is "Wavelength B"
    And the Wavelength setting title is "Wavelength (nm)"
    And the Wavelength setting hint text is "190 to 700 nm"

      ### Scenario testing changes of the Wavelength Mode ###
  Scenario: Wavelength B setting group is not displayed when switching to Single Mode
    When the Wavelength Mode selector is set to "Single"
    And the TUV Detector Menu is open
    Then the Wavelength B setting group is not displayed

      ### Scenarios testing favorites and filering ###

  Scenario: Wavelength B can be set as Favorite
    When the Wavelength B setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Wavelength B" menu title is available

  @quarantine @defect:INSISPP-8338
  Scenario: Wavelength B is removed from Favorites when switching to Single Wavelength Mode
    Given the Wavelength B setting group is set as Favorite
    When the Wavelength Mode selector is set to "Single"
    And the Favorite Settings menu is opened
    Then the "Wavelength B" menu title is not displayed

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "Search Text" is entered into the search bar
    Then the Wavelength B setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text  |
      | Wavelength   |
      | Wavelength B |

      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "TUV Detector" menu is highlighted
    And the "Wavelength B" menu is highlighted
    And the Wavelength B input has value set to "230"
    And the Wavelength B menu summary is "230 nm"

  Scenario Outline: Wavelength B valid value is accepted
    When the Wavelength B input is set to "<value>"
    Then the Wavelength B input is not in error
    And no issue is raised
    And the Wavelength B menu summary is "<value> nm"

    Examples:
      | value |
      | 190   |
      | 700   |

  @quarantine @defect:INSISPP-8355
  Scenario: Wavelength B value is reset to default when the Wavelength Mode is toggled
    Given the Wavelength B is in error
    When the Wavelength Mode selector is set to "Single" and back to "Dual"
    Then the Wavelength B input has default value set to "230"

      ### Scenarios testing the mechanism for raising validation issues ###

  Scenario Outline: An issue is raised when the Wavelength B value is out of range
    When the Wavelength B input is set to an out of range value "<value>"
    Then the Wavelength B input is in error
    And an issue is raised
    And the issue has title "Wavelength B" and description "Invalid Range"

    Examples:
      | value |
      | 189.9 |
      | 701   |

  Scenario: Wavelength valiation issue is cleared when a valid value is entered
    Given the Wavelength B input is in error
    When the Wavelength B value is set to valid value "500"
    Then the Wavelength B input has value set to "500"
    And the Wavelength B input is not in error
    And no issues are present

  Scenario: A Wavelength B issue can be clicked to navigate to the Wavelength B section
    Given the Wavelength B input is in error
    And the System menu is opened
    When the "Wavelength B" issues indicator is selected
    Then the Wavelength B setting group is displayed

  @quarantine @defect:INSISPP-8354
  Scenario: Wavelength B issue is cleared when Wavelength Mode is changed to Single
    Given the Wavelength B input is in error
    And an issue is raised
    When the Wavelength Mode selector is set to "Single"
    Then no issues are raised

      ### Scenario testing the input field ###

  Scenario Outline: Wavelength B does not accept unexpected input
    When the Wavelength B input is set to "<value>"
    Then the Wavelength B input is in error
    And the Wavelength B input is empty
    And the Wavelength B setting input hint text is "Required"
    And an issue is raised
    And the issue has title "Wavelength B" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

      ### Scenarios for saving methods ###

  Scenario: Settings are saved and restored
    Given the Wavelength B input is set to valid value "300"
    When the method is saved
    And the method is closed and reopened
    Then the Wavelength B input is set to "300"

  Scenario: Wavelength B input valiation issue is kept when method is reloaded
    Given the Wavelength B input is in error
    Then an issue is raised
    When the method is saved
    Then there is still a single issue raised
    When the method is closed and reopened
    Then there is still a single issue raised