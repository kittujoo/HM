"""
File_Name: channel_common_condition_card.py
Desc: This file contains locator object of the web elements in the setting screen of the channel a conditional card
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/20/2021

"""
from selenium.webdriver.common.by import By


class ChannelSettingScreenLocators:
    SELECTOR_COMPONENT = (By.ID, "ispp-id-tuv-coreSelector-mode")
    HEADER = (By.XPATH, "//div[@class = 'secondary-panel-header-container']//div[contains(text(),'Wavelength')]")
    WAVE_LENGTH_MODE_READ_BACK = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelengthMode']//span["
                                            "@class='readback-units ng-star-inserted']")
    WAVE_LENGTH_1_READ_BACK_VALUE = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelA']//div[contains(@class,'info-list-item-subtitle')]")
    WAVE_LENGTH_1_READ_BACK_UNITS = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength1']//span[2]")
    WAVE_LENGTH_2_READ_BACK_VALUE = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelB']//div[contains(@class,'info-list-item-subtitle')]")
    WAVE_LENGTH_2_READ_BACK_UNITS = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelength2']//span[2]")
    WAVE_LENGTH_MODE_SINGLE_SELECTOR_COMPONENT = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[1]")
    WAVE_LENGTH_MODE_DUAL_SELECTOR_COMPONENT = (
        By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-coreSelector-mode']//li[2]")
    DUAL_WAVE_LENGTH_ENTRY_FIELD_HEADER = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelB']//div[1]")
    SINGLE_WAVE_LENGTH_ENTRY_FIELD_HEADER = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelA']//div[1]")
    DUAL_WAVE_LENGTH_ENTRY_FIELD_LABEL = (By.XPATH, "//mat-label[contains(text(),'Wavelength 2')]")
    SINGLE_WAVE_LENGTH_ENTRY_FIELD_LABEL = (By.XPATH, "//mat-label[contains(text(),'Wavelength 1')]")

    SINGLE_WAVE_LENGTH_ENTRY_FIELD = (
        By.XPATH, "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelA']//div[@class='info-list-item-subtitle ng-star-inserted']")
    DUAL_WAVE_LENGTH_ENTRY_FIELD = (
        By.XPATH,
        "//ics-info-list-icon[@id='ispp-id-TUV-infoListIcon-wavelength-channelB']//div[@class='info-list-item-subtitle ng-star-inserted']")
    WAVELENGTH_LIST = (By.XPATH, "//ics-picker-base//div[@class ='wheel-wrapper']/div[1]//ul")


