@ics @weekly @ics_multiple_sample_set_acquisition_feature
Feature: Multiple Sample Sets Acquisition Test

  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And the "predefined_data" instrument version specific project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state


  @real @new @ignore
  Scenario Outline: Multiple Sample Sets Acquisition
    Given Samples tab is selected
    And new line is added in sample set
    When the sample set is configured with the following data
      | Function         | Method Set   | Plate Position | Inj Vol | Number of Inj | Processing | Run Time | Data Start | Next Inj Delay | Sample Weight | Dilution |
      | Wet prime        | isocratic UV |                |         |               |            | 30       |            |                |               |          |
      | Condition Column | isocratic UV |                |         |               |            | 30       |            |                |               |          |
      | Inject Samples   | isocratic UV | "<Position 1>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Inject Standards | isocratic UV | "<Position 2>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Inject Samples   | isocratic UV | "<Position 3>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Inject Standards | isocratic UV | "<Position 4>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Inject Samples   | isocratic UV | "<Position 5>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Inject Controls  | isocratic UV | "<Position 6>" | 2       | 4             | Normal     | 60       | 0          | 0              | 1             | 1        |
      | Wash Needle      | isocratic UV |                |         |               |            | 15       |            |                |               |          |

    And the sample set is saved with name "<Sample Name>"
    And the acquisition starts
    Then the sample set acquisition completes with state "System Idle-Sample Set Complete"

      # note that Examples 1-3 are duplicated for 4-6 to achieve the expected runtime of 6-7 days
    Examples:
      | Sample Name | Position 1 | Position 2 | Position 3 | Position 4 | Position 5 | Position 6 |
      | SS_Run_1    | 1:A,1      | 1:A,2      | 1:D,3      | 1:D,4      | 1:F,6      | 1:F,7      |
      | SS_Run_2    | 2:A,1      | 2:A,2      | 2:D,3      | 2:D,4      | 2:F,6      | 2:F,7      |
      | SS_Run_3    | 3:A,1      | 3:A,2      | 3:D,3      | 3:D,4      | 3:F,6      | 3:F,7      |
      | SS_Run_4    | 1:A,1      | 1:A,2      | 1:D,3      | 1:D,4      | 1:F,6      | 1:F,7      |
      | SS_Run_5    | 2:A,1      | 2:A,2      | 2:D,3      | 2:D,4      | 2:F,6      | 2:F,7      |
      | SS_Run_6    | 3:A,1      | 3:A,2      | 3:D,3      | 3:D,4      | 3:F,6      | 3:F,7      |


  @real_or_simulation @new @ignore
  Scenario Outline: Multiple Sample Sets Acquisition with Abort option
    Given Samples tab is selected
    And new line is added in sample set
    When the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And number of injections "<Number of Inj>" is added
    And run time "<Run time>" is added
    And sample set is saved with "SS_Run_1"
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"
    When select Abort option "<Abort>" from Sample set
    Then the sample set acquisition completes with state "<State>"

    Examples:
      | Function       | Method Set   | Plate | Injection volume | Number of inj | Run time | Status                    | Abort                               | State                                         |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:A,1 | 2                | 1             | 3        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Inject Samples | isocratic UV | 2:D,3 | 2                | 1             | 3        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |


  @real @new @ignore
  Scenario Outline: Multiple Sample Sets Acquisition with system clock time change
    Given Samples tab is selected
    And new line is added in sample set
    When the sample set is configured with the following data
      | Function         | Method Set   | Plate Position | Inj Vol | Number of Inj | Processing | Run Time | Data Start | Next Inj Delay | Sample Weight | Dilution |
      | Wet prime        | isocratic UV |                |         |               |            | 3        |            |                |               |          |
      | Condition Column | isocratic UV |                |         |               |            | 3        |            |                |               |          |
      | Inject Samples   | isocratic UV | "<Position 1>" | 2       | 1             | Normal     | 3        | 0          | 0              | 1             | 1        |
      | Inject Standards | isocratic UV | "<Position 2>" | 2       | 1             | Normal     | 3        | 0          | 0              | 1             | 1        |

    And the sample set is saved with name "SS_Run_1"
    And injection is started
    Then the acquisition starts
    When system clock time is changed with "<Time Difference in Hours>"
    Then the sample set acquisition completes with state "System Idle-Sample Set Complete"

    Examples:
      | Position 1 | Position 2 | Time Difference in Hours |
      | 1:A,1      | 1:A,2      | -1                       |
      | 1:A,1      | 1:A,2      | +1                       |
      | 2:A,1      | 2:A,2      | -1                       |
      | 2:A,1      | 2:A,2      | -1                       |


  @real @new @ignore
  Scenario Outline: Multiple Sample Sets Acquisition with network disconnect and reconnect short time
    Given Samples tab is selected
    And new line is added in sample set
    When the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And number of injections "<Number of Inj>" is added
    And run time "<Run time>" is added
    And sample set is saved with "SS_Run_1"
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition starts
    And Control Panel shows "Idle" state
    Then the sample set acquisition completes with state "System Idle-Sample Set Complete"

    Examples:
      | Function       | Method Set   | Plate | Injection volume | Number of inj | Run time | Status                    | Disconnect time |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 5               |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 10              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 15              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 5               |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 10              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 15              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 5               |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 10              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 15              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 5               |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 10              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 15              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 5               |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 10              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 15              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 5               |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 10              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 15              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 5               |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 10              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 15              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 5               |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 10              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 15              |


  @real @new @ignore
  Scenario Outline: Multiple Sample Sets Acquisition with network disconnect and reconnect longer time
    Given Samples tab is selected
    And new line is added in sample set
    When the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And number of injections "<Number of Inj>" is added
    And run time "<Run time>" is added
    And sample set is saved with "SS_Run_1"
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stop
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition is stoped
    And Control Panel shows "Idle" state
    And the sample set state is "System Idle-Instrument failure"

    Examples:
      | Function       | Method Set   | Plate | Injection volume | Number of inj | Run time | Status                    | Disconnect time |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 60              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 80              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Preparing                 | 100             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 60              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 80              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Applying method condition | 100             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 60              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 80              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Setting up                | 100             |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 60              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 80              |
      | Inject Samples | isocratic UV | 1:A,1 | 2                | 1             | 3        | Running                   | 100             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 60              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 80              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Preparing                 | 100             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 60              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 80              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Applying method condition | 100             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 60              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 80              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Setting up                | 100             |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 60              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 80              |
      | Inject Samples | isocratic UV | 1:D,3 | 2                | 1             | 3        | Running                   | 100             |
