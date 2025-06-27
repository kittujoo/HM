"""
File_Name: wash_solvents_configuration_settings_screen_locators.py
Desc: This file contains locator objects of the web elements in solvent bottle configuration screen locators
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 12/15/2021

"""
from selenium.webdriver.common.by import By


class WashSolventsConfigurationSettingsScreenLocators:
    NEEDLE_WASH_PANEL = (By.XPATH, "//div[@class='vertical-panel-container']//li[1]")
    NEEDLE_WASH_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-0']")
    NEEDLE_WASH_BOTTLE_VOLUME_INFO = (By.XPATH, "")
    NEEDLE_WASH_LINE_COLOR = (By.XPATH, "//ics-color-picker[@id='ispp-id-wash-solvents-color-picker-0']")

    SEAL_WASH_PANEL = (By.XPATH, "//div[@class='vertical-panel-container']//li[2]")
    SEAL_WASH_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-1']")
    SEAL_WASH_BOTTLE_VOLUME_INFO = (By.XPATH, "")
    SEAL_WASH_LINE_COLOR = (By.XPATH, "//ics-color-picker[@id='ispp-id-wash-solvents-color-picker-1']")

    SAMPLE_METERING_PANEL = (By.XPATH, "//div[@class='vertical-panel-container']//li[2]")
    SAMPLE_METERING_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@id='ispp-id-solvent-bottle-installed-toggle-2']")
    SAMPLE_METERING_BOTTLE_VOLUME_INFO = (By.XPATH, "")
    SAMPLE_METERING_LINE_COLOR = (By.XPATH, "//ics-color-picker[@id='ispp-id-wash-solvents-color-picker-2']")





