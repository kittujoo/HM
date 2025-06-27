"""
File_Name: replace_seal_workflow_constants.py
Desc: This file contains the constants of all the replace seal workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/27/22
"""

class ReplaceSealWorkflowConstants:
    # Welcome
    WelcomeFirstParagraph = "Replace the needle seal each time you replace the needle and during period maintenance. The procedure itself is covered in the user assistance guide for this system. To access this procedure on you mobile device, tap the ? in the upper right of this screen."
    WelcomeSecondParagraph = "This workflow prepares the system for you to replace the needle seal."
    WelcomeThirdParagraph = "After you replace the needle seal, you will be presented with recommended procedures to perform next."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph]

    # Caution
    CautionText = "To avoid personal contamination with biologically hazardous, toxic, and corrosive materials, wear chemical-resistant, powder-free gloves when performing this procedure."

    # Procedure one
    ProcedureOneFirstParagraph = "The needle carriage is now in position to allow you to replace the seal."
    ProcedureOneSecondParagraph = "Open the compartment door and follow the procedure provided by Waters. Scan the QR code to see the procedure now on your mobile device."
    ProcedureOneThirdParagraph = "Tap NEXT once you have replaced the seal."
    expected_procedure_one_text = [ProcedureOneFirstParagraph, ProcedureOneSecondParagraph, ProcedureOneThirdParagraph]
