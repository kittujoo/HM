  """
  File_Name: seal_wash_pump.feature
  Desc: This file contains the scenarios for testing the isym_bridge seal wash apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 07/09/2020

  """

  # This feature is not test complete as there are some contradictory on the requirements. These requirements needed to be
  #  reviewed by the HW/FW folks. The FTN PRD detail is not sufficient to determine full Orion behavior
  #  Therefore there is a hold off on further dev on Service and Test for this feature, at this point

@seal
Feature: Kiosk | Seal wash pump functionality

  Background:
    Given Initial setup of the seal wash pump

  Scenario Outline: Verify the user able to complete the priming process for the given amount of time
    When Request the seal wash pump to start priming for the given "<duration>"
    Then Validate seal wash pump info with "<expected_state>","<expected_remaining_time_ms>","<expected_error_code>" for the "<duration>"

    Examples:
      | duration | expected_state | expected_remaining_time_ms | expected_error_code |
      | 25       | IDLE           | 0                          | 0                   |
      | 35       | IDLE           | 0                          | 0                   |

  Scenario: Verify the user not able start a prime process when the system is in error condition
    When Trigger an error on the seal wash pump
    And Validate the system in error condition
    And Request the seal wash pump to start priming
    Then Validate system does not start the priming process and throws an error

  Scenario: Verify the user able to stop an ongoing priming process
    When Request the seal wash pump to start priming
    And Request the seal wash pump to stop the priming process
    Then Validate seal wash pump info with "<expected_state>","<expected_remaining_time_ms>","<expected_error_code>"

  Scenario: Verify the user not able start a prime process for an out of range duration
    When Request the seal wash pump to start priming
    Then Validate the system throws an error for the out of range prime duration

