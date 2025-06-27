@kiosk @ALIST-228 @kiosk_startup_workflow_feature
Feature: Kiosk | Startup Workflow functionality

  @simulation @weekly
  Scenario: To validate the startup workflow welcome screen
    When User navigates to startup workflow welcome screen
    Then User validates the welcome context in the welcome screen
    And User validates the usage list text in the welcome screen
    And User validates the recommendation text in the welcome screen

  @real @weekly
  Scenario Outline: To validate the navigation of the startup workflow by the user
    When User taps the startup workflow panel
    And User selects the solvent line "<solvent_line>"
    And User sets the "<time_stepper>" using "<unit>" to "<desired_time>"
    Then User validates the time was changed to "<desired_time>"
    When User sets the prime seal wash settings based upon "<prime_seal_toggle>", "<unit>", and "<seal_wash_prime_duration>"
    And User enables the prime needle wash solvent stepper components with "<prime_needle_toggle>" and "<cycles_number>"
    And User enables the prime sample metering solvent section with "<sample_metering_toggle>" and "<number_of_cycles>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for sample metering pump
    And User sets the sample temperature based upon "<samp_temp_toggle>" and "<desired_sample_temp_value>"
    And User sets the column temperature based upon "<col_temp_toggle>" and "<desired_column_number_temp_value>"
    And User turns the uv lamp to "True" state
    And User enables set final conditions and set a "<flow_rate>"
    And User enters the solvent "<comp_line_1>", "<comp_line_2>", "<comp_line_3>", "<comp_line_4>" for equilibration
    Then User validates the total composition is "<total_composition>"
    When User sets the equilibrate volume to "<equilibration_time>"
    Then User validates that all settings are presented on the summary page
    When User taps start button
    Then User verify that the start conditions set have been executed

    Examples:
      | time_stepper     | unit | solvent_line | desired_time | prime_seal_toggle | seal_wash_prime_duration | cycles_number | prime_needle_toggle | sample_metering_toggle | line_1     | line_2    | line_3      | line_4      | number_of_cycles | samp_temp_toggle | col_temp_toggle | desired_sample_temp_value | desired_column_number_temp_value | flow_rate | comp_line_1 | comp_line_2 | comp_line_3 | comp_line_4 | total_composition | equilibration_time |
      | priming_duration | 30   | A,D          | 02:00        | True              | 00:30                    | 10            | True                | True                   | A,True,20  | B,True,10 | C,True,25.5 | D,True,44.5 | 10               | True             | True            | 30                        | 30                               | 1.8       | A,True,25.5 | B,True,20   | C,True,10   | D,True,44.5 | 100.0             | 02:00              |
      | priming_duration | 30   | A,B,C,D      | 10:30        | True              | 10:00                    | 20            | False               | True                   | A,True,90  | B,True,10 | C,False,0   | D,False,0   | 30               | True             | True            | 30                        | 30                               | 0.001     | A,True,44.5 | B,True,44.5 | C,True,5.5  | D,True,5.5  | 100.0             | 10:00              |
      | priming_duration | 30   | A,C,D        | 03:30        | False             | 00:00                    | 15            | True                | True                   | A,True,40  | B,False,0 | C,True,20   | D,True,40   | 25               | True             | False           | 30                        | 00                               | 2         | A,True,17.5 | B,False,0   | C,True,25.5 | D,True,57   | 100.0             | 30:00              |
      | priming_duration | 30   | A            | 59:30        | True              | 03:30                    | 50            | True                | True                   | A,True,100 | B,False,0 | C,False,0   | D,False,0   | 50               | False            | True            | 00                        | 40                               | 10        | A,True,100  | B,False,0   | C,False,0   | D,False,0   | 100.0             | 02:00              |


  @real @weekly
  Scenario: To validate the navigation of the startup workflow by the user when the selection were disabled
    When User taps the startup workflow panel
    And User deselect all lines on the prime solvents section
    And User select disable on the prime seal wash solvent section
    And User select disable on the prime needle wash solvent section
    And User select disable on the prime sample metering solvent section
    And User set to off the sample temperature in the temperature control section
    And User set to off the column temperature in the temperature control section
    And User turns the uv lamp to "False" state
    And User disables set final conditions
    Then User validates that all settings are presented on the summary page
    When User taps start button
    Then User verify that the start conditions set have been executed


  @real @daily
  Scenario: To validate the workflow process completes
    When User taps the startup workflow panel
    And User navigates to the summary screen
    And User taps start button
    Then User verify that the start conditions set have been executed


  @real @weekly
  Scenario Outline: To validate the startup workflow when user abort it
    When User taps the startup workflow panel
    And User selects the solvent line "<solvent_line>"
    And User sets the "<time_stepper>" using "<unit>" to "<desired_time>"
    Then User validates the time was changed to "<desired_time>"
    When User sets the prime seal wash settings based upon "<prime_seal_toggle>", "<unit>", and "<seal_wash_prime_duration>"
    And User enables the prime needle wash solvent stepper components with "<prime_needle_toggle>" and "<cycles_number>"
    And User enables the prime sample metering solvent section with "<sample_metering_toggle>" and "<number_of_cycles>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for sample metering pump
    And User sets the sample temperature based upon "<samp_temp_toggle>" and "<desired_sample_temp_value>"
    And User sets the column temperature based upon "<col_temp_toggle>" and "<desired_column_number_temp_value>"
    And User turns the uv lamp to "True" state
    And User enables set final conditions and set a "<flow_rate>"
    And User enters the solvent "<comp_line_1>", "<comp_line_2>", "<comp_line_3>", "<comp_line_4>" for equilibration
    Then User validates the total composition is "<total_composition>"
    When User sets the equilibrate volume to "<equilibration_time>"
    Then User validates that all settings are presented on the summary page
    When User taps start button
    And User stops the start up workflow at different "<stop_time_minutes>"
    Then User validates the status stopped for the startup workflow

    Examples:
      | time_stepper     | unit | solvent_line | desired_time | prime_seal_toggle | seal_wash_prime_duration | cycles_number | prime_needle_toggle | sample_metering_toggle | line_1     | line_2    | line_3      | line_4      | number_of_cycles | samp_temp_toggle | col_temp_toggle | desired_sample_temp_value | desired_column_number_temp_value | flow_rate | comp_line_1 | comp_line_2 | comp_line_3 | comp_line_4 | total_composition | equilibration_time | stop_time_minutes |
      | priming_duration | 30   | A,D          | 02:00        | True              | 00:30                    | 10            | True                | True                   | A,True,20  | B,True,10 | C,True,25.5 | D,True,44.5 | 10               | True             | True            | 30                        | 30                               | 1.8       | A,True,25.5 | B,True,20   | C,True,10   | D,True,44.5 | 100.0             | 02:00              | 1                 |
      | priming_duration | 30   | A,B,C,D      | 10:30        | True              | 10:00                    | 20            | False               | True                   | A,True,90  | B,True,10 | C,False,0   | D,False,0   | 30               | True             | True            | 30                        | 30                               | 0.001     | A,True,44.5 | B,True,44.5 | C,True,5.5  | D,True,5.5  | 100.0             | 10:00              | 5                 |
      | priming_duration | 30   | A,C,D        | 03:30        | False             | 00:00                    | 15            | True                | True                   | A,True,40  | B,False,0 | C,True,20   | D,True,40   | 25               | True             | False           | 30                        | 00                               | 2         | A,True,17.5 | B,False,0   | C,True,25.5 | D,True,57   | 100.0             | 30:00              | 20                |
      | priming_duration | 30   | A            | 59:30        | True              | 03:30                    | 50            | True                | True                   | A,True,100 | B,False,0 | C,False,0   | D,False,0   | 50               | False            | True            | 00                        | 40                               | 10        | A,True,100  | B,False,0   | C,False,0   | D,False,0   | 100.0             | 02:00              | 1                 |


  @real @daily
  Scenario: To validate the workflow abort process completes
    When User taps the startup workflow panel
    And User navigates to the summary screen
    And User taps start button
    And User aborts the workflow
    Then User validates the status screen for the startup workflow