"""
File_Name: calibrate_axes_constants.py
Desc: This file contains the constants of the calibrate axes workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 3/9/22
__modified__ = "Tyler Prada" added summary screen related constants 6/17/22
__modified__ = "Tyler Prada" added B0 values 7/28/22
__modified__ = "Tyler Prada" added platter path values 8/31/22
"""


class CalibrateAxesConstants:
    WelcomeFirstParagraphZ_axis = "Calibrate the needle (Z-axis) before you use the system for the first time (and whenever you replace the sample needle)."

    WelcomeSecondParagraphZ_axis = "Failing to calibrate the needle can damage it. The calibration procedure is automatic and works the same for all needles."

    WelcomeThirdParagraphZ_axis = "Remove all sample plates from the compartment before calibrating the needle."

    expected_welcome_paragraph_text_Z_axis = [WelcomeFirstParagraphZ_axis, WelcomeSecondParagraphZ_axis,
                                              WelcomeThirdParagraphZ_axis]

    WelcomeFirstParagraphZp_axis = "Calibrate the foot (Zp-axis) before you use the system for the first time, and whenever you replace the needle assembly components."

    WelcomeSecondParagraphZp_axis = "Tap NEXT to proceed."

    expected_welcome_paragraph_text_Zp_axis = [WelcomeFirstParagraphZp_axis, WelcomeSecondParagraphZp_axis]

    WelcomeFirstParagraphHardStop_axis = "Calibrate the wash tower hard stop before you use the system for the first time, and whenever you replace any needle assembly components or the hard stop."

    WelcomeSecondParagraphHardStop_axis = "Tap NEXT to proceed."

    expected_welcome_paragraph_text_HardStop_axis = [WelcomeFirstParagraphHardStop_axis, WelcomeSecondParagraphHardStop_axis]

    ZAxis = "Z-axis"
    ZpAxis = "Zp-axis"
    HardStopAxis = "Hard Stop"
    PassMessage = "Passed"
    OffsetUnit = "mm"

    DefaultAxesPathTestTime = 300 # 5min

    DefaultCompartmentDoor = "Closed"
    DefaultSamplePlate = "Removed"
    DefaultTrayDoor = "Pulled out"
    DefaultNeedleAdaptor = "Installed"
    DefaultTestTime = "Less than 1 minute"
    MaximumToleranceInMinutes = 5


class CalibratePlatterConstants:
    OffsetValueMin = 0
    OffsetValueMax = 10


class CalibrateOffsetConstants:
    OffsetValue = 0


class CalibrateB0AxesConstants:
    # Values as per Fadi on 7/25/22
    # Rn: 121.7224 mm + / - 2.54 mm
    # Lc: 74.4243 mm + / - 2.54 mm
    # Bo: 102.9251 deg + / - 2 degrees
    # To: 80.395 deg + / - 2 degrees

    # Calculated based on the above info ^
    # RnMin 119.1844 RnMax 124.2644
    # LcMin 71.8843 LcMax 76.9643
    # BetaMin 100.9251 BetaMax 104.9251
    # ThetaMin 78.395 ThetaMax 82.395

    RnValueMin = 119.1844
    RnValueMax = 124.2644
    LcValueMin = 71.8843
    LcValueMax = 76.9643
    BetaValueMin = 100.9251
    BetaValueMax = 104.9251
    ThetaValueMin = 78.395
    ThetaValueMax = 82.395
