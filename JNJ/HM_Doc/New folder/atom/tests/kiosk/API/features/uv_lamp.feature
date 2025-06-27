  """
  File_Name: uv_lamp.feature
  Desc: This file contains the scenarios for testing the isym_bridge uv lamp apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 03/10/2020
  __author__ = "Sharmila Vairamani" Added scenarios to test new attributes of the lamp api - 05/12/2020


  """
@api
Feature: Kiosk | UV lamp functionality

  Background:
    Given Initial setup of the uv lamp

  Scenario Outline: To verify uv lamp is turned on
    When Request uv lamp power on
    Then Validate uv lamp new state: "<expected_new_state>" old state: "<expected_old_state>"  last_error_code: "<expected_last_error_code>"

    Examples:
      | expected_new_state | expected_old_state | expected_last_error_code |
      | READY              | WARMING            | 0                        |


  Scenario Outline: To verify uv lamp turned off
    When Request uv lamp power off
    Then Validate uv lamp new state: "<expected_new_state>" old state: "<expected_old_state>"  last_error_code: "<expected_last_error_code>"

    Examples:
      | expected_new_state | expected_old_state | expected_last_error_code |
      | OFF                | READY              | 0                        |


  Scenario Outline: To verify the clear alarm is not changing the lamp state from warming to off when there is no error
    When Request uv lamp power on
    And Request uv lamp clear alarm
    Then Validate uv lamp new state: "<expected_new_state>" old state: "<expected_old_state>"  last_error_code: "<expected_last_error_code>"

    Examples:
      | expected_new_state | expected_old_state | expected_last_error_code |
      | READY              | WARMING            | 0                        |


  Scenario Outline: To verify the clear alarm is clearing the error condition only
    When Trigger an error on the uv lamp
    And Request uv lamp clear alarm
    Then Validate uv lamp new state: "<expected_new_state>" old state: "<expected_old_state>"  last_error_code: "<expected_last_error_code>"

    Examples:
      | expected_new_state | expected_old_state | expected_last_error_code |
      | OFF                | ERROR              | 0                        |


  Scenario: To verify the last lamp on time is updated when the lamp state is power on
    When Request uv lamp power on
    Then Validate the last lamp on time is updated the moment the lamp is turned on


  Scenario: To verify the total lamp on time is updated when the lamp state is power off
    When Request uv lamp power on
    Then Validate the total lamp on time is updated the moment the lamp is turned off
