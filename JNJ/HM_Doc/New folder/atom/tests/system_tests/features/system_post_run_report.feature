@ALIST-258 @system @real @weekly @tuv @tuv_bio @post_run_report_feature @new @ignore
Feature: System | Post run report
  The post run report should contain a list of the parameters used after a sample was run.
  The post run is an useful way to view the behaviour of the system after a run was made and troubleshoot potential issues.


  Scenario: Post run report titles and labels
    Given a sample was run
    When a post run report was made available
    Then the post run report contains the following
      | Label                                     |
      | Alliance iS Post Run Report               |
      | Sample                                    |
      | System                                    |
      | Driver software version                   |
      | Instrument Version                        |
      | Serial Number                             |
      | Acquisition Start Time                    |
      | Acquisition End Time                      |
      | Dwell volume                              |
      | Tubing Kit                                |
      | QSM                                       |
      | Minimum System Pressure                   |
      | Maximum System Pressure                   |
      | Average System Pressure                   |
      | Mixer Assembly                            |
      | Mixer volume                              |
      | FTN                                       |
      | Extension Loop Size                       |
      | Needle Volume                             |
      | Minimum Sample Temperature                |
      | Maximum Sample Temperature                |
      | Average Sample Temperature                |
      | Seal Wash Pump Flow Rate                  |
      | Extension Loop Installed                  |
      | CHC                                       |
      | Minimum Column Temperature                |
      | Maximum Column Temperature                |
      | Average Column Temperature                |
      | Column Type                               |
      | Column Serial Number                      |
      | Column Part Number                        |
      | Column GTIN                               |
      | TUV                                       |
      | Lamp On                                   |
      | Lamp Minutes                              |
      | Lamp Serial Number                        |
      | Flow Cell Type                            |
      | Shutter Configuration - Autoclose Shutter |
      | Lamp Warmup Delay                         |
      | Pre-Run Checks                            |
      | Mobile Phase is not expired               |
      | System is qualified                       |
      | No pending performance maintenance        |
      | eConnect Column must be installed         |
      | eConnect Column must match method         |
      | Sample plates must be installed           |
      | Sample plates must match method           |
      | All vials present                         |
      | Run time checks                           |
      | Mobile phase is low                       |
      | Wash solvent is low                       |
      | Alarms                                    |
      | Alarm                                     |


  Scenario: Pre-run checks set to Off are reported as Disabled
    Given the following settings are done in Kiosk app
      | Setting                            | Value |
      | Mobile Phase is not expired        | Off   |
      | System is qualified                | Off   |
      | No pending performance maintenance | Off   |
      | eConnect Column must be installed  | Off   |
      | eConnect Column must match method  | Off   |
      | Sample plates must be installed    | Off   |
      | Sample plates must match method    | Off   |
      | All vials present                  | Off   |
    And a sample has finished running
    When the post run report is made available
    Then the post run report contains the following information
      | Setting                            | Value    |
      | Mobile phase is not expired        | Disabled |
      | System is qualified                | Disabled |
      | No pending performance maintenance | Disabled |
      | eConnect Column must be installed  | Disabled |
      | eConnect Column must match method  | Disabled |
      | Sample plates must be installed    | Disabled |
      | Sample plates must match method    | Disabled |
      | All vials present                  | Disabled |


  Scenario: Pre-run checks set to On are reported as Enabled
    Given the following setting are done in Kiosk app
      | Setting                            | Value |
      | Mobile Phase is not expired        | On    |
      | System is qualified                | On    |
      | No pending performance maintenance | On    |
      | eConnect Column must be installed  | On    |
      | eConnect Column must match method  | On    |
      | Sample plates must be installed    | On    |
      | Sample plates must match method    | On    |
      | All vials present                  | On    |
    When a sample has finished running
    And the post run report is made available
    Then the post run report contains the following information
      | Setting                            | Value   |
      | Mobile phase is not expired        | Enabled |
      | System is qualified                | Enabled |
      | No pending performance maintenance | Enabled |
      | eConnect Column must be installed  | Enabled |
      | eConnect Column must match method  | Enabled |
      | Sample plates must be installed    | Enabled |
      | Sample plates must match method    | Enabled |
      | All vials present                  | Enabled |


  Scenario: Run Time Checks set to Off are reported as Disabled
    Given the following setting are done in Kiosk app
      | Setting             | Value |
      | Mobile phase is low | Off   |
      | Wash solvent is low | Off   |
    When a sample has finished running
    And the post run report is made available
    Then the post run report contains the following information
      | Setting             | Value    |
      | Mobile phase is low | Disabled |
      | Wash solvent is low | Disabled |


  Scenario: Settings from the instrument method appear correctly in the post run report
    Given an instrument method was set with TUV Lamp "On"
    When a sample is run with the same instrument method
    And the run finishes succesfully
    And the post run report is made available
    Then the post run report contains "Lamp On True"


  Scenario: Settings from the instrument method appear correctly in the post run report
    Given an instrument method was set with TUV Lamp "OFf"
    When a sample is run with the same instrument method
    And the run finishes succesfully
    And the post run report is made available
    Then the post run report contains "Lamp On False"


  Scenario: Column Temperature is reported correctly in the post run report
    Given an instrument method is configured with the following Settings
      | Setting                                 | Value |
      | Column Temperature Enabled              | On    |
      | Column Temperature                      | 40    |
      | Column Temperature Tolerance Enabled    | On    |
      | Column Temperature Tolerance            | 2     |
      | Column Temperature Data Channel Enabled | On    |
    When a sample is run with the same instrument method
    And the run finishes succesfully
    And the post run report is made available
    And the column temperature data channel information is made available
    Then column temperature data channel and the post run report contain the same information


  Scenario: Column Temperature is reported correctly in the post run report
    Given an instrument method is configured with the following Settings
      | Setting                                 | Value |
      | Sample Temperature Enabled              | On    |
      | Sample Temperature                      | 20    |
      | Sample Temperature Tolerance Enabled    | On    |
      | Sample Temperature Tolerance            | 2     |
      | Sample Temperature Data Channel Enabled | On    |
    When a sample is run with the same instrument method
    And the run finishes succesfully
    And the post run report is made available
    And the sample temperature data channel information is made available
    Then sample temperature data channel and the post run report contain the same information


  Scenario: Hardware info from the instrument used during the run is reported correctly in post run report
    Given the instrument has an eColumn installed
    And the instrument is configured with an extension loop
    And the instrument is configured with a standard tubing kit
    And the instrument is configured with a 100 µL loop
    When a sample is run
    And the run finishes succesfully
    And the post run report is made available
    Then the value of "INFO" is the same between the kiosk and post run report
      | INFO                    |
      | Driver Software Version |
      | Instrument Version      |
      | Serial Number           |
      | Dwell Volume            |
      | Tubing Kit              |
      | Mixer Assembly          |
      | Mixer Volume            |
      | Extension Loop Size     |
      | Needle Volume           |
      | Column Type             |
      | Column Serial Number    |
      | Column Part Number      |
      | Lamp Serial Number      |


  Scenario: TUV leak detected is reported in the alarm section of the post run report
    Given a sample is configured with a run time of 10 Minutes
    When the sample is run
    And a leak occurs during the run
    And the post run report is made available
    Then the post run report contains the leak alarm
