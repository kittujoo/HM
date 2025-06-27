"""
File_Name: sample_temperature_test_constants.py
Desc: This file contains the constants of the sample temperature test test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 12/15/22
__modified__ = "Tyler Prada" Post-FCS update 7/19/23
"""


class SampleTemperatureTestConstants:
    WelcomeFirstParagraph = "The test ensures that the temperature control system can heat and cool the compartment at a preset rate."
    WelcomeSecondParagraph = "Depending on the ambient temperature, this test takes 5-20 minutes to complete."
    WelcomeThirdParagraph = "Note: To prevent damage to samples, ensure that you remove all sample plates from the compartment before you start the test."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph]

    StatusValidateText = "Status"
    ClosedDoorStatus = "Closed"
    TimeToLoadDoorState = 10
    FailureMessage = "failed to load door state"
    PassMessage = "Passed"
    ToleranceTime = 25
