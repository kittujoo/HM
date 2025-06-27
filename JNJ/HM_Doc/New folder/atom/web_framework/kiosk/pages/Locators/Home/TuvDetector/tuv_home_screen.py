"""
File_Name: tuv_home_screen.py
Desc: This file contains locator object of the web elements in the TUV home screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved.
__author__    = "Sharmila Vairamani" Initial Check-in 03/25/2021
__modified__ = "Sharmila Vairamani" Added channel A and B condition card locators
__modified__ = "Tyler Prada" added uv lamp and flow cell condition card 11/18/22
"""
from selenium.webdriver.common.by import By


class TUVHomeScreenLocators:
    WAVELENGTH_CONDITIONAL_CARD = (
        By.XPATH, "//div[@id='isppK-id-TUV-wavelength-mode']//div[@class='condition-card-information-area']")
    WAVE_LENGTH_MODE_READ_BACK = (By.XPATH, "//li[@id='ispp-id-tuv-informationPanelItem-wavelengthMode']//span["
                                            "@class='readback-value ng-star-inserted']")
    WAVE_LENGTH_1_READ_BACK_VALUE = (
        By.XPATH,
        "//div[@id='isppK-id-TUV-conditionCard-channelA']//div[@class='condition-card-readBackValues ng-star-inserted'][1]//span[@class='condition-card-firstVal']")
    WAVE_LENGTH_1_READ_BACK_UNITS = (
        By.XPATH,
        "//div[@class='tuv-channel-x-condition-card']//div[@ng-reflect-ng-class='units0']")
    WAVE_LENGTH_2_READ_BACK_VALUE = (By.XPATH,
                                     "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackValues ng-star-inserted'][1]//span[@class='condition-card-firstVal']")

    WAVE_LENGTH_2_READ_BACK_UNITS = (By.XPATH,
                                     "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackUnits units0 ng-star-inserted']")

    WAVELENGTH_CONDITION_CARD_HEADER = (
        By.XPATH, "//div[@class='tuv-channel-x-condition-card ng-star-inserted']//div[@class='condition-card-title']")
    CHANNEL_A_CONDITION_CARD = (By.XPATH, "//div[contains(text(),'Channel A')]")
    CHANNEL_B_CONDITION_CARD = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='tuv-channel-x-condition-card']")
    CHANNEL_A_ABSORBANCE_UNITS = (By.XPATH,
                                  "//div[@id='isppK-id-TUV-conditionCard-channelA']//div[@class='condition-card-readBackUnits units1 ng-star-inserted']")
    CHANNEL_A_ABSORBANCE_VALUE_BEFORE_DECIMAL = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-channelA']//div[@class='condition-card-readBackValues ng-star-inserted'][2]//span[@class='condition-card-firstVal']")

    CHANNEL_B_ABSORBANCE_UNITS = (By.XPATH,
                                  "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackUnits units1 ng-star-inserted']")
    CHANNEL_B_ABSORBANCE_VALUE = (By.XPATH,
                                  "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackValues ng-star-inserted'][2]//span[@class='condition-card-firstVal']")
    CHANNEL_A_ABSORBANCE_VALUE_AFTER_DECIMAL = (By.XPATH,
                                                 "//div[@id='isppK-id-TUV-conditionCard-channelA']//div[@class='condition-card-readBackValues ng-star-inserted'][2]//span[3]")

    CHANNEL_B_ABSORBANCE_VALUE_BEFORE_DECIMAL = (By.XPATH,
                                                 "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackValues ng-star-inserted'][2]//span[@class='condition-card-firstVal']")

    CHANNEL_B_ABSORBANCE_VALUE_AFTER_DECIMAL = (By.XPATH,
                                                "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-readBackValues ng-star-inserted'][2]//span[3]")

    CHANNEL_A_READ_BACK_STATUS = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-channelA']//div[@class='condition-card-status-area']/div[1]")
    CHANNEL_B_READ_BACK_STATUS = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-channelB']//div[@class='condition-card-status-area']/div[1]")
    UV_LAMP_CONDITIONAL_CARD = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-lampState']//div[@class='condition-card-information-area']")
    FLOW_CELL_CONDITIONAL_CARD = (By.XPATH, "//div[@id='isppK-id-TUV-conditionCard-flow-cell']//div[@class='condition-card-information-area']")
    LAMP_READBACK_STATUS = (By.XPATH, "//div[@id ='isppK-id-TUV-conditionCard-lampState']//div[contains(@class, 'footer-status')]")
    LAMP_STATUS_BAR = (By.XPATH, "//*[@id='isppK-id-TUV-conditionCard-lampState']/ics-tuv-lampstate-condition/div/ics-condition-card/div/div[2]/ics-progress-bar/div")
   