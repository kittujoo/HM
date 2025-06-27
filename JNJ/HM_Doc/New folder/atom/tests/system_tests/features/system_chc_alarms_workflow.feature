@system @ALIST-231 @system_chc_alarms_feature
Feature: System | CHC Alarms Workflow

  Background:
    Given an instrument system in "IDLE" state is connected

  @real @weekly @new @ignore
  Scenario Outline: To verify chc alarms are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is CHC
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type                         | message                                           | issue                                             |
      | TagReaderDoorOpen                  | Column compartment door is open                   | Column compartment door is open                   |
      | TagReaderBoardNotDetected          | RFID reader/writer hardware not installed         | RFID reader/writer hardware not installed         |
      | TagReaderBoardFailed               | RFID reader/writer hardware failure               | RFID reader/writer hardware failure               |
      | TagReaderBoardCommunicationFailure | RFID reader/writer hardware communication failure | RFID reader/writer hardware communication failure |
      | TagReaderCorruptTag                | Corrupt tag detected                              | Corrupt tag detected                              |
