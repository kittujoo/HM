@ics @ALIST-229 @weekly @ics_console_flow_state_feature
Feature: ICS Console-Control flow state

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And Console is launched from Control Panel
    And Console page shows "IDLE" state

  @real_or_simulation
  Scenario Outline: Change flow state
    Given flow is "<current_flow_state>"
    When select Commands from Console
    And set flow to "<new_flow_state>"
    Then Console Commands page shows flow status as "<commands_page_flow_status>"
    And Console Home page shows flow "<new_flow_state>"
    And Control Panel shows flow "<new_flow_state>"

    Examples:
      | current_flow_state | new_flow_state | commands_page_flow_status |
      | OFF                | ON             | Flow On                   |
      | ON                 | OFF            | Flow Off                  |


  @real_or_simulation
  Scenario Outline: Flow state doesn't change after system reset
    Given flow is "<current_flow_state>"
    When select Commands from Console
    And system reset is selected from Console
    Then Console page shows "IDLE" state
    And Console Commands page shows flow status as "<commands_page_flow_status>"
    And Console Home page shows flow "<new_flow_state>"
    And Control Panel shows flow "<new_flow_state>"

    Examples:
      | current_flow_state | new_flow_state | commands_page_flow_status |
      | OFF                | OFF            | Flow Off                  |
      | ON                 | ON             | Flow On                   |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute flow state with emergency stop option
    Given flow is "<current_flow_state>"
    When select Commands from Console
    And set flow to "<new_flow_state>"
    And Emergency Stop from Console is selected
    Then Emergency Stop starts
    And Console Commands page shows "SYSTEM HALTED"
    And Console Commands page shows flow "OFF"
    And Control Panel page shows flow "0.000"

    When select Commands from Console
    And system reset is selected from Console
    Then system reset starts
    And Console Commands page shows "IDLE" state
    And Console Commands page shows flow "OFF"
    And Console Home page shows flow "0.000"
    And Control Panel shows flow "0.000"

    Examples:
      | current_flow_state | new_flow_state |
      | OFF                | ON             |
      | ON                 | OFF            |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute flow state with network disconnect and reconnect
    Given flow is "<current_flow_state>"
    When select Commands from Console
    And set flow to "<new_flow_state>"
    And network card for instrument is disconnected
    Then Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect_time>" seconds since it was disconnected
    Then Console Commands page shows "IDLE" state
    And Console Commands page shows flow "<new_flow_state>"
    And Console Commands page shows flow status as "<commands_page_flow_status>"
    And Console Home page shows flow "<new_flow_state>"
    And Control Panel shows flow "<new_flow_state>"

    Examples:
      | current_flow_state | new_flow_state | commands_page_flow_status | Disconnect_time |
      | OFF                | ON             | Flow On                   | 5               |
      | OFF                | ON             | Flow On                   | 10              |
      | OFF                | ON             | Flow On                   | 12              |
      | ON                 | OFF            | Flow Off                  | 5               |
      | ON                 | OFF            | Flow Off                  | 10              |
      | ON                 | OFF            | Flow Off                  | 12              |
      | OFF                | ON             | Flow On                   | 60              |
      | OFF                | ON             | Flow On                   | 80              |
      | OFF                | ON             | Flow On                   | 100             |
      | ON                 | OFF            | Flow Off                  | 60              |
      | ON                 | OFF            | Flow Off                  | 80              |
      | ON                 | OFF            | Flow Off                  | 100             |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute flow state with system clock time
    Given flow is "<current_flow_state>"
    When select Commands from Console
    And set flow to "<new_flow_state>"
    And system clock time is changed with "<time_difference_in_hours>"
    Then Console Commands page shows flow "<new_flow_state>"
    And Console Commands page shows flow status as "<commands_page_flow_status>"
    And Console Home page shows flow "<new_flow_state>"
    And Control Panel shows flow "<new_flow_state>"

    Examples:
      | current_flow_state | time_difference_in_hours | new_flow_state | commands_page_flow_status |
      | OFF                | -1                       | ON             | Flow On                   |
      | ON                 | -1                       | OFF            | Flow Off                  |
      | OFF                | +1                       | ON             | Flow On                   |
      | ON                 | +1                       | OFF            | Flow Off                  |
