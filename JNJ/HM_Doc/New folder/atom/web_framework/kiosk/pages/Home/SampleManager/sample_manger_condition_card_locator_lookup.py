"""
File_Name: sample_manager_condition_card_locator_lookup_.py
Desc: This file contains dictionaries of the sampl temperature locators
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/26/2021


"""
from web_framework.kiosk.pages.Locators.Home.SampleManager.sample_temperature_condition_card import \
    SampleTemperatureSettingScreenLocators


class SampleManagerLocatorLookup:
    """
    This class contains dictionary which has the webelement mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the scroll component in the sample
    temperature settings page

    """

    sample_temperature_settings_dictionary = {
        "21": SampleTemperatureSettingScreenLocators.TWENTY_ONE_OPTION,
        "25": SampleTemperatureSettingScreenLocators.TWENTY_FIVE_OPTION,
        "33": SampleTemperatureSettingScreenLocators.THIRTY_THREE_OPTION,
        "38": SampleTemperatureSettingScreenLocators.THIRTY_EIGHT_OPTION,
        "30": SampleTemperatureSettingScreenLocators.THIRTY_OPTION,
        "36": SampleTemperatureSettingScreenLocators.THIRTY_SIX_OPTION,
        "40": SampleTemperatureSettingScreenLocators.FORTY_OPTION

    }
