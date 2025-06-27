"""
File_Name: replace_lamp_workflow_constants.py
Desc: This file contains the constants of all the replace lamp workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/24/22
"""

class ReplaceLampWorkflowConstants:
    # Welcome
    WelcomeFirstParagraph = "Change the lamp when it repeatedly fails to ignite, or when the detector fails to calibrate."
    WelcomeSecondParagraph = "The TUV lamp is automatically sensed upon installation, and its serial number and installation date are automatically entered into the Lamp Change Record table."
    WelcomeThirdParagraph = "Waters warrants 2000 hours of lamp life, or one year since date of purchase, whichever comes first."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph]

    # Caution
    BurnCautionText = "To prevent burn injuries, allow the lamp to cool for 30 minutes before removing it. The lamp housing gets extremely hot during operation."
    GeneralCautionText = "To avoid eye injury from ultraviolet radiation exposure:"
    GeneralCautionBulletOne = "Wear eye protection that filters ultraviolet light"
    GeneralCautionBulletTwo = "Keep the lamp in the housing during operation"
    expected_caution_text = [BurnCautionText, GeneralCautionText, GeneralCautionBulletOne, GeneralCautionBulletTwo]

    # Preconditions
    PreconditionsFirstParagraph = "The Lamp and Flow are automatically shut off."
    PreconditionsSecondParagraph = "The lamp and lamp housing may be hot. Wait 30 minutes from now (or 15 minutes with the fans running) for these components to cool before touching them."
    PreconditionsThirdParagraph = "Ensure that sufficient time has passed and the lamp is cool enough to touch, then tap NEXT."
    expected_preconditions_text = [PreconditionsFirstParagraph, PreconditionsSecondParagraph, PreconditionsThirdParagraph]

    # Removal
    RemovalStepOne = "Detach the lamp power connector from the detector."
    RemovalStepTwo = "Loosen the single captive screw that attaches the lamp cover."
    RemovalStepThree = "Loosen the two captive screws in the lamp base."
    RemovalStepFour = "Gently remove the lamp from the lamp housing."
    RemovalWarningText = "Lamp gas is under slight pressure. To prevent shattering the glass, use care when disposing of the lamp."
    RemovalCautionParagraphOne = "Do not touch the glass bulb of the new lamp. Dirt or fingerprints adversely affect detector operation. If the bulb needs cleaning, gently rub it with ethanol and lens tissue."
    RemovalCautionParagraphTwo = "Do not use abrasive tissue."
    RemovalCautionParagraphThree = "Do not apply excessive pressure."
    expected_removal_text = [RemovalStepOne, RemovalStepTwo, RemovalStepThree, RemovalStepFour, RemovalWarningText, RemovalCautionParagraphOne, RemovalCautionParagraphTwo, RemovalCautionParagraphThree]

    # First Installation
    InstallationStepOne = "Unpack the new lamp from its packing material without touching the bulb."
    InstallationStepTwo = "Inspect the new lamp and lamp housing."
    InstallationStepThree = "Position the lamp so that the cut-out on the lamp base plate is in line with the positioning pin on the lamp housing."
    InstallationStepFour = "Gently push the lamp forward until it is installed. Ensure that it is flush with the optics bench."
    FirstInstallationCautionText = "For best results, Waters recommends that you alternate between tightening the captive screws, and pushing the lamp forward."
    expected_first_installation_text = [InstallationStepOne, InstallationStepTwo, InstallationStepThree, InstallationStepFour, FirstInstallationCautionText]

    # Second Installation
    InstallationStepFive = "Tighten the two captive screws, and then reconnect the lamp power connector."
    InstallationStepSix = "Close the lamp cover and hand-tighten the cover's captive screw."
    InstallationStepSeven = "Power-on the system."
    SecondInstallationCautionText = "For best results, Waters recommends that you alternate between tightening the captive screws, and pushing the lamp forward."
    expected_second_installation_text = [InstallationStepFive, InstallationStepSix, InstallationStepSeven, SecondInstallationCautionText]
