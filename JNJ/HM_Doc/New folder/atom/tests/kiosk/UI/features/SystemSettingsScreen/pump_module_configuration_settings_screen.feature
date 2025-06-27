@kiosk @ALIST-228 @pump_module_configuration_feature
Feature: Kiosk | Pump module configuration settings screen


  @real @weekly
  Scenario: To verify that changing the config toggles are saving
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User switches the pump leak sensor setting to ON
    And User switches the light when door is opened setting to ON
    And User confirms the change
    And User navigates to the pump module configuration settings screen
    Then User validates the changed pump module configuration settings are ON


  @simulation @weekly
  Scenario: To verify when changing but cancelling the config toggles, they are not saving
    Given User navigates to the pump module configuration screen
    And User navigates to the pump module configuration settings screen
    And The state of the pump configuration settings are opposite
    When User navigates to the pump module configuration settings screen
    And User switches the pump leak sensor setting to ON
    And User switches the light when door is opened setting to ON
    And User cancels the change
    And User navigates to the pump module configuration settings screen
    Then User validates the changed pump module configuration settings are OFF


  @real @weekly
  Scenario Outline: To verify turning ON/OFF pump leak sensor from leak sensor configuration screen
    Given User navigates to the leak sensor configuration screen
    And Pump leak sensor was "<initial_state>"
    When User switches the pump leak sensor "<expected_state>"
    And User navigates to the configuration settings screen
    Then User validates the leak sensor configuration state is "<expected_state>"

    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |


  @simulation @weekly
  Scenario Outline: To verify turning ON/OFF pump leak sensor from configuration setting screen
    Given User navigates to the configuration settings screen
    And Pump leak configuration was "<initial_state>"
    When User switches the pump leak configuration sensor "<expected_state>"
    And User navigates to the leak sensor configuration screen
    Then User validates the leak sensor state is "<expected_state>"

    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |


  @real @weekly
  Scenario Outline: To verify the mixer configuration values are being displayed properly
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User selects the "<mixer_option>"
    Then User validates the "<mixer_value>" is properly displayed in the label
    And User confirms the mixer change

    Examples:
      | mixer_option | mixer_value |
      | 100MM        | 675         |
      | 50MM         | 375         |
      | 30MM         | 200         |


  @simulation @weekly
  Scenario Outline: To verify a valid custom value can be entered and saved the mixer configuration paths
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User selects the "<mixer_option>"
    And User enters the "<mixer_value>"
    And User confirms the change
    And User navigates to the pump module configuration settings screen
    Then User validates the custom "<mixer_value>" was properly saved

    Examples:
      | mixer_option | mixer_value |
      | Custom       | 500         |
      | Custom       | 925         |


  @simulation @weekly
  Scenario Outline: To verify the custom value range for mixer configuration paths
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User selects the "<mixer_option>"
    And User enters the "<mixer_value>"
    Then User validates the "<done_button_status>" status

    Examples:
      | mixer_option | mixer_value | done_button_status |
      | Custom       | 5           | Disabled           |
      | Custom       | 50          | Enabled            |
      | Custom       | 300         | Enabled            |
      | Custom       | 1000        | Enabled            |
      | Custom       | 1010        | Disabled           |


  @simulation @weekly
  Scenario: To verify chosen mixer from the list could not be selected for None option
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User selects the None mixer option
    Then User validates the mixer volume is not shown


  @monthly @manual @ignore
  Scenario: To verify when leak sensor is removed from the pump, "Leak sensor Not Present" message appears.
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User switches the Leak sensor to OFF
    And User removes the leak sensor is from the pump
    Then The Leak sensor Not Present is displayed on the pump module configuration settings screen


  @monthly @manual @ignore
  Scenario: To verify when the pump compartment door is open the light turns on
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User switches the Light when door is open to ON
    And User opens the compartment door
    Then The light turns on


  @monthly @manual @ignore
  Scenario: To verify when the pump compartment door is open the light turns off
    Given User navigates to the pump module configuration screen
    When User navigates to the pump module configuration settings screen
    And User switches the Light when door is open to OFF
    And User opens the compartment door
    Then The light does not turn on
