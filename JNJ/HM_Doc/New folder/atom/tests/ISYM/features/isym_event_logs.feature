@isym @ALIST-233 @isym_event_log_feature
Feature: iSym | Event Log Test

  @isym_single_log_events
  Scenario: Validate Event Log Is Generated For Single Entry Request
    Given the latest log id is stored
    And the event log entry is added manually
    When the single event log information is requested
    Then the event log information is available


  @isym_multiple_log_event
  Scenario: Validate Event Log Is Generated For Multiple Entry Request
    Given the event log entry is added manually
    When all the event log information are requested
    Then the event log information is available


  @isym_event_log_valid_payload
  Scenario: Runs To Completion With Non Default Property Values - Add Entry
    When the event log entry is added with non-default values
    Then the response status code is "200"


  @isym_event_log_valid_payload
  Scenario: Runs To Completion With Non Default Property Values - Single Entry
    Given the latest log id is stored
    When the single event log entry is requested with non-default values
    Then the response status code is "200"


  @isym_event_log_valid_payload
  Scenario: Runs To Completion With Non Default Property Values - Multiple Entry
    When multiple event log entries are requested with non-default values
    Then the response status code is "200"


  @isym_event_log_valid_payload
  Scenario Outline: Runs To Completion With Valid Enums - Add Entry
    When the event log entry is added with "<property_name>" = "<property_value>"
    Then the response status code is "200"

    Examples:
      | property_name | property_value              |
      | eventtype     | AuditEventType_SOFTWARE     |
      | eventtype     | AuditEventType_HARDWARE     |
      | eventtype     | AuditEventType_INSTALLATION |


  @isym_event_log_valid_payload
  Scenario Outline: Runs To Completion With Valid Boundary Values - Multiple Entry
    When multiple event log entries are requested with "<property_name>" = "<property_value>"
    Then the response status code is "200"

    Examples:
      | property_name | property_value |
      | pageNumber    | 1              |
      | eventsPerPage | 1              |
      | eventsPerPage | 25             |
      | eventsPerPage | 50             |


  @isym_event_log_invalid_payload
  Scenario Outline: Invalid Values - Add Entry
    When the event log entry is added with "<property_name>" = "<property_value>"
    Then the response status code is "500"

    Examples:
      | property_name | property_value |
      | eventtype     | True           |
      | user          | 1.0            |
      | comments      | 1.0            |


  @isym_event_log_invalid_payloadd
  Scenario Outline: Invalid Values - Multiple Entry
    When multiple event log entries are requested with "<property_name>" = "<property_value>"
    Then the response status code is "500"

    Examples:
      | property_name  | property_value |
      | pageNumber     | True           |
      | eventsPerPage  | True           |
      | earliestDate   | 1.0            |
      | latestDate     | 1.0            |
      | sqlWhereClause | 1.0            |


  @isym_event_log_invalid_payload
  Scenario Outline: Invalid Values - Single Entry
    When multiple event log entries are requested with "<property_name>" = "<property_value>"
    Then the response status code is "500"
    Examples:
      | property_name | property_value |
      | id            | True           |


  @isym_event_log_invalid_payload
  Scenario Outline: Additional Values - Add Entry
    When the event log entry is added with "<property_name>" = "<property_value>"
    Then the response status code is "500"
    Examples:
      | property_name | property_value |
      | case_number   | 100            |


  @isym_event_log_invalid_payload
  Scenario Outline: Additional Values - Multiple Entry
    When multiple event log entries are requested with "<property_name>" = "<property_value>"
    Then the response status code is "500"
    Examples:
      | property_name | property_value |
      | case_number   | 100            |


  @isym_event_log_invalid_payload
  Scenario Outline: Additional Values - Single Entry
    When the single event log entry is requested with "<property_name>" = "<property_value>"
    Then the response status code is "500"
    Examples:
      | property_name | property_value |
      | case_number   | 100            |


  @isym_event_log_invalid_payload
  Scenario: Missing Values - Add Entry
    When the event log entry is added with missing properties:
      | user      |
      | eventtype |
      | comments  |
    Then the response status code is "500"


  @isym_event_log_invalid_payload @quarantine
  Scenario: Missing Values - Multiple Entry
    When multiple event log entries are requested with "eventsPerPage" missing
    Then the response status code is "500"


  @isym_event_log_invalid_payload @quarantine
  Scenario: Missing Values - Single Entry
    When the single event log entry is requested with "id" missing
    Then the response status code is "500"
