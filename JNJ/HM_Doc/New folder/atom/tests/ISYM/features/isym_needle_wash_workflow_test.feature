  """
  Desc: Feature to validate ISYM wash needle workflow.
  """

@isym @isym_wash_needle_feature @isym_needle_wash_feature
Feature: iSym | Wash Needle Test Workflow

  Background:
    Given the system state is Idle

  @isym_workflows_completion @isym_smftn_wash_needle_workflow
  Scenario Outline: Wash needle test with valid duration
    When the wash needle operation requested with washDurationSec = "<value>" seconds
    Then the response status code is "200"
    And the wash needle state is active for "<value>" seconds
    And the wash needle state becomes inactive
    And the last wash needle request was stored as "<value>"

    Examples:
      | value |
      | 7     | # intermediate
      | 1     | # min
      | 50    | # max

  @isym_workflows_completion @isym_smftn_wash_needle_invalid
  Scenario Outline: Wash needle test with out of range duration
    When the wash needle operation requested with washDurationSec = "<value>" seconds
    Then the response status code is "500"

    Examples:
      | value |
      | 51    | # above max
      | 0     | # below min

  @isym_workflows_completion @isym_smftn_wash_needle_invalid
  Scenario: Wash needle test without wash duration second property payload
    When the wash needle operation requested without washDurationSec property
    Then the response status code is "500"


  @isym_workflows_completion @isym_smftn_wash_needle_invalid
  Scenario: Wash needle test with wash duration second property value as string
    When the wash needle operation requested with washDurationSec as string
    Then the response status code is "500"


  @isym_workflows_completion @isym_smftn_wash_needle_invalid
  Scenario: Wash needle test with additional property in payload
    When the wash needle operation requested with additional property duration as 34
    Then the response status code is "500"


  @isym_workflows_completion @isym_smftn_wash_needle_invalid @quarantine
  Scenario: Wash needle test with property prime cycles in payload
    When the wash needle operation requested with primeCycles
    Then the response status code is "500"


  @isym_workflows_completion @isym_smftn_needle_wash_workflow
  Scenario: Needle wash test
    When the needle wash operation requested
    Then the response status code is "200"
    And the needle wash state is active
    And the needle wash state becomes inactive


  @isym_workflows_completion @isym_smftn_needle_wash_invalid
  Scenario: Needle wash request with a payload containing a random value
    When the needle wash operation requested with payload as string
    Then the response status code is "500"


  @isym_workflows_completion @isym_smftn_needle_wash_invalid
  Scenario Outline: Needle wash request with a payload of prime cycles or wash duration
    When the needle wash operation requested with payload "<property_name>"
    Then the response status code is "500"

    Examples:
      | property_name   |
      | primeCycles     |
      | washDurationSec |
