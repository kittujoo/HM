"""
File_Name: needle_seal_readiness_constants.py
Desc: This file contains the constants of the needle seal readiness test workflow
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 5/17/22
"""


class NeedleSealReadinessConstants:
    WelcomeFirstParagraph = \
        "The needle seal readiness test indicates whether or not " \
        "there is a leak at the needle seal before you start an injection. " \
        "The sample manager moves the injection valve to the load position and monitors the solvent manager pressure."
    WelcomeSecondParagraph = \
        "When the pressure is stable, the sample manager engages the needle on the seal, " \
        "and then moves the injection valve to the injection position."
    WelcomeThirdParagraph = "The sample manager monitors pump pressure and verifies " \
                            "that the pressure does not decrease."
    WelcomeListParagraph = "Perform this test:"
    WelcomeListItemOne = "After you replace the seal."
    WelcomeListItemTwo = "After you replace the needle."
    WelcomeFourthParagraph = "The test will take about 1 minute to complete."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph,
                                       WelcomeThirdParagraph]

    expected_instruction_text = [WelcomeListParagraph, WelcomeListItemOne, WelcomeListItemTwo]

    DefaultFlowRate = "1.000 mL/min"
    DefaultSystemPressure = "25.00 psi"
    DefaultTestTime = "2 minutes"
    MinPressureDifference = 0  ##TODO need to verify
    MaxPressureDifference = 25  ##TODO need to verify
    SetupHeader = "Setup"
    StatusHeader = "Status"
    FlowHintMessage = "0.200 to 5.000 mL/min"
    CompHintMessage = "0 to 100%"
    SummaryLineOne = "Verify that the solvent bottle contains a sufficient amount of liquid."
    SummaryLineTwo = "Tap START when ready."
    expected_summary_text = [SummaryLineOne, SummaryLineTwo]

    SetupLineOne = "Before starting this test, establish an appropriate flow and composition through the pump. " \
                   "You can monitor the pressure on the next page."
    SetupLineTwo = "Adjust the flow rate if needed, and then tap NEXT."

    expected_setup_text = [SetupLineOne, SetupLineTwo]

    StatusLineOne = "Results appear when the test completes."

    ResultsLineOne = "The test passes when the sample manager verifies that the pump pressure does not decrease."
    ResultsLineTwo = "The system log adds an entry for this test."

    expected_results_info = [ResultsLineOne, ResultsLineTwo]

    FailedResultState = "Failed"
    PassedResultState = "Passed"

    CompLineOne = "Before starting this test, establish an appropriate flow and composition through the pump. " \
                  "You can monitor the pressure on the next page."

    CompLineTwo = "Tap NEXT when ready."

    expected_comp_setup_text = [CompLineOne, CompLineTwo]
