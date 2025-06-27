  """
  File_Name: column_manager.feature
  Desc: This file contains the scenarios for testing the isym_bridge column manager apis
  __copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
  __author__    = "Sharmila Vairamani" Initial Check-in 04/07/2020
  __modified__ =  "Sharmila Vairamani"  added clear alarm and trigger error test scenarios - 06/25/2020

  """
@ColumnApi
Feature: Kiosk | Column manager functionality

  Background:
    Given Initial setup of the column manager

  Scenario Outline: The  user cannot set the temperature of the column when the temperature control is off
    When Request the control action to "<action>" for the column "<column_id>"
    And  Set the desired "<temperature>" for the column "<column_id>"
    Then Validate the column "<column_id>" info for "<action>" for change in value of "<state>" "<set_point>" "<target_temperature>"

    Examples:
      | action | temperature | column_id | state | set_point | target_temperature |
      | OFF    | 120         | CM1-Col1  | IDLE  | 120       | 45                 |
      | OFF    | 100         | CM1-Col2  | IDLE  | 100       | 45                 |
      | OFF    | 20          | CM1-Col3  | IDLE  | 20        | 45                 |


  Scenario Outline: To verify the system throws an error when user sets an out of range temperature
    When Request the control action to "<action>" for the column "<column_id>"
    Then Validate the system throws an error for setting an "<invalid_temperature>" for column "<column_id>"

    Examples:
      | action | invalid_temperature | column_id |
      | ON     | 10                  | CM1-Col1  |
      | ON     | 156                 | CM1-Col2  |
      | ON     | 158                 | CM1-Col3  |


  Scenario Outline: To verify user can set the column temperature when the temperature control is on
    When Request the control action to "<action>" for the column "<column_id>"
    And Set the desired "<temperature>" for the column "<column_id>"
    Then Validate the column "<column_id>" info for "<action>" for change in value of "<state>" "<set_point>" "<target_temperature>"

    Examples:
      | action | temperature | column_id | state     | set_point | target_temperature |
      | ON     | 40          | CM1-Col1  | AT_TARGET | 40        | 40                 |
      | ON     | 70          | CM1-Col2  | AT_TARGET | 70        | 70                 |
      | ON     | 80          | CM1-Col3  | AT_TARGET | 80        | 80                 |


  Scenario Outline: To verify the user cannot set temperature when the column is in error condition
    When Trigger an error on the column manager "<column_id>"
    Then Validate the user cannot set the "<temperature>" for the column "<column_id>"

    Examples:
      | column_id | temperature |
      | CM1-Col1  | 45          |
      | CM1-Col2  | 45          |
      | CM1-Col3  | 45          |


  Scenario Outline: To verify clear alarm change the state of the column from error to idle
    When Trigger an error on the column manager "<column_id>"
    And Request the clear alarm to clear the alarm condition for column "<column_id>"
    Then Validate the column "<column_id>" info for "<action>" for change in value of "<state>" "<set_point>" "<target_temperature>"

    Examples:
      | action | column_id | state | set_point | target_temperature |
      | OFF    | CM1-Col1  | IDLE  | 45        | 45                 |
      | OFF    | CM1-Col2  | IDLE  | 45        | 45                 |
      | OFF    | CM1-Col3  | IDLE  | 45        | 45                 |


  Scenario Outline: To verify the user cannot turn on the control when the column manager is in error condition
    When Trigger an error on the column manager "<column_id>"
    Then Validate the user cannot turn "<action>" the control for the column manager "<column_id>"

    Examples:
      | action | column_id |
      | OFF    | CM1-Col1  |
      | ON     | CM1-Col2  |
      | OFF    | CM1-Col3  |


  Scenario Outline: To verify the column resumes its initial state when the action is turned on after clearing the error
    When Trigger an error on the column manager "<column_id>"
    And Request the clear alarm to clear the alarm condition for column "<column_id>"
    And Request the control action to "<action>" for the column "<column_id>"
    Then Validate the "<column_id>" info change in "<state>" "<set_point>" "<target_temperature>"

    Examples:
      | action | column_id | state     | set_point | target_temperature |
      | ON     | CM1-Col1  | AT_TARGET | 45        | 45                 |
      | ON     | CM1-Col2  | AT_TARGET | 45        | 45                 |
      | ON     | CM1-Col3  | AT_TARGET | 45        | 45                 |



