@ALIST-230 @method_editor @simulation @daily @pda @tuv_bio @pda_bio @method_editor_gradient_end_stop_flow_feature @new @ignore
Feature: Method Editor | QSM Gradient End Stop Flow
  The Gradient End Stop Flow controls the stop flow after the lines in the gradient table have been executed.
  The Gradient End Stop Flow can be enabled to allow the system to perform a Stop Flow after the gradient has been executed.


  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Gradient End Stop Flow menu is opened


      ### Scenario Testing Labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Gradient End Stop Flow menu title is "Gradient End Stop Flow"
    And the Append with stop flow title text is "Append with stop flow"
    And the Append with stop flow setting summary is "Enable to append the stop flow line at the end of the gradient table"

  Scenario: Titles and descriptions are displayed - Append with Stop Flow enabled
    When the Append with Stop Flow selector is set to On
    Then the Time Period setting title is "Time Period (min)"
    And the Time Period setting summary is "Time after gradient ends when flow will stop"
    And the Time Period setting input hint text is "0.1 to 60.0 min"


      ### Scenarios testing favorites and filtering ###

  Scenario: Gradient End Stop Flow can be set as Favorite
    When the Gradient End Stop Flow setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Gradient End Stop Flow" menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Gradient End Stop Flow setting group is displayed
    And the "Pump" menu is highlighted

    Examples:
      | Search Text            |
      | Gradient               |
      | Gradient End           |
      | Stop flow              |
      | Stop                   |
      | Gradient End Stop Flow |


      ### Scenarios testing default, minimum and maximum values ###

  Scenario: Default settings are correct
    Then the "Pump" menu is highlighted
    And the "Gradient End Stop Flow" menu is highlighted
    And the Append with Stop Flow selector is set to Off
    And the Gradient End Stop Flow menu summary is "Disabled"
    When the Append with Stop Flow selector is set to On
    Then the Time Period input has value set to "1"
    And the Gradient End Stop Flow menu summary is "Enabled"


  Scenario Outline: Time Period valid value is accepted
    Given the Append with Stop Flow selector is set to On
    When the Time Period input is set to "<value>"
    Then the Time Period input is not in error
    And no issue is raised

    Examples:
      | value |
      | 0.1   |
      | 60.0  |


  Scenario Outline: An issue is raised when the Time Period is out of range
    Given the Append with Stop Flow selector is set to On
    When the Time Period input is set to out of range value "<value>"
    Then the Time Period input is in error
    And an issue is raised
    And the issue has title "Gradient End Stop Flow" and description "Invalid Range"

    Examples:
      | value |
      | -1    |
      | 0.0   |
      | 60.1  |


      # Scenarios testing the mechanism for raising validation issues #


  Scenario: Time Period input validation issue is cleared when Append with Stop Flow is toggled Off
    Given the Append with Stop Flow selector is set to On
    And the Time Period input is in error
    When the Append with Stop Flow selector is set to Off
    Then no issues are present


  Scenario: Time Period input validation issue is cleared when Append with Stop Flow is toggled Off and On
    Given the Append with Stop Flow selector is set to On
    And the Time Period input is in error
    When the Append with Stop Flow selector is set to Off and back to On
    Then the Time Period input has value set to default "1"
    And the Time Period input is not in error
    And no issues are present


  Scenario: Time Period validation issue is cleared when Append with Stop Flow is toggled Off
    Given the Append with Stop Flow selector is set to On
    And the Time Period selector is in error
    When the Append with Stop Flow selector is set to Off
    Then no issues are present


  Scenario: Time Period validation issue is cleared when a valid value is entered
    Given the Append with Stop Flow selector is set to On
    And the Time Period selector is in error
    When the Time Period input is set to valid value "5"
    Then no issues are present

  Scenario: A Gradient End Stop Flow issue can be clicked to navigate to the Gradient End Stop Flow section
    Given the Append with Stop Flow selector is set to On
    And the Time Period input is in error
    And the System menu is opened
    When the "Gradient End Stop Flow" issues indicator is selected
    Then the Gradient End Stop Flow setting group is displayed


      ### Scenarios for testing the input fields ###


  Scenario Outline: Time Period input does not accept unexpected input
    Given the Append with Stop Flow selector is set to On
    When the Time Period input is set to "<value>"
    Then the Time Period input is in error
    And the Time Period input is empty
    And the Time Period input hint text is "Required"
    And an issue is raised
    And the issue has title "Gradient End Stop Flow" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |
      | e           |


      # Potential defect. Check if the value shouldn't be rounded_value in the input field
  Scenario Outline: Time Period rounding when too many decimal places are entered
    Given the Append with Stop Flow selector is set to On
    When the Time Period input is set to "<value>"
    Then the Time Period input has value set to "<rounded_value>"


    Examples:
      | value             | rounded_value |
      | 5.04999           | 5.0           |
      | 5.65111           | 5.7           |
      | 8.999999999999999 | 9.0           |

      ### Scenario for Saving methods ###

  Scenario: Settings are saved and restored
    Given the Append with Stop Flow selector is set to On
    And the Time Period input is set to "20"
    When the method is saved
    And the method is closed and reopened
    Then the Append with Stop Flow selector is set to On
    And Time Period input is set to "20"


      # Potential defect. When saving the method an extra issue is raised
  Scenario: Time Period input validation issue persists when method is reloaded
    Given the Append with Stop Flow selector is set to On
    And the Time Period input is in error
    Then a single issue is raised
    When the method is saved
    Then there is still a single issue raised
    And the method is closed and reopened
    Then there is still a single issue raised
