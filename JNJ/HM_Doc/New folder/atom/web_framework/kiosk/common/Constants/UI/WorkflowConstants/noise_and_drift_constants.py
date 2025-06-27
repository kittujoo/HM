"""
File_Name: wait_time_constants.py
Desc: This file contains the constants used for wait times throughout the application
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/26/22
"""


class NoiseAndDriftConstants:
    NoiseDriftTestWait = 1500
    LampOnState = "Turned On"
    LampOffState = "Turned Off"
    WelcomeFirstParagraph = "If you observe large spikes, baseline drift, or excessive noise in the baseline perform the Noise and Drift test."
    WelcomeSecondParagraph = "For best results, ensure that the flow cell is clean, contains degassed water, and is bubble free."
    WelcomeThirdParagraph = "This test takes about 15 minutes to complete."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph]

    # -- summary screen -- #
    DefaultFlowRate = "1.000 mL/min"
    DefaultComposition = "25:25:25:25% Acetonitrile:Methanol:Water:Trifluoroecetic Acid"
    # TODO: the <cell type> is a placeholder for an integration that is not ready yet, this will need to be changed once integration is completed
    DefaultFlowCell = "<Cell Type>"
    DefaultDataRate = "1 Hz"
    DefaultFilter = "Off"
    DefaultLamp = "On for more than 1 hr"
    DefaultWavelengthA = "254 nm"
    # DefaultWavelengthB = ""
    DefaultAmbientTemperature = "254.5 °C"
    DefaultTestTime = "18 minutes"

    CautionFirstParagraph = "Test results are impacted if water is present on the flow cell."
    CautionSecondParagraph = "For best results, Waters recommends keeping the flow on during this test."
    CautionThirdParagraph = "Waters recommends keeping the lamp powered-on for at least 1 hour prior to the test."
    expected_caution_paragraph_text = [CautionFirstParagraph, CautionSecondParagraph, CautionThirdParagraph]

    LampOffReadBackMessage = "Off"
    LampOnReadBackMessage = "On for "

    FlowOffReadBackMessage = "Flow is off"
    FlowOnReadBackMessage = "Flow is on"
