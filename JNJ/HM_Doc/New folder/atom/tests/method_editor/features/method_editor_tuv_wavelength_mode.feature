@method_editor @ALIST-230 @simulation @daily @tuv @tuv_bio @method_editor_tuv_wavelength_mode @new @ignore
Feature: Method Editor | TUV Detector Wavelength Mode
  The TUV Detector can be configured to collect data for one or two wavelengths.
  JIRA corresponding requirement: SRS-1290.

  Background:
    Given an acquisition method that contains default settings is opened
    And the TUV Detector menu is opened
    And the Wavelength Mode menu is opened

  Scenario: Title and description are displayed
    Then the Wavelength Mode menu title is "Wavelength Mode"
    And the setting group title is "Wavelength Mode"
    And the Wavelength Mode setting title is "Wavelength Mode"
    And the Wavelength Mode setting summary is "Limit use of Dual mode to more standard chromatography where peaks span at least 20 seconds"

  Scenario: Wavelength Mode can be set as Favorite
    When the Wavelength Mode setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Wavelength Mode" menu title is available

  Scenario Outline: Wavelength Mode setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Wavelength Mode setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text     |
      | Wavelength mode |
      | Single mode     |
      | Dual mode       |

  Scenario: Default settings are correct
    Then the "TUV Detector" menu is highlighted
    And the "Wavelength Mode" menu is highlighted
    And the Wavelength Mode selector is set to "Single"
    And the Wavelength Mode menu summary is "Single mode"
    And Wavelength B is not displayed in the TUV Detector menu
    And Data Rate menu summary is "10 Hz"
    And Filter menu summary is "Normal (0.2s)"

  Scenario: Default settings are correct when selecting Dual Mode
    When the Wavelength Mode selector is set to "Dual"
    Then the Wavelength Mode menu summary is "Dual mode"
    And Wavelength B menu is displayed in TUV Detector menu
    And Wavelength B menu summary is "230 nm"
    And Data Rate menu summary is "1 Hz"
    And Filter menu summary is "Normal (2 s)"

  Scenario Outline: Setting is saved and restored
    Given the Wavelength Mode is set to "<Wavelength Mode>"
    When the method is saved
    And the method is closed and reopened
    Then the Wavelength Mode is set to "<Wavelength Mode>"

    Examples:
      | Wavelength Mode |
      | Single          |
      | Dual            |
