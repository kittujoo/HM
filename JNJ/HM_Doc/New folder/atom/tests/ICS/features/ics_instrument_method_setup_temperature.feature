@ics @ALIST-229 @real_or_simulation @daily @ics_method_setup_temperature_feature
Feature: ICS instrument method setup temperature state

  Background:
    Given the "ics_atom_project" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And the instrument method editor window is opened

  Scenario Outline: Change temperature state
    Given instrument method has column temperature parameter "<column_value>"
    And instrument method has sample temperature parameter "<sample_value>"
    And instrument method is saved with name "<instrument_method>"
    And sample temperature initial state is set as "<current_sample_temp_state>"
    And column temperature initial state is set as "<current_column_temp_state>"
    And entry from drop down instrument method is selected "<instrument_method>"

    When Setup run section is selected
    Then Setup run goes to "Monitoring - Setting Up" state
    And Setup run goes to "System Idle" state
    When Console is launched from Control Panel
    Then Console sample temperature shows "<sample_value>"
    And Console column temperature shows "<column_value>"

    Examples:
      | current_sample_temp_state | current_column_temp_state | column_value | sample_value | instrument_method       |
      | OFF                       | OFF                       | OFF          | 5            | column off              |
      | OFF                       | OFF                       | 20           | OFF          | sample off              |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  |
      | ON                        | ON                        | 30           | 10           | temperature values two  |
      | ON                        | ON                        | 40           | 15           | temperature value three |

      # Steps to be automated after line 23: And Control Panel shows "IDLE" state
      # And Control Panel column temperature shows "<column_value>"
      # And Control Panel sample temperature shows "<sample_value>"


  @real_or_simulation @new @ignore
  Scenario Outline: Execute Change temperature state with Emergency stop option
    Given instrument method has column temperature parameter "<column_value>"
    And instrument method has sample temperature parameter "<sample_value>"
    And instrument method is saved with name "<instrument_method>"
    And sample temperature initial state is set as "<current_sample_temp_state>"
    And column temperature initial state is set as "<current_column_temp_state>"
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And entry from dropdown instrument method is selected "<instrument_method>"

    When Setup run section is selected
    Then Setup starts with state "Monitoring-Setting up"
    And column temperature is "<column_value>"
    And sample temperature is "<sample_value>"

    When select Commands from Console
    And Emergency Stop from Console is selected
    Then Emergency Stop starts
    And Console Commands page shows "SYSTEM HALTED"
    And Control Panel shows "SYSTEM HALTED"

    When select Commands from Console
    And system reset is selected from Console
    Then system reset starts
    And Console Commands page shows "IDLE" state
    And Console sample temperature shows "<sample_value>"
    And Console column temperature shows "<column_value>"
    And Control Panel shows "IDLE" state
    And Control Panel column temperature shows "<column_value>"
    And Control Panel sample temperature shows "<sample_value>"


    Examples:
      | current_sample_temp_state | current_column_temp_state | column_value | sample_value | instrument_method       |
      | OFF                       | OFF                       | OFF          | 5            | column off              |
      | OFF                       | OFF                       | 20           | OFF          | sample off              |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  |
      | ON                        | ON                        | 30           | 10           | temperature values two  |
      | ON                        | ON                        | 40           | 15           | temperature value three |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute Change temperature state with network disconnect and reconnect
    Given instrument method has column temperature parameter "<column_value>"
    And instrument method has sample temperature parameter "<sample_value>"
    And instrument method is saved with name "<instrument_method>"
    And sample temperature initial state is set as "<current_sample_temp_state>"
    And column temperature initial state is set as "<current_column_temp_state>"
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And entry from dropdown instrument method is selected "<instrument_method>"

    When Setup run section is selected
    Then Setup starts with state "Monitoring-Setting up"
    And column temperature is "<column_value>"
    And sample temperature is "<sample_value>"

    When network card for instrument is disconnected
    Then Control Panel shows "Alliance iS Unable to Connect" state

    When network card is reconnected after at least "<disconnect_time>" seconds since it was disconnected
    Then Control Panel shows "IDLE" state
    And Control Panel column temperature shows "<column_value>"
    And Control Panel sample temperature shows "<sample_value>"
    And Console Commands page shows "IDLE" state
    And Console sample temperature shows "<sample_value>"
    And Console column temperature shows "<column_value>"

    Examples:
      | current_sample_temp_state | current_column_temp_state | column_value | sample_value | instrument_method       | disconnect_time |
      | OFF                       | OFF                       | OFF          | 5            | column off              | 10              |
      | OFF                       | OFF                       | 20           | OFF          | sample off              | 10              |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  | 10              |
      | ON                        | ON                        | 30           | 10           | temperature values two  | 10              |
      | ON                        | ON                        | 40           | 15           | temperature value three | 10              |
      | OFF                       | OFF                       | OFF          | 5            | column off              | 60              |
      | OFF                       | OFF                       | 20           | OFF          | sample off              | 60              |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  | 60              |
      | ON                        | ON                        | 30           | 10           | temperature values two  | 60              |
      | ON                        | ON                        | 40           | 15           | temperature value three | 60              |


  @real_or_simulation @new @ignore
  Scenario Outline: Execute Change temperature state with system clock time change
    Given instrument method has column temperature parameter "<column_value>"
    And instrument method has sample temperature parameter "<sample_value>"
    And instrument method is saved with name "<instrument_method>"
    And sample temperature initial state is set as "<current_sample_temp_state>"
    And column temperature initial state is set as "<current_column_temp_state>"
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state
    And entry from dropdown instrument method is selected "<instrument_method>"

    When Setup run section is selected
    Then Setup starts with state "Monitoring-Setting up"
    And column temperature is "<column_value>"
    And sample temperature is "<sample_value>"

    When system clock time is changed with "<time_difference_in_hours>"
    Then the sample set completes with state "System Idle"
    And Control Panel shows "IDLE" state
    And Control Panel column temperature shows "<column_value>"
    And Control Panel sample temperature shows "<sample_value>"
    And Console Commands page shows "IDLE" state
    And Console sample temperature shows "<sample_value>"
    And Console column temperature shows "<column_value>"

    Examples:
      | current_sample_temp_state | current_column_temp_state | column_value | sample_value | instrument_method       | time_difference_in_hours |
      | OFF                       | OFF                       | OFF          | 5            | column off              | -1                       |
      | OFF                       | OFF                       | OFF          | 5            | column off              | +1                       |
      | OFF                       | OFF                       | 20           | OFF          | sample off              | -1                       |
      | OFF                       | OFF                       | 20           | OFF          | sample off              | +1                       |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  | -1                       |
      | OFF                       | OFF                       | 20           | 5            | temperature values one  | +1                       |
      | ON                        | ON                        | 30           | 10           | temperature values two  | -1                       |
      | ON                        | ON                        | 30           | 10           | temperature values two  | +1                       |
      | ON                        | ON                        | 40           | 15           | temperature value three | -1                       |
      | ON                        | ON                        | 40           | 15           | temperature value three | +1                       |
