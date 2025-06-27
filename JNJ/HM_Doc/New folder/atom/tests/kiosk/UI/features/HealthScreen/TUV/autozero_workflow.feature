@kiosk @ALIST-228
Feature: Kiosk | Autozero and reset Workflow functionality

  Background:

    Given the lamp is On

  @real @weekly @updated @quarantine @defect:INSISPP-8103
  Scenario: To validate autozero functions

    When User navigates to health troubleshoot area
    And  User navigates to TUV section
    And  User taps Autozero Offsets panel
    And  User validates the Information autozero offsets screen
    And  User taps autozero button
    Then User validates that the Channel A Offset and Channel B Offset displayed values are non-zero
    And  User navigates to home area
    And  User validates the Channel Offset value is zero


  @real @weekly
  Scenario: To validate reset functions

    When User navigates to health troubleshoot area
    And  User navigates to TUV section
    And  User taps Autozero Offsets panel
    And  User validates the Information autozero offsets screen
    And  User taps reset button
    Then User validates that the Channel A Offset and Channel B Offset displayed values are zero
    And  User navigates to home area
    And  User validates the Channel Offset value is non-zero
