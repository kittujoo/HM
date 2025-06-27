@kiosk @ALIST-228
Feature: Kiosk | TUV configuration settings screen

  @real @daily @quarantine @defect:INSSYS-141
  Scenario Outline: To validate the screens and features within the TUV system settings
    When User navigates to the TUV system settings
    Then User validates the lamp information is present
    And User validates the flow cell information is present
    And User sets the close shutter preference as "<desired_close_shutter_preference>"
    And User toggles leak sensor mode "<leak_sensor_enabled>" to monitor the leak sensor in the system
    And User confirms the selection
    And User navigates to the TUV system settings
    And User validates the "<expected_close_shutter_preference>" preference option was saved
    And User validates the "<expected_leak_sensor_options>" leak sensor option was saved

    Examples:
      | desired_close_shutter_preference | leak_sensor_enabled | expected_close_shutter_preference | expected_leak_sensor_options |
      | True                             | True                | True                              | True                         |
      | False                            | False               | False                             | False                        |
      | True                             | False               | True                              | False                        |
      | False                            | True                | False                             | True                         |


  @real @daily
  Scenario Outline: To verify the TUV configuration settings option is not changed when the user taps the cancel button
    Given The settings are opposite of the desired "<desired_close_shutter_preference>" and "<leak_sensor_enabled>" options
    When User navigates to the TUV system settings
    And User sets the close shutter preference as "<desired_close_shutter_preference>"
    And User toggles leak sensor mode "<leak_sensor_enabled>" to monitor the leak sensor in the system
    And User cancels the selection
    Then User navigates to the TUV system settings
    And User validates the "<expected_close_shutter_preference>" preference option was saved
    And User validates the "<expected_leak_sensor_options>" leak sensor option was saved

    Examples:
      | desired_close_shutter_preference | leak_sensor_enabled | expected_close_shutter_preference | expected_leak_sensor_options |
      | True                             | True                | False                             | False                        |
      | False                            | False               | True                              | True                         |


  @real @daily
  Scenario Outline: To verify turning ON/OFF TUV leak sensor from sensor tab
    Given User navigates to the leak sensor configuration screen
    And TUV leak sensor was "<initial_state>"
    When User switches the TUV leak sensor "<expected_state>"
    And User navigates to the configuration settings screen
    Then User validates the leak sensor configuration state is "<expected_state>"
    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |


  @real @daily
  Scenario Outline: To verify turning ON/OFF TUV leak sensor from Module Configuration Tab
    Given User navigates to the TUV module configuration screen
    And TUV leak configuration was "<initial_state>"
    When User switches the TUV leak configuration sensor "<expected_state>"
    And User navigates to the leak sensor screen
    Then User validates the TUV leak sensor state is "<expected_state>"
    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |
