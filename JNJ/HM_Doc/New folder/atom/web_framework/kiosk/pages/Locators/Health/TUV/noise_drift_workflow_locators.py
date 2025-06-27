"""
File_Name: noise_drift_workflow_locators.py
Desc: This file contains locator object of the web elements in the noise & drift workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 4/20/22
__modified__ = "Sharmila Vairamani" updates the locators - 6/13/2022

"""
from selenium.webdriver.common.by import By


class NoiseDriftWorkflowLocators:
    WELCOME_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Welcome')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH,
                     "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]//div[@class='primary-action']")
    TUV_DETECTOR_BANNER = (By.XPATH, "//*[contains(text(),'TUV Detector')]")
    NOISE_AND_DRIFT_TEST_BUTTON = (By.XPATH, "//div[contains(text(),'Noise and Drift Test')]")


class NoiseDriftWelcomeLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-tuv-noise-and-drift-test-overview//div[@class='column']//p[1]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//ics-tuv-noise-and-drift-test-overview//div[@class='column']//p[2]")
    WELCOME_PARAGRAPH_THREE = (By.XPATH, "//ics-tuv-noise-and-drift-test-overview//div[@class='column']//p[3]")


class NoiseDriftSetupLocators:
    # flow page
    SETUP_FLOW_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-setup-flow-workflow")
    LAMP_STATE_TOGGLE = (
        By.XPATH, "//ics-toggle[@formcontrolname='lampStateToggle']//div[@class='ics-toggle']/mat-slide-toggle")
    LAMP_STATE = (By.XPATH, "//div[text()=' Lamp state ']/following-sibling::div")
    FLOW_RATE_TOGGLE = (
        By.XPATH, "//ics-toggle[@formcontrolname='flowRateToggle']//div[@class='ics-toggle']/mat-slide-toggle")
    FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id='ispp-id-tuv-noise-and-drift-te']/div")
    FLOW_RATE_DEFAULT_BUTTON = (By.XPATH, "//ics-action-button[@id='ispp-id-settingsKeypad-optionalBtn1']//button")
    RESET_COMPOSITION_BUTTON = (By.XPATH, "//button[@id ='ispp-id-qsmFlowRateCondition-resetCompositionBtn']")
    SOLVENT_A_EDIT_FIELD = (
        By.XPATH,
        "//div[@class='solvent-composition-modal-content-line ng-star-inserted'][1]//ics-edit-field//input")
    SOLVENT_B_EDIT_FIELD = (
        By.XPATH,
        "//div[@class='solvent-composition-modal-content-line ng-star-inserted'][2]//ics-edit-field//input")
    SOLVENT_C_EDIT_FIELD = (
        By.XPATH,
        "//div[@class='solvent-composition-modal-content-line ng-star-inserted'][3]//ics-edit-field//input")
    SOLVENT_D_EDIT_FIELD = (
        By.XPATH,
        "//div[@class='solvent-composition-modal-content-line ng-star-inserted'][4]//ics-edit-field//input")

    SOLVENT_A_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_0']")
    SOLVENT_B_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_1']")
    SOLVENT_C_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_2']")
    SOLVENT_D_LOCK_ICON = (By.XPATH, "//mat-icon[@id='lockIcon_3']")
    SOLVENT_A_LINE_ID = (By.XPATH, "//label[contains(text(),'%A')]")
    SOLVENT_B_LINE_ID = (By.XPATH, "//label[contains(text(),'%B')]")
    SOLVENT_C_LINE_ID = (By.XPATH, "//label[contains(text(),'%C')]")
    SOLVENT_D_LINE_ID = (By.XPATH, "//label[contains(text(),'%D')]")
    # solvent composition page
    SETUP_SOLVENT_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-setup-solvent-composition-workflow")

    # wavelength page
    SETUP_WAVELENGTH_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-setup-wavelength-workflow")
    SINGLE_CHANNEL_OPTION = (By.XPATH, "//ics-core-selector//li[1]")
    DUAL_CHANNEL_OPTION = (By.XPATH, "//ics-core-selector//li[2]")
    CHANNEL_A_PANEL = (By.XPATH,
                       "//ics-info-list-item[contains(@ng-reflect-title,'Channel A')]//div[contains(@class,'info-list-item-content')]")
    CHANNEL_B_PANEL = (By.XPATH,
                       "//ics-info-list-item[contains(@ng-reflect-title,'Channel B')]//div[contains(@class,'info-list-item-content')]")
    WAVELENGTH_PICKER = (
        By.XPATH, "//ics-picker-base[@ng-reflect-id='WavelengthPickerComponent']//div//div//div[4]//div[1]//ul")
    PICKER_DEFAULT_BUTTON = (By.XPATH, "//ics-picker-button")

    # data rate page
    SETUP_DATA_RATE_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-setup-data-rate-workflow")
    DATA_RATE_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[1]//ul")
    FILTER_TOGGLE = (By.XPATH, "//ics-toggle[@formcontrolname='filterToggle']")
    SLOW_FILTER_OPTION = (By.XPATH, "//ics-core-selector[@formcontrolname='filterOption']//li[1]")
    NORMAL_FILTER_OPTION = (By.XPATH, "//ics-core-selector[@formcontrolname='filterOption']//li[2]")
    FAST_FILTER_OPTION = (By.XPATH, "//ics-core-selector[@formcontrolname='filterOption']//li[3]")
    DATA_RATE = (By.XPATH, "//ics-info-list-item[contains(@ng-reflect-title,'Data Rate')]//div[contains(@class,'info-list-item-content')]")
    DATA_RATE_HZ_BANNER = (By.XPATH, "//div[text()=' Hz ']")

    CAUTION_PARAGRAPH_ONE = (By.XPATH, "//ics-information-card-item//div[contains(@class,'description')]//section[1]")
    CAUTION_PARAGRAPH_TWO = (By.XPATH, "//ics-information-card-item//div[contains(@class,'description')]//section[2]")
    CAUTION_PARAGRAPH_THREE = (By.XPATH, "//ics-information-card-item//div[contains(@class,'description')]//section[3]")
    LAMP_READ_BACK_MESSAGE = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Lamp state']//div[contains(@class,'subtitle')][1]")
    FLOW_READ_BACK_MESSAGE = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Set Flow Rate']//div[contains(@class,'subtitle')][1]")
    FLOW_DEFAULT_VALUE_BUTTON = (By.ID, "ispp-id-settingsKeypad-optionalBtn1")
    WAVELENGTH_DEFAULT_BUTTON = (By.XPATH, "//div[@class='content-container']//ics-picker-button/div")
    FILTER_STATE_TOGGLE = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Use Filter']//mat-slide-toggle")


class NoiseDriftSummaryLocators:
    SUMMARY_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-summary-workflow")
    FLOW_RATE_INFO_LABEL = (By.XPATH,
                            "//div[@class='summary-columns-container']//div[contains(@class,'first')]//ics-workflow-summary//li[1]//div[2]")
    COMPOSITION_INFO_LABEL = (By.XPATH,
                              "//div[@class='summary-columns-container']//div[contains(@class,'first')]//ics-workflow-summary//li[2]//div[2]")
    FLOW_CELL_INFO_LABEL = (By.XPATH,
                            "//div[@class='summary-columns-container']//div[contains(@class,'first')]//ics-workflow-summary//li[3]//div[2]")
    DATA_RATE_INFO_LABEL = (By.XPATH,
                            "//div[@class='summary-columns-container']//div[contains(@class,'first')]//ics-workflow-summary//li[4]//div[2]")
    FILTER_INFO_LABEL = (By.XPATH,
                         "//div[@class='summary-columns-container']//div[contains(@class,'first')]//ics-workflow-summary//li[5]//div[2]")
    LAMP_INFO_LABEL = (By.XPATH,
                       "//div[@class='summary-columns-container']//div[contains(@class,'second')]//ics-workflow-summary//li[1]//div[2]")
    WAVELENGTH_A_INFO_LABEL = (By.XPATH,
                               "//div[@class='summary-columns-container']//div[contains(@class,'second')]//ics-workflow-summary//li[2]//div[2]")
    AMBIENT_TEMPERATURE_INFO_LABEL = (By.XPATH,
                                      "//div[@class='summary-columns-container']//div[contains(@class,'second')]//ics-workflow-summary//li[3]//div[2]")
    TEST_TIME_INFO_LABEL = (By.XPATH,
                            "//div[@class='summary-columns-container']//div[contains(@class,'second')]//ics-workflow-summary//li[4]//div[2]")

    STATUS_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-status-workflow")
    WAVELENGTH_B_INFO_LABEL = (By.XPATH, "//div[contains(text(),'Wavelength B')]//following-sibling::div")


class NoiseDriftResultsLocators:
    RESULTS_BANNER = (By.ID, "ispp-id-tuv-noise-and-drift-test-results-workflow")
    DOWN_ARROW_ICON = (By.XPATH,
                       "//ics-collapsible-table[@id='ispp-id-tuv-noise-and-drift-test-collapsible-table']//div[@class='item-icon-position ng-star-inserted']")

    FLOW_RATE_INFO = (By.XPATH, "//div[@class='table scroll']//ul[5]/li[2]//ul/li")
    COMPOSITION_INFO = (By.XPATH, "//div[@class='table scroll']//ul[6]//li[2]//ul//li/div")
    AMBIENT_TEMPERATURE_INFO = (By.XPATH, "//div[@class='table scroll']//ul[8]//li[2]//ul//li/div")
    FLOW_CELL_TYPE_INFO = (By.XPATH, "//div[@class='table scroll']//ul[7]//li[2]//ul//li/div")
    WORKFLOW_STOPPED_BANNER = (By.XPATH, "//div[contains(text(),'Workflow stopped unexpectedly')]")
