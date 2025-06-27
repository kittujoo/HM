"""
File_Name: solvent_bottles_locator_lookup.py
Desc: This file contains dictionaries of the locators in the mobile phase settings screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 07/19/2022

"""
from web_framework.kiosk.pages.Locators.System.SolventBottlesManager.mobile_phase_configuration_settings_screen_locators import \
    MobilePhaseConfigurationScreenLocators


class SolventBottlesLookup:
    """
    This class contains dictionary which has the web element mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """

    line_color_dictionary = {

        "Red": MobilePhaseConfigurationScreenLocators.RED_ICON,
        "Yellow": MobilePhaseConfigurationScreenLocators.YELLOW_ICON,
        "Pink": MobilePhaseConfigurationScreenLocators.PINK_ICON,
        "Green": MobilePhaseConfigurationScreenLocators.GREEN_ICON,
        "Orange": MobilePhaseConfigurationScreenLocators.ORANGE_ICON,
        "Blue": MobilePhaseConfigurationScreenLocators.BLUE_ICON

    }
