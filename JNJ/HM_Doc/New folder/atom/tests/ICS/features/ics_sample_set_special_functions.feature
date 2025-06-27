@ics @ALIST-229 @weekly @ics_sample_set_functions_feature
Feature: Sample set special functions

  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And the "predefined_data" instrument version specific project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And new line is added in sample set


  @real_or_simulation
  Scenario Outline: Execute special functions with run time
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And run time "<Run Time>" is added
    And the sample set is saved
    And the acquisition starts
    Then the sample set status is set to "<Status>"
    And the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | Function         | Run Time | Status                           |
      | Wet Prime        | 5.00     | Sample Set - Wet Prime           |
      | Condition Column | 5.00     | Sample Set - Conditioning Column |
      | Equilibrate      | 5.00     | Sample Set - Equilibrating       |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special function with run time and abort option
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And run time "<Run Time>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"
    When select Abort option "<Abort>" from Sample set
    Then the sample set acquisition completes with state "<State>"

    Examples:
      | Function         | Run Time | Status                    | Abort                               | State                                         |
      | Wet Prime        | 1        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wet Prime        | 1        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wet Prime        | 1        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wet Prime        | 1        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wet Prime        | 1        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wet Prime        | 1        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Condition column | 1        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Condition column | 1        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Condition column | 1        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Condition column | 1        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Condition column | 1        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Condition column | 1        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Condition column | 1        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Condition column | 1        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Condition column | 1        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Condition column | 1        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Condition column | 1        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Condition column | 1        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Condition column | 1        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Condition column | 1        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Condition column | 1        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Condition column | 1        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Equilibrate      | 1        | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Equilibrate      | 1        | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Equilibrate      | 1        | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Equilibrate      | 1        | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Equilibrate      | 1        | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special functions with run time plus network disconnect and reconnect short time
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And run time "<Run Time>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition starts
    And the sample set acquisition completes with state "System Idle - Sample Set Complete"
    And Control Panel shows "Idle" state


    Examples:
      | Function         | Run Time | Status                    | Disconnect time |
      | Wet Prime        | 1        | Preparing                 | 5               |
      | Wet Prime        | 1        | Preparing                 | 10              |
      | Wet Prime        | 1        | Preparing                 | 12              |
      | Wet Prime        | 1        | Preparing                 | 15              |
      | Wet Prime        | 1        | Applying method condition | 5               |
      | Wet Prime        | 1        | Applying method condition | 10              |
      | Wet Prime        | 1        | Applying method condition | 12              |
      | Wet Prime        | 1        | Applying method condition | 15              |
      | Wet Prime        | 1        | Setting up                | 5               |
      | Wet Prime        | 1        | Setting up                | 10              |
      | Wet Prime        | 1        | Setting up                | 12              |
      | Wet Prime        | 1        | Setting up                | 15              |
      | Wet Prime        | 1        | Running                   | 5               |
      | Wet Prime        | 1        | Running                   | 10              |
      | Wet Prime        | 1        | Running                   | 12              |
      | Wet Prime        | 1        | Running                   | 15              |
      | Condition column | 1        | Preparing                 | 5               |
      | Condition column | 1        | Preparing                 | 10              |
      | Condition column | 1        | Preparing                 | 12              |
      | Condition column | 1        | Preparing                 | 15              |
      | Condition column | 1        | Applying method condition | 5               |
      | Condition column | 1        | Applying method condition | 10              |
      | Condition column | 1        | Applying method condition | 12              |
      | Condition column | 1        | Applying method condition | 15              |
      | Condition column | 1        | Setting up                | 5               |
      | Condition column | 1        | Setting up                | 10              |
      | Condition column | 1        | Setting up                | 12              |
      | Condition column | 1        | Setting up                | 15              |
      | Condition column | 1        | Running                   | 5               |
      | Condition column | 1        | Running                   | 10              |
      | Condition column | 1        | Running                   | 12              |
      | Condition column | 1        | Running                   | 15              |
      | Equilibrate      | 1        | Preparing                 | 5               |
      | Equilibrate      | 1        | Preparing                 | 10              |
      | Equilibrate      | 1        | Preparing                 | 12              |
      | Equilibrate      | 1        | Preparing                 | 15              |
      | Equilibrate      | 1        | Applying method condition | 5               |
      | Equilibrate      | 1        | Applying method condition | 10              |
      | Equilibrate      | 1        | Applying method condition | 12              |
      | Equilibrate      | 1        | Applying method condition | 15              |
      | Equilibrate      | 1        | Setting up                | 5               |
      | Equilibrate      | 1        | Setting up                | 10              |
      | Equilibrate      | 1        | Setting up                | 12              |
      | Equilibrate      | 1        | Setting up                | 15              |
      | Equilibrate      | 1        | Running                   | 5               |
      | Equilibrate      | 1        | Running                   | 10              |
      | Equilibrate      | 1        | Running                   | 12              |
      | Equilibrate      | 1        | Running                   | 15              |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special functions with run time plus network disconnect and reconnect longer time
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And run time "<Run Time>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition is stoped
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Idle" state


    Examples:
      | Function         | Run Time | Status                    | Disconnect time |
      | Wet Prime        | 1        | Preparing                 | 60              |
      | Wet Prime        | 1        | Preparing                 | 80              |
      | Wet Prime        | 1        | Preparing                 | 100             |
      | Wet Prime        | 1        | Preparing                 | 120             |
      | Wet Prime        | 1        | Applying method condition | 60              |
      | Wet Prime        | 1        | Applying method condition | 80              |
      | Wet Prime        | 1        | Applying method condition | 100             |
      | Wet Prime        | 1        | Applying method condition | 120             |
      | Wet Prime        | 1        | Setting up                | 60              |
      | Wet Prime        | 1        | Setting up                | 80              |
      | Wet Prime        | 1        | Setting up                | 100             |
      | Wet Prime        | 1        | Setting up                | 120             |
      | Wet Prime        | 1        | Running                   | 60              |
      | Wet Prime        | 1        | Running                   | 80              |
      | Wet Prime        | 1        | Running                   | 100             |
      | Wet Prime        | 1        | Running                   | 120             |
      | Condition column | 1        | Preparing                 | 60              |
      | Condition column | 1        | Preparing                 | 80              |
      | Condition column | 1        | Preparing                 | 100             |
      | Condition column | 1        | Preparing                 | 120             |
      | Condition column | 1        | Applying method condition | 60              |
      | Condition column | 1        | Applying method condition | 80              |
      | Condition column | 1        | Applying method condition | 100             |
      | Condition column | 1        | Applying method condition | 120             |
      | Condition column | 1        | Setting up                | 60              |
      | Condition column | 1        | Setting up                | 80              |
      | Condition column | 1        | Setting up                | 100             |
      | Condition column | 1        | Setting up                | 120             |
      | Condition column | 1        | Running                   | 60              |
      | Condition column | 1        | Running                   | 80              |
      | Condition column | 1        | Running                   | 100             |
      | Condition column | 1        | Running                   | 120             |
      | Equilibrate      | 1        | Preparing                 | 60              |
      | Equilibrate      | 1        | Preparing                 | 80              |
      | Equilibrate      | 1        | Preparing                 | 100             |
      | Equilibrate      | 1        | Preparing                 | 120             |
      | Equilibrate      | 1        | Applying method condition | 60              |
      | Equilibrate      | 1        | Applying method condition | 80              |
      | Equilibrate      | 1        | Applying method condition | 100             |
      | Equilibrate      | 1        | Applying method condition | 120             |
      | Equilibrate      | 1        | Setting up                | 60              |
      | Equilibrate      | 1        | Setting up                | 80              |
      | Equilibrate      | 1        | Setting up                | 100             |
      | Equilibrate      | 1        | Setting up                | 120             |
      | Equilibrate      | 1        | Running                   | 60              |
      | Equilibrate      | 1        | Running                   | 80              |
      | Equilibrate      | 1        | Running                   | 100             |
      | Equilibrate      | 1        | Running                   | 120             |


  @real_or_simulation
  Scenario: Execute Purg Inj function without run time
    When function "Purge Inj" is selected
    And method set "isocratic UV" is selected
    And the sample set is saved
    And the acquisition starts
    Then the sample set status is set to "Sample Set - Purging"
    And the sample set acquisition completes with state "System Idle - Sample Set Complete"


  @real_or_simulation
  Scenario: Execute Wash Needle function without run time
    When function "Wash Needle" is selected
    And method set "isocratic UV" is selected
    And sample prep "2" is added
    And the sample set is saved
    And the acquisition starts
    Then the sample set status is set to "Sample Set - Washing Needle"
    And the sample set acquisition completes with state "System Idle - Sample Set Complete"


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special function without run time and abort option
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And sample prep "<Sample prep>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"
    When select Abort option "<Abort>" from sample set
    Then the sample set acquisition completes with state "<State>"

    Examples:
      | Function    | Sample prep | Status                    | Abort                               | State                                         |
      | Wash Needle | 2           | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wash Needle | 2           | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wash Needle | 2           | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wash Needle | 2           | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Wash Needle | 2           | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Wash Needle | 2           | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Purge inj   |             | Preparing                 | Abort now                           | System Idle - Aborted by System\Administrator |
      | Purge inj   |             | Preparing                 | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Purge inj   |             | Preparing                 | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Purge inj   |             | Preparing                 | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Purge inj   |             | Applying method condition | Abort now                           | System Idle - Aborted by System\Administrator |
      | Purge inj   |             | Applying method condition | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Purge inj   |             | Applying method condition | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Purge inj   |             | Applying method condition | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Purge inj   |             | Setting up                | Abort now                           | System Idle - Aborted by System\Administrator |
      | Purge inj   |             | Setting up                | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Purge inj   |             | Setting up                | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Purge inj   |             | Setting up                | Abort run and continue on next line | System Idle - Sample Set Complete             |
      | Purge inj   |             | Running                   | Abort now                           | System Idle - Aborted by System\Administrator |
      | Purge inj   |             | Running                   | Abort after Vial is completed       | System Idle - Sample Set Complete             |
      | Purge inj   |             | Running                   | Abort after Injection is completed  | System Idle - Sample Set Complete             |
      | Purge inj   |             | Running                   | Abort run and continue on next line | System Idle - Sample Set Complete             |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special function without run time plus network disconnect and reconnect short time
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And sample prep "<Sample prep>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition starts
    And the sample set state is "System Idle - Sample Set Complete"
    And Control Panel shows "Idle" state


    Examples:
      | Function    | Sample prep | Status                    | Disconnect time |
      | Wash Needle | 1           | Preparing                 | 5               |
      | Wash Needle | 1           | Preparing                 | 10              |
      | Wash Needle | 1           | Preparing                 | 12              |
      | Wash Needle | 1           | Preparing                 | 15              |
      | Wash Needle | 1           | Applying method condition | 5               |
      | Wash Needle | 1           | Applying method condition | 10              |
      | Wash Needle | 1           | Applying method condition | 12              |
      | Wash Needle | 1           | Applying method condition | 15              |
      | Wash Needle | 1           | Setting up                | 5               |
      | Wash Needle | 1           | Setting up                | 10              |
      | Wash Needle | 1           | Setting up                | 12              |
      | Wash Needle | 1           | Setting up                | 15              |
      | Wash Needle | 1           | Running                   | 5               |
      | Wash Needle | 1           | Running                   | 10              |
      | Wash Needle | 1           | Running                   | 12              |
      | Wash Needle | 1           | Running                   | 15              |
      | Purge inj   |             | Preparing                 | 5               |
      | Purge inj   |             | Preparing                 | 10              |
      | Purge inj   |             | Preparing                 | 12              |
      | Purge inj   |             | Preparing                 | 15              |
      | Purge inj   |             | Applying method condition | 5               |
      | Purge inj   |             | Applying method condition | 10              |
      | Purge inj   |             | Applying method condition | 12              |
      | Purge inj   |             | Applying method condition | 15              |
      | Purge inj   |             | Setting up                | 5               |
      | Purge inj   |             | Setting up                | 10              |
      | Purge inj   |             | Setting up                | 12              |
      | Purge inj   |             | Setting up                | 15              |
      | Purge inj   |             | Running                   | 5               |
      | Purge inj   |             | Running                   | 10              |
      | Purge inj   |             | Running                   | 12              |
      | Purge inj   |             | Running                   | 15              |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute special function without run time plus network disconnect and reconnect longer time
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And sample prep "<Sample prep>" is added
    And the sample set is saved
    And the acquisition starts
    Then the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition is stoped
    And the sample set acquisition completes with state "System Idle-Instrument failure"
    And Control Panel shows "Idle" state


    Examples:
      | Function    | Sample prep | Status                    | Disconnect time |
      | Wash Needle | 1           | Preparing                 | 60              |
      | Wash Needle | 1           | Preparing                 | 80              |
      | Wash Needle | 1           | Preparing                 | 100             |
      | Wash Needle | 1           | Preparing                 | 120             |
      | Wash Needle | 1           | Applying method condition | 60              |
      | Wash Needle | 1           | Applying method condition | 80              |
      | Wash Needle | 1           | Applying method condition | 100             |
      | Wash Needle | 1           | Applying method condition | 120             |
      | Wash Needle | 1           | Setting up                | 60              |
      | Wash Needle | 1           | Setting up                | 80              |
      | Wash Needle | 1           | Setting up                | 100             |
      | Wash Needle | 1           | Setting up                | 120             |
      | Wash Needle | 1           | Running                   | 60              |
      | Wash Needle | 1           | Running                   | 80              |
      | Wash Needle | 1           | Running                   | 100             |
      | Wash Needle | 1           | Running                   | 120             |
      | Purge inj   |             | Preparing                 | 60              |
      | Purge inj   |             | Preparing                 | 80              |
      | Purge inj   |             | Preparing                 | 100             |
      | Purge inj   |             | Preparing                 | 120             |
      | Purge inj   |             | Applying method condition | 60              |
      | Purge inj   |             | Applying method condition | 80              |
      | Purge inj   |             | Applying method condition | 100             |
      | Purge inj   |             | Applying method condition | 120             |
      | Purge inj   |             | Setting up                | 60              |
      | Purge inj   |             | Setting up                | 80              |
      | Purge inj   |             | Setting up                | 100             |
      | Purge inj   |             | Setting up                | 120             |
      | Purge inj   |             | Running                   | 60              |
      | Purge inj   |             | Running                   | 80              |
      | Purge inj   |             | Running                   | 100             |
      | Purge inj   |             | Running                   | 120             |


  @real @new @ignore
  Scenario Outline: Execute special functions with run time and system clock time change
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And run time "<Run Time>" is added
    And the sample set is saved
    And the acquisition starts
    Then the sample set status is set to "<Status>"
    When system clock time is changed with "<Time difference in hours>"
    Then the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | Function         | Run Time | Status           | Time difference in hours |
      | Wet Prime        | 1        | Wet Prime        | -1                       |
      | Wet Prime        | 1        | Wet Prime        | +1                       |
      | Condition column | 1        | Condition column | -1                       |
      | Condition column | 1        | Condition column | +1                       |
      | Equilibrate      | 1        | Equilibrate      | -1                       |
      | Equilibrate      | 1        | Equilibrate      | +1                       |


  @real @new @ignore
  Scenario Outline: Execute special function without run time and system clock time change
    When function "<Function>" is selected
    And method set "isocratic UV" is selected
    And sample prep "<Sample prep>" is added
    And the sample set is saved
    And the acquisition starts
    Then the sample set status is set to "<Status>"
    When system clock time is changed with "<Time difference in hours>"
    Then the sample set acquisition completes with state "System Idle - Sample Set Complete"

    Examples:
      | Function    | Sample prep | Status      | Time difference in hours |
      | Wash Needle | 2           | Wash Needle | -1                       |
      | Wash Needle | 2           | Wash Needle | +1                       |
      | Purge inj   |             | Purge Inj   | -1                       |
      | Purge inj   |             | Purge Inj   | +1                       |
