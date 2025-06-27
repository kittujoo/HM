"""
FileName: leak_sensors.feature
Desc: This file contains the scenarios for testing the leak sensors system settings screen
"""

@kiosk @ALIST-228
Feature: Kiosk | System leak sensor configuration screen

  @simulation
  Scenario Outline: To verify turning ON/OFF leak sensors from sensor tab and being saved
    Given User navigates to the leak sensors configuration screen
    And Leak sensors was set to "<initial_state>" state
    When User switches the leak sensor to "<expected_state>" state
    Then User validates the leak sensor state is "<expected_state>"

    Examples:
      | initial_state | expected_state |
      | ON            | OFF            |
      | OFF           | ON             |
