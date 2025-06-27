"""
File_Name: system_leak_test_summary_screen_locator_lookup.py
Desc: This file contains dictionaries of the locators in the  leak test summary  screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/03/2021


"""
from web_framework.kiosk.pages.Locators.Health.system_leak_test_locators import SystemLeakTestWorkflowSetupLocators


class SystemLeakTestSettingsLookup:
    """
    This class contains dictionary which has the web element mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """


    end_point_text_dictionary = {
        "Vent Valve": SystemLeakTestWorkflowSetupLocators.END_POINT_VENT_VALVE_OPTION,
        "Column": SystemLeakTestWorkflowSetupLocators.END_POINT_COLUMN_OPTION}

    prime_options_text_dictionary = {
        "Don't Prime": SystemLeakTestWorkflowSetupLocators.DO_NOT_PRIME_OPTION,
        "Prime": SystemLeakTestWorkflowSetupLocators.DO_PRIME_OPTION}

    retry_options_text_dictionary = {
        "Null": SystemLeakTestWorkflowSetupLocators.DO_NOT_RETRY_OPTION,
        "Two": SystemLeakTestWorkflowSetupLocators.ONE_TIMES_RETRY_OPTION,
        "Five": SystemLeakTestWorkflowSetupLocators.FIVE_TIMES_RETRY_OPTION}

    solvent_line_dictionary = {
        "A": SystemLeakTestWorkflowSetupLocators.SOLVENT_LINE_A,
        "B": SystemLeakTestWorkflowSetupLocators.SOLVENT_LINE_B,
        "C": SystemLeakTestWorkflowSetupLocators.SOLVENT_LINE_C,
        "D": SystemLeakTestWorkflowSetupLocators.SOLVENT_LINE_D

    }