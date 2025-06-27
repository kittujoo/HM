"""
File_Name: replace_needle_constant.py
Desc: This file contains the constants of all the replace needle  workflow screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 09/19/2022

"""


class ReplaceNeedleConstant:
    WelcomeFirstParagraph = "Replace the needle when it is visibly damaged or bent. The procedure itself is covered in the user assistance guide for this system. To access this procedure on you mobile device, tap the ? in the upper right of this screen."

    WelcomeSecondParagraph = "This workflow prepares the system for you to replace the needle."

    WelcomeThirdParagraph = "After you replace the needle, you will be presented with recommended procedures to perform next."

    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph,
                                       WelcomeThirdParagraph]

    caution_text = "To avoid personal contamination with biologically hazardous, toxic, and corrosive materials, wear chemical-resistant, powder-free gloves when performing this procedure."

    ProcedureFirstParagraph = "The needle carriage is now in position to allow you to replace the needle."

    ProcedureSecondParagraph = "Open the compartment door and follow the procedure provided by Waters. Scan the QR code to see the procedure now on your mobile device."

    ProcedureThirdParagraph = "Tap NEXT once you have replaced the needle."

    expected_procedure_paragraph_text = [ProcedureFirstParagraph, ProcedureSecondParagraph,
                                         ProcedureThirdParagraph]

    TestOneRunningText = "Prime the sample metering pump"

    TestTwoRunningText = "Calibrate the needle"

    TestThreeRunningText = "Test the Needle Seal Readiness"
    expected_test_text = [TestOneRunningText, TestTwoRunningText, TestThreeRunningText]
    warning_text = "Remove any sample plates from the sample compartment and close the compartment door."

    information_text ="The workflow automatically advances to the next page once the carriage is in the service position."
