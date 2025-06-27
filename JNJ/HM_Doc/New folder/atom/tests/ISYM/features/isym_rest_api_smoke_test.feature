  """
  Desc: Smoke test to validate that isym satisfies minimum requirements for implemented functionalities.

  """
@rest_api_smoke_test
Feature: iSym | Rest API Smoke Test

  @rest_api_get_state
  Scenario: Instrument's current state can be retrieved via http get request
    When a command to get the instrument state is sent via HTTP request
    Then the HTTP reply returns the current state of the instrument

  @rest_api_endpoints @quarantine
  Scenario: Instrument isym routes can be retrieved
    When instrument routes are requested
    Then the routes returns a list of endpoints
    And the endpoints returned are not changed
