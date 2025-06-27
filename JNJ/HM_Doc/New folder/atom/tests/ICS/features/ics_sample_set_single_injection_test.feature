@ics @ALIST-229 @real_or_simulation @daily @ics_single_injection_feature
Feature: ICS | Single Injection Test

  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And the "predefined_data" instrument version specific project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state

  Scenario Outline: Single Injection from Sample Set
    When the sample name field "<Sample Name>" is entered
    And the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And run time "<Run Time>" is added
    And injection is started
    Then the acquisition starts
    And the sample set acquisition completes with state "System Idle - Single Inject Complete"

    Examples:
      | Sample Name | Function         | Method Set   | Plate | Injection Volume | Run Time |
      | SSV1        | Inject Samples   | isocratic UV | 1:A,1 | 5.0              | 2.00     |
      | SSV2        | Inject Standards | isocratic UV | 1:A,1 | 5.0              | 2.00     |
      | SSV3        | Inject Controls  | isocratic UV | 1:A,1 | 5.0              | 2.00     |


  @new @ignore
  Scenario Outline: Single Injection from Sample Set with Abort option
    When the sample name field "<Sample Name>" is entered
    And the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And run time "<Run Time>" is added
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"
    When select Abort option from Sample set
    Then the sample set acquisition completes with state "<State>"

    Examples:
      | Sample Name | Function       | Method Set   | Plate | Injection Volume | Run Time | Status    | State                                         |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | System Idle - Aborted by System\Administrator |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | System Idle - Aborted by System\Administrator |


  @new @ignore
  Scenario Outline: Single Injection from Sample Set with network disconnect and reconnect short time
    When the sample name field "<Sample Name>" is entered
    And the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And run time "<Run Time>" is added
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition starts
    And the sample set acquisition completes with state "System Idle-Single Inject Complete"
    And Control Panel status is set to "IDLE"


    Examples:
      | Sample Name | Function       | Method Set   | Plate | Injection Volume | Run Time | Status    | Disconnect Time |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 5               |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 10              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 15              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 5               |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 10              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 15              |


  @new @ignore
  Scenario Outline: Single Injection from Sample Set with network disconnect and reconnect longer time
    When the sample name field "<Sample Name>" is entered
    And the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And run time "<Run Time>" is added
    And injection is started
    Then the acquisition starts
    And the Control Panel status is set to "<Status>"

    When network card for instrument is disconnected
    Then the acquisition stops
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect time>" seconds since it was disconnected
    Then the acquisition is stoped
    And the sample set state is "System Idle-Instrument failure"
    And Control Panel shows "IDLE" state

    Examples:
      | Sample Name | Function       | Method Set   | Plate | Injection Volume | Run Time | Status    | Disconnect Time |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 60              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 80              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Preparing | 100             |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 60              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 80              |
      | SSV1        | Inject Samples | isocratic UV | 1:A,1 | 5                | 2        | Running   | 100             |


  @new @ignore
  Scenario Outline: Single Injection from Sample Set with system clock time
    When the sample name field "<Sample Name>" is entered
    And the entry from the dropdown menu for function "<Function>" is selected
    And the entry from dropdown menu for method set "<Method Set>" is selected
    And the plate position "<Plate>" is added
    And injection volume "<Injection Volume>" is added
    And run time "<Run Time>" is added
    And injection is started
    Then the acquisition starts
    When system clock time is changed with "<Time difference in hours>"
    Then the sample set acquisition completes with state "System Idle-Single Inject Complete"

    Examples:
      | Sample Name | Function         | Method Set   | Plate | Injection Volume | Run Time | Time difference in hours |
      | SSV1        | Inject Samples   | isocratic UV | 1:A,1 | 5                | 1        | -1                       |
      | SSV1        | Inject Samples   | isocratic UV | 1:A,1 | 5                | 1        | +1                       |
      | SSV2        | Inject Standards | isocratic UV | 1:A,1 | 5                | 1        | -1                       |
      | SSV2        | Inject Standards | isocratic UV | 1:A,1 | 5                | 1        | +1                       |
