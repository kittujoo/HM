"""
File_Name: user_profile_settings_page_locator_lookup_.py
Desc: This file contains dictionaries of the locators in the user settings screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 12/09/2020
__modified__ = "Tyler Prada" added sections for screensaver and datetime 06/30/2021

"""
from web_framework.kiosk.pages.Locators.User.user_settings_screen_locators import UserSettingsScreenPageLocators


class UserSettingsPageLocatorLookup:
    """
    This class contains dictionary which has the webelement mapped to his corresponding locators. Dictionary is created
    for ui components like slider that allows the user to select from varies options. The feature file where all the scenarios
    are written uses the key of any dictionary in this class to select any options from the slider component in the user
    settings page
    """

    volume_settings_dictionary = {
        "mute": UserSettingsScreenPageLocators.MUTE_VOLUME_SETTINGS,
        "high": UserSettingsScreenPageLocators.HIGH_VOLUME_SETTINGS,
        "low": UserSettingsScreenPageLocators.LOW_VOLUME_SETTINGS
    }

    screen_lock_period_dictionary = {
        "5 min": UserSettingsScreenPageLocators.FIVE_MINUTE_SCREEN_LOCK_OPTION,
        "15 min": UserSettingsScreenPageLocators.FIFTEEN_MINUTE_SCREEN_LOCK_OPTION,
        "30 min": UserSettingsScreenPageLocators.THIRTY_MINUTE_SCREEN_LOCK_OPTION,
        "120 min": UserSettingsScreenPageLocators.ONE_HUNDRED_AND_TWENTY_MINUTE_SCREEN_LOCK_OPTION
    }

    theme_settings_dictionary = {
        "light": UserSettingsScreenPageLocators.LIGHT_THEME_OPTION,
        "dark": UserSettingsScreenPageLocators.DARK_THEME_OPTION
    }

    datetime_format_dictionary = {
        # time formats
        "24 Hour": UserSettingsScreenPageLocators.HOUR_24_FORMAT_OPTION,
        "12 Hour": UserSettingsScreenPageLocators.HOUR_12_FORMAT_OPTION,
        # date formats
        "29 February 2020": UserSettingsScreenPageLocators.DAY_MONTH_YEAR_OPTION,
        "February 29, 2020": UserSettingsScreenPageLocators.MONTH_DAY_YEAR_OPTION,
        "2020, 29 February": UserSettingsScreenPageLocators.YEAR_DAY_MONTH_OPTION,
        "Feb/29/2020": UserSettingsScreenPageLocators.LETTER_MONTH_DAY_YEAR_OPTION,
        "02/29/2020": UserSettingsScreenPageLocators.NUMBER_MONTH_DAY_YEAR_OPTION,
        "2020/02/29": UserSettingsScreenPageLocators.NUMBER_YEAR_MONTH_DAY_OPTION,
        "2020 February 29": UserSettingsScreenPageLocators.YEAR_LETTER_MONTH_DAY_OPTION
    }

    date_time_format_pattern = {
        # time format patterns
        "13:00": '[0-9]{2}:[0-9]{2}$',
        "1:00 PM": '[0-9]{2}:[0-9]{2} [AP]M$',
        # date format patterns
        'Feb/29/2020': '^[A-Z]{1}[a-z]{2}/[0-9]{2}/[0-9]{4}',
        '2020, 29 February': '^[0-9]{4}, [0-9]{2} [A-Z]{1}[a-z]{2,8}',
        'February 29, 2020': '^[A-Z]{1}[a-z]{2,8} [0-9]{2}, [0-9]{4}',
        '02/29/2020': '^[0-9]{2}/[0-9]{2}/[0-9]{4}',
        '29 February 2020': '^[0-9]{2} [A-Z]{1}[a-z]{2,8} [0-9]{4}',
        '2020/02/29': '^[0-9]{4}/[0-9]{2}/[0-9]{2}',
        '2020 February 29': '^[0-9]{4} [A-Z]{1}[a-z]{2,8} [0-9]{2}'
    }

    time_zone_dictionary = {
        "Belarus": UserSettingsScreenPageLocators.BELARUS_TIME_ZONE,
        "Central Atlantic": UserSettingsScreenPageLocators.ATLANTIC_TIME_ZONE,
        "UTC": UserSettingsScreenPageLocators.UTC_ZONE

    }
