"""
File_Name: prime_solvents_workflow_locators.py
Desc: This file contains locator object of the web elements in the startup workflow screens
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__ = "Tyler Prada" Initial Check-in 4/25/23
"""
from selenium.webdriver.common.by import By


class PrimeSolventsWorkflowLocators:
    START_PANEL = (By.XPATH, "//ics-modal[@id='ispp-id-setup-solvents-hub']//ics-info-list-item[2]//"
                             "div[contains(@class,'info-list-item-content')]")
    SELECTIONS_BACK = (By.XPATH, "//ics-primary-action")
    WELCOME_PAGE_BANNER = (By.ID, "ispp-id-prime-solvents-overview-workflow")
    CAUTIONS_PAGE_BANNER = (By.ID, "ispp-id-prime-solvents-cautions-workflow")

    PRIME_SOLVENT_SELECTION_BANNER = (By.XPATH, "//div[@id ='ispp-id-prime-solvents-prime-by-solvent-workflow']//"
                                                "div[contains(text(),'Solvent')]")
    PRIME_SOLVENT_DURATION_BANNER = (By.XPATH, "//div[contains(text(),'Duration ')]")
    PRIME_SOLVENT_ORDER_BANNER = (By.ID, "ispp-id-prime-solvents-prime-by-solvent-arrange-priming-orders-workflow")

    PRIME_COMP_SELECTION_BANNER = (By.XPATH, "//div[@id ='ispp-id-prime-solvents-prime-by-composition-workflow']//"
                                             "div[contains(text(),'Composition')]")
    PRIME_COMP_DURATION_BANNER = (By.XPATH,
                                  "//div[@id ='ispp-id-prime-solvents-prime-by-composition-duration-workflow']//"
                                  "div[contains(text(),'Composition')]")

    FINAL_FLOW_BANNER = (By.ID, "ispp-id-prime-solvents-final-conditions-a-workflow")
    FINAL_COMP_BANNER = (By.ID, "ispp-id-prime-solvents-final-conditions-b-workflow")

    # summary id ispp-id-prime-solvents-summary-workflow

    BACK_BUTTON = (By.XPATH, "//ics-primary-action[@id='navigation-back']")
    START_BUTTON = (By.XPATH, "//div[@class='secondary-panel-footer-actions']//"
                              "ics-primary-action//div[@class='primary-action']")
    CANCEL_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']//"
                               "div[contains(@class,'tray-container')]")
    DONE_BUTTON = (By.XPATH, "//div[@class='primary-action']")
    STEPPER_BUTTON_PLUS = (By.XPATH, "//mat-icon[@data-mat-icon-name='ics-img-increment']/ancestor::ics-input-stepper-button")
    STEPPER_BUTTON_MINUS = (By.XPATH, "//mat-icon[@data-mat-icon-name='ics-img-decrement']/ancestor::ics-input-stepper-button")
    STEPPER_BUTTON_RESET = (By.XPATH, "//mat-icon[@data-mat-icon-name='ics-img-reset']/ancestor::ics-input-stepper-button-reset")


class PrimeSolventsWelcomeScreenLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-prime-solvents-overview//p[1]")
    WELCOME_LIST_PARAGRAPH = (By.XPATH, "//ics-prime-solvents-overview//p[2]")
    WELCOME_PARAGRAPH_TWO = (By.XPATH, "//ics-prime-solvents-overview/div/div[1]/p[3]")
    WELCOME_LIST_FIRST_POINT = (By.XPATH, "//ics-prime-solvents-overview/div/div[1]/ol/li[1]")
    WELCOME_LIST_SECOND_POINT = (By.XPATH, "//ics-prime-solvents-overview/div/div[1]/ol/li[2]")
    WELCOME_LIST_THIRD_POINT = (By.XPATH, "//ics-prime-solvents-overview/div/div[1]/ol/li[3]")
    FIRST_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-item[1]//div[contains(@class, 'description')][1]")
    SECOND_CAUTION_TEXT = (By.XPATH, "//ics-warning-and-caution-item[2]//div[contains(@class, 'description')][1]")


class SolventLinesOptionLocators:
    # selections
    SOLVENT_LINE_TOGGLE = (By.XPATH, "//ics-info-list-item//ics-toggle")
    SOLVENT_LINE_A = (By.XPATH, "//ics-info-list-item[contains(@ng-reflect-title,'Prime Solvent A')][1]//mat-checkbox")
    SOLVENT_LINE_B = (By.XPATH, "//ics-info-list-item[contains(@ng-reflect-title,'Prime Solvent B')][1]//mat-checkbox")
    SOLVENT_LINE_C = (By.XPATH, "//ics-info-list-item[contains(@ng-reflect-title,'Prime Solvent C')][1]//mat-checkbox")
    SOLVENT_LINE_D = (By.XPATH, "//ics-info-list-item[contains(@ng-reflect-title,'Prime Solvent D')][1]//mat-checkbox")

    # duration
    DURATION_FIELD = (By.XPATH, "//input")
    DEFAULT_BUTTON = (By.XPATH, "//ics-action-button")
    PRIMING_STEPPER_COMPONENT = (By.XPATH, "//ics-input-stepper[@ng-reflect-name='primeDurationInputControl']")

    # arrangement


class CompositionOptionLocators:
    # composition
    COMPOSITION_TOGGLE = (By.ID, "ispp-id-prime-by-composition-toggle")
    SOLVENT_LINE_A = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_0']//input")
    SOLVENT_LINE_B = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_1']//input")
    SOLVENT_LINE_C = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_2']//input")
    SOLVENT_LINE_D = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_3']//input")

    # duration
    DURATION_FIELD = (By.XPATH, "//input")
    DEFAULT_BUTTON = (By.XPATH, "//ics-action-button")
    TIME_EDIT_FIELD = (By.XPATH, "//ics-edit-field[@ng-reflect-unique-id ='ispp-id-prime-by-duration-inpu']//input")


class FinalOptionsLocators:
    # flow
    FLOW_RATE_FIELD = (By.XPATH, "//ics-info-list-item[@id='ispp-id-QSM-flow-item1']//input")
    EQ_FIELD = (By.XPATH, "//ics-info-list-item[@id='ispp-id-QSM-flow-rate-item2']//input")
    DEFAULT_BUTTON = (By.XPATH, "//ics-action-button")  # contents of this button change depending on what field above is selected

    # composition
    SOLVENT_LINE_A = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_0']//input")
    SOLVENT_LINE_B = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_1']//input")
    SOLVENT_LINE_C = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_2']//input")
    SOLVENT_LINE_D = (By.XPATH, "//ics-solvent-input[@ng-reflect-input-unique-id='editField_3']//input")


class PrimeSummaryLocators:
    PRIME_BY_LINE_DETAILS = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Prime by Solvent Line']//div[contains(@class,'subtitle')]/div")
    PRIME_BY_COMPOSITION_DETAILS = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Prime by Composition']//div[contains(@class, 'subtitle')]/div")
    FINAL_CONDITION_DETAILS = (By.XPATH, "//ics-info-list-item[@ng-reflect-title = 'Final Conditions']//"
                                         "div[contains(@class, 'subtitle')]")
    PRIME_SUMMARY_HEADER = (By.XPATH, "//div[@id ='ispp-id-prime-solvents-summary-workflow']//div[contains(text(),'Summary')]")
    RESULTS_HEADER = (By.XPATH, "//div[@class ='secondary-panel-workflow-header-content']//div[@class='current step']")
    WORKFLOW_COMPLETE_STATE = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')]/div")
