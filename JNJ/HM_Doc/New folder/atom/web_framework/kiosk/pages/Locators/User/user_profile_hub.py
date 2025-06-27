"""
File_Name: user_profile_hub.py
Desc: This file contains locator object of the web elements in the user profile hub screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 08/18/2021
__modified__ = "Tyler Prada" Tweaks due to UI changes 6/8/22
__modified__ = "Tyler Prada" User Preferences overhaul 9/14/22
__modified__ = "Tyler Prada" added sign out modal locators 9/28/22
__modified__ = "Tyler Prada" Locator adjustments 9/19/23
"""
from selenium.webdriver.common.by import By


class UserProfileHubPageLocators:
    SOUND_TAB = (By.XPATH, "//ics-vertical-scrolling-list-link-item[1]//ics-vertical-scrolling-list-item")
    DATE_AND_TIME_TAB = (By.XPATH, "//ics-vertical-scrolling-list-link-item[1]//ics-vertical-scrolling-list-item")
    DISPLAY = (By.XPATH, "//ics-vertical-scrolling-list-link-item[3]//ics-vertical-scrolling-list-item")
    SCREEN_SAVER = (By.XPATH, "//ics-vertical-scrolling-list-link-item[4]//ics-vertical-scrolling-list-item")
    INSTRUMENT_NAME = (By.XPATH, "//ics-vertical-scrolling-list-link-item[2]//ics-vertical-scrolling-list-item")
    REMOTE_USER = (By.XPATH, "//ics-vertical-scrolling-list-link-item[8]//ics-vertical-scrolling-list-item")
    LOCK_SCREEN = (By.XPATH, "//ics-vertical-scrolling-list-link-item[3]//ics-vertical-scrolling-list-item")

    SIGN_OUT_BUTTON = (By.ID, "ispp-id-user-settings-sign-out-icon")
    SIGN_OUT_CONFIRM = (By.XPATH, "//div[contains(@class,'dialog-action-button')]//ics-action-button")
    SIGN_OUT_CANCEL = (By.XPATH, "//div[contains(@class,'dialog-cancel-button')]//ics-action-button")
    SIGN_OUT_TIMER = (By.XPATH, "//*[local-name()='svg' and @class='ring timer-ring']/*[name()='circle']")

    CANCEL_BUTTON = (By.XPATH,
                     "//div[@class='cdk-global-overlay-wrapper'][1]//ics-primary-action[@class='primary-action-cancel ng-star-inserted']//div[contains("
                     "@class,'tray-container')]")
