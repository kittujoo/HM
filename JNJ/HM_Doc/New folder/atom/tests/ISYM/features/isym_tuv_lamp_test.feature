  """
  Desc: Feature to validate Isym Tuv Lamp workflow
  """

@isym @isym_tuv_lamp_feature
Feature: iSym | Tuv Lamp Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_lamp_on
  Scenario: Turning ON Lamp
    Given the lamp is OFF
    When the lamp is requested to turn ON
    Then the state of the lamp changes to "LampState_WARMING"
    And the state of the lamp changes to "LampState_READY"
    And the lamp status is ON


  @isym_workflows_completion @isym_lamp_off
  Scenario: Turning OFF Lamp
    Given the lamp is ON
    When the lamp is requested to turn OFF
    Then the state of the lamp changes to "LampState_OFF"
    And the lamp status is OFF


  @isym_workflows_completion @isym_tuv_lamp_history_workflow
  Scenario: ISYM Tuv Lamp History Workflow
    When the tuv lamp history is requested
    Then the tuv lamp history with serial number, installation date, lamp minutes and ignitions counts is available


  @isym_workflows_completion @isym_tuv_lamp_intensity_workflow
  Scenario: ISYM Tuv Lamp Intensity Workflow
    When the tuv lamp intensity is requested
    Then the tuv lamp intensity with lamp intensity lamp usage is available


  @isym_workflows_completion @isym_tuv_lamp_hours_workflow
  Scenario: ISYM Tuv Lamp Hours Workflow
    When the tuv lamp hours is requested
    Then the tuv lamp hours information is available


  @isym_workflows_completion @isym_tuv_replace_lamp_workflow
  Scenario: ISYM Tuv Replace Lamp Workflow
    When the tuv replace lamp is requested
    Then the tuv lamp replacement activity started
    And the tuv lamp replacement activity completed

    When the tuv lamp replacement complete confirmation requested
    Then the tuv lamp replacement complete activity started
    And the tuv lamp replacement complete activity completed
