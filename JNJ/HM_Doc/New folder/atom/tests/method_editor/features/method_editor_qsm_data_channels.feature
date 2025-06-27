@method_editor @ALIST-230 @simulation @daily @tuv_bio @pda @pda_bio @method_editor_qsm_data_channels_feature @new @ignore
Feature: Method Editor | QSM Data Channels
    Data and diagnostic channels can be enabled to record additional information during an acquisition.

  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is opened
    And the Data Channels: Pump menu is opened

  Scenario: Titles and descriptions are displayed
    Then the Data Channels: Pump menu title is "Data Channels: Pump"
    And the System Pressure setting has title "System Pressure" and description "Overall solvent pressure (psi)"
    And the Flow Rate setting has title "Flow Rate" and description "System flow rate (mL/min)"
    And the % A setting has title "% A" and description "Percent composition of solvent A"
    And the % B setting has title "% B" and description "Percent composition of solvent B"
    And the % C setting has title "% C" and description "Percent composition of solvent C"
    And the % D setting has title "% D" and description "Percent composition of solvent D"
    And the Primary setting has title "Primary" and description "Primary (left head) pressure (psi)"
    And the Accumulator setting has title "Accumulator" and description "Accumulator (right head) pressure (psi)"
    And the Degasser setting has title "Degasser" and description "Degasser pressure (psi)"

  Scenario: Data Channels: Pump can be set as Favorite
    When the Data Channels: Pump setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Data Channels: Pump" menu title is available

      ### Need to clarify which search texts are expected to give results ###
      ### Additionally, some search texts may give multiple results as they are found in multiple menus ###
  Scenario Outline: Setting can be searced for
    When the System menu is opened
    And "<Search_Text>" is entered into the search bar
    Then the Data Channels: Pump setting group is displayed
    And the "Pump" menu is highlighted

    Examples:
      | Search_Text        |
      | Data Channels Pump |
      | Primary            |
      | Accumulator        |
      | Degasser           |

  Scenario: Default settings are correct
    Then the "Pump" menu is highlighted
    And the "Data Channels: Pump" menu is highlighted
    And the selectors are in the following states:
      | Setting         | State |
      | System Pressure | Off   |
      | Flow Rate       | Off   |
      | %A              | Off   |
      | %B              | Off   |
      | %C              | Off   |
      | %D              | Off   |
      | Primary         | Off   |
      | Accumulator     | Off   |
      | Degasser        | Off   |

  Scenario: Settings are saved and restored
    Given the System Pressure selector is turned "On"
    And the Flow Rate selector is turned "On"
    And the % A selector is turned "On"
    And the % B selector is turned "On"
    And the % C selector is turned "On"
    And the % D selector is turned "On"
    And the Primary selector is turned "On"
    And the Accumulator selector is turned "On"
    And the Degasser selector is turned "On"
    When the method is saved
    And the method is closed and reopened
    Then the System Pressure selector is turned "On"
    And the Flow Rate selector is turned "On"
    And the % A selector is turned "On"
    And the % B selector is turned "On"
    And the % C selector is turned "On"
    And the % D selector is turned "On"
    And the Primary selector is turned "On"
    And the Accumulator selector is turned "On"
    And the Degasser selector is turned "On"