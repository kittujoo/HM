  """
  Desc: Feature to validate ISYM About Test.
  """

@isym @isym_about_feature @quarantine
Feature: iSym | About Response Validation

  @isym_workflows_completion @quarantine
  Scenario: Validate About API Response
    When the about information is requested
    Then the about information is available
