"""
File_Name: sample_manager_home_screen.py
Desc: This file contains specific user action on the elements in the sample pressure settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/5/2021
__modified__ = "Sharmila Vairamani" Added temperature condition card locators - 04/06/2021
__modified__= "Tyler Prada" Added valve position locators 4/9/2021
__modified__ ="Sharmila Vairmani" Added room temperature condition cards - 04/19/2021
__modified__ ="Tyler Prada" Added pagination locator for 2nd page - 04/21/2021
__modified__ ="Tyler Prada" Added injection count condition card locators - 7/11/22
"""

from selenium.webdriver.common.by import By


class SampleManagerHomeScreenLocators:
    HOME_PAGE_TWO = (By.XPATH, "//ul[contains(@class,'pagination-container')]//li[2]//span[@class='page-dot']")

    SAMPLE_PRESSURE_CONDITIONAL_CARD = (By.XPATH, "//div[@class='sample-pressure-container']")
    SAMPLE_PRESSURE_NUMBER_VALUE = (
        By.XPATH, "//ics-condition-card[@id='ispp-id-ftn-sample-pressure']//span[@class='condition-card-firstVal']")
    SAMPLE_PRESSURE_DECIMAL_VALUE = (
        By.XPATH, "//ics-condition-card[@id='ispp-id-ftn-sample-pressure']//span[@class='condition-card-input-second'][2]")
    SAMPLE_PRESSURE_UNIT = (By.XPATH,
                            "//ics-condition-card[@id='ispp-id-ftn-sample-pressure']//div[contains(@class,'readBackUnits')]")

    SAMPLE_TEMPERATURE_CONDITIONAL_CARD = (
        By.XPATH,
        "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[@class='condition-card-information-area']")

    TEMPERATURE_TITLE_ICON = (By.XPATH,
                              "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[@class='condition-card-header-icon']//mat-icon[1]")
    SETPOINT_TEMPERATURE = (
        By.XPATH, "//div[@class='condition-card-values']//div[2]//ics-condition-card-input[1]//div[1]//span[2]")
    SETPOINT_TEMPERATURE_AFTER_DECIMAL = (
        By.XPATH, "//div[@class='condition-card-values']//div[2]//ics-condition-card-input[1]//div[1]//span[3]")
    SETPOINT_TEMPERATURE_UNITS = (
        By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[contains(text(),'Setpoint (°C)')]")
    SETPOINT_STATUS = (By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[@class='condition-card-status-area']/div")

    SETPOINT_LOCATOR = (By.XPATH, "//div[@class='condition-card-values']/div[2]/ics-condition-card-input")
    CURRENT_TEMPERATURE = (By.XPATH,
                           "//div[contains(text(),'Current (°C)')]/parent::div//span[@class='condition-card-firstVal']")
    CURRENT_TEMPERATURE_AFTER_DECIMAL = (By.XPATH,
                                         "//div[contains(text(),'Current (°C)')]/parent::div//"
                                         "span[@class='condition-card-input-second'][2]")
    CURRENT_TEMPERATURE_UNITS = (
        By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[contains(text(),'Current (°C)')]")
    STATUS_READ_BACK = (By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-sampleTemperature']//div[contains(@class,'condition-card-footer-status')]")

    PROGRESS_BAR_COMPONENT = (
        By.XPATH,
        "//div[@id ='isppK-id-FTN-conditionCard-sampleTemperature']//div[@class='inner-progress-bar']//div[1]")

    VALVE_POSITION_CONDITIONAL_CARD = (By.XPATH, "//div[@id='isppK-id-FTN-inject-vale-position']")
    DISPLAYED_VALVE_POSITION_CONDITIONAL_CARD = (
        By.XPATH, "//div[@id='isppK-id-FTN-inject-vale-position']//span[@class='condition-card-firstVal']")

    ROOM_TEMPERATURE_CONDITIONAL_CARD = (By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']")
    ROOM_TEMPERATURE_NUMBER_VALUE = (
        By.XPATH, "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//span[@class='condition-card-firstVal']")
    ROOM_TEMPERATURE_DECIMAL_VALUE = (
        By.XPATH,
        "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//span[@class='condition-card-input-second'][2]")
    ROOM_PRESSURE_UNIT = (By.XPATH,
                          "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class='condition-card-readBackUnits units0 ng-star-inserted']")

    CURRENT_POINT = (By.XPATH,
                     "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class='progress-bar']//span[@class='currentPoint']")
    LEFT_POINT = (By.XPATH,
                  "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class='progress-bar']//span[@class='range-margin-left']")
    RIGHT_POINT = (By.XPATH,
                   "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class='progress-bar']//span[@class='range-margin-right']")
    ROOM_TEMPERATURE_READ_BACK_MESSAGE = (By.XPATH,
                                          "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class ='condition-card-footer-status ng-star-inserted']")
    ROOM_TEMPERATURE_TITLE_ICON = (By.XPATH,
                                   "//div[@id='isppK-id-FTN-conditionCard-roomTemperature']//div[@class='condition-card-header-icon']//mat-icon[1]")

    INJECTION_COUNT_CONDITION_CARD = (By.XPATH, "//div[@class='ftn-injection-card-container']")
    INJECTION_COUNT_VALUE = (By.XPATH, "//div[@class='ftn-injection-card-container']//span[@class='condition-card-firstVal']")
    INJECTION_COUNT_THRESHOLD_LABEL = (By.XPATH, "//div[@class='ftn-injection-card-container']//div[contains(@class,'condition-card-footer-status')]")
    AMBIENT_TEMPERATURE_READBACK_MESSAGE = (By.XPATH, "//div[@id = 'isppK-id-FTN-conditionCard-roomTemperature']//div[@class='condition-card-status-area']/div")
