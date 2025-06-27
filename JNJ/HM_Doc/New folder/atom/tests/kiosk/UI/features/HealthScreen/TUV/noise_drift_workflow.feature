@kiosk @ALIST-228 @noiseanddrift
Feature: Kiosk | Noise & Drift Workflow functionality

  @real @weekly @ignore #The Last run, last tested and test conditions functionalities are not implemented; need to be decided if it will/will not be implemented
  Scenario Outline: To validate the Last run, Last tested on and test conditions fields
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    And User taps noise-drift start panel
    And User validates the welcome context in the welcome screen
    And User enters the "<flow_rate>", "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User sets the "<channel_a_value>"
    And User sets the "<data_rate_value>" and "<filter_time_constant>"
    Then User validates the solvent details
    And User validates the wavelength and data rate details
    When User taps start
    Then User verifies the test was completed
    And User validates the results data in the result screen
    When User navigates to health troubleshoot area
    And User navigates to TUV section
    Then Last run field is updated with current data
    When User taps noise-drift start panel
    Then the Last tested on and test conditions fields are updated with current data and previously defined conditions

    Examples:
      | flow_rate | line_1    | line_2    | line_3    | line_4    | channel_a_value | data_rate_value | filter_time_constant |
      | 2.000     | A,True,45 | B,True,25 | C,True,15 | D,True,15 | 260             | 5               | Fast                 |


  @real @weekly
  Scenario: To run the noise drift workflow with lamp states Off
    Given User sets pre-required date and time format
    And User navigates to Commands area
    And User set the lamp detector "Off"
    And User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User validates the welcome context in the welcome screen
    And User taps next
    Then User validate the lamp state is Off
    When User navigates to the summary screen
    Then User validate the lamp state in the summary screen is Off
    When User taps start
    Then User verifies the test was completed
    And User validates the results page
    When User goes back to Commands area
    Then User validate the lamp state is On in command screen
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details


  @real @weekly
  Scenario: To run the noise drift workflow with lamp states On
    Given User sets pre-required date and time format
    And User navigates to Commands area
    And User set the lamp detector "On"
    And User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User validates the welcome context in the welcome screen
    And User taps next
    Then User validate the lamp state is On
    When User navigates to the summary screen
    Then User validate the lamp state in the summary screen is On
    When User taps start
    Then User verifies the test was completed
    And User validates the results page
    When User goes back to Commands area
    Then User validate the lamp state is On in command screen
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

  @real @weekly
  Scenario Outline: to validate the user is able to set the flowrate in the accepted range
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User taps next
    And User turns the flow "<flow_state>"
    And User sets the flow rate to "<flow_rate>"
    Then Validate that the edit field shows "<error_state>"

    Examples:
      | flow_state | flow_rate | error_state |
      | On         | 0.001     | False       |
      | On         | 10.000    | False       |
      | On         | 1.000     | False       |
      | On         | 0.000     | True        |
      | On         | 10.500    | True        |


  @real @weekly
  Scenario: to validate the user is able to set the flowrate Off
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User taps next
    And User turns the flow "Off"
    Then Validate the Next button is enabled


  @real @daily
  Scenario Outline: To validate the Composition lines
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User taps next
    And User turns the flow "<flow_state>"
    And User sets the flow rate to "<flow_rate>"
    And User taps next
    And User enters the "<flow_rate>", "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User sets the "<channel_a_value>"
    And User sets the data rate as "<data_rate_value>" and filter time as "<filter_time_constant>"
    Then User validates the solvent details
    And User validates the wavelength details for "<wavelength_mode>"
    And User validates the data rate details and filter
    When User taps start
    Then User verifies the test was completed
    And User validates the results data in the result screen
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details


    Examples:
      | flow_state | flow_rate | line_1    | line_2    | line_3    | line_4    | channel_a_value | data_rate_value | filter_time_constant | wavelength_mode |
      | On         | 1.000     | A,True,30 | B,True,30 | C,True,20 | D,True,20 | 260             | 10              | Fast                 | single          |


  @real @weekly
  Scenario Outline: To validate the Reset Composition button
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User taps next
    And User turns the flow "<flow_state>"
    And User sets the flow rate to "<flow_rate>"
    And User taps next
    And User enters the "<flow_rate>", "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User sets the "<channel_a_value>"
    And User sets the data rate as "<data_rate_value>" and filter time as "<filter_time_constant>"
    Then User validates the solvent details
    And User validates the wavelength details for "<wavelength_mode>"
    And User validates the data rate details and filter
    When User goes back to composition screen
    And User sets 100% A composition button
    And User navigates to summary screen
    Then User validates the solvent details

    Examples:
      | flow_state | flow_rate | line_1    | line_2    | line_3    | line_4    | channel_a_value | data_rate_value | filter_time_constant | wavelength_mode |
      | On         | 1.000     | A,True,30 | B,True,30 | C,True,20 | D,True,20 | 260             | 10              | Fast                 | single          |


  @real @weekly
  Scenario Outline: To validate the Channel A wavelength, Data Rate, Use Filter and Filter Time Constant
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User taps next
    And User turns the flow "<flow_state>"
    And User sets the flow rate to "<flow_rate>"
    And User taps next
    And User enters the "<flow_rate>", "<line_1>", "<line_2>", "<line_3>", "<line_4>"
    And User sets the "<channel_a_value>"
    And User sets the "<data_rate_value>", "<use_filter>" and "<filter_time_constant>"
    Then User validates the solvent details

    Examples:
      | channel_a_value | data_rate_value | use_filter | filter_time_constant | line_1     | line_2   | line_3   | line_4   | flow_state | flow_rate |
      | 400             | 80              | OFF        | Fast                 | A,True,100 | B,True,0 | C,True,0 | D,True,0 | On         | 1.000     |
      | 260             | 160             | ON         | Fast                 | A,True,100 | B,True,0 | C,True,0 | D,True,0 | On         | 1.000     |
      | 300             | 20              | On         | Normal               | A,True,100 | B,True,0 | C,True,0 | D,True,0 | On         | 1.000     |
      | 350             | 10              | On         | Slow                 | A,True,100 | B,True,0 | C,True,0 | D,True,0 | On         | 1.000     |


  @real @weekly
  Scenario Outline: To run the noise drift workflow when user abort it
    Given User navigates to health troubleshoot area
    And User navigates to TUV section
    When User taps noise-drift start panel
    And User validates the welcome context in the welcome screen
    And User taps next
    And User navigates to the summary screen
    And User taps start
    When User stops the workflow after "<stop_time>"
    Then User validates the status stopped for the noise and drift workflow
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | stop_time |
      | 3         |
      | 25        |

    
