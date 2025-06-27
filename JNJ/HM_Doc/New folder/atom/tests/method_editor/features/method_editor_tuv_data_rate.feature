@method_editor @ALIST-230 @simulation @daily @tuv @tuv_bio @method_editor_tuv_data_rate @new @ignore
Feature: Method Editor | TUV Data Rate
  High data rates are needed for narrow peaks and low data rates for wide peaks.
  JIRA corresponding requirement: SRS-1386.

  Background:
    Given an acquisition method that contains default settings is opened
    And the TUV Detector menu is opened
    And the Data Rate menu is opened

      ### Scenario testing labels ###

  Scenario: Title and description are displayed
    Then the Data Rate menu title is "Data Rate"
    And the setting group title text is "Data Rate"
    And the Data Rate setting title is "Data Rate (Hz)"
    And the Data Rate setting summary is "Select the rate according to the expected peak widths"

      ### Scenarios testing favorites and filtering ###

  Scenario: Data Rate can be set as Favorite
    When the Data Rate setting group is set as Favorite
    And the Favorite menu is opened
    Then only the "Data Rate" menu title is displayed

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Data Rate setting group is displayed
    And the "TUV Detector" menu is highlighted

    Examples:
      | Search Text |
      | Data Rate   |
      | Hz          |

      ### Scenarios testing the default values and Data Rate options ###

  Scenario: Default setting is correct (Single Mode)
    Then the "TUV Detector" menu is highlighted
    And the "Data Rate" menu is highlighted
    And the Data Rate selector is set to "10"
    And Data Rate menu summary is "10 Hz"

  Scenario: Default setting is correct for Dual Mode
    Given the Wavelength Mode selector is set to "Dual"
    Then the Data Rate selector is set to "1"
    And Data Rate menu summary is "1 Hz"

  Scenario: Available options for Single Wavelength Mode
    When the Wavelength Mode selector is set to "Single"
    Then the Data Rate dropdown selector has the following options "Data Rate"
      | Data Rate |
      | 1         |
      | 2         |
      | 5         |
      | 10        |
      | 20        |
      | 40        |
      | 80        |
      | 160       |

  Scenario: Available options for Dual Wavelength Mode
    When the Wavelength Mode selector is set to "Dual"
    Then the Data Rate dropdown selector has the following options "Data Rate"
      | Data Rate |
      | 1         |
      | 2         |

  Scenario Outline: Data Rate setting is reset to default when switching the Wavelength Mode
    Given the Wavelength Mode selector is set to "<StartWavelengthMode>"
    And the Data Rate selector is set to "<StartDataRate>"
    When the Wavelength Mode selector is set to "<EndWavelengthMode>"
    Then the Data Rate selector is set to "<EndDataRate>"

    Examples:
      | StartWavelengthMode | StartDataRate | EndWavelengthMode | EndDataRate |
      | Single              | 40            | Dual              | 1           |
      | Dual                | 2             | Single            | 10          |

      ### Scenarios for saving methods ###

  Scenario Outline: Data Rate setting can be saved - Single
    Given the Data Rate selector is set to "<Data Rate>"
    When the method is saved
    And the method is closed and reopened
    Then the Data Rate selector is set to "<Data Rate>"
    And the Data Rate menu summary is set to "<Data Rate>"

    Examples:
      | Data Rate |
      | 1         |
      | 20        |
      | 160       |

  Scenario Outline: Data Rate setting can be saved - Dual
    Given the Wavelength Mode selector is set to "Dual"
    And the Data Rate selector is set to "<Data Rate>"
    When the method is saved
    And the method is closed and reopened
    Then the Data Rate selector is set to "<Data Rate>"
    And the Data Rate menu summary is set to "<Data Rate>"

    Examples:
      | Data Rate |
      | 1         |
      | 2         |