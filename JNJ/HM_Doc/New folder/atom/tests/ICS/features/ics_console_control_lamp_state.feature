@ics @ALIST-229 @daily @ics_console_lamp_state_feature
Feature: ICS Console-Control lamp state

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And Console is launched from Control Panel
    And Console page shows "IDLE" state

  @real_or_simulation
  Scenario Outline: Change lamp state
    Given lamp is "<current_lamp_state>"
    When select Commands from Console
    And set lamp to "<new_lamp_state>"
    Then Console Commands page shows lamp "<new_lamp_state>"
    When User selects Home from Console
    Then Console Home page shows lamp "<new_lamp_state>"
    And Control Panel shows lamp "<new_lamp_state>"

    Examples:
      | current_lamp_state | new_lamp_state |
      | OFF                | ON             |
      | ON                 | OFF            |


  @real_or_simulation
  Scenario Outline: Lamp state doesn't change after system reset
    Given lamp is "<current_lamp_state>"
    When select Commands from Console
    And system reset is selected from Console
    Then Console page shows "IDLE" state
    And Console Commands page shows lamp "<new_lamp_state>"
    When User selects Home from Console
    Then Console Home page shows lamp "<new_lamp_state>"
    And Control Panel shows lamp "<new_lamp_state>"

    Examples:
      | current_lamp_state | new_lamp_state |
      | OFF                | OFF            |
      | ON                 | ON             |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute lamp state with emergency stop option
    Given lamp is "<current_lamp_state>"
    When select Commands from Console
    And set lamp to "<new_lamp_state>"
    And Emergency Stop from Console is selected
    Then Emergency Stop starts
    And Console Commands page shows "SYSTEM HALTED"
    And Console Commands page shows lamp "<current_lamp_state>"
    And Control Panel page shows lamp "<current_lamp_state>"

    When select Commands from Console
    And system reset is selected from Console
    Then system reset starts
    And Console Commands page shows "IDLE" state
    And Console Commands page shows lamp "<current_lamp_state>"
    And Console Home page shows lamp "<current_lamp_state>"
    And Control Panel shows lamp "<current_lamp_state>"

    Examples:
      | current_lamp_state | new_lamp_state |
      | OFF                | ON             |
      | ON                 | OFF            |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute lamp state with network disconnect and reconnect
    Given lamp is "<current_lamp_state>"
    When select Commands from Console
    And set lamp to "<new_lamp_state>"
    And network card for instrument is disconnected
    Then Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<Disconnect_time>" seconds since it was disconnected
    Then Console Commands page shows "IDLE" state
    And Console Commands page shows lamp "<new_lamp_state>"
    And Console Home page shows lamp "<new_lamp_state>"
    And Control Panel shows lamp "<new_lamp_state>"

    Examples:
      | current_lamp_state | new_lamp_state | Disconnect_time |
      | OFF                | ON             | 5               |
      | OFF                | ON             | 10              |
      | OFF                | ON             | 12              |
      | ON                 | OFF            | 5               |
      | ON                 | OFF            | 10              |
      | ON                 | OFF            | 12              |
      | OFF                | ON             | 60              |
      | OFF                | ON             | 80              |
      | OFF                | ON             | 100             |
      | ON                 | OFF            | 60              |
      | ON                 | OFF            | 80              |
      | ON                 | OFF            | 100             |


  @real @new @ignore
  Scenario Outline: Execute lamp state with system clock time
    Given lamp is "<current_lamp_state>"
    When select Commands from Console
    And set lamp to "<new_lamp_state>"
    And system clock time is changed with "<time_difference_in_hours>"
    Then Console Commands page shows lamp "<new_lamp_state>"
    And Console Home page shows lamp "<new_lamp_state>"
    And Control Panel shows lamp "<new_lamp_state>"

    Examples:
      | current_lamp_state | time_difference_in_hours | new_lamp_state |
      | OFF                | -1                       | ON             |
      | ON                 | -1                       | OFF            |
      | OFF                | +1                       | ON             |
      | ON                 | +1                       | OFF            |
