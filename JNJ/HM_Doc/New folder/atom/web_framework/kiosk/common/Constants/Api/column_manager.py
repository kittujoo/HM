"""
File_Name: column_manager_constants.py
Desc: This file contains the constants of column manager
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 04/07/2020

"""


class ColumnManagerErrorCodes:
    OutOfRange = 3013  # Setpoint out of range
    CommandRejectedInAlarm = 3010  # Command failed because device in alarm state


class ColumnManagerErrorMessages:
    OutOfRangeMessage = "SetPoint must be between [20 and 150]"
    CommandRejectedInAlarmMessage = "command rejected because device is in error state.  Clear error before re-trying."


class ColumnManagerStates:
    Idle = 'IDLE'  # Column is idle
    Heating = 'HEATING'  # Column is heating
    Cooling = 'COOLING'  # Column is cooling
    AtTarget = 'AT_TARGET'  # Column is at target temperature
    Error = 'ERROR'  # An error has occurred


class ColumnManagerConstants:
    MaxTimeToReachMaxTemperature = 30  # maximum taken by the column to reach the maximum temperature
    temperature = 45
