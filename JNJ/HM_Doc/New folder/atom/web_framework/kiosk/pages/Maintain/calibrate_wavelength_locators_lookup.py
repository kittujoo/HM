"""
File_Name: calibrate_wavelength_locator_lookup.py
Desc: This file contains dictionaries of the locators in the calibrate wavelength workflow  screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = Sharmila Vairamani" Initial Check-in 06/06/2022

"""
from web_framework.kiosk.pages.Locators.Maintain.calibrate_wavelength_locators import CalibrateWavelengthWorkflowLocators


class CalibrateWavelengthLookup:
    """
    This class contains dictionary which has the web element mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """

    solvent_line_dictionary = {
        "A": CalibrateWavelengthWorkflowLocators.SOLVENT_LINE_A,
        "B": CalibrateWavelengthWorkflowLocators.SOLVENT_LINE_B,
        "C": CalibrateWavelengthWorkflowLocators.SOLVENT_LINE_C,
        "D": CalibrateWavelengthWorkflowLocators.SOLVENT_LINE_D

    }
