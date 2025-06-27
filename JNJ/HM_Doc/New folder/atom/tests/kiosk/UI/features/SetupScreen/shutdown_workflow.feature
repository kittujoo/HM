@kiosk @ALIST-228 @shutdown
Feature: Kiosk | Shutdown Workflow functionality

  @real @daily
  Scenario Outline: To validate the complete cycle of shutdown workflow
    When User taps the setup button in the home screen
    And User taps the shutdown workflow panel
    And User validates the welcome context in the welcome screen
    And User set the sample temperature as "<sample_temperature>"
    And User set the column temperature as "<column_temperature>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for "<flow_rate>"
    And User turns "<lamp_state>" the lamp
    Then User validates the summary screen details for temperature "<sample_temperature>", "<column_temperature>"
    And User validates the lamp state "<lamp_state>"
    And User validates the summary screen details for "<flow_rate>"
    And User taps on start button
    And User validates the test completes successfully
    And User validates the home screen for lamp state "<lamp_state>"
    And User validates the home screen for flow rate "<flow_rate>"
    And User validates the home screen for sample temperature "<sample_temperature>"
    And User validates the home screen for column temperature "<column_temperature>"

    Examples:
      | sample_temperature | column_temperature | lamp_state | flow_rate | line_1     | line_2    | line_3    | line_4    |
      | 8                  | 8                  | On         | 2         | A,True,85  | B,True,5  | C,True,5  | D,True,5  |
      

  @real @weekly
  Scenario Outline: To validate the complete cycle of shutdown workflow
    When User taps the setup button in the home screen
    And User taps the shutdown workflow panel
    And User validates the welcome context in the welcome screen
    And User set the sample temperature as "<sample_temperature>"
    And User set the column temperature as "<column_temperature>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for "<flow_rate>"
    And User turns "<lamp_state>" the lamp
    Then User validates the summary screen details for temperature "<sample_temperature>", "<column_temperature>"
    And User validates the lamp state "<lamp_state>"
    And User validates the summary screen details for "<flow_rate>"
    And User taps on start button
    And User validates the test completes successfully
    And User validates the home screen for lamp state "<lamp_state>"
    And User validates the home screen for flow rate "<flow_rate>"
    And User validates the home screen for sample temperature "<sample_temperature>"
    And User validates the home screen for column temperature "<column_temperature>"

    Examples:
      | sample_temperature | column_temperature | lamp_state | flow_rate | line_1     | line_2    | line_3    | line_4    |
      | 10                 | 20                 | On         | 0.001     | A,True,45  | B,False,0 | C,True,30 | D,True,25 |
      | 40                 | 40                 | On         | 0.1       | A,True,100 | B,False,0 | C,False,0 | D,False,0 |


  @real @daily
  Scenario Outline: To validate the shutdown workflow when user abort it
    When User taps the shutdown workflow panel
    And User validates the welcome context in the welcome screen
    And User set the sample temperature as "<sample_temperature>"
    And User set the column temperature as "<column_temperature>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for "<flow_rate>"
    And User turns "<lamp_state>" the lamp
    Then User validates the summary screen details for temperature "<sample_temperature>", "<column_temperature>"
    And User validates the lamp state "<lamp_state>"
    And User validates the summary screen details for "<flow_rate>"
    And User taps on start button
    And User aborts the prime workflow
    Then User validates the status screen for the shutdown workflow

    Examples:
      | sample_temperature | column_temperature | lamp_state | flow_rate | line_1    | line_2    | line_3    | line_4    |
      | Off                | Off                | Off        | Off       |           |           |           |           |
      | 10                 | 30                 | On         | 1.8       | A,True,25 | B,True,25 | C,True,25 | D,True,25 |

  @simulation @weekly
  Scenario Outline: The flow edit field in shutdown shows different state for different range of flow
    When User taps the shutdown workflow panel
    And User navigates to the flow settings screen
    Then Validate that the edit field shows "<error_state>" for "<flow_rate>"

    Examples:
      | error_state | flow_rate |
      | False       | 0.11      |
      | False       | 0.001     |
      | True        | 0.00      |
      | True        | 10.24     |
      | False       | 5.00      |


  @real @weekly @new @negative @ignore #need to find a way to trigger an alarm through isym
  Scenario Outline: To validate the shutdown workflow when user trigger an error
    When User taps the shutdown workflow panel
    And User validates the welcome context in the welcome screen
    And User set the sample temperature as "<sample_temperature>"
    And User set the column temperature as "<column_temperature>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for "<flow_rate>"
    And User turns "<lamp_state>" the lamp
    Then User validates the summary screen details for temperature "<sample_temperature>", "<column_temperature>"
    And User validates the lamp state "<lamp_state>"
    And User validates the summary screen details for "<flow_rate>"
    And User taps on start button
    And User raises an alarm (e.g. leak) during workflow execution
    Then User validates the workflow will state the expected behavior when an error occurs during a workflow

    Examples:
      | sample_temperature | column_temperature | lamp_state | flow_rate | line_1    | line_2    | line_3    | line_4    |
      | 10                 | 30                 | On         | 1.8       | A,True,25 | B,True,25 | C,True,25 | D,True,25 |

  @real @daily
  Scenario Outline: To validate the complete cycle of shutdown workflow when everything is turned off
    When User taps the shutdown workflow panel
    And User validates the welcome context in the welcome screen
    And User set the sample temperature as "<sample_temperature>"
    And User set the column temperature as "<column_temperature>"
    And User enters the solvent "<line_1>", "<line_2>", "<line_3>", "<line_4>" for "<flow_rate>"
    And User turns "<lamp_state>" the lamp
    Then User validates the summary screen details for temperature "<sample_temperature>", "<column_temperature>"
    And User validates the lamp state "<lamp_state>"
    And User validates the summary screen details for "<flow_rate>"
    And User taps on start button
    And User validates the test completes successfully

    Examples:
      | sample_temperature | column_temperature | lamp_state | flow_rate | line_1 | line_2 | line_3 | line_4 |
      | Off                | Off                | Off        | Off       |        |        |        |        |
