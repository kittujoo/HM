"""
File_Name: replace_flow_cell_workflow_constants.py
Desc: This file contains the constants of all the replace flow cell workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 10/14/22
"""

class ReplaceFlowCellWorkflowConstants:
    # Welcome
    WelcomeFirstParagraph = "Replace the flow cell if you notice that it is leaking, or if you suspect that it is clogged."
    WelcomeSecondParagraph = "To avoid contaminating the flow cell wear clean, chemical-resistant, powder-free gloves when removing or replacing it."
    WelcomeThirdParagraph = "To avoid damaging the flow cell ensure that you handle it with care. Also, do not disassemble the flow cell."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeThirdParagraph]

    # Caution
    HotSurfaceText = "To avoid damaging the flow cell, handle it with care. Do not disassemble the flow cell."
    CautionText = "To avoid contaminating the flow cell wear clean, chemical-resistant, powder-free gloves when removing or replacing it."
    expected_caution_text = [HotSurfaceText, CautionText]

    # Removal
    RemovalStepOne = "Open the detector door."
    RemovalStepTwo = "Disconnect the detector’s inlet and outlet tubing from the main column connection."
    RemovalStepThree = "Using a 1/4-inch flat-blade screwdriver, loosen the 3 thumbscrews on the flow cell assembly’s front plate."
    RemovalStepFour = "Grasp the handle and then gently pull the assembly toward you."
    expected_removal_text = [RemovalStepOne, RemovalStepTwo, RemovalStepThree, RemovalStepFour]

    # install page 1
    InstallStepFive = "Unpack and inspect the new flow cell, ensuring that the flow cell type is correct for your application."
    InstallStepSix = "Square the flow cell assembly in front of the opening, and then insert it slowly so that the guides on the front part of the cell flange engage the rails in the sample cell compartment."
    InstallStepSeven = "After the flange and rails are engaged, continue inserting the flow cell until the dowel pins on the instrument engage the corresponding holes on the cell holder."
    InstallStepEight = "Continue to insert the flow cell until the three thumbscrews align with their holes in the bulkhead."
    expected_first_installation_page_text = [InstallStepFive, InstallStepSix, InstallStepSeven, InstallStepEight]

    # install page 2
    InstallStepNine = "Verify that the screws are secure using a screw driver."
    InstallStepTen = "Connect the inlet tubing to the main column connection and flow cell inlet, and then connect the outlet tubing to the flow cell outlet."
    InstallStepEleven = "Close the detector door."
    expected_second_installation_page_text = [InstallStepNine, InstallStepTen, InstallStepEleven]
