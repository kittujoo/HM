"""
File_Name: plots_settings_screen_locator_lookup_.py
Desc: This file contains dictionaries of the locators in the plots settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/03/2021

"""
from web_framework.kiosk.pages.Locators.Plots.plots_screen_locators import PlotsSettingsScreenLocators as pssl, TimeWheelLocators


class PlotsSettingsLookup:
    """
    This class contains dictionary which has the web element mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """

    time_window_text_dictionary = {
        "Five": pssl.FIVE_MINUTE_TIME_WINDOW,
        "Fifteen": pssl.FIFTEEN_MINUTE_TIME_WINDOW,
        "Custom": pssl.CUSTOM_TIME_WINDOW}

    action_icons_text_dictionary = {
        "First": pssl.FIRST_MORE_ACTION_ICON,
        "Second": pssl.SECOND_MORE_ACTION_ICON,
        "Third": pssl.THIRD_MORE_ACTION_ICON}

    time_in_hours_dictionary = {
        "One": TimeWheelLocators.ONE_HOUR,
        "Two": TimeWheelLocators.TWO_HOUR,
        "Three": TimeWheelLocators.THREE_HOUR}

    time_in_minutes_dictionary = {
        "One": TimeWheelLocators.ONE_MINUTE,
        "Two": TimeWheelLocators.TWO_MINUTE,
        "Three": TimeWheelLocators.THREE_MINUTE}

    settings_icons_text_dictionary = {
        "First": pssl.FIRST_SETTINGS_ICON,
        "Second": pssl.SECOND_SETTINGS_ICON,
        "Third": pssl.THIRD_SETTINGS_ICON}

    plots_color_dictionary = {

        "Red": pssl.RED_ICON,
        "Yellow": pssl.YELLOW_ICON,
        "Pink": pssl.PINK_ICON,
        "Green": pssl.GREEN_ICON,
        "Orange": pssl.ORANGE_ICON,
        "Blue": pssl.BLUE_ICON


    }

    plots_options_dictionary ={
        "alphabetic order": pssl.ALPHABETIC_ORDER_OPTION,
        "catogary": pssl.CATOGARY_OPTION

    }