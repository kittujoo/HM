@ics
Feature: Raise alarms on real environment

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state

  @real @PP_unit @raise_high_pressure_alarm_example
  Scenario: Pump system high pressure alarm is raised on Qsm
    When the "PumpSystemHighPressure" alarm is raised on Qsm with pressure value "5" and flow "2"
    Then run samples application is open for the current project and system
    And Control Panel shows "ERROR" state
    And the message center shows "Qsm : Pump system over 5.0 psi at 2.0 mL/min" message

