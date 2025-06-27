"""
File_Name: shutdown_workflow_locators.py
Desc: This file contains locator object of the web elements in the shutdown workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "sharmla vairamani" Initial Check-in 10/13/2022
"""
from selenium.webdriver.common.by import By


class ShutdownWorkflowLocators:
    SAMPLE_TEMPERATURE_LIST = (By.XPATH,
                               "//ics-picker-wrapper[@ng-reflect-title='Sample Temperature']//div[contains(@class,'wheel-wrapper')][1]//div/ul")
    TOGGLE_BUTTON_STATE = (By.XPATH, "//ics-toggle")
    TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item//ics-toggle")
    COLUMN_TOGGLE_BUTTON_STATE = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Set Column Temperature']//ics-toggle")
    COLUMN_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Set Column Temperature']//ics-toggle")
    FLOW_TOGGLE_BUTTON_STATE = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Set Flow Rate']//ics-toggle")
    FLOW_TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Set Flow Rate']//ics-toggle//mat-slide-toggle")
    SAMPLE_TEMPERATURE_FIVE = (By.XPATH,
                               "//ics-picker-wrapper[@ng-reflect-title='Sample Temperature']//div[contains(@class,'wheel-wrapper')][1]//div/ul//li[2]")
    COLUMN_TEMPERATURE_LIST = (By.XPATH,
                               "//ics-picker-wrapper[@ng-reflect-title='Column Temperature']//div[contains(@class,'wheel-wrapper')][1]//div/ul")
    COLUMN_TEMPERATURE_FIVE = (By.XPATH,
                               "//ics-picker-wrapper[@ng-reflect-title='Column Temperature']//div[contains(@class,'wheel-wrapper')][1]//div/ul//li[2]")

    FLOW_RATE_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-instrument-basic-shutd']//input")
    LAMP_TOGGLE_BUTTON = (By.XPATH, "//ics-toggle[@ng-reflect-name='lampControlModeToggle']//mat-slide-toggle")
    SOLVENT_A = (By.XPATH, "//ics-solvent-entry[@ng-reflect-unique-id='editField_0']//input")
    SOLVENT_B = (By.XPATH, "//ics-solvent-entry[@ng-reflect-unique-id='editField_1']//input")
    SOLVENT_C = (By.XPATH, "//ics-solvent-entry[@ng-reflect-unique-id='editField_2']//input")
    SOLVENT_D = (By.XPATH, "//ics-solvent-entry[@ng-reflect-unique-id='editField_3']//input")
    COLUMN_TEMPERATURE_HEADER = (
        By.XPATH,
        "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-column-temperature']//div[@class='current step']")
    SAMPLE_TEMPERATURE_HEADER = (
        By.XPATH,
        "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-sample-temperature']//div[@class='current step']")
    LAMP_HEADER = (
        By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-lamp-control']//div[@class='current step']")
    SUMMARY_HEADER = (
        By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-summary']//div[@class='current step']")
    FLOW_RATE_HEADER = (
        By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-flow-control']//div[@class='current step']")
    SOLVENT_HEADER = (
        By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-composition']//div[@class='current step']")
    WELCOME_HEADER = (
        By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-welcome']//div[@class='current step']")

    COLUMN_TEMPERATURE_INFO = (By.XPATH,
                               "//ics-vertical-scrolling-list-item[2]//div[@class='content']//div[2]")

    SAMPLE_TEMPERATURE_INFO = (By.XPATH,
                               "//ics-vertical-scrolling-list-item[1]//div[@class='content']//div[2]")

    LAMP_INFO = (By.XPATH,
                 "//ics-vertical-scrolling-list-item[5]//div[@class='content']//div[2]")
    LAMP_INFO_OFF = (By.XPATH, "//ics-vertical-scrolling-list-item[4]//div[@class='content']//div[2]")

    FLOW_RATE_INFO = (By.XPATH,
                      "//ics-vertical-scrolling-list-item[3]//div[@class='content']//div[2]")

    SOLVENT_INFO = (By.XPATH,
                    "//ics-vertical-scrolling-list-item[4]//div[@class='content']//div[2]")

    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-instrument-basic-shutdown-welcome//p[1]")

    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//ics-instrument-basic-shutdown-welcome//p[2]")
    WELCOME_PARAGRAPH_THREE = (By.XPATH, "//ics-instrument-basic-shutdown-welcome//p[contains(text(),'Tap')]")
    WORKFLOW_COMPLETE_STATE = (By.XPATH, "//ics-progressing-info-list[@id ='ispp-id-instrument-basic-shutdown-status-progressing-info-list']//div[contains(@class,'subtitle')]/div")

    STATUS_HEADER = (By.XPATH, "//div[@id ='ispp-id-instrument-basic-shutdown-workflow-status']//div[@class ='current step']")
    FLOW_EDIT_FIELD_STATE = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-instrument-basic-shutd']/div")
