"""
File_Name: scan_wavelength_workflow_locators.py
Desc: This file contains locator object of the web elements in the scan wavelength workflow screens
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 09/01/22
__modified__ = "Tyler Prada" added flush option locators and page banner locators 10/7/22
"""
from selenium.webdriver.common.by import By


class ScanWavelengthWelcomeLocators:
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-overview-workflow")
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//p[1]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//p[2]")
    WELCOME_PARAGRAPH_THREE = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//p[3]")
    WELCOME_PARAGRAPH_FOUR = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//ol/li[1]")
    WELCOME_PARAGRAPH_FIVE = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//ol/li[2]")
    WELCOME_PARAGRAPH_SIX = (By.XPATH, "//section[@id ='tuvScanWorkflowWelcomeSection']//p[6]")


class ScanWavelengthSetupLocators:
    MODE_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-mode-workflow")
    SAMPLE_DELIVERY_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-sample-delivery-workflow")
    TOOLS_MATERIALS_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-tools-and-materials-workflow")
    PM_CALIBRATION_TEST = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-scan-mode']//li[1]")
    GENERAL_SAMPLE_SCAN = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-scan-mode']//li[2]")
    CUVETTES_SAMPLE_DELIVERY = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-scan-sample-delivery']//li[1]")
    FLOW_CELL_DELIVERY = (By.XPATH, "//ics-core-selector[@id='ispp-id-tuv-scan-sample-delivery']//li[2]")
    MINI_WAVELENGTH = (By.XPATH, "//div[@class='picker-content']//div[contains(@class,'wheel-date')][1]")
    MAXI_WAVELENGTH = (By.XPATH, "//div[@class='picker-content']//div[contains(@class,'wheel-date')][3]")
    WAVELENGTH_VALUE = (By.XPATH,"//div[@class='picker-content']//div[contains(text(),'192')]")
    SCAN_RATE_PICKER_COMPONENT = (By.XPATH,"//div[@class='picker-content']//div[contains(@class,'wheel-date')][1]")
    SCAN_RATE_PANEL = (By.XPATH, "//ics-info-list-icon[@id='ispp-id-setup-scan-rate-field']//div[contains(text(),'Scan Rate')]")


class PMTestUsingCuvettesLocators:
    LINE_ONE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[1]")
    LINE_TWO = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[2]")
    LINE_THREE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[3]")


class PMTestUsingFlowcellLocators:
    LINE_ONE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[1]")
    LINE_TWO = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[2]")
    LINE_THREE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[3]")
    LINE_FOUR = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[4]")


class SampleScanUsingCuvettes:
    LINE_ONE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[1]")
    LINE_TWO = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[2]")
    LINE_THREE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[3]")


class SampleScanUsingFlowcell:
    LINE_ONE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[1]")
    LINE_TWO = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[2]")
    LINE_THREE = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[3]")
    LINE_FOUR = (By.XPATH, "//ics-information-card-item[@ng-reflect-title='Recommended Materials']//ul/li[4]")


class PreparationLocator:
    PREPARATION_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-preparations-workflow")
    PRECONDITIONS_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-preconditions-blank-scan-workflow")
    LINE_ONE = (By.XPATH, "//div[@class='tuv-scan-preparations-content']//li[1]")
    LINE_TWO = (By.XPATH, "//div[@class='tuv-scan-preparations-content']//li[2]")
    LINE_THREE = (By.XPATH, "//div[@class='tuv-scan-preparations-content']//li[3]")
    CHECK_BOX = (By.XPATH, "//div[@class='tuv-scan-preparations-content']//mat-checkbox")
    LAMP_CONDITION_LABEL = (By.XPATH, "//div[@class='tuv-scan-preconditions-blank-scan-content']//ics-info-list-item[@ng-reflect-title='Lamp']//ics-info-list-item-state/div")
    CUVETTE_CONDITION_LABEL = (By.XPATH, "//div[@class='tuv-scan-preconditions-blank-scan-content']//ics-info-list-item[@ng-reflect-title='Cuvette']//ics-info-list-item-state/div")
    TUV_DOOR_CONDITION_LABEL = (By.XPATH, "//div[@class='tuv-scan-preconditions-blank-scan-content']//ics-info-list-item[@ng-reflect-title='TUV Door']//ics-info-list-item-state/div")
    PRECONDITIONS_CHECK_BOX = (By.XPATH, "//ics-info-list[@class='confirm-info-list']//mat-checkbox" )

class ScanWavelengthFlushOptionLocators:
    FLUSH_DETECTOR_VALUE = (By.XPATH, "//div[@class= 'input-stepper-container']//input")
    FLOW_OPTIONS_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-flush-options-1-workflow")
    SECOND_FLOW_OPTIONS_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-flush-options-2-workflow")
    FLUSH_DETECTOR_TOGGLE = (By.XPATH, "//ics-toggle")
    FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field//input")
    FLUSH_DURATION_STEPPER = (By.XPATH, "//ics-input-stepper")
    FIRST_SOLVENT_SELECTOR_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-flush-options-1-solvent-selector-workflow")
    SECOND_SOLVENT_SELECTOR_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-flush-options-2-solvent-selector-workflow")
    SOLVENT_LINE_A = (By.XPATH, "//mat-radio-group//mat-radio-button[1]")
    SOLVENT_LINE_B = (By.XPATH, "//mat-radio-group//mat-radio-button[2]")
    SOLVENT_LINE_C = (By.XPATH, "//mat-radio-group//mat-radio-button[3]")
    SOLVENT_LINE_D = (By.XPATH, "//mat-radio-group//mat-radio-button[4]")
    DECREMENT_INPUT_STEPPER = (By.XPATH, "//div[@class= 'input-stepper-container']//div[contains(@class,'decrement')]//div")
    INCREMENT_INPUT_STEPPER = (By.XPATH, "//div[@class= 'input-stepper-container']//div[contains(@class,'increment')]//div")
    RESET_STEPPER = (By.XPATH, "//ics-input-stepper-button-reset//mat-icon")

class ScanWavelengthSummaryScreenLocators:
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-tuv-scan-wavelengths-summary-blank-scan-workflow")
    MIN_WAVE_INFO = (By.XPATH,"//div[contains(text(),'Wavelengths Range')]//following-sibling::div")
    SCAN_RATE_INFO = (By.XPATH, "//ics-vertical-scrolling-list[@id='ispp-id-tuv-scan-summary-blank-scan-vertical-list']//ics-info-list-item[2]//div[contains(@class,'info-list-item-subtitle')][1]//div")
    # SCAN_RATE_INFO = (By.XPATH, "//div[contains(text(),' Scan Rate ')]//following-sibling::div//div")
