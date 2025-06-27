"""
File_Name: column_condition_card.py
Desc: This file contains locator object of the web elements in column condition card
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 05/27/2020
__modified__= "Sharmila Vairamani" changed the locator for column info- 07/29/2020
__modified__ = "Sharmila Vairamani" changed the locator for column position- 10/20/2020
__modified__ = "Sharmila Vairamani" Moved to the column manager folder and changed the class name  03/09/2021
__modified__ = "Sharmila Vairamani" Changed the locator MONITOR_INJECTION_COUNT_INFO - 04/07/2021


"""
from selenium.webdriver.common.by import By


class ColumnSettingsScreenLocators:
    COLUMN_INFO_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-title']//div[contains(text(),'Column')]")
    COLUMN_COLUMN_POSITION = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-cm-command-column-position-settings']//li[1]")
    BYPASS_COLUMN_POSITION = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-cm-command-column-position-settings']//li[2]")
    WASTE_COLUMN_POSITION = (By.XPATH, "//ics-info-list-item[@id='ispp-id-cm-command-column-position-settings']//li[3]")
    INFO_ICON = (By.XPATH,
                 "//ics-tab[@id ='ispp-id-cm-condition-column-user-details-tab']")
    SETTINGS_ICON = (By.ID, "ispp-id-cm-condition-column-user-settings-tab")

    HISTORY_ICON = (By.XPATH,
                    "//ics-tab[@id ='ispp-id-cm-condition-column-user-action-tab']")
    COLUMN_POSITION_INFO = (
        By.XPATH, "//ics-vertical-information-panel[@id='ispp-id-cm-command-column-settings-tab']//li[1]//div[2]//span[1]")
    MONITOR_INJECTION_COUNT_INFO = (
        By.XPATH, "//li[@id='ispp-id-cm-informationPanelItem-columnMonitorInjectionCount']//span[1]")

    MONITOR_INJECTION_COUNT_TAB = (By.ID, "ispp-id-cm-informationPanelItem-columnMonitorInjectionCount")
    TOGGLE_BUTTON = (
        By.XPATH, "//ics-info-list-item[@id='ispp-id-CM-toggle-monitorInjectionCount']//mat-slide-toggle[1]")
    INJECTION_COUNT_ENTRY_FIELD = (By.XPATH,
                                   "//ics-edit-field[@ng-reflect-unique-id='ispp-id-CM-entryField-injectio']//input")
    COLUMN_SETTINGS_HEADER = (By.XPATH, "//div[@class='secondary-panel-header-icon']//mat-icon[@class='mat-icon "
                                        "notranslate mat-icon-no-color']")
    INJECTION_COUNT_EDIT_FIELD_STATE = (
        By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-CM-entryField-injectio']/div")

    COMMENTS_SECTION = (By.XPATH, "//ics-comment-card//div[@class = 'ics-comment-form']//form//textarea")

    INJECTION_WARNING_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id = 'ispp-id-CM-toggle-injectionCountWarning']//ics-toggle")

    INJECTION_ALARM_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id = 'ispp-id-CM-toggle-injectionsAlarm']//ics-toggle")
    MAXIMUM_TEMPERATURE_TAB = (By.XPATH, "//li[@id = 'ispp-id-cm-informationPanelItem-maximumTemperature']/div")
    TEMPERATURE_WARNING_TOGGLE_BUTTON = (By.XPATH, "//ics-info-list-item[@id = 'ispp-id-CM-toggle-setMaximumTemperatureWarning']//ics-toggle")
    TEMPERATURE_SPINNER_COMPONENT_HEADER = (By.XPATH, "//ics-picker-content[@ng-reflect-id ='ispp-id-CM-picker-maximumTempe']")
    MAXIMUM_TEMPERATURE_BUTTON = (By.XPATH, "//ics-picker-button[@ng-reflect-text = '90°C,Maximum']")
    COMMENTS_TAB = (By.XPATH, "//li[@id = 'ispp-id-cm-informationPanelItem-comments']/div")
    MAXIMUM_TEMPERATURE_LIST = (By.XPATH, "//ics-picker-base[@ng-reflect-id = 'ispp-id-CM-picker-maximumTempe']//ul")
    MAX_TEMPERATURE_READ_BACK_MESSAGE = (By.XPATH,
                                         "//ics-info-list-item[@id = 'ispp-id-CM-infoListItem-maximumTemperature']//div[@class= 'info-list-item-subtitle ng-star-inserted']")
    COLUMN_NAME = (By.XPATH, "//div[text()='Column Name']/following-sibling::div")
    READ_ICON = (By.ID, "ispp-id-cm-command-column-details-read")
    INFO_TEXT = (By.XPATH, "//ics-information-card//ics-information-card-item//section[1]")
    INSTRUCTION_HEADER = (By.XPATH, "//ics-information-card//ics-information-card-item//section[2]")
    INSTRUCTION_ONE = (By.XPATH, "//ics-information-card//ics-information-card-item//ol/li[1]")
    INSTRUCTION_TWO = (By.XPATH, "//ics-information-card//ics-information-card-item//ol/li[2]")


class ColumnInfoScreenLocators:
    COLUMN_POSITION = (By.XPATH, "//li[@id='isppK-id-CM-infoListItem-columnPosotion']//div[2]")
    TOTAL_INJECTION_COUNT = (By.XPATH, "//li[@id='isppK-id-CM-infoListItem-totalInjection']//div[2]")
    TOTAL_SAMPLES_ON_COLUMN = (By.XPATH, "//li[@id='isppK-id-CM-infoListItem-totalSamples']//div[2]")
    TOTAL_SAMPLE_SETS_ON_COLUMN = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-totalSamplesSets']//div[2]")
    MAXIMUM_PRESSURE = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-maximulPressure']//div[2]")
    MAXIMUM_TEMPERATURE = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-maximumTemperature']//div[2]")
    SERIAL_NUMBER = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-serialNumber']//div[2]")
    LOT_NUMBER = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-lotNumber']//div[2]")
    PART_NUMBER = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-partNumber']//div[2]")
    DATE_OF_FIRST_INJECTION = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-dateFirstInjection']//div[2]")
    DATE_OF_LAST_INJECTION = (By.XPATH, "//li[@id='ispp-id-CM-infoListItem-dateLastInjection']//div[2]")


class ColumnHistoryScreenLocators:
    # All the history locators will be maintained here, as of now this page is not developed, so this class is left
    # empty
    pass


class ColumnDetailsLocators:
    COLUMN_NAME_INFO = (By.XPATH, "//div[contains(text(),'Column Name')]/following-sibling::div")
    COLUMN_DESCRIPTION_INFO = (By.XPATH, "//div[contains(text(),'Description')]/following-sibling::div")
    SERIAL_NUMBER_INFO = (By.XPATH, "//div[contains(text(),'Serial')]/following-sibling::div")
    GTIN_INFO = (By.XPATH, "//div[contains(text(),'GTIN')]/following-sibling::div")
    PART_NUMBER = (By.XPATH, "//div[contains(text(),'Number')]/following-sibling::div")
    MAXIMUM_PRESSURE_INFO = (By.XPATH, "//div[contains(text(),'Pressure')]/following-sibling::div")
    MAXIMUN_TEMPERATURE_INFO = (By.XPATH, "//div[contains(text(),'Temperature')]/following-sibling::div")
    LOW_PH_INFO = (By.XPATH, "//div[contains(text(),'Lower')]/following-sibling::div")
    HIGH_PH_INFO = (By.XPATH, "//div[contains(text(),'Higher')]/following-sibling::div")
