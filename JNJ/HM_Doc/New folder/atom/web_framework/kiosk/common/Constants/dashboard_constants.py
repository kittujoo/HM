"""
File_Name: dashboard_constants.py
Desc: This file contains the constants used in the dashboard
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 9/10/2021
"""


class SystemStateConstants:
    StandbySystemState = "standby"
    BootingSystemState = "booting"
    SleepingSystemState = "sleeping"
    BusySystemState = "Busy"
    IdleSystemState = "IDLE"
    MaxiTimeToIdle = 900
    MaxiTimeToAbort = 120
    ErrorSystemState = "ERROR"
    StoppedValidateText = "Workflow interrupted"
    HaltingSystemState = "Halting"
    HaltedSystemState = "SYSTEM HALTED"
    ResettingSystemState = "RESETTING"
