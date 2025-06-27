"""
File_Name: user_settings_screen_locators.py
Desc: This file contains locator object of the web elements in the user settings screen
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 10/20/2020
__modified__ = "Sharmila Vairamani" Added all the locators in the tab - 12/09/2020
__modified__ = "Tyler Prada" added locators for screensaver and datetime 06/30/2021
__modified__ = "Tyler Prada" modified user settings header locator 7/16/2021
__modified__ = "Sharmila Vairamani" Moving it to different folder
__modified__ = "Tyler Prada" Update to locators for date&time related elements and various UI changes 6/8/22
__modified__ = "Tyler Prada" User Preferences overhaul 9/14/22
__modified__ = "Tyler Prada" added instrument text area locator 9/28/22
__modified__ = "Tyler Prada" Locator adjustments 9/19/23
"""
from selenium.webdriver.common.by import By


class UserSettingsScreenPageLocators:
    """
    The locators for the elements under the sound settings preference tab
    """

    VOLUME_UP = (By.ID, "ispp-id-baseSlider-right-icon")
    SOUND_PREFERENCE_SETTINGS_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']/li[1]")
    SOUND_PREFERENCE_SETTINGS_HEADER = (By.ID, "ispp-id-userSettings-volumeSettings")
    MUTE_VOLUME_SETTINGS = (By.XPATH, "//mat-icon[@id ='ispp-id-baseSlider-left-icon']")
    HIGH_VOLUME_SETTINGS = (By.XPATH, "//mat-icon[@id ='ispp-id-baseSlider-right-icon']")
    LOW_VOLUME_SETTINGS = (By.XPATH, "//div[@class='mat-slider-ticks-container']/div[@class='mat-slider-ticks']")
    USER_SETTINGS_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'Preferences')]")
    NEVER_SUPPRESS_SOUND_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[1]")
    FIVE_MINUTE_SUPPRESS_SOUND_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[2]")
    TWENTY_MINUTE_SUPPRESS_SOUND_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[3]")

    """
        The locators for the elements under the screen lock tab
    """

    SCREEN_LOCK_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']/li[5]")
    SCREEN_LOCK_HEADER = (By.ID, "ispp-id-user-lock-settings")
    FIVE_MINUTE_SCREEN_LOCK_OPTION = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-lockSettings-coreSelector-mode']//li[1]")
    FIFTEEN_MINUTE_SCREEN_LOCK_OPTION = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-lockSettings-coreSelector-mode']//li[2]")
    THIRTY_MINUTE_SCREEN_LOCK_OPTION = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-lockSettings-coreSelector-mode']//li[3]")
    ONE_HUNDRED_AND_TWENTY_MINUTE_SCREEN_LOCK_OPTION = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-lockSettings-coreSelector-mode']//li[4]")
    LOCK_SCREEN_DURATION = (By.XPATH, "//ics-vertical-scrolling-list-link-item[3]//ics-vertical-scrolling-list-item//div[3]/div[2]")
    
    """
         The locators for the elements under the theme settings tab
    """

    THEME_SETTINGS_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']/li[3]")
    THEME_SETTINGS_HEADER = (By.ID, "ispp-id-userSettings-selectTheme")
    DARK_THEME_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-themeSettings-coreSelector-mode']//li[1]")
    LIGHT_THEME_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-themeSettings-coreSelector-mode']//li[2]")
    
    """
        The locators for the elements under the date/time settings tab
    """

    DATE_TIME_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'Date and Time')]")
    DATETIME_SETTINGS_TAB = (By.XPATH,
                             "//ul[@class='vertical-panel-menu']/li[2]")
    DATE_FORMAT_PANEL = (By.XPATH, "//ics-info-list-icon//ics-info-list-item[@ng-reflect-title='Set Date Format']")
    SELECT_DATE_PANEL = (By.XPATH, "//ics-info-list-icon//ics-info-list-item[@ng-reflect-title='Select Date']")
    SELECT_MONTH_SPINNER = (By.XPATH, "//ics-picker-base//div[contains(@class,'wheel-date')][1]//ul")
    SELECT_DAY_SPINNER = (By.XPATH, "//ics-picker-base//div[contains(@class,'wheel-date')][2]//ul")
    SELECT_YEAR_SPINNER = (By.XPATH, "//ics-picker-base//div[contains(@class,'wheel-date')][3]//ul")
    DATE_FORMAT_LIST = (By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-system-date-picker']//ul")
    DAY_MONTH_YEAR_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' 29 February 2020 ')]")
    MONTH_DAY_YEAR_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' February 29, 2020 ')]")
    YEAR_DAY_MONTH_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' 2020, 29 February ')]")
    LETTER_MONTH_DAY_YEAR_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' Feb/29/2020 ')]")
    NUMBER_MONTH_DAY_YEAR_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' 02/29/2020 ')]")
    NUMBER_YEAR_MONTH_DAY_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' 2020/02/29 ')]")
    YEAR_LETTER_MONTH_DAY_OPTION = (
        By.XPATH, "//li[contains(@class,'wheel-item')]//div[contains(text(),' 2020 February 29 ')]")
    HOUR_12_FORMAT_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-system-date-time-coreSelector']//li[1]")
    HOUR_24_FORMAT_OPTION = (By.XPATH, "//ics-core-selector[@id='ispp-id-system-date-time-coreSelector']//li[2]")
    TIME_TOGGLE = (By.ID, "ispp-id-userSettings-use24HourFormat-toggle")
    EXAMPLE_DATE_LABEL = (
        By.XPATH, "//ics-info-list-icon//ics-info-list-item[@ng-reflect-title='Set Date Format']//div[contains(@class,'info-list-item-subtitle')][1]")
    EXAMPLE_TIME_LABEL = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-userSettings-use24HourFormat-infoListItem']//div[@class ='info-list-item-subtitle ng-star-inserted']")

    CANCEL_BUTTON = (By.XPATH,"//div[@class='cdk-global-overlay-wrapper'][2]//ics-primary-action[@class='primary-action-cancel ng-star-inserted']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH,"//div[@class='cdk-global-overlay-wrapper'][2]//ics-primary-action[@class='primary-action-done ng-star-inserted']//div[contains(@class,'tray-container')]")
    TIME_ZONE_PICKER = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-system-timeZone-picker']")
    TIME_ZONE_OPTIONS = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-system-timeZone-picker']//li")
    TIME_ZONE_TAB = (By.XPATH, "//ics-info-list-icon[@id = 'ispp-id-userSettings-timeZone-infoListItem']//ics-info-list-item//div[@class='info-list-item-content inline divider-item']")
    TIME_ZONE_PANEL = (By.XPATH, "//ics-info-list-icon//ics-info-list-item[@ng-reflect-title='Select Time Zone']")
    TIME_ZONE_OPTIONS = "//ics-picker-base[@ng-reflect-id = 'ispp-id-system-timeZone-picker']//"
    BELARUS_TIME_ZONE = (By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-system-timeZone-picker']//li[17]/div[1]")
    ATLANTIC_TIME_ZONE = (By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-system-timeZone-picker']//li[20]/div[1]")
    UTC_ZONE = (By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-system-timeZone-picker']//li[24]/div[1]")

    SELECTED_TIME_ZONE_LABEL = (By.XPATH,
                                "//ics-info-list-icon[@id ='ispp-id-userSettings-timeZone-infoListItem']//div[@class='info-list-item-subtitle ng-star-inserted']")

    DATE_FORMAT_PICKER = (By.XPATH, "//div[@id='ispp-id-system-date-picker']//ics-picker-base")

    """
    The locators for the elements the system name settings tab
    """
    INSTRUMENT_NAME_TEXT_AREA = (By.XPATH, "//textarea")
    SYSTEM_NAME_DISPLAY_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-link-item[2]//div[@class='vertical-scrolling-list-item']//div[3]//div[2]")
    SYSTEM_NAME_COMMENT_CARD = (By.XPATH, "//div[@class='ics-comment-form']/form/div")

