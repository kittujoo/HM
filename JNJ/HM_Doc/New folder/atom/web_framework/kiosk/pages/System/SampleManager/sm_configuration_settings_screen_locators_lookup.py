"""
File_Name: sm_configuration_settings_screen_locator_lookup_.py
Desc: This file contains dictionaries of the locators in the sample manager configuration settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 01/21/2021
__modified__ = "Tyler Prada" added more extension loops 9/27/23
"""
from web_framework.kiosk.pages.Locators.System.SampleManager.sm_configuration_settings_screen import VolumeSettingsTab, \
    CompartmentLightTab, OptionsTab


class SMConfigurationSettingsScreenLocatorsLookup:
    """
    This class contains dictionary which has the webelement mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """

    extension_loop_dictionary = {
        "50": VolumeSettingsTab.FIFTY_MICRO_LITRE_OPTION,
        "100": VolumeSettingsTab.HUNDRED_MICRO_LITRE_OPTION,
        "250": VolumeSettingsTab.TWO_FIFTY_MICRO_LITRE_OPTION,
        "1000": VolumeSettingsTab.ONE_THOUSAND_MICRO_LITRE_OPTION,
        "2000": VolumeSettingsTab.TWO_THOUSAND_MICRO_LITRE_OPTION
    }

    syringe_size_dictionary = {
        "100": VolumeSettingsTab.HUNDRED_MICRO_LITRE_SYRINGE_OPTION,
        "250" : VolumeSettingsTab.TWO_FIFTY_MICRO_LITRE_SYRINGE_OPTION,
        "500" : VolumeSettingsTab.FIVE_HUNDRED_MICRO_LITRE_SYRINGE_OPTION

    }

    plate_scanned_light_option_dictionary = {

        "on": CompartmentLightTab.LIGHT_TURN_ON_FOR_PLATE_OPTION,
        "off": CompartmentLightTab.LIGHT_TURN_OFF_FOR_PLATE_OPTION

    }

    door_open_light_option_dictionary = {
        "on": CompartmentLightTab.LIGHT_TURN_ON_FOR_DOOR_OPTION,
        "off": CompartmentLightTab.LIGHT_TURN_OFF_FOR_DOOR_OPTION
    }

    injection_option_dictionary = {
        "fails": OptionsTab.INJECTION_FAILS_OPTIONS,
        "continues": OptionsTab.INJECTION_CONTINUES_OPTIONS
    }

