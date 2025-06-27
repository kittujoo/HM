"""
File_Name: pump_maintenance_workflow_constants.py
Desc: This file contains the constants of all the pump maintenance workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/3/22
"""


class PumpMaintenanceWorkflowConstants:
    # Welcome
    WelcomeParagraph = "Replace the pump head plunger and seal when…"

    LeftListItemOne = "Chemical-resistant, powder-free gloves"
    LeftListItemTwo = "1/2 inch open-end wrench"
    LeftListItemThree = "T27 TORX driver"
    LeftListItemFour = "Pliers"
    LeftListItemFive = "Seal removal tool"
    LeftListItemSix = "Sharp tool, such as a dental pick"

    RightListItemOne = "Methanol"
    RightListItemTwo = "Fluoropolymer ring"
    RightListItemThree = "Plunger seal"
    RightListItemFour = "Plunger seal spacer"
    RightListItemFive = "Seal wash seal"

    expected_welcome_text = [WelcomeParagraph, LeftListItemOne, LeftListItemTwo,
                             LeftListItemThree, LeftListItemFour, LeftListItemFive,
                             LeftListItemSix, RightListItemOne, RightListItemTwo,
                             RightListItemThree, RightListItemFour, RightListItemFive]

    # Caution
    FirstCautionText = "To prevent injury, always observe Good Laboratory Practice when you handle solvents, change tubing, or operate this device. Consult the Material Safety Data Sheets regarding the solvents you use."
    SecondCautionText = "To prevent contamination to system components, wear clean, chemical-resistant, powder-free gloves when performing this procedure."
    expected_caution_text = [FirstCautionText, SecondCautionText]

    # Procedure
    ProcedureTopText = "Replacing the plunger seal in the primary pump head involved these steps:"

    ProcedureStepOne = "Flushing the pump with nonhazardous solvent"
    ProcedureStepTwo = "Moving the pump head plunger backward"
    ProcedureStepThree = "Removing the pump head"
    ProcedureStepFour = "Removing the pump head plunger"
    ProcedureStepFive = "Removing the pump head seals"
    ProcedureStepSix = "Installing the new pump head seals"
    ProcedureStepSeven = "Installing the new pump head plunger"
    ProcedureStepEight = "Reinstalling the pump head"

    ProcedureBottomText = "Once completed, Waters recommends that you check for leaks by running the System Leak Test."
    expected_procedure_text = [ProcedureTopText, ProcedureStepOne, ProcedureStepTwo,
                               ProcedureStepThree, ProcedureStepFour, ProcedureStepFive,
                               ProcedureStepSix, ProcedureStepSeven, ProcedureStepEight,
                               ProcedureBottomText]
