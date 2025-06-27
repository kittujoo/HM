@ics @ALIST-229 @real @daily @ics_system_shutdown_procedure_feature
Feature: System Shutdown

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And column temperature initial state is set as "On"
    And Column Temperature is "30.0"
    And sample temperature initial state is set as "On"
    And Sample Temperature is "10.0"

  Scenario Outline: States are Off after running system shutdown procedure
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is turned "<initial_state>"
    And Flow rate is turned "<initial_state>"
    And column temperature initial state is set as "<initial_state>"
    And sample temperature initial state is set as "<initial_state>"

    When User selects Setup from Console
    And Shutdown section is selected
    Then Console page shows "WORKFLOW ACTIVE" state
    And Shutdown section text is "Active"
    And Console page shows "WORKFLOW CLOSURE" state
    And Console page shows "IDLE" state
    When User selects Home from Console
    Then Console Home page shows lamp "Off"
    And Console shows Flow rate set to "1.000 mL/min"
    And Console shows Column Temperature state set to "Off"
    And Console shows Sample Temperature state set to "Off"
    And Console page shows "IDLE" state
    And Control Panel shows Flow rate set to "1.000"
    And Control Panel shows Lamp "Off"
    And Control Panel shows Column Temperature is "30.0"
    And Control Panel shows Sample Temperature is "10.0"

    Examples:
      | initial_state |
      | Off           |
      | On            |


  @new @ignore
  Scenario Outline: System Shutdown with emergency stop
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is "<current_shutdown_state>"
    And Flow rate is "<current_shutdown_state>"
    And Column Temperature is "<current_shutdown_state>"
    And Sample Temperature is "<current_shutdown_state>"

    When select Setup from Console
    And Shutdown section is selected
    Then Shutdown section is active

    When select Commands from Console
    And Emergency Stop is selected
    And Emergency Stop starts
    And select Setup from Console
    And Shutdown section is selected
    Then Shutdown section is inactive
    And a message is displayed "System Halted"

    When select Commands from Console
    And System Reset is selected
    Then System Reset starts

    When System Reset finish succesfully
    Then Shutdown finish succesfully
    And Console page shows "IDLE" state
    And Shutdown section is active
    And Control Panel shows Flow rate set to "<new_shutdown_state>"
    And Control Panel shows Lamp "<new_shutdown_state>"
    And Control Panel shows Column Temperature "<new_shutdown_state>"
    And Control Panel shows Sample Temperature "<new_shutdown_state>"

    Examples:
      | current_shutdown_state | new_shutdown_state |
      | OFF                    | OFF                |
      | ON                     | OFF                |


  @new @ignore
  Scenario Outline: System Shutdown with system clock changes foward with one hour
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is "<current_shutdown_state>"
    And Flow rate is "<current_shutdown_state>"
    And Column Temperature is "<current_shutdown_state>"
    And Sample Temperature is "<current_shutdown_state>"

    When select Setup from Console
    And Shutdown section is selected
    And Shutdown starts with state "WORKFLOW ACTIVE"
    And Lamp is "<new_shutdown_state>"
    And Flow rate is "1.000"
    And Column Temperature is "<new_shutdown_state>"
    And Sample Temperature is "<new_shutdown_state>"
    And system clock is changed foward with one hour
    Then Shutdown finish succesfully
    And Console page shows "IDLE" state
    And Shutdown section is active
    And Control Panel shows Flow rate set to "1.000"
    And Control Panel shows Lamp "<new_shutdown_state>"
    And Control Panel shows Column Temperature "<new_shutdown_state>"
    And Control Panel shows Sample Temperature "<new_shutdown_state>"

    Examples:
      | current_shutdown_state | new_shutdown_state |
      | OFF                    | OFF                |
      | ON                     | OFF                |


  @new @ignore
  Scenario Outline: System Shutdown with system clock changes backwards with one hour
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is "<current_shutdown_state>"
    And Flow rate is "<current_shutdown_state>"
    And Column Temperature is "<current_shutdown_state>"
    And Sample Temperature is "<current_shutdown_state>"

    When select Setup from Console
    And Shutdown section is selected
    And Shutdown starts with state "WORKFLOW ACTIVE"
    And Lamp is "<new_shutdown_state>"
    And Flow rate is "1.000"
    And Column Temperature is "<new_shutdown_state>"
    And Sample Temperature is "<new_shutdown_state>"
    And system clock is changed backwards with one hour
    Then Shutdown finish succesfully
    And Console page shows "IDLE" state
    And Shutdown section is active
    And Control Panel shows Flow rate set to "1.000"
    And Control Panel shows Lamp "<new_shutdown_state>"
    And Control Panel shows Column Temperature "<new_shutdown_state>"
    And Control Panel shows Sample Temperature "<new_shutdown_state>"

    Examples:
      | current_shutdown_state | new_shutdown_state |
      | OFF                    | OFF                |
      | ON                     | OFF                |


  @new @ignore
  Scenario Outline: System Shutdown with disconect and reconnect
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is "<current_shutdown_state>"
    And Flow rate is "<current_shutdown_state>"
    And Column Temperature is "<current_shutdown_state>"
    And Sample Temperature is "<current_shutdown_state>"

    When select Setup from Console
    And Shutdown section is selected
    And Shutdown starts with state "WORKFLOW ACTIVE"
    And Lamp is "<new_shutdown_state>"
    And Flow rate is "1.000"
    And Column Temperature is "<new_shutdown_state>"
    And Sample Temperature is "<new_shutdown_state>"
    And network card for instrument is disconnected
    Then Shutdown stops
    And Control Panel shows "Alliance iS Unable to Connect" state

    When network card for instrument is reconnected
    And select Setup from Console
    And Shutdown section is selected
    Then Shutdown section is inactive

    When select Commands from Console
    And System Reset is selected
    Then System Reset starts

    When System Reset finish succesfully
    Then Shutdown finish succesfully
    And Console page shows "IDLE" state
    And Shutdown section is active
    And Control Panel shows Flow rate set to "<new_shutdown_state>"
    And Control Panel shows Lamp "<new_shutdown_state>"
    And Control Panel shows Column Temperature "<new_shutdown_state>"
    And Control Panel shows Sample Temperature "<new_shutdown_state>"

    Examples:
      | current_shutdown_state | new_shutdown_state |
      | OFF                    | OFF                |
      | ON                     | OFF                |
