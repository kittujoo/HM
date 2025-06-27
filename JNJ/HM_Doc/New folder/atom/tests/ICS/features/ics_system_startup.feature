  """

Feature to validate System Startup test

  """
@ics @real_or_simulation @daily @ics_system_startup_feature @new @ignore
Feature: System Startup

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state

  Scenario Outline: System Startup
    Given Console is launched from Control Panel
    And Console page shows "IDLE" state
    And Lamp is "<current_startup_state>"
    And Flow rate is "<current_startup_state>"
    And Column Temperature is "<current_startup_state>"
    And Sample Temperature is "<current_startup_state>"

    When select Setup from Console
    And Startup section is selected
    And Startup starts with state "WORKFLOW ACTIVE"
    And Lamp is "<new_startup_state>"
    And Flow rate is "1.000"
    And Column Temperature is "<new_startup_state>"
    And Sample Temperature is "<new_startup_state>"
    Then Startup finish succesfully
    And Console page shows "IDLE" state
    And Startup section is active
    And Control Panel shows Flow rate set to "1.000"
    And Control Panel shows Lamp "<new_startup_state>"
    And Control Panel shows Column Temperature "<new_startup_state>"
    And Control Panel shows Sample Temperature "<new_startup_state>"

    Examples:
      | current_startup_state | new_startup_state |
      | OFF                   | ON                |
      | ON                    | ON                |
