"""
File_Name: flow_cell_condition_card_locators.py
Desc: This file contains locator object of the web elements in the flow cell condition card
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 11/18/22

"""
from selenium.webdriver.common.by import By


class FlowCellConditionCardLocators:

    HEADER = (By.XPATH, "//div[contains(@class,'header')]//ics-dynamic-component//div[contains(@class,'-title') and contains(text(),'Flow Cell')]")
    ACTIONS_NAV_BUTTON = (By.ID, "ispp-id-flow-cell-condition-user-action-tab")
    DETAILS_NAV_BUTTON = (By.ID, "ispp-id-flow-cell-condition-user-details-tab")


class FlowCellConditionCardActionsLocators:

    REPLACE_FLOW_CELL_PANEL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Replace Flow Cell']")


class FlowCellConditionCardDetailsLocators:

    SERIAL_NUMBER_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[1]//div[contains(@class,'description')]")
    CELL_NAME_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[2]//div[contains(@class,'description')]")
    PART_NUMBER_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[3]//div[contains(@class,'description')]")
    VOLUME_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[4]//div[contains(@class,'description')]")
    PART_LENGTH_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[5]//div[contains(@class,'description')]")
    CELL_TYPE_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[6]//div[contains(@class,'description')]")
    PRESSURE_LIMIT_INFO_LABEL = (By.XPATH, "//ics-vertical-scrolling-list-item[7]//div[contains(@class,'description')]")
