@ALIST-230 @method_editor @simulation @daily @pda @tuv_bio @pda_bio @method_editor_flow_ramp_period @new @ignore
Feature: Method Editor | QSM Flow ramp period
  The Flow ramp period controls how fast a flow is reached after a flow setting is send to the instrument
  The Flow ramp period is defined as the time period to ramp flow to 2.00 mL/min.

  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Flow Ramp Period menu is opened

      ### Scenario Testing Labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Flow Ramp Period menu title is "Flow Ramp Period"
    And the Flow Ramp Period title text is "Flow Ramp Period (min)"
    And the Flow Ramp Period summary text is "Time period to ramp flow to 2.00 mL/min"
    And the Flow Ramp Period hint text is "0.066667 to 0.500000 min"
    And the Effective Ramp Rate title text is "Effective Ramp Rate"
    And the Effective Ramp Rate summary is "30.000 mL/min/min"

      ### Scenarios testing favorites and filtering ###

  Scenario: Flow Ramp Period can be set as Favorite
    When the Flow Ramp Period setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Flow Ramp Period" menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Flow Ramp Period setting group is displayed
    And the "Pump" menu is highlighted

    Examples:
      | Search Text      |
      | Flow             |
      | Ramp             |
      | Period           |
      | Flow Ramp Period |
      | Ramp Period      |

      ### Scenarios testing default, minimum, maximum and in range values ###

  Scenario: Default settings are correct
    Then the "Pump" menu is highlighted
    And the "Flow Ramp Period" menu is highlighted
    And the Flow Ramp Period input has value set to "0.066667"
    And the Flow Ramp Period hint text is "0.066667 to 0.500000 min"
    And the Effective Ramp Rate summary text is "30.000 mL/min/min"


  Scenario Outline: Flow Ramp Period valid value is accepted
    When the Flow Ramp Rate input is set to valid value "<ramp_rate_value>"
    Then the Effective Ramp Rate summary text is "<effective_ramp_rate_value>"
    And the Flow Ramp Rate input is not in error
    And no issue is raised

    Examples:
      | ramp_rate_value | effective_ramp_rate_value |
      | 0.066667        | 30.000                    |
      | 0.080000        | 25.000                    |
      | 0.150000        | 13.333                    |
      | 0.153333        | 13.044                    |
      | 0.412815        | 4.845                     |
      | 0.500000        | 4.000                     |

      # Scenarios testing the mechanism for raising validation issues ###

  Scenario Outline: An issue is raised when the Flow Ramp Period is out of range wrong numerical values
    When the Flow Ramp Period input is set to out of range value "<ramp_rate_value>"
    Then the Effective Ramp Rate summary text is "<effective_ramp_rate_value>"
    And the Flow Ramp Period input is in error
    And an issue is raised
    And the issue has title "Flow Ramp Period" and description "Invalid Range"

    Examples:
      | ramp_rate_value | effective_ramp_rate_value |
      | -1              | -2.000                    |
      | 0.0             | ∞                         |
      | 0.066666        | 30.000                    |
      | 0.500001        | 4.000                     |

  Scenario: Issue is cleared when a valid value is entered
    Given the Flow Ramp Period input is in error
    And a single issue is raised
    When the Flow Ramp Period input is set to valid value "0.080000"
    Then the Effective Ramp Rate summary text is "25.000"
    And the Flow Ramp Period input is no longer in error
    And no issue is raised

  Scenario: A Flow Ramp Period issue can be clicked to navigate to the Flow Ramp Period section
    Given the Flow Ramp Period is in error
    And the System menu is opened
    When the "Flow Ramp Period" issues indicator is selected
    Then the Flow Ramp Period setting group is displayed


      ### Scenarios for testing the input fields ###

      # Potential defect. Check if the value shouldn't be rounded_value also in the input field
  Scenario Outline: Flow Ramp Period input rounding when too many decimal places are entered (more than 6)
    When the Flow Ramp Period input is set to "<value>"
    Then the Flow Ramp Period input has value set to "<value>"
    And the Flow Ramp Period menu summary is rounded to 6 decimal places showing "<rounded_value> min"

    Examples:
      | value      | rounded_value |
      | 0.07000000 | 0.070000      |
      | 0.08999999 | 0.090000      |
      | 0.15555555 | 0.155556      |


  Scenario Outline: Flow Ramp Period Input does not accept unexpected input
    When the Flow Ramp Period input is set to "<value>"
    Then the Flow Ramp Period input is in error
    And the Flow Ramp Period input is empty
    And the Flow Ramp Period input hint text is "Required"
    And the Effective Ramp Rate summary text is "∞"
    And an issue is raised
    And the issue has title "Flow Ramp Period" and description "Invalid Range"

    Examples:
      | value       |
      | abc         |
      | #$%         |
      | empty input |


      ### Scenarios for Saving methods ###

  Scenario: Settings are saved and restored
    Given the Flow Ramp Period input is set to valid value "0.080000"
    When the method is saved
    And the method is closed and reopened
    Then the Flow Ramp Period input is set to "0.080000"
    And no issues are raised

      # Potential defect. When saving the method an extra issue is raised
  Scenario: Flow Ramp Period input validation issue persists when method is reloaded
    Given the Flow Ramp Period input is in error
    Then a single issue is raised
    When the method is saved
    Then there is still a single issue raised
    When the method is closed and reopened
    Then there is still a single issue raised

