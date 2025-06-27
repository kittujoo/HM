@kiosk @ALIST-228 @needlesealreadiness
Feature: Kiosk | Needle Seal Readiness Workflow functionality

  @real @weekly @ignore #(INS-34484)
  Scenario Outline: To validate the successful completion of needle seal readiness test workflow
    Given User gets the system pressure from the dashboard
    When User navigates to sample manager section
    When User taps needle seal readiness test start panel
    And User validates the welcome context in the welcome screen
    And User enters the "<flow_rate>"
    And User enters the composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    Then User validates the summary screen details for "<flow_rate>" "<line_1>" "<line_2>" "<line_3>" "<line_4>" and system pressure
    And User starts the needle seal readiness test
    And User validates the result screen for the needle readiness test for "<flow_rate>" and pressure difference
    When user enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | flow_rate | line_1      | line_2      | line_3    | line_4    |
      | 1.000     | A,True,22.3 | B,True,47.7 | C,True,30 | D,False,0 |
      | 0.200     | A,True,25   | B,True 25   | C,True,25 | D,True,25 |
      | 5.000     | A,True,25   | B,True 25   | C,True,25 | D,True,25 |

  @real @daily @ignore #(INS-34484)
  Scenario: To validate needle seal readiness test workflow completes
    Given User gets the system pressure from the dashboard
    When User navigates to sample manager section
    When User taps needle seal readiness test start panel
    And User validates the welcome context in the welcome screen
    And User enters the flow rate
    And User enters the composition for solvent A, B, C, D
    Then User validates the summary screen details
    And User starts the needle seal readiness test
    And User validates the result screen for the needle readiness test for flow rate and pressure difference
    When user enters the log screen
    Then the log entry is created with correct time, date, category and action details

  @real @daily @ignore
  Scenario Outline: To validate the needle seal work flow when user abort it
    Given User sets pre-required date and time format
    And User gets the system pressure from the dashboard
    When User navigates to sample manager section
    When User taps needle seal readiness test start panel
    And User validates the welcome context in the welcome screen
    And User enters the "<flow_rate>"
    And User enters the composition "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    Then User validates the summary screen details for "<flow_rate>" "<line_1>" "<line_2>" "<line_3>" "<line_4>"
    And User starts the needle seal readiness test
    And User aborts the prime workflow
    Then User validates the status screen for the needle readiness workflow
    When User enters the log screen
    Then the log entry is created with correct time, date, category and action details

    Examples:
      | flow_rate | line_1      | line_2    | line_3      | line_4    |
      | 1.000     | A,True,33.9 | B,True,20 | C,True,46.1 | D,False,0 |


  @simulation @weekly
  Scenario Outline: The flow edit field shows different state for different range of flow
    Given User gets the system pressure from the dashboard
    When User navigates to sample manager section
    When User taps needle seal readiness test start panel
    And User validates the welcome context in the welcome screen
    Then Validate that the edit field shows "<error_state>" for "<flow_rate>"

    Examples:
      | error_state | flow_rate |
      | True        | 0.19      |
      | False       | 2.22      |
      | True        | 0.00      |
      | True        | 5.01      |
      | False       | 5.00      |
      | False       | 0.20      |


  @simulation @weekly
  Scenario Outline: The solvent composition edit field shows different state for different range of composition
    Given User gets the system pressure from the dashboard
    When User navigates to sample manager section
    When User taps needle seal readiness test start panel
    And User validates the welcome context in the welcome screen
    And User enters the "<flow_rate>"
    Then User validate the solvent edit field shows "<error_state>" for "<actual_composition>"

    Examples:
      | flow_rate | actual_composition | error_state |
      | 1.000     | 4000               | True        |
      | 1.000     | 22                 | False       |
      | 1.000     | 101                | True        |
      | 1.000     | 99.9               | False       |
