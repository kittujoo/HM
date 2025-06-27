  """
  File_Name: system.feature
  Desc: This file contains the scenarios for testing the isym_bridge system apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 09/14/2020

  """

@system_methods_feature @api
Feature: Kiosk | system methods functionality

  Background:
    Given Initial setup of the system


  Scenario: To verify the system able to start using the start up method

    When Request system to shutdown
    And Validate system transition state from SHUTTINGDOWN to UNINITIALIZED for the duration 5000
    Then Request system to start
    And Validate system transition state from INITIALIZING to READY for the duration 10000


  Scenario: To verify the system is able to go into sleep mode using the sleep method
    When Request system to sleep
    Then Validate system transition state from BUSY to ASLEEP for the duration 5000

  Scenario: To verify the system able to wake up using the wake up method
    When Request system to sleep
    Then Validate system transition state from BUSY to ASLEEP for the duration 5000
    And Request system to wake up
    And Validate system transition state from BUSY to READY for the duration 5000


  Scenario: To verify the system is able to reset when the state of the system is ready
    When Request system to reset
    Then Validate system transition state from BUSY to READY for the duration 5000


  Scenario: To verify the system is able to reset when the state of the system is asleep
    When Request system to sleep
    And Validate system transition state from BUSY to ASLEEP for the duration 5000
    And Request system to reset
    Then Validate system transition state from BUSY to READY for the duration 5000


  Scenario: To verify the system is not able to reset when the state of the system is in uninitialised state
    When Request system to shutdown
    Then Validate system throws an error when system is made to reset with request system_reset_url


  Scenario: To verify the system is not able to sleep when the state of the system is in uninitialised state
    When Request system to shutdown
    Then Validate system throws an error when system is made to sleep with request system_sleep_url


  Scenario: To verify the system is not able to wake when the state of the system is in uninitialised state
    When Request system to shutdown
    Then Validate system throws an error when system is made to wakeup with request system_wake_up_url


  Scenario: To verify the system is not able to wake up when the state of the system is in ready state
    When Request system to shutdown
    And Validate system transition state from SHUTTINGDOWN to UNINITIALIZED for the duration 5000
    And Request system to start
    Then Validate system throws an error when system is made to wakeup with request system_wake_up_url


  Scenario: To verify the system in ready state throws an error when system wake up method is request
    When Request system to shutdown
    And Validate system transition state from SHUTTINGDOWN to UNINITIALIZED for the duration 5000
    And Request system to start
    And Validate system transition state from INITIALIZING to READY for the duration 10000
    Then Validate system throws an error when system is made to wakeup with request system_wake_up_url


  Scenario: To verify the system in asleep state throws an error when sleep method is request
    When Request system to sleep
    And Validate system transition state from BUSY to ASLEEP for the duration 5000
    Then Validate system throws an error when system is made to sleep with request system_sleep_url
