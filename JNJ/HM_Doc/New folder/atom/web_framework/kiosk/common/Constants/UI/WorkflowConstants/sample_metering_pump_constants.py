"""
File_Name: sample_metering_pump_constants.py
Desc: This file contains the constants of the sample metering pump leak test test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/10/22
__modified__ = "Tyler Prada" Post FCS adjustments 6/13/23
"""


class SampleMeteringPumpConstants:
    MaximumToleranceInMinutes = 20
    SampleMeteringPumpDefaultWaitTime = 1200  # 20min
    SampleMeteringPumpPrimingWaitTime = 2000  # 33min
    # leak rate needs to be between 0.000 and 500.000 ml/min
    min_leak_rate = 0.0000
    max_leak_rate = 500.0000

    WelcomeFirstParagraph = "This diagnostic tests for leaks between the sample metering pump and the injection valve. " \
                            "It also indicates if the sample metering pump is working."
    WelcomeSecondParagraph = "The test will run at the maximum pressure of the sample metering pump."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph]

    DefaultPrimingOption = "Priming enabled"

