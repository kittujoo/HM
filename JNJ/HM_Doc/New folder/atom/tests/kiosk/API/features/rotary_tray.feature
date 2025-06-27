  """
  File_Name: rotary_tray.feature
  Desc: This file contains the scenarios for testing the isym_bridge rotary_tray apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 02/10/2020

  """
@rotary
Feature: Kiosk | Rotary Tray functionality

  Background:
    Given Initial setup of the rotary tray


  Scenario Outline: To verify the tray is in extend position
    When Request rotary tray to extend
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"

    Examples:
      | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | EXTENDED       | 0                     | 0              | 0                   |


  Scenario Outline: To verify when the tray is in retract position
    When Request rotary tray to extend
    Then Request the rotary tray to retract
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"

    Examples:
      | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | LOADED         | 0                     | 0              | 0                   |


  Scenario: To verify the system should throw an error when the user tries to move the plate in extended position
    When Request rotary tray to extend
    Then Validate that the api should throw an error when the rotary tray move
    And  Request the rotary tray to retract


  Scenario Outline: To verify the system throws an error when the user tries to extend an extended plate
    When Request rotary tray to extend
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"
    And validate the system throws an error when we extent the extended rotary tray

    Examples:
      | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | EXTENDED       | 0                     | 0              | 0                   |


  Scenario: To verify the system throw an error when the user tries to retract the loaded plate
    When Request rotary tray to extend
    And Request the rotary tray to retract
    Then validate the system throws an error when we retract the rotary tray


  Scenario Outline: To verify rotary tray is homed
    When Request rotary tray configuration
    And  Request rotary tray to home
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"

    Examples:
      | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | LOADED         | 0                     | 0              | 0                   |


  Scenario Outline: To verify that the tray moves to the correct position
    When Request rotary tray to move plate "<move_mode>"
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"

    Examples:
      | move_mode      | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | NEXT_PLATE     | LOADED         | 1                     | 120            | 0                   |
      | PREVIOUS_PLATE | LOADED         | 2                     | 240            | 0                   |


  Scenario Outline: To verify that the tray moves to the correct position
    When Request rotary tray to move plate "<plate_position>"
    Then Validate rotary tray state: "<expected_state>" active_plate: "<expected_active_plate>" angle: "<expected_angle>" error_code: "<expected_error_code>"

    Examples:
      | plate_position | expected_state | expected_active_plate | expected_angle | expected_error_code |
      | 2              | LOADED         | 2                     | 240            | 0                   |
      | 0              | LOADED         | 0                     | 0              | 0                   |
      | 1              | LOADED         | 1                     | 120            | 0                   |
