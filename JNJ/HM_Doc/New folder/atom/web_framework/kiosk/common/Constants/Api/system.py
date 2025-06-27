"""
File_Name: system_constants.py
Desc: This file contains the constants of system
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/14/2020
__modified__ = "Sharmila Vairamani" Added system error codes  - 09/17/2020

"""


class SystemStates:
    uninitialized = "UNINITIALIZED"  # System is uninitialized
    initializing = "INITIALIZING"  # System is initializing
    ready = 'READY'  # System is ready
    busy = 'BUSY'  # System is actively running a command
    asleep = 'ASLEEP'  # System is asleep
    shutting_down = 'SHUTTINGDOWN'  # System is shutting down
    error = 'ERROR'  # System in error condition


class SystemStatesTransitionTime:
    max_initializing_time = 10000  # maximum time in ms required by the system to reach ready state
    max_asleep_time = 5000  # maximum time in ms required by the system to reach asleep state
    max_waking_up_time = 5000  # maximum time in ms required by the system to reach wake state from sleep state
    max_shutting_down_time = 5000  # maximum time in ms required by the system to reach uninitialized state
    max_resetting_time = 5000  # maximum time in ms required to reset the system


class SystemErrorCodes:
    error = 9100
    no_error = 0
