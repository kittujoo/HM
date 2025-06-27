  """
  File_Name: prime_solvent.feature
  Desc: This file contains the scenarios for testing the isym_bridge prime solvent apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 08/19/2020

  """
@prime_solvent
Feature: Kiosk | prime solvent functionality

  Background:
    Given Initial setup for the prime solvent

  Scenario Outline: To verify user is able to prime solvents sequentially in order specified
    When Request start prime by time method "<prime_by_time_lines>" for "<prime_duration>" with "<end_prime_solvent_composition>" for "<prime_end_duration>"
    Then Validate prime by time info "<prime_by_time_lines>" for "<prime_duration>" with "<end_prime_solvent_composition>" for "<prime_end_duration>"

    Examples:

      | prime_by_time_lines | prime_duration | end_prime_solvent_composition | prime_end_duration |
      | A,C                 | 6              | C=50,D=50                     | 6                  |
      | A,B,C,D             | 6              | A=50,B=50                     | 6                  |
      | C,D,A,B             | 6              | A=50,B=50                     | 6                  |
      | D                   | 6              | A=50,B=50                     | 6                  |


  Scenario Outline: To verify user is able to prime solvents in parallel by composition
    When Request start prime by composition "<solvent_compositions_string>" for "<prime_duration>" with end prime condition "<end_prime_solvent_composition>" for "<prime_end_duration>"
    Then Validate prime info "<solvent_compositions_string>" for "<prime_duration>" with "<end_prime_solvent_composition>" for "<prime_end_duration>"

    Examples:

      | solvent_compositions_string | prime_duration | end_prime_solvent_composition | prime_end_duration |
      | A=25,B=25,C=25,D=25         | 6              | A=50,B=50                     | 6                  |
      | A=10,B=10,C=10,D=70         | 6              | A=25,B=25,C=25,D=25           | 6                  |
      | C=50,D=50                   | 6              | A=25,B=25,C=25,D=25           | 6                  |


  Scenario Outline: To verify user is not able to prime solvents when invalid solvent id is given as a input
    When Validate the api throws an error when invalid solvent "<prime_by_time_lines>" is used for priming
    Then Clear the error condition in prime solvent

    Examples:

      | prime_by_time_lines |
      | A,A,C,D             |
      | E,A,D,B             |
      | A,B,D,D             |


  Scenario Outline: To verify user is not able to prime solvents when solvent composition is given more than 100 percentage
    When Validate the api throws an error when an invalid solvent composition "<solvent_compositions_string>" is applied
    Then Clear the error condition in prime solvent

    Examples:

      | solvent_compositions_string |
      | A=125,B=25,C=25,D=25        |


  Scenario: To verify user is not able to prime the solvent when more than hundred percent solvent composition is given in prime end condition
    When Validate the api throws an error when more then 100 percent solvent composition is applied in prime end condition
    Then Clear the error condition in prime solvent


  Scenario Outline: To verify system throws error when the user primes at flow rate lower than that set in the configuration
    When  Validate system throws error when the user primes at "<flow_rate>" lower than that set in the configuration
    Then Clear the error condition in prime solvent

    Examples:
      | flow_rate |
      | 0.1       |
      | 5.2       |


  Scenario Outline: To verify user able to prime solvents sequentially in ordered specified and also parallel by composition
    When Request start "<prime_by_time_lines>" and "<solvent_compositions_string>" for "<prime_duration>" with end prime condition "<end_prime_solvent_composition>" for "<prime_end_duration>"
    Then Validate info response for "<prime_by_time_lines>" for "<prime_duration>" and "<solvent_compositions_string>" "<prime_by_composition_duration>" for "<prime_duration>" with end prime condition "<end_prime_solvent_composition>" for "<prime_end_duration>"

    Examples:
      | prime_by_time_lines | prime_duration | solvent_compositions_string | prime_by_composition_duration | end_prime_solvent_composition | prime_end_duration |
      | A,C                 | 6              | A=25,B=25,C=25,D=25         | 6                             | C=50,D=50                     | 6                  |
      | A,B,C,D             | 6              | A=10,B=10,C=10,D=70         | 6                             | A=50,B=50                     | 6                  |



