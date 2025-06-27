@ALIST-230 @method_editor @simulation @daily @pda @tuv_bio @pda_bio @method_editor_pressure_limits_feature @new @ignore
Feature: Method Editor | QSM Pressure limits
  The Pressure limits controls the minimum and maximum pressure limit
  The Pressure limits values are set by user in accordance to the solvent and flowrate used


  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Pressure Limits menu is opened


      ### Scenario Testing Labels ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Pressure Limits menu title is "Pressure Limits"
    And the Automatically Set Maximum Pressure Limits title text is "Automatically Set Maximum Pressure Limits"
    And the Automatically Set Maximum Pressure Limits setting summary is "Enable to automatically adjust the pressure limits based on the flow rate"

  Scenario Outline: Titles and descriptions are displayed - Defaults when disabling Automatically Set Maximum Pressure Limits
    When the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure unit is set to "<pressure_units>"
    Then the Pressure Limits setting title is "<pressure_limits_text>"
    And the Pressure Limits setting summary is "Note: Actual maximum pressure may be limited by flow rate."
    And the Pressure Limits Minimum setting input hint text is "<pressure_limits_minimum_hint_text>"
    And the Pressure Limits Maximum setting input hint text is "<pressure_limits_maximum_hint_text>"

    Examples:
      | pressure_units | pressure_limits_text  | pressure_limits_minimum_hint_text | pressure_limits_maximum_hint_text |
      | psi            | Pressure Limits (psi) | 0 to 9999 psi                     | 1 to 10000 psi                    |
      | bar            | Pressure Limits (bar) | 0 to 688 bar                      | 1 to 689 bar                      |
      | kPa            | Pressure Limits (kPa) | 0 to 68947 kPa                    | 1 to 68948 kPa                    |


      ### Scenarios testing favorites and filtering ###

  Scenario: Pressure Limits can be set as Favorite
    When the Pressure Limits setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Pressure Limits" menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Pressure Limits setting group is displayed

    Examples:
      | Search Text     |
      | Pressure        |
      | Pressure Limits |



      ### Scenarios testing default, minimum and maximum values ###

  Scenario Outline: Default settings are correct
    When the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure unit is set to "<pressure_units>"
    Then the Pressure Limits minimum input value is set to "<min_value>"
    And the Pressure Limits maximum input value is set to "<max_value>"
    And the Pressure Limits menu summary is "<menu_summary_text>"

    Examples:
      | pressure_units | min_value | max_value | menu_summary_text |
      | psi            | 0         | 10000     | 0 to 10000 psi    |
      | bar            | 0         | 689       | 0 to 689 bar      |
      | kPa            | 0         | 68948     | 0 to 68948 kPa    |


  Scenario Outline: Pressure Limits valid values are accepted
    Given Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the pressure units is set to "<pressure_units>"
    When the Pressure Limits minimum input is set to valid value "<min_value>"
    And the Pressure Limits maximum input is set to valid value "<max_value>"
    Then the Pressure Limits input is not in error
    And no issue is raised

    Examples:
      | pressure_units | min_value | max_value |
      | psi            | 0         | 1         |
      | psi            | 9999      | 10000     |
      | bar            | 0         | 1         |
      | bar            | 688       | 689       |
      | kPa            | 0         | 1         |
      | kPa            | 68947     | 68948     |


      # Scenario Testing hint box changes according to values in input box #

  Scenario Outline: Pressure Limits valid values are accepted and hint boxes change accordingly
    Given Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the pressure units is set to "<press_units>"
    When the Pressure Limits minimum input is set to valid value "<min_value>"
    And the Pressure Limits maximum input is set to valid value "<max_value>"
    Then the Pressure Limits minimum input hint text is "<pressure_limits_minimum_hint_text>"
    And the Pressure Limits maximum input hint text is "<pressure_limits_maximum_hint_text>"
    And no issue is raised

    Examples:
      | press_units | min_value | max_value | pressure_limits_minimum_hint_text | pressure_limits_maximum_hint_text |
      | psi         | 0         | 1         | 0 to 0 psi                        | 1 to 10000 psi                    |
      | psi         | 1000      | 2000      | 0 to 1999 psi                     | 1001 to 10000 psi                 |
      | psi         | 9999      | 10000     | 0 to 9999 psi                     | 10000 to 10000 psi                |
      | bar         | 0         | 1         | 0 to 0 bar                        | 1 to 689 bar                      |
      | bar         | 200       | 400       | 0 to 399 bar                      | 201 to 689 bar                    |
      | bar         | 688       | 689       | 0 to 688 bar                      | 689 to 689 bar                    |
      | kPa         | 0         | 1         | 0 to 0 kPa                        | 1 to 68948 kPa                    |
      | kPa         | 20000     | 40000     | 0 to 39999 kPa                    | 20001 to 68948 kPa                |
      | kPa         | 68947     | 68948     | 0 to 68947 kPa                    | 68948 to 68948 kPa                |


      # Scenarios testing the mechanism for raising validation issues #

  Scenario Outline: An issue is raised when the Minimum Pressure limit is invalid
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the pressure units is set to "<pressure_units>"
    And the Pressure Limits Maximum input is set to "10000"
    When the Pressure Limits Minimum input is set to invalid value "<value>"
    Then the Pressure Limits input is in error
    And an issue is raised
    And the issue has title "Pressure Limits" and description "Invalid Range"

    Examples:
      | pressure_units | value |
      | psi            | -1    |
      | psi            | 10000 |
      | psi            | 10001 |
      | bar            | -1    |
      | bar            | 689   |
      | bar            | 690   |
      | kPa            | -1    |
      | kPa            | 68948 |
      | kPa            | 68949 |


  Scenario Outline: An issue is raised when the Maximum Pressure limit is invalid
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the pressure units is set to "<pressure_units>"
    And the Pressure Limits Minimum input is set to "0"
    When the Pressure Limits Maximum input is set to invalid value "<value>"
    Then the Pressure Limits input is in error
    And an issue is raised
    And the issue has title "Pressure Limits" and description "Invalid Range"

    Examples:
      | pressure_units | value |
      | psi            | 0     |
      | psi            | 10001 |
      | psi            | 10002 |
      | bar            | 0     |
      | bar            | 690   |
      | bar            | 691   |
      | kPa            | 0     |
      | kPa            | 68949 |
      | kPa            | 68950 |


  Scenario Outline: Pressure Limits validation issue is cleared when Automatically Set Maximum Pressure Limits is toggled On and Off
    Given the Automatically Set Maximum Pressure Limits is set to "Off"
    And the Pressure Limits input is in error
    And the Pressure units is set to "<pressure_units>"
    When the Automatically Set Maximum Pressure Limits is set to "On" and back to "Off"
    Then the Pressure Limits Minimum input has value set to default "<min_value>"
    And the Pressure Limits Maximum input has value set to default "<max_value>"
    And the Pressure Limits input is not in error
    And no issues are present

    Examples:
      | pressure_units | min_value | max_value |
      | psi            | 0         | 10000     |
      | bar            | 0         | 689       |
      | kPa            | 0         | 68948     |


  Scenario Outline: Pressure Limits validation issue is cleared when Automatically Set Maximum Pressure Limits is set to On
    Given the Pressure limits input is in error
    And the Pressure unit is "<pressure_units>"
    When the Automatically Set Maximum Pressure Limits is set to "On"
    Then the Pressure Limits input is no longer in error
    And the Pressure Limits summary text has values set to default "<pressure_limits_summary_text>"

    Examples:
      | pressure units | pressure_limits_summary_text |
      | psi            | 0 to 10000 psi               |
      | bar            | 0 to 689 bar                 |
      | kPa            | 0 to 68948 kPa               |


  Scenario: Pressure Limits validation issue is cleared when a valid value is entered
    Given the Automatically Set Maximum Pressure Limits is set to "Off"
    And the Pressure Limits input is in error
    When the Pressure Limits Minimum input is set to valid value "0"
    And the Pressure Limits Maximum value is set to valid value "50"
    Then no issues are present

  Scenario: A Pressure Limits issue can be clicked to navigate to the Pressure Limits section
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits input is in error
    And the System menu is opened
    When the "Pressure Limits" issues indicator is selected
    Then the Pressure Limits setting group is displayed


      ### Scenarios for testing the input fields ###

      ### Potential defect ###
  Scenario Outline: Pressure Limits Minimum input does not accept unexpected input
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits Maximum value is set to "100"
    When the Pressure Limits Minimum input is set to "<value>"
    Then the Pressure Limits input is in error
    And an issue is raised
    And the issue has title "Pressure limits" and description "Invalid Range"

    Examples:
      | value    |
      | e        |
      | E        |
      | e1122221 |
      | E1212121 |

  Scenario Outline: Pressure Limits Maximum input does not accept unexpected input
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits Minimum value is set to "0"
    When the Pressure Limits Maximum input is set to "<value>"
    Then the Pressure Limits input is in error
    And an issue is raised
    And the issue has title "Pressure limits" and description "Invalid Range"

    Examples:
      | value    |
      | e        |
      | E        |
      | e1122221 |
      | E1212121 |


      # Potential defect. Check if the value shouldn't be rounded_value in the input field
  Scenario Outline: Pressure limits rounding when too many decimal places are entered
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    When the Pressure Limits Mimimum input is set to "<min_value>"
    And the Pressure Limits Maximum input is set to "<max_value>"
    Then the Pressure Limits Minimum input has value set to "<min_rounded_value>"
    And the Pressure Limits Maximum input has value set to "max_rounded_value"


    Examples:
      | min_value  | min_rounded_value | max_value  | max_rounded_value |
      | 0.111111   | 0                 | 1.58787    | 2                 |
      | 50.878174  | 51                | 60.000585  | 60                |
      | 99.999999  | 100               | 101.999999 | 102               |
      | 104.005555 | 104               | 106.01547  | 106               |

      ### Scenario for Saving methods ###

  Scenario: Valid Settings are saved and restored
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits Minimum input is set to valid value "20"
    And the Pressure Limits Maximum input is set to valid value "40"
    When the method is saved
    And the method is closed and reopened
    Then the Pressure Limits Minimum is set to valid value "20"
    And the Pressure Limits Maximum is set to valid value "40"

  Scenario: Pressure Limits inputs validation issue persists when method is saved
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits Minimum input is set to invalid value "4"
    And the Pressure Limits Maximum input is set to invalid value "2"
    And the Pressure Limits input is in error
    When the method is saved
    Then the Pressure Limits input is still in error


  Scenario: Pressure Limits inputs validation issue persists when method is reloaded
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure Limits Minimum input is set to invalid value "4"
    And the Pressure Limits Maximum input is set to invalid value "2"
    And the Pressure Limits input is in error
    When the method is saved
    And the method is closed and reopened
    Then the Pressure Limits Minimum is set to invalid value "4"
    And the Pressure Limits Maximum is set to invalid value "2"
    And the Pressure Limits input is in error

      ### Scenarios for clearing validation errors ###
  Scenario Outline: Pressure Limits inputs error is cleared by turning the selector on and back off
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure units is "<pressure_units>"
    And the Pressure Limits Minimum input is set to invalid value "4"
    And the Pressure Limits Maximum input is set to invalid value "2"
    And the Pressure Limits input is in error
    When the Automatically Set Maximum Pressure Limits selector is toggled "On" and back "Off"
    Then the Pressure Limits Minimum is set to default value "min_value"
    And the Pressure Limits Maximum is set to default value "max_value"
    And the Pressure Limits input is no longer in error

    Examples:
      | pressure_units | min_value | max_value |
      | psi            | 0         | 10000     |
      | bar            | 0         | 689       |
      | kPa            | 0         | 68948     |


  Scenario Outline: Pressure Limits inputs error is cleared by entering a valid value
    Given the Automatically Set Maximum Pressure Limits selector is set to "Off"
    And the Pressure units is "<pressure_units>"
    And the Pressure Limits Minimum input is set to invalid value "4"
    And the Pressure Limits Maximum input is set to invalid value "2"
    When the Pressure Limits Minimum input is set to valid value "2"
    And the Pressure Limits Maximum is set to valid value "58"
    Then the Pressure Limits Minimum hint text is "<min_value_hint_text>"
    And the Pressure Limits Maximum hint text is "<max_value_hint_text>"
    And the Pressure Limits input is no longer in error

    Examples:
      | pressure_units | min_value_hint_text | max_value_hint_text |
      | psi            | 0 to 57 psi         | 3 to 10000 psi      |
      | bar            | 0 to 57 bar         | 3 to 689 bar        |
      | kPa            | 0 to 57 kPa         | 3 to 68948  kPa     |

