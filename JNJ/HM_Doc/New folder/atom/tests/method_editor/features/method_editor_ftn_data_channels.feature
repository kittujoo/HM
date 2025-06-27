@method_editor @ALIST-230 @simulation @daily @tuv_bio @pda @pda_bio @method_editor_ftn_data_channels_feature
Feature: Method Editor | FTN Data Channels
  Data and diagnostic channels can be enabled to record additional information during an acquisition.

  Background:
    Given an acquisition method that contains default settings is open
    And the Sample Manager menu is opened
    And the Data Channels: Sample Manager menu is opened

  Scenario: Titles and descriptions are displayed
    Then the Data Channels: Sample Manager menu title is "Data Channels: Sample Manager"
    And the Sample Temperature setting has title "Sample Temperature" and description "Compartment temperature (°C)"
    And the Sample Pressure setting has title "Sample Pressure" and description "Sample pressure (psi)"

  Scenario: Data Channels: Sample Manager can be set as Favorite
    When the Data Channels: Sample Manager setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the "Data Channels: Sample Manager" menu title is displayed

  @quarantine @defect:INSSYS-26
  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search_Text>" is entered into the search bar
    Then the Data Channels: Sample Manager setting group is displayed
    And the "Sample Manager" menu is highlighted

    Examples:
      | Search_Text                   |
      | Data Channels: Sample Manager |
      | Compartment temperature       |
      | Sample pressure               |

  Scenario: Default settings are correct
    Then the "Sample Manager" menu is highlighted
    And the "Data Channels: Sample Manager" menu is highlighted
    And the Sample Temperature selector is set to "Off"
    And the Sample Pressure selector is set to "Off"

  Scenario: Settings are saved and restored
    Given the Sample Temperature selector is turned "On"
    And the Sample Pressure selector is turned "On"
    When the method is saved
    And the method is closed and reopened
    And the Sample Manager menu is opened
    And the Data Channels: Sample Manager menu is opened
    Then the Sample Temperature selector is set to "On"
    And the Sample Pressure selector is set to "On"
