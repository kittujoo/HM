  """
  Desc: ISYM sample set validation

  """

@isym @isym_sample_set_validation_feature
Feature: iSym | sample set validation

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_sample_set_validation_workflow
  Scenario: Submit Time Sample Set Validation
    When configure validation is requested
    And the sample set is validated
    Then the correct validation result is received