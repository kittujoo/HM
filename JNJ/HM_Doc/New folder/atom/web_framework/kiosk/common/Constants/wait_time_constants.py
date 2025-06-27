"""
File_Name: wait_time_constants.py
Desc: This file contains the constants used for wait times throughout the application
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/26/22
"""


class WaitTimeConstants:
    SmallWait = 120  # 1min
    MidWait = 300  # 5min
    LongWait = 600  # 10min

    NoiseDriftTestWait = 1200  # 20min
    NeedleSealReadinessTest = 900
    SampleTemperatureTest = 1200
    AutoZeroTest = 300
    PlotsTestWait = 60
    SetTemperatureWait = 3600
