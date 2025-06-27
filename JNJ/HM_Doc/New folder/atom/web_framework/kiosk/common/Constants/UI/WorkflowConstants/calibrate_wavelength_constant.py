"""
File_Name: calibrate_wavelength_constant.py
Desc: This file contains the constants of all the workflow screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 06/06/2022
__modified__ = "Tyler Prada" added default summary text 7/18/22
__modified__ = "Tyler Prada" Added wavelength values 9/7/22
"""


class CalibrateWavelengthConstant:
    WelcomeFirstParagraph = "In this workflow, you can verify calibration or recalibrate the wavelengths."

    WelcomeSecondParagraph = "Although wavelength verification runs automatically each time the detector is powered-on, Waters recommends that you verify the calibration once a month."

    WelcomeThirdParagraph = "Calibrate the wavelengths to adjust the detector and to ensure that wavelength readings are accurate. The calibration corrects errors in wavelength detection caused by aging optics or excessive vibration."

    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph,
                                       WelcomeThirdParagraph]

    BetterResultsForPointOne = "Ensure the flow cell is clean"
    BetterResultsForPointTwo = "Use acetonitrile to flush the column"
    Expected_status = "Passed"

    expected_better_results_text = [BetterResultsForPointOne, BetterResultsForPointTwo]

    RecommendationText = "It is recommended that you verify calibration or calibrate now."

    # TODO: This text will come from ISYM but this has not ben integrated yet 7/18/22
    DefaultLampTime = "On for 3 hours"
    DefaultFlowCell = "Analythical"
    DefaultDoorStatus = "Door is closed"
    DefaultIntensity = "Intensity: @230 nm"
    DefaultEnergy = "Energy: 1.2345 nA"
    DefaultReference = "Reference: 1.2345 nA"
    DefaultRation = "Ration: 1.000"
    DefaultColumnFlush = "Flush the column for 10 minutes prior to calibration."
    DefaultBufferFlush = "Flush the column for 20 minutes prior to calibration."
    NoFlushMessage = "Column flush options not enabled"
    FlushSelectedMessage = "10 minutes"
    FlushNotSelectedMessage = "Not selected"
    PreFlushNotSelectedMessage = "Not selected"
    PreFlushSelectedMessage = "10 minutes"

    WavelengthMaxValue257 = 257
    WavelengthMaxValu3797 = 379
    WavelengthMaxValue521 = 521

    # MaxiTimeToCalibrate = 600
    MaxiTimeToCalibrate = 3000

    lamp_state = "On"
    flow_cell_state = "Type unprogrammed"
    expected_precondition = [lamp_state, flow_cell_state]

    StoppedValidateText = "Workflow interrupted"
