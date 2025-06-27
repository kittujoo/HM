  """
  Desc: Feature to validate ISYM Emergency Stop Test
  """

@isym @isym_emergency_stop_feature
Feature: iSym | Emergency Stop Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_abort @isym_emergency_stop_test_workflow
  Scenario Outline: iSym Emergency Stop Test
    When flow started with given data:
      | flowRateTargetMlPerMin | <flowRateTargetMlPerMin> |
      | solventAPct            | <solventAPct>            |
      | solventBPct            | <solventBPct>            |
      | solventCPct            | <solventCPct>            |
      | solventDPct            | <solventDPct>            |
    Then the response status code is "200"
    And flow status result has next data:
      | flowRateTargetMlPerMin | <flowRateTargetMlPerMin> |
      | solventAPct            | <solventAPct>            |
      | solventBPct            | <solventBPct>            |
      | solventCPct            | <solventCPct>            |
      | solventDPct            | <solventDPct>            |
    Then the flowRateCurrentMlPerMin changes to "<flowRateTargetMlPerMin>"
    When Emergency Stop command is sent
    Then the response status code is "200"
    And the system state changes to Halted
    And the flowRateCurrentMlPerMin changes to "0.0"

    Examples:
      | flowRateTargetMlPerMin | solventAPct | solventBPct | solventCPct | solventDPct |
      | 10.0                   | 25.0        | 25.0        | 25.0        | 25.0        |
      | 0.001                  | 50.0        | 50.0        | 0.0         | 0.0         |
      | 5.0                    | 0.0         | 0.0         | 0.0         | 100.0       |
      | 1.0                    | 0.0         | 0.0         | 50.0        | 50.0        |
