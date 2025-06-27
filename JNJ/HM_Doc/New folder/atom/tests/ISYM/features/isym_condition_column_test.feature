  """
  Desc: Feature to validate ISYM Condition Column workflow.
  """

@isym @isym_condition_column_feature
Feature: iSym | Condition Column Test Workflow

  Background:
    Given the system state is Idle
    And the Exclusive Idle system state is set
    When the correct method data is sent
    Then the system state changes to At Method Conditions


  @isym_workflows_completion @isym_condition_column_workflow @quarantine @defect:INSISYM-4622
  Scenario: Condition Column
    When condition column is started with a runtime set to "1.0" minutes
#    Then the system state changes to Preparing
    Then the system state changes to Running
    And the system state changes to Exclusive Idle
    And the post run report is available

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


#       to be uncommented when Preparing state check will be supported
#
#  @isym_workflows_abort @isym_condition_column_preparing_abort
#  Scenario: Condition Column abort while at Preparing state
#    When condition column is started with a runtime set to "1.0" minutes
#           #Then the system state changes to Preparing
#    Then the system state changes to Running
#
#    When the system stop command is requested
#    Then the system state changes to Exclusive Idle
#
#    When the Exclusive Idle system state is released
#    Then the system state changes to Idle


  @isym_workflows_abort @isym_condition_column_running_abort
  Scenario: Condition Column abort while at Running state
    When condition column is started with a runtime set to "1.0" minutes
    Then the system state changes to Running

    When the system stop command is requested
    Then the system state changes to Exclusive Idle

    When the Exclusive Idle system state is released
    Then the system state changes to Idle


  @isym_workflows @isym_condition_column_edge_cases
  Scenario: Runtime is set to Just Below Minimum
    When condition column is started with a runtime set to "-0.1" minutes
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_condition_column_edge_cases
  Scenario: Runtime is set to Just Above Maximum
    When condition column is started with a runtime set to "600.1" minutes
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_condition_column_edge_cases
  Scenario: Passing Runtime as Negative Value
    When condition column is started with a runtime set to "-1.0" minutes
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_condition_column_edge_cases
  Scenario: Passing Runtime as Zero Decimal Value
    When condition column is started with a runtime set to "1.0" minutes
    Then the system state changes to Running


  @isym_workflows @isym_condition_column_edge_cases
  Scenario: Passing Runtime as Zero Value
    When condition column is started with a runtime set to "0.0" minutes
    Then the system state changes to Running


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime as String Type data
    When condition column is started with a runtime set to "one" minutes with string type value
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime as Boolean Type data
    When condition column is started with a boolean type value as "false"
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime as Array Type data
    When condition column is started with a runtime set to "1.0" minutes with array type value
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime as Object Type data
    When condition column is started with a runtime as Object type value
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime as Null Value
    When column condition is started with a runtime set to null value
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Passing Runtime with an Additional Property
    When condition column is started with "runTimeMax" as "false"
    Then the system state changes to Exclusive Fail


  @isym_workflows @isym_invalid_input_types
  Scenario: Condition Column started with an Empty Payload
    When condition column is started with a empty payload
    Then the system state changes to Exclusive Fail
