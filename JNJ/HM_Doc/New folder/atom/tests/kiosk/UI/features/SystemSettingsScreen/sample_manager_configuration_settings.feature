@kiosk @ALIST-228 @kiosk_sample_manager_configuration_feature
Feature: Kiosk | Sample Manager configuration settings screen

  @simulation @weekly
  Scenario Outline: To verify the user is able to set and save various configuration settings
    When User navigates to volume settings screen
    And User selects the "<extension_loop_volume>"
    And User taps the compartment light preference settings tab
    And User toggles the light preference to "<when_the_door_is_open_toggle>"
    And User taps the options tab
    And User toggles leak sensor mode "<leak_sensor_enabled>"
    And User toggles multi draw mode "<multi_draw_enabled>"
    And User confirms the configuration settings for the sample manager
    Then User navigates to volume settings screen
    And Validate "<extension_loop_volume>" option has been selected in volume settings
    And User taps the compartment light preference settings tab
    And User validates the "<when_the_door_is_open_toggle>" state
    And User taps the options tab
    And Validate options settings with "<leak_sensor_enabled>" and "<multi_draw_enabled>"

    Examples:
      | extension_loop_volume | when_the_door_is_open_toggle | leak_sensor_enabled | multi_draw_enabled |
      | 50                    | True                         | False               | False              |
      | 100                   | False                        | True                | False              |


  @simulation @weekly
  Scenario: To verify extension loop volume can not be selected if Extension loop installed is disable
    When User navigates to volume settings screen
    And User disable the Extension loop installed
    Then User validates the extension loop volume is not shown


  @simulation @weekly
  Scenario: To verify when changing but cancelling the Extension loop, Compartment light and Leak Sensor toggles, they are not saving
    Given User switches all the toggles in sample manager configuration to "ON"
    When User navigates to volume settings screen
    And User switches the "Extension loop volume" to "OFF"
    And User taps the compartment light preference settings tab
    And User switches the "When the door is open" to "OFF"
    And User taps the options tab
    And User switches the "Leak Sensor" to "OFF"
    And User switches the "Multi Draw" to "OFF"
    And User cancels the change
    And User navigates to volume settings screen
    Then User validates that all the toggles are "ON"


  @simulation @weekly
  Scenario Outline: To verify multi-draw volume options and information
    When User navigates to options settings screen
    And User toggles multi draw mode "<multi_draw_enabled>"
    And User taps the volume settings tab
    Then User validates the volume options and "<multi_draw_installation_text>" depending on "<multi_draw_enabled>"

    Examples:
      | multi_draw_installation_text      | multi_draw_enabled |
      | Multi-draw valve installed        | True               |
      | Multi-draw valve is not installed | False              |


  @simulation @weekly
  Scenario Outline: To verify turning ON/OFF sm leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    When User toggles the SM leak sensor to "<expected_state>"
    And User navigates to the configuration settings screen
    Then User validates the SM configure leak sensor state is "<expected_state>"

    Examples:
      | expected_state |
      | ON             |
      | OFF            |


  @simulation @weekly
  Scenario Outline: To verify turning ON/OFF sm leak sensor from module configuration tab
    Given User navigates to the SM configuration settings screen
    When  User toggles SM configure leak sensor to "<expected_state>"
    And   User navigates to the leak sensors screen
    Then  User validates the SM leak sensor state is "<expected_state>"

    Examples:
      | expected_state |
      | ON             |
      | OFF            |


  @monthly @manual @ignore
  Scenario: To verify when the SM compartment door is open the light turns on
    When User navigates to the SM configuration screen
    And User navigates to the Compartment light configuration settings screen
    And User switches the Light when door is open to ON
    And  User open the compartment door
    Then The light turns on


  @monthly @manual @ignore
  Scenario: To verify when the SM compartment door is open the light turns off
    When User navigates to the SM configuration screen
    And User navigates to the Compartment light configuration settings screen
    And User switches the Light when door is open to OFF
    And  User open the compartment door
    Then The light turns Off


  @monthly @manual @ignore
  Scenario: To verify when  leak sensor is removed from the SM, "Leak sensor Not Present" message appears
    When User navigates to the SM module configuration screen
    And User navigates to the Options configuration settings screen
    And User switches the leak sensor to OFF
    And  User removes the leak sensor is from the SM
    Then The Leak sensor Not Present is displayed on the SM module configuration settings screen
    And User is not allow enabling of this sensor


      # Prerequisite: this test should be run ONLY if the multi-draw valve is installed
  @monthly @manual @ignore
  Scenario Outline: To verify Multi-draw valve option
    When User navigates to options settings screen
    And User toggles multi draw mode "<multi_draw_enabled>"
    And User taps the volume settings tab
    Then User validates the possible volume options are 50, 100, 250, 1000 and 2000
    And User selects 1000 for draw volume
    And User confirms the configuration settings for the sample manager
    Then User navigates to volume settings screen
    And Validate draw volume is 10000

    Examples:
      | multi_draw_enabled |
      | True               |
      | False              |