@method_editor @ALIST-230 @simulation @daily @method_editor_sample_temperature_feature
Feature: Method Editor | FTN Sample Temperature
  The sample manager controls the temperature of the sample manager and any sample organizer in the system.
  The temperature can be turned off to equilibrate the samples to ambient temperature.


  Background:
    Given an acquisition method that contains default settings is open
    And the Sample Manager menu is opened
    And the Sample Temperature menu is opened


      ### Scenarios testing labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Sample Temperature menu title is "Sample Temperature"
    And the setting group title text is "Sample Temperature"
    And the Compartment Temperature setting title is "Set Compartment Temperature"
    And the Compartment Temperature setting summary is "Enable to control the compartment temperature"

  Scenario: Titles and descriptions are displayed - Compartment Temperature enabled
    When the Compartment Temperature selector is set to "On"
    Then the Temperature Setpoint setting title is "Temperature Setpoint (°C)"
    And the Temperature Setpoint setting input hint text is "4.0 to 40.0 °C"
    And the Temperature Tolerance setting title is "Set Temperature Tolerance"
    And the Temperature Tolerance setting summary is "Enable to hold next injections until temperature is within tolerance"

  Scenario: Titles and descriptions are displayed - Temperature Tolerance enabled
    When the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    Then the Tolerance setting title is "Tolerance (±°C)"
    And the Tolerance setting input hint text is "0.5 to 10.0 °C"


      ### Scenarios testing favorites and filtering ###

  Scenario: Sample Temperature can be set as Favorite
    When the Sample Temperature setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Sample Temperature" menu title is displayed

  @quarantine @defect:INSSYS-26 @new @ignore
  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Sample Temperature setting group is displayed
    And the "Sample Manager" menu is highlighted

    Examples:
      | Search Text                 |
      | Sample Temperature          |
      | Set Compartment Temperature |
      | Temperature Setpoint        |
      | Set Temperature Tolerance   |
      | Tolerance                   |

      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "Sample Manager" menu is highlighted
    And the "Sample Temperature" menu is highlighted
    And the Compartment Temperature selector is set to "Off"
    And the Sample Temperature menu summary is "Off"
    When the Compartment Temperature selector is set to "On"
    Then the Temperature Setpoint input has value set to "20"
    And the Temperature Tolerance selector is set to "Off"
    And the Sample Temperature menu summary is "20.0 °C"
    When the Temperature Tolerance selector is set to "On"
    Then the Tolerance input has value set to "5"
    And the Sample Temperature menu summary is "20.0 °C ± 5.0 °C"


  Scenario Outline: Temperature Setpoint valid value is accepted
    Given the Compartment Temperature selector is set to "On"
    When the Temperature Setpoint input is set to "<value>"
    Then the Temperature Setpoint input is not in error
    And no issue is raised

    Examples:
      | value |
      | 4.0   |
      | 40.0  |


  Scenario Outline: An issue is raised when the Temperature Setpoint is out of range
    Given the Compartment Temperature selector is set to "On"
    When the Temperature Setpoint input is set to out of range value "<value>"
    Then the Temperature Setpoint input is in error
    And an issue is raised
    And the issue has title "Sample Temperature" and description "Invalid Range"

    Examples:
      | value |
      | -1.0  |
      | 3.9   |
      | 40.1  |


  Scenario Outline: Tolerance valid value is accepted
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    When the Tolerance input is set to "<value>"
    Then the Tolerance input is not in error
    And no issue is raised

    Examples:
      | value |
      | 0.5   |
      | 10.0  |


  Scenario Outline: An issue is raised when the Tolerance is out of range
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    When the Tolerance input is set to out of range value "<value>"
    Then the Tolerance input is in error
    And an issue is raised
    And the issue has title "Sample Temperature" and description "Invalid Range"

    Examples:
      | value |
      | -1.0  |
      | 0.4   |
      | 10.1  |


      # Scenarios testing the mechanism for raising validation issues ###


  Scenario: A single Sample Temperature issue is raised when multiple sample temperature inputs are out of range
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    When the Temperature Setpoint input is in error
    And the Tolerance input is in error
    Then the Temperature Setpoint input is in error
    And the Tolerance input is in error
    And an issue is raised
    And the issue has title "Sample Temperature" and description "Invalid Range"


  @quarantine @defect:INSISPP-8366 @new @ignore
  Scenario: Temperature Setpoint validation issue is cleared when Compartment Temperature is toggled Off
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Setpoint input is in error
    When the Compartment Temperature selector is set to "Off"
    Then no issues are present


  Scenario: Temperature Setpoint validation issue is cleared when Compartment Temperature is toggled Off and On
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Setpoint input is in error
    When the Compartment Temperature selector is set to "Off" and back to "On"
    Then the Temperature Setpoint input has value set to default "20"
    And the Temperature Setpoint input is not in error
    And no issues are present


  Scenario: Temperature Setpoint validation issue is cleared when a valid value is entered
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Setpoint input is in error
    When the Temperature Setpoint input is set to valid value "30"
    Then the Temperature Setpoint input has value set to "30"
    And the Temperature Setpoint input is not in error
    And no issues are present


  @quarantine @defect:INSISPP-8366 @new @ignore
  Scenario: Tolerance validation issue is cleared when Temperature Tolerance is toggled Off
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the Tolerance input is in error
    When the Temperature Tolerance selector is set to "Off"
    Then no issues are present


  Scenario: Tolerance validation issue is cleared when Temperature Tolerance is toggled Off and On
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the Tolerance input is in error
    When the Temperature Tolerance selector is set to "Off" and back to "On"
    Then the Tolerance input has value set to default "5"
    And the Tolerance input is not in error
    And no issues are present


  Scenario: Tolerance validation issue is cleared when a valid value is entered
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the Tolerance input is in error
    When the Tolerance input is set to valid value "9"
    Then the Tolerance input has value set to "9"
    And the Temperature Setpoint input is not in error
    And no issues are present


  Scenario: Only the Tolerance validation issue is cleared when Temperature Tolerance is toggled Off and On
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the Temperature Setpoint input is in error
    And the Tolerance input is in error
    When the Temperature Tolerance selector is set to "Off" and back to "On"
    Then the Tolerance input is not in error
    And the Temperature Setpoint input is still in error
    And an issue is still raised
    And the issue has title "Sample Temperature" and description "Invalid Range"

  
  Scenario Outline: A Sample Temperature issue can be clicked to navigate to the Sample Temperature section
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the <Input> input is in error
    And the System menu is opened
    When the "Sample Temperature" issues indicator is selected
    Then the Sample Temperature setting group is displayed

    Examples:
      | Input                |
      | Temperature Setpoint |
      | Tolerance            |


      ### Scenarios for testing the input fields ###

      # Potential defect. Check if the value shouldn't be rounded_value also in the input field
  @new @ignore
  Scenario Outline: Temperature Setpoint rounding when too many decimal places are entered
    Given the Compartment Temperature selector is set to "On"
    When the Temperature Setpoint input is set to "<value>"
    Then the Temperature Setpoint input has value set to "<value>"
    And the Sample Temperature menu summary is rounded to 1 decimal place showing "<rounded_value> °C"

    Examples:
      | value             | rounded_value |
      | 5.04999           | 5.0           |
      | 5.65111           | 5.7           |
      | 8.999999999999999 | 9.0           |


      # Potential defect. Check if the value shouldn't be rounded_value also in the input field
  @new @ignore
  Scenario Outline: Tolerance rounding when too many decimal places are entered
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    When the Tolerance input is set to "<value>"
    Then the Tolerance input has value set to "<value>"
    And the Sample Temperature menu summary is rounded to 1 decimal place showing "20.0 °C ± <rounded_value> °C"

    Examples:
      | value             | rounded_value |
      | 5.04999           | 5.0           |
      | 5.65111           | 5.7           |
      | 8.999999999999999 | 9.0           |

  @new @ignore
  Scenario Outline: Temperature Setpoint does not accept unexpected input
    Given the Compartment Temperature selector is set to "On"
    When the Temperature Setpoint input is set to "<value>"
    Then the Temperature Setpoint input is in error
    And the Temperature Setpoint input is empty
    And the Temperature Setpoint setting input hint text is "Required"
    And an issue is raised
    And the issue has title "Sample Temperature" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |

  @new @ignore
  Scenario Outline: Tolerance does not accept unexpected input
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    When the Tolerance input is set to "<value>"
    Then the Tolerance input is in error
    And the Tolerance input is empty
    And the Tolerance setting input hint text is "Required"
    And an issue is raised
    And the issue has title "Sample Temperature" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |


      ### Scenarios for Saving methods ###

  @new @ignore
  Scenario: Settings are saved and restored
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Setpoint input is set to valid value "30"
    And the Temperature Tolerance selector is set to "On"
    And the Tolerance input is set to valid value "9"
    When the method is saved
    And the method is closed and reopened
    Then the Compartment Temperature selector is set to "On"
    And Temperature Setpoint input is set to "30"
    And the Temperature Tolerance selector is set to "On"
    And Tolerance input is set to "9"


  @quarantine @defect:INSISPP-8148 @new @ignore
  Scenario Outline: Sample Temperature inputs validation issue is persisted when method is reloaded
    Given the Compartment Temperature selector is set to "On"
    And the Temperature Tolerance selector is set to "On"
    And the <Input> input is in error
    Then a single issue is raised
    When the method is saved
    Then there is still a single issue raised
    When the method is closed and reopened
    Then there is still a single issue raised

    Examples:
      | Input                |
      | Temperature Setpoint |
      | Tolerance            |
