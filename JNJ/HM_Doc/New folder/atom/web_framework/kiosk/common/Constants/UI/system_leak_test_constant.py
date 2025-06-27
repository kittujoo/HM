"""
File_Name: system_leak_test_constant.py
Desc: This file contains the constants of all the workflow screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/11/2022

"""


class SystemLeakTestConstant:
    DefaultSolvent = "Solvent B (don't prime, first)"
    DefaultEndPoint = "Vent Valve"
    DefaultTestFailOption = "Don't retry"
    DefaultEstimatedTime = "5 minutes"
    DefaultPrimeOption = "don't prime"
    WelcomeFirstParagraph = "The leak test evaluates the fluid-handling integrity of the system. The test helps identify problems with check valves, tubes, " \
                            "fittings, plungers, plunger high-pressure seals, or the vent valve on the pump."

    WelcomeSecondParagraph = "Symptoms of leaks can include visible drips, inconsistent retention times, or increased baseline noise."
    WelcomeThirdParagraph = "Perform a leak test whenever you replace or loosen fittings during maintenance."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeSecondParagraph,
                                       WelcomeThirdParagraph]

    BetterResultsForPointOne = "Run the test at your typical maximum operating pressure"
    BetterResultsForPointTwo = "Use only fresh, clean, degassed solvent"
    BetterResultsForPointThree = "Prime the system before performing the test"

    expected_better_results_text = [BetterResultsForPointOne, BetterResultsForPointTwo, BetterResultsForPointThree]

    recommendationText = "Do not perform the tests until you condition the seals for at least 15 to 30 minutes at 9000 psi. The leak test can fail if the seals are not conditioned."
    PrimaryLeakRate = 500
    AccumulatorLeakRate = 500
    PrimaryResultState = "Passed"
    AccumulatorResultState = "Passed"
    PrimaryFinalStroke = 50
    AccumulatorFinalStroke = 30
    PrimaryCompressionAttempts = 3
    AccumulatorCompressionAttempts = 3
    ResultValidateText = "Results"
    StatusValidateText = "Status"
    StoppedValidateText = "Workflow interrupted"
    SystemLeakTestTime = 6000
    LeakTestPassedState = "Passed"
    LeakTestFailedState = "Failed"
    Target_pressure_difference = 2000
    MaximumToleranceInMinutes = 20
