"""
File_Name: mobile_phase_configuration_settings_locators.py
Desc: This file contains locator object of the web elements in the mobile phase configuration setting screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
"""
from selenium.webdriver.common.by import By


class SolventConfigurationsScreenLocators:
    NEEDLE_WASH_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']/li[1]")
    SEAL_WASH_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']/li[2]")
    NEEDLE_WASH_TOGGLE = (By.XPATH, "//ics-needle-wash-solvent-settings-page//ics-toggle")
    SEAL_WASH_TOGGLE = (By.XPATH, "//ics-seal-wash-solvent-settings-page//ics-toggle")

    NEEDLE_WASH_VOLUME = (By.XPATH, "//ics-needle-wash-solvent-settings-page//ics-info-list-item[@id='ispp-id-solvent-bottle-size-0']")
    SEAL_WASH_VOLUME = (By.XPATH, "//ics-seal-wash-solvent-settings-page//ics-info-list-item[@id='ispp-id-solvent-bottle-size-1']")

    NEEDLE_WASH_COLOR = (By.XPATH, "//ics-needle-wash-solvent-settings-page//ics-info-list-item[contains(@id,'ispp-id-solvent-line-color')]")
    SEAL_WASH_COLOR = (By.XPATH, "//ics-seal-wash-solvent-settings-page//ics-info-list-item[contains(@id,'ispp-id-solvent-line-color')]")

    NEEDLE_WASH_VOLUME_TAG = (By.XPATH,
                              "//ics-needle-wash-solvent-settings-page//ics-info-list-item[@id='ispp-id-solvent-bottle-size-0']//div["
                              "@class='info-list-item-subtitle ng-star-inserted']")
    SEAL_WASH_VOLUME_TAG = (By.XPATH,
                            "//ics-seal-wash-solvent-settings-page//ics-info-list-item[@id='ispp-id-solvent-bottle-size-1']//div["
                            "@class='info-list-item-subtitle ng-star-inserted']")

    NEEDLE_WASH_LINE_COLOR = (By.XPATH, "//ics-vertical-information-panel//li[1]//ics-solvent-badge/div")
    SEAL_WASH_LINE_COLOR = (By.XPATH, "//ics-vertical-information-panel//li[2]//ics-solvent-badge/div")

    SET_DEFAULT = (By.XPATH, "//ics-picker-button")
