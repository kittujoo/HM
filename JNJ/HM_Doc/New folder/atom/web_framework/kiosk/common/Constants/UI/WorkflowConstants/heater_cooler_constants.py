"""
File_Name: heater_cooler_constants.py
Desc: This file contains the constants of the heater/cooler workflow
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 1/14/21
__modified__ = "Tyler Prada" added welcome text constants 1/20/22
__modified__ = "Tyler Prada" Added summary and result screen constants 2/15/22
__modified__ = "Tyler Prada" Adjustments due to workflow changes & results rework 7/22/22
"""


class HeaterCoolerConstants:
    InProgressBannerText = "Test in Progress"
    TestCompleteBannerText = "Test Complete"

    WelcomeFirstParagraph = "The test ensures that the temperature control can heat and cool the compartment at a preset rate. Depending on the ambient temperature, this test takes 5-20 minutes to complete."
    WelcomeSecondParagraph = "Note: To prevent damage to the column, ensure that you remove it from the compartment before you start the test."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph]

    # -- Summary Screen -- #
    DefaultTestMode = "Quick, 1 minute"
    DefaultAmbientTemperature = "31.0 °C"
    DefaultColumnTemperature = "23.0 °C"
    DefaultColumnDoor = "Closed"
    DefaultTimeEstimate = "10 minutes"

    # -- Results Screen -- #
    DefaultResultsAmbientTemperature = "24.5"
    DefaultTargetRate = "10.0"
    DefaultMeasuredRate = "16.4"

    AmbientTemperatureMin = 0.0
    AmbientTemperatureMax = 40.0
    TargetRateMin = 2.0
    #TargetRateMax = 10.0
    MeasuredRateMin = 0.0
    MeasuredRateMax = 40.0

    MaxTimeTocompleteheaterCooler = 1200
    StatusValidateText = "Status"
    TimeToLoadDoorState = 10
    FailureMessage = "failed to load door state"
    ClosedDoorStatus = "Closed"
    PassMessage = "Passed"
    ToleranceTime = 25

