"""
File_Name: replace_column_workflow_constants.py
Desc: This file contains the constants of all the replace column workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 9/21/22
"""

class ReplaceColumnWorkflowConstants:
    WelcomeFirstParagraph = "When making the column compartment plumbing connections, consult the topics in the instructions about assembling and tightening the various fittings used to connect the column compartment to the system."
    WelcomeSecondParagraph = "When connecting tubing, heed the following recommendations for installing and tightening fittings."
    WelcomeListItemOne = "To prevent band spreading, ensure that the tubing bottoms in the connection port before you tighten the compression fitting."
    WelcomeListItemTwo = "Whenever you loosen fittings during maintenance, examine them for cracks, stripped threads, and deformations."
    WelcomeListItemThree = "Do not reuse fittings with metallic ferrules more than six times."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph, WelcomeListItemOne, WelcomeListItemTwo, WelcomeListItemThree]

    HotSurfaceText = "To prevent burn injuries, set the column temperature to Off, and then allow the column compartment and its components to cool for 60 minutes before touching them. Monitor the column compartment's internal temperature to ensure that all components are cool."
    CorrosiveMaterialsText = "To avoid personal contamination with biologically hazardous, toxic, and corrosive materials, wear chemical-resistant, powder-free gloves when performing this procedure."
    GeneralCautionText = "To avoid eye injury, use eye protection when performing this procedure."
    expected_caution_paragraph_text = [HotSurfaceText, CorrosiveMaterialsText, GeneralCautionText]

    RemovalFirstParagraph = "For safety, temperature and flow controls are automatically shut off."
    RemovalSecondParagraph = "Consult the removal procedure for your specific column."
    # TODO: Wrong text is being displayed for the installation screen
    InstallationFirstParagraph = ""

    NewSerialNumber = "186003034"
    NewPartNumber = "186003034"
    NewDescription = "XBridge BEH C18, 130A, 3.5 μm, 4.6 mm X 150 mm"
