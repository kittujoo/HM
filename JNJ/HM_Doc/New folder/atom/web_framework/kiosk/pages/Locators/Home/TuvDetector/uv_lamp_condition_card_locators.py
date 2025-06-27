"""
File_Name: uv_lamp_condition_card_locators.py
Desc: This file contains locator object of the web elements in the UV lamp condition card
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22

"""
from selenium.webdriver.common.by import By


class UVLampConditionCardLocators:

    HEADER = (By.XPATH, "//ics-dynamic-component//div[contains(@class,'-title') and contains(text(),'UV Lamp')]")
    ACTIONS_NAV_BUTTON = (By.ID, "ispp-id-tuv-lamp-state-action-tab")
    DETAILS_NAV_BUTTON = (By.ID, "ispp-id-tuv-lamp-state-details-tab")
    SETTINGS_NAV_BUTTON = (By.ID, "ispp-id-tuv-lamp-state-settings-tab")
    CANCEL_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'cancel')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")


class UVLampConditionCardActionsLocators:

    REPLACE_LAMP_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Replace lamp']")


class UVLampConditionCardSettingsLocators:

    SERIAL_NUMBER_INFO_LABEL = (By.XPATH, "//ics-info-list[1]//div[contains(@class,'subtitle')][1]")
    INSTALL_DATE_INFO_LABEL = (By.XPATH, "//ics-info-list[2]//div[contains(@class,'subtitle')][1]")
    LAMP_HOURS_INFO_LABEL = (By.XPATH, "//ics-info-list[3]//div[contains(@class,'subtitle')][1]")
    SUCCESSFUL_IGNITIONS = (By.XPATH, "//ics-info-list[4]//div[contains(@class,'subtitle')][1]")
    FAILED_IGNITIONS = (By.XPATH, "//ics-info-list[5]//div[contains(@class,'subtitle')][1]")
    LIFE_WARNING_TOGGLE = (By.ID, "ispp-id-tuv-lamp-state-lamp-life-warning-toggle")
    LIFE_LIMIT_INFO_LABEL = (By.XPATH, "//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]")


