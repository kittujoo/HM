"""
File_Name: delta_pressure_condition_card.py
Desc: This file contains locator objects of the web elements in the flow path settings screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 7/26/2021

"""
from selenium.webdriver.common.by import By


class DeltaPressureSettingsScreenLocators:
    DELTA_PRESSURE_HEADER_LABEL = (By.XPATH, "//div[@class='secondary-panel-header-title' and contains(text(),'Delta Pressure')]")
    DELTA_PRESSURE_TOGGLE = (By.XPATH, "//ics-info-list-item[@id  = 'ispp-id-deltaPressureWarning-toggle']//ics-toggle")

    PRESSURE_READ_BACK_HEADER = (By.XPATH, "//ics-info-list-item[@id ='ispp-id-deltaPressureTolerance-infoListItem']")
    PRESSURE_PICKER_HEADER = (By.XPATH, "//ics-range-picker[@ng-reflect-id= 'ispp-id-deltaPressure-picker']")
    DELTA_PRESSURE_LIST = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-deltaPressure-picker']//div[@class ='wheel-wrapper']//div[2]/ul")
    PRESSURE_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@id ='ispp-id-deltaPressureTolerance-infoListItem']//div[@class = 'info-list-item-subtitle ng-star-inserted']")
    INDICATOR_BAR_STATUS = (By.XPATH, "//ics-condition-card[@id = 'ispp-id-qsm-conditionCard-deltaPressure']//div[@class ='progress-bar']/div")
    DELTA_PRESSURE_READ_BACK_MESSAGE = (By.XPATH, "//ics-condition-card[@id = 'ispp-id-qsm-conditionCard-deltaPressure']//div[@class='condition-card-additional ng-star-inserted']")
    BEFORE_DECIMAL_DELTA_PRESSURE_READ_BACK_MESSAGE = (By.XPATH, "//ics-condition-card[@id = 'ispp-id-qsm-conditionCard-deltaPressure']//div[@class='condition-card-values']//span[2]")
    AFTER_DECIMAL_DELTA_PRESSURE_READ_BACK_MESSAGE = (By.XPATH, "//ics-condition-card[@id = 'ispp-id-qsm-conditionCard-deltaPressure']//div[@class='condition-card-values']//span[3]")
    PRESSURE_UNITS = (By.XPATH, "//ics-condition-card[@id = 'ispp-id-qsm-conditionCard-deltaPressure']//div[@ng-reflect-klass='condition-card-readBackUnits']")
