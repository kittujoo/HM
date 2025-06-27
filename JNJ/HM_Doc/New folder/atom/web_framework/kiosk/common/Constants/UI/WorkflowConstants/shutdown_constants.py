"""
File_Name: shutdown_constants.py
Desc: This file contains the constants of the shutdown workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila" Initial Check-in 10/13/2022

"""


class ShutdownConstants:
    LampOffInfo = "Power-off"
    LampOnInfo = "Power-on"
    WelcomeFirstParagraph = "System shutdown automates a set of activities to help ensure a reliable and proper shutdown of the system."
    WelcomeListParagraph = "In this workflow, you will set up the parameters for your shutdown activities and run this activity."
    WelcomeSecondParagraph = "Tap NEXT to proceed."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeListParagraph, WelcomeSecondParagraph]

    SampleTempOffMessage = "Off"
    ColumnTempOffMessage = "Off"
    FlowOffMessage = "Off"
    WorkFlowCompleteState = "Complete"
    error_message = "The workflow is not completed "
    TimeToComplete = 600
    StatusValidateText = "Status"
