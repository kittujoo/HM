"""
File_Name: system_logs_screen_locators.py
Desc: This file contains locator object of the web elements in system log screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 0/0/22

"""
from selenium.webdriver.common.by import By


class SystemLogsScreenLocators:
    HEADER = (By.XPATH, "//ics-dynamic-component//div[contains(@class,'-title') and contains(text(),'Logs')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'back')]//div[@class='tray-icon-circle available']/mat-icon")
    TOP_BACK_BUTTON = (By.XPATH, "//div[contains(@class, 'secondary-panel-header-back')]")
    LOG_TABLE = (By.XPATH, "//ics-table")
    LOG_TABLE_ROW = (By.XPATH, "//div[@class='table scroll']//ul[contains(@class,'row')]")
    LOG_TABLE_COLUMN = (By.XPATH, "//ul[contains(@class,'table-row odd') or contains(@class, 'table-row even')]/descendant::li[contains(@class, "
                                  "'table-column')]")
    FIRST_LOG_ENTRY = (By.XPATH, "//ul[contains(@class,'table-row odd') or contains(@class, 'table-row even')][1]")
    LAST_ENTRY = (By.XPATH, "//ul[contains(@class,'table-row odd') or contains(@class, 'table-row even')][last()]")
    ERROR_ENTRY = (By.XPATH, "//div[text()=' Error / device ']")
    ERROR_ROW = (By.XPATH, "//div[text()=' Error / device ']/ancestor::ul")

    TODAY_FILTER_BUTTON = (By.XPATH, "//ics-core-selector//li[1]")
    PAST48HR_FILTER_BUTTON = (By.XPATH, "//ics-core-selector//li[2]")
    WEEK_FILTER_BUTTON = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-date-range-']//ul//li[2]")
    MONTH_FILTER_BUTTON = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-date-range-']//ul//li[3]")
    ALL_FILTER_BUTTON = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-date-range-']//ul//li[4]")
    RANGE_FILTER_LABEL = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-log-filter-date-range-list-item']//div[@class='info-list-item']/div[2]")
    CONTENT_FILTER_LABEL = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-log-filter-content-list-item']//div[@class='info-list-item']/div[2]")

    ADD_ENTRY_BUTTON = (By.ID, "ispp-id-logs-action-bar-add-entry-tab")
    REFRESH_BUTTON = (By.ID, "ispp-id-logs-action-bar-refresh-tab")
    FILTER_BUTTON = (By.ID, "ispp-id-logs-action-bar-filter-tab")
    DATE_TAB = (By.XPATH, "//ics-info-list-icon[@ng-reflect-title ='Date Range']//div[@class='info-list-item-body']")
    CONTENT_TAB = (By.XPATH, "//ics-info-list-icon[@ng-reflect-title ='Content']//div[@class='info-list-item-body']")
    NEXT_PAGE = (By.XPATH, "//ics-primary-action[@id='ispp-id-navigation-next']")
    BACK_PAGE = (By.XPATH, "//ics-primary-action[@id='ispp-id-navigation-back']")
    BACK_PAGE_AVAILABLE = (By.XPATH, "//ics-primary-action[@id='ispp-id-navigation-back']//div[contains(@class,'tray-icon-circle available')]")
    PAGE_NUMBER = (By.XPATH, "//div[@class='page-identification']")
    MAX_CHAR = (By.XPATH, "//textarea/following-sibling::div")

    ERROR_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-content-pic']//ul//li[3]")
    WARNINGS_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-content-pic']//ul//li[4]")
    INFORMATION_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-content-pic']//ul//li[5]")
    ALL_OPTION = (By.XPATH, "//ics-picker-base[@ng-reflect-id ='ispp-id-log-filter-content-pic']//ul//li[2]")

    PUMP_MODULE = (By.ID, "ispp-id-log-filter-module-pump-checkbox")
    AUTO_SAMPLER_MODULE = (By.ID, "ispp-id-log-filter-module-autosampler-checkbox")
    COLUMN_MODULE = (By.ID, "ispp-id-log-filter-module-column-checkbox")
    DETECTOR_MODULE = (By.ID, "ispp-id-log-filter-module-detector-checkbox")

    """
    The locators for the elements in add log entry tab
    """
    ADD_ENTRY_HEADER = (By.XPATH, "//ics-dynamic-component//div[contains(@class,'-title') and contains(text(),'New Log')]")
    ADD_ENTRY_TEXT_AREA = (By.XPATH, "//textarea[contains(@class, 'comment-area')]")

    """
    The locators for the elements in log details screen
    """
    LOG_DETAIL_DATE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-log-details-infoListItem-date']/descendant::div[contains(@class, "
                                 "'info-list-item-subtitle ')]")
    LOG_DETAIL_CATEGORY = (By.XPATH, "//ics-info-list-item[@id='ispp-id-log-details-infoListItem-category']/descendant::div[contains(@class, "
                                     "'info-list-item-subtitle ')]")
    LOG_DETAIL_SOURCE = (By.XPATH, "//ics-info-list-item[@id='ispp-id-log-details-infoListItem-source']/descendant::div[contains(@class, "
                                   "'info-list-item-subtitle ')]")
    LOG_ENTRY_DETAILS = (By.XPATH, "//ics-info-list-item[@id='ispp-id-log-details-infoListItem-details']/descendant::div[contains(@class, "
                                   "'info-list-item-subtitle ')]")
    LOG_BACK_BUTTON = (By.XPATH, "//div[4]/div/mat-dialog-container[contains(@id,'mat-dialog-')]//descendant::div[contains(@class, "
                                 "'secondary-panel-header-')]/ics-primary-action")
