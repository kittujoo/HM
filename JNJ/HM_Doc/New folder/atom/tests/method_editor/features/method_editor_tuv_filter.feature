@method_editor @ALIST-230 @simulation @daily @tuv_bio @method_editor_tuv_filter @new @ignore
Feature: Method Editor | TUV Filter
  The Filter Time Constant smoothes the data and reduces the noise from the detector.
  JIRA corresponding requirement: SRS-1291.


  Background:
    Given an acquisition method that contains default settings is opened
    And the TUV Detector menu is opened
    And the Filter menu is opened

      ### Scenarios testing labels ###

  Scenario: Titles and descriptions are displayed - Default view
    Then the Filter menu title is "Filter"
    And the setting group title is "Set Data Filter"
    And the Set Data Filter setting summary is "Enable to apply filter during acquisition"
    And the Filter Mode setting title is "Filter Mode"
    And the Filter Mode setting summary is "Select a present filter time constant or select Custom and enter a value"
    And the Filter Time Constant setting title is "Filter Time Constant (s)"
    And the Filter Time Constant setting summary is "Available filter time constants depend on the set data rate"

  Scenario: Titles and descriptions are displayed - Set Data Filter disabled
    When the Set Data Filter selector is set to "Off"
    Then no settings for filter are displayed

      ### Scenarios testing favorites and filtering ###

  Scenario: Filter can be set as Favorite
    When the Filter setting group is set as Favorite
    And the Favorites menu is opened
    Then only the "Filter" menu title is displayed

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Filter setting group is displayed
    And the "TUV Detector"  menu is highlighted

    Examples:
      | Search Text          |
      | Filter               |
      | Filter Time Constant |

      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "TUV Detector" menu is highlighted
    And the "Filter" menu is highlighted
    And the Set Data Filter selector is set to "On"
    And the Filter Mode selector is set to "Normal"

      ### Hint Text is rounded when compared to requirement for 40, 80 and 160 Hz; the values for 80 Hz are out of range ###
  @quarantine @defect:INSISPP-8430
  Scenario Outline: Filter Modes, hint texts, Filter Time Constants and Menu Summaries are correct
    When the Wavelength Mode selector is set to "<Wavelength Mode>"
    And the Data Rate selector is set to "<Data Rate>"
    And the Filter Mode selector is set to "<Filter Mode>"
    Then the Filter Time Constant input is read-only
    And the Filter Time Constant input has value set to "<Filter Time Constant>"
    And the Filter Time Constant hint text is "<Hint Text>"
    And the Filter menu summary is "<Menu Summary>"

    Examples:
      | Wavelength Mode | Data Rate | Filter Mode | Filter Time Constant | Hint Text            | Menu Summary      |
      | Single          | 1         | Slow        | 4                    | 0.50000 to 5.00000 s | Slow (4 s)        |
      | Single          | 1         | Normal      | 2                    | 0.50000 to 5.00000 s | Normal (2 s)      |
      | Single          | 1         | Fast        | 1                    | 0.50000 to 5.00000 s | Fast (1 s)        |
      | Dual            | 1         | Slow        | 4                    | 0.50000 to 5.00000 s | Slow (4 s)        |
      | Dual            | 1         | Normal      | 2                    | 0.50000 to 5.00000 s | Normal (2 s)      |
      | Dual            | 1         | Fast        | 1                    | 0.50000 to 5.00000 s | Fast (1 s)        |
      | Single          | 2         | Slow        | 2                    | 0.25000 to 5.00000 s | Slow (2 s)        |
      | Single          | 2         | Normal      | 1                    | 0.25000 to 5.00000 s | Normal (1 s)      |
      | Single          | 2         | Fast        | 0.5                  | 0.25000 to 5.00000 s | Fast (0.5 s)      |
      | Dual            | 2         | Slow        | 2                    | 0.25000 to 5.00000 s | Slow (2 s)        |
      | Dual            | 2         | Normal      | 1                    | 0.25000 to 5.00000 s | Normal (1 s)      |
      | Dual            | 2         | Fast        | 0.5                  | 0.25000 to 5.00000 s | Fast (0.5 s)      |
      | Single          | 5         | Slow        | 0.8                  | 0.10000 to 5.00000 s | Normal (0.8 s)    |
      | Single          | 5         | Normal      | 0.4                  | 0.10000 to 5.00000 s | Normal (0.4)      |
      | Single          | 5         | Fast        | 0.2                  | 0.10000 to 5.00000 s | Fast (0.2 s)      |
      | Single          | 10        | Slow        | 0.4                  | 0.10000 to 5.00000 s | Slow (0.4 s)      |
      | Single          | 10        | Normal      | 0.2                  | 0.10000 to 5.00000 s | Normal (0.2 s)    |
      | Single          | 10        | Fast        | 0.1                  | 0.10000 to 5.00000 s | Fast (0.1 s)      |
      | Single          | 20        | Slow        | 0.2                  | 0.05000 to 2.50000 s | Slow (0.2 s)      |
      | Single          | 20        | Normal      | 0.1                  | 0.05000 to 2.50000 s | Normal (0.1 s)    |
      | Single          | 20        | Fast        | 0.05                 | 0.05000 to 2.50000 s | Fast (0.05 s)     |
      | Single          | 40        | Slow        | 0.1                  | 0.02500 to 1.25000 s | Slow (0.1 s)      |
      | Single          | 40        | Normal      | 0.05                 | 0.02500 to 1.25000 s | Normal (0.05) s   |
      | Single          | 40        | Fast        | 0.025                | 0.02500 to 1.25000 s | Fast (0.025 s)    |
      | Single          | 80        | Slow        | 0.05                 | 0.01250 to 0.62500 s | Slow (0.05 s)     |
      | Single          | 80        | Normal      | 0.025                | 0.01250 to 0.62500 s | Normal (0.025 s)  |
      | Single          | 80        | Fast        | 0.0125               | 0.01250 to 0.62500 s | Fast (0.0125 s)   |
      | Single          | 160       | Slow        | 0.025                | 0.00625 to 0.31250 s | Slow (0.025 s)    |
      | Single          | 160       | Normal      | 0.0125               | 0.00625 to 0.31250 s | Normal (0.0125 s) |
      | Single          | 160       | Fast        | 0.00625              | 0.00625 to 0.31250 s | Fast (0.00625 s)  |


      ### Hint Text is rounded when compared to requirement, the values are out of range ###
      ### Default values for Data Rate values 1 and 2 Hz are out of range and an issue is raised ###
  @quarantine @defect:INSISPP-8430 @defect:INSISPP-8429
  Scenario Outline: Custom Filter Time Constant default values are correct
    When the Wavelength Mode selector is set to "<Wavelength Mode>"
    And the Data Rate selector is set to "<Data Rate>"
    And the Filter Mode selector is set to "Custom"
    Then the Filter Time Constant input is "<Filter Time Constant Default>"
    And the Filter Time Constant input hint text is "<Hint Text>"
    And the Filter menu summary is "<Filter Menu Summary>"

    Examples:
      | Wavelength Mode | Data Rate | Filter Time Constant Default | Hint Text            | Filter Menu Summary |
      | Single          | 1         | ###                          | 0.50000 to 5.00000 s | ###                 |
      | Dual            | 1         | ###                          | 0.50000 to 5.00000 s | ###                 |
      | Single          | 2         | ###                          | 0.25000 to 5.00000 s | ###                 |
      | Dual            | 2         | ###                          | 0.25000 to 5.00000 s | ###                 |
      | Single          | 5         | 0.1                          | 0.10000 to 5.00000 s | Custom (0.1 s)      |
      | Single          | 10        | 0.1                          | 0.10000 to 5.00000 s | Custom (0.1 s)      |
      | Single          | 20        | 0.1                          | 0.05000 to 2.50000 s | Custom (0.1 s)      |
      | Single          | 40        | 0.1                          | 0.02500 to 1.25000 s | Custom (0.1 s)      |
      | Single          | 80        | 0.1                          | 0.01250 to 0.62500 s | Custom (0.1 s)      |
      | Single          | 160       | 0.1                          | 0.00625 to 0.31250 s | Custom (0.1 s)      |

      ### Scenario below covers 1 and 2 Hz Data Rate, Single and Dual Wavelength Mode ###
  Scenario Outline: Filter Time Constant Custom values are accepted
    Given the Wavelength Mode selector is set to "<Wavelength Mode>"
    And the Data Rate selector is set to "<Data Rate>"
    And the Filter Mode selector is set to "Custom"
    When the Filter Time Constant input is set to "<Value>"
    Then the Filter Time Constant input is not in error
    And no issue is raised

    Examples:
      | Wavelength Mode | Data Rate | Value |
      | Single          | 1         | 0.5   |
      | Single          | 1         | 5.00  |
      | Dual            | 1         | 0.5   |
      | Dual            | 1         | 5.00  |
      | Single          | 2         | 0.25  |
      | Single          | 2         | 5.00  |
      | Dual            | 2         | 0.25  |
      | Dual            | 2         | 5.00  |

      ### For Data Rates 80 and 160: Permitted ranges are different from requirement; hint text values are out of the permitted range; dp is different from reqirement ###
  @quarantine @defect:INSISPP-8430
  Scenario Outline: Accepted Filter Time Constant Values with Single Mode
    Given the Wavelength Mode selector is set to "Single"
    And the Data Rate selector is set to "<Data Rate>"
    When the Filter Time Constant input is set to "<Value>"
    Then the Filter Time Constant input is not in error
    And no issue is raised

    Examples:
      | Data Rate | Value   |
      | 5         | 0.1     |
      | 5         | 5.00    |
      | 10        | 0.1     |
      | 10        | 5.00    |
      | 20        | 0.05    |
      | 20        | 2.50    |
      | 40        | 0.03    |
      | 40        | 1.25    |
      | 80        | 0.0125  |
      | 80        | 0.625   |
      | 160       | 0.00625 |
      | 160       | 0.3125  |

  Scenario Outline: Filter Mode is switched to Normal when Wavelength Mode is changed
    Given the Wavelength Mode selector is set to "<Wavelength Mode Initial>"
    And the Data Rate selector is set to "<Data Rate>"
    And the Filter Mode selector is set to "<Filter Mode>"
    When the Wavelength Mode is set to "<Wavelength Mode Final>"
    Then the Filter Mode is set to "Normal"

    Examples:
      | Wavelength Mode Initial | Data Rate | Filter Mode | Wavelength Mode Final |
      | Single                  | 1         | Slow        | Dual                  |
      | Dual                    | 2         | Fast        | Single                |

      ### Possible Defect ###
  @quarantine @defect:INSISPP-8431
  Scenario Outline: Filter Mode is switched to Normal when Data Rate is changed
    Given the Data Rate is set to "<Initial Data Rate>"
    And the Filter Mode selector is set to "<Initial Filter Mode>"
    When the Data Rate is set to "<Final Data Rate>"
    Then the Filter Mode is set to "Normal"

    Examples:
      | Initial Data Rate | Initial Filter Mode | Final Data Rate |
      | 40                | Custom              | 1               |
      | 2                 | Slow                | 160             |

  Scenario Outline: An issue is raised when the Filter Time Constant Value is out of range
    Given the Wavelength Mode selector is set to "<Wavelength Mode>"
    And the Data Rate selector is set to "<Data Rate>"
    And the Filter Mode selector is set to "Custom"
    When the Filter Time Constant input is set to an out of range value "<Value>"
    Then the Filter Time Constant input is in error
    And an issue is raised
    And the issue has title "Filter" and description "Invalid Range"

    Examples:
      | Wavelength Mode | Data Rate | Value |
      | Single          | 1         | 0.49  |
      | Single          | 1         | 5.01  |
      | Dual            | 1         | 0.49  |
      | Dual            | 1         | 5.01  |
      | Single          | 2         | 0.24  |
      | Single          | 2         | 5.01  |
      | Dual            | 2         | 0.24  |
      | Dual            | 2         | 5.01  |

  @quarantine @defect:INSISPP-8430
  Scenario Outline: An issue is raised when the Filter Time Constant Value is out of range
    Given the Wavelength Mode selector is set to "Single"
    And the Data Rate selector is set to "<Data Rate>"
    When the Filter Time Constant input is set to "<Value>"
    Then the Filter Time Constant input is in error
    And an issue is raised
    And the issue has title "Filter" and description "Invalid Range"

    Examples:
      | Data Rate | Filter time Constant Value |
      | 5         | 0.09                       |
      | 5         | 5.01                       |
      | 10        | 0.09                       |
      | 10        | 5.01                       |
      | 20        | 0.04                       |
      | 20        | 2.51                       |
      | 40        | 0.024                      |
      | 40        | 1.251                      |
      | 80        | 0.01249                    |
      | 80        | 0.62501                    |
      | 160       | 0.00624                    |
      | 160       | 0.31251                    |

      ### Scenarios testing the mechanism for raising validation issues ###

  Scenario Outline: Filter validation issue is cleared when the Filter Mode is changed
    Given the Filter Mode is set to "Custom"
    And the Filter Time Constant input is in error
    When the Filter Mode is changed to "<New Filter Mode>"
    Then no issues are present

    Examples:
      | New Filter Mode |
      | Fast            |
      | Normal          |
      | Slow            |

      ### Issue not cleared when the Set Data Filter is set to Off ###
  @quarantine @defect:INSISPP-8432
  Scenario: Filter validation issue is cleared when the Set Data Filter selector is set to Off
    Given the Filter Mode is set to "Custom"
    And the Filter Time Constant input is in error
    When the Set Data Filter selector is set to "Off"
    Then no issues are present

  Scenario: Filter validation issue is cleared when the Set Data Filter selector is toggled Off and On
    Given the Filter Mode is set to "Custom"
    And the Filter Time Constant input is in error
    When the Set Data Filter selector is set to "Off" and back to "On"
    Then the Filter Mode is set to "Normal"
    And no issues are present

  Scenario: Filter validation issue is cleared when a valid value is entered
    Given the Filter Mode is set to "Custom"
    And the Filter Time Constant input is in error
    When the Filter Time Constant input is set to a valid value "0.3"
    Then the Filter Time Constant input has value set to "0.3"
    And the Filter Time Constant input is not in error
    And no issues are present

  Scenario: A Filter issue can be clicked to navigate to the Filter section
    Given the Filter Time Constant input is in error
    And the System menu is opened
    When the "Filter" issues indicator is selected
    Then the Filter setting group is displayed

      ### Scenarios testing the input fields ###

      ### Scenario will fail for "." example, defect reported ###
  @quarantine @defect:INSISPP-8480
  Scenario Outline: Filter Time Constant does not accept unexpected input
    When the Filter Time Constant input is set to "<value>"
    Then the Filter Time Constant input is in error
    And the Filter Time Constant input is empty
    And the Filter Time Constant hint text is "Required"
    And an issue is raised
    And the issue has title "Filter" and description "Invalid Range"

    Examples:
      | value                       |
      | .                           |
      | empty input                 |
      | abc~!@#$%^&*()_+-=`':;,<>/? |

      ### Scenarios for saving methods ###

  Scenario Outline: Filter Mode settings are saved and restored
    Given the Wavelength Mode is set to "<Wavelength Mode>"
    And the Filter Mode selector is set to "<Filter Mode>"
    When the method is saved
    And the method is closed and reopened
    Then the Filter Mode selector is set to "<Filter Mode>"

    Examples:
      | Wavelength Mode | Filter Mode |
      | Single          | Slow        |
      | Single          | Normal      |
      | Single          | Fast        |
      | Dual            | Slow        |
      | Dual            | Normal      |
      | Dual            | Fast        |

  Scenario Outline: Custom Filter Mode settings are saved and restored - Custom Mode
    Given the Wavelength Mode is set to "<Wavelength Mode>"
    And the Filter Mode selector is set to "Custom"
    And the Filter Time Constant input is set to "4"
    When the method is saved
    And the method is closed and reopened
    Then the Filter Mode selector is set to "Custom"
    And the Filter Time Constant input is set to "4"

    Examples:
      | Wavelength Mode |
      | Single          |
      | Dual            |

  Scenario: Filter issue is persisted when method is reloaded
    Given the Filter Time Constant input is in error
    Then a single issue is raised
    When the method is saved
    Then there is still a single issue raised
    When the method is closed and reopened
    Then there is still a single issue raised