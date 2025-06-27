"""
File_Name: mobile_phase_configuration_settings_locators.py
Desc: This file contains locator object of the web elements in the mobile phase configuration setting screen
__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 8/8/22
__modified__ = "Tyler Prada" added prime solvent workflow locators 8/16/22
__modified__ = "Tyler Prada" changed prime solvent panel 12/6/22
__modified__ = "Tyler Prada" Additions/adjustments for mobile phase merge 6/20/23
__modified__ = "Tyler Prada" Added replace solvent & details screen locators 8/31/23
__modified__ = "Tyler Prada" Added needle&seal example sets | locator cleanup 9/7/23
"""
from selenium.webdriver.common.by import By


class MobilePhaseConfigurationSettingsScreenLocators:
    DONE_BUTTON = (
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper'][2]//ics-primary-action[contains(@class,'done')]")
    CANCEL_BUTTON = (
        By.XPATH, "//div[@class='cdk-global-overlay-wrapper'][2]//ics-primary-action[contains(@class,'cancel')]")
    STOP_BUTTON = (By.XPATH, "//ics-secondary-panel-footer//ics-primary-action//ics-tray[@ng-reflect-text='Cancel']"
                             "//div[contains(@class,'tray-container')]")
    DETAILS_BUTTON = (By.XPATH, "//ics-tab[2]")
    SOLVENT_NAME = (By.XPATH, "//ics-solvent-badge-header//div[@class='secondary-panel-header-title']")

    REPLACE_SOLVENT_PANEL = (By.ID, "ispp-id-replace-solvent-info-list-item")
    PRIME_SOLVENT_PANEL = (By.ID, "ispp-id-prime-solvent-info-list-item")
    CONFIGURE_SOLVENT_PANEL = (By.ID, "ispp-id-configure-solvent-info-list-item")
    CONFIGURE_SOLVENT_INFO = (By.XPATH, "//ics-info-list-item[@id='ispp-id-configure-solvent-info-list-item']"
                                        "//div[contains(@class,'subt')][1]")
    VOLUME_SPINNER = (By.XPATH, "//ul[@class='image-picker-wheel-scroll']")
    BOTTLE_TOGGLE_A = (By.XPATH, "//ics-mobile-phase-a-settings-page//ics-toggle")
    BOTTLE_TOGGLE_B = (By.XPATH, "//ics-mobile-phase-b-settings-page//ics-toggle")
    BOTTLE_TOGGLE_C = (By.XPATH, "//ics-mobile-phase-c-settings-page//ics-toggle")
    BOTTLE_TOGGLE_D = (By.XPATH, "//ics-mobile-phase-d-settings-page//ics-toggle")
    MOBILE_PHASE_A_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[1]")
    MOBILE_PHASE_B_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[2]")
    MOBILE_PHASE_C_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[3]")
    MOBILE_PHASE_D_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[4]")
    MOBILE_PHASE_NEEDLE_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[1]")
    MOBILE_PHASE_SEAL_TAB = (By.XPATH, "//ul[@class='vertical-panel-menu']//li[2]")

    SOLVENT_BADGE_A = (By.XPATH, "//li[1]//ics-solvent-badge//div")
    SOLVENT_BADGE_B = (By.XPATH, "//li[2]//ics-solvent-badge//div")
    SOLVENT_BADGE_C = (By.XPATH, "//li[3]//ics-solvent-badge//div")
    SOLVENT_BADGE_D = (By.XPATH, "//li[4]//ics-solvent-badge//div")
    SOLVENT_BADGE_NEEDLE = (By.XPATH, "//li[1]//ics-solvent-badge//div")
    SOLVENT_BADGE_SEAL = (By.XPATH, "//li[2]//ics-solvent-badge//div")
    SOLVENT_A_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventA']//span[@class='condition-card-firstVal']")
    SOLVENT_B_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventB']//span[@class='condition-card-firstVal']")
    SOLVENT_C_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventC']//span[@class='condition-card-firstVal']")
    SOLVENT_D_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventD']//span[@class='condition-card-firstVal']")
    NEEDLE_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-needleWash']//span[@class='condition-card-firstVal']")
    SEAL_NOT_CONFIGURED = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-sealWash']//span[@class='condition-card-firstVal']")
    NEEDLE_WASH_TOGGLE = (By.XPATH, "//ics-needle-wash-solvent-settings-page//ics-toggle")
    SEAL_WASH_TOGGLE = (By.XPATH, "//ics-seal-wash-solvent-settings-page//ics-toggle")

    SOLVENT_BOTTLE_VOLUME_A = (By.ID, "ispp-id-solvent-bottle-size-0")
    SOLVENT_BOTTLE_VOLUME_B = (By.ID, "ispp-id-solvent-bottle-size-1")
    SOLVENT_BOTTLE_VOLUME_C = (By.ID, "ispp-id-solvent-bottle-size-2")
    SOLVENT_BOTTLE_VOLUME_D = (By.ID, "ispp-id-solvent-bottle-size-3")

    BOTTLE_VOLUME_INFO_LABEL = (By.XPATH, "//ics-info-list-item[@id='ispp-id-solvent-bottle-size-0']//div[contains(@class,'subtitle')][1]//div")

    SOLVENT_BOTTLE_2L_OPTION = (By.XPATH, "//ics-picker-wrapper//ul//li[4]")
    SOLVENT_BOTTLE_4L_OPTION = (By.XPATH, "//ics-picker-wrapper//ul//li[5]")
    SOLVENT_BOTTLE_5L_OPTION = (By.XPATH, "//ics-picker-wrapper//ul//li[6]")

    SOLVENT_LINE_COLOR = (By.ID, "ispp-id-solvent-line-color-0")

    # space after color within class selector is intentional, do not remove
    LINE_COLOR_INFO_LABEL_A = (By.XPATH, "//ics-mobile-phase-a-settings-page//ics-info-list-item[contains(@id, 'ispp-id-solvent-line-color')]")
    LINE_COLOR_INFO_LABEL_B = (By.XPATH, "//ics-mobile-phase-b-settings-page//ics-info-list-item[contains(@id, 'ispp-id-solvent-line-color')]")
    LINE_COLOR_INFO_LABEL_C = (By.XPATH, "//ics-mobile-phase-c-settings-page//ics-info-list-item[contains(@id, 'ispp-id-solvent-line-color')]")
    LINE_COLOR_INFO_LABEL_D = (By.XPATH, "//ics-mobile-phase-d-settings-page//ics-info-list-item[contains(@id, 'ispp-id-solvent-line-color')]")

    LINE_COLOR_BLUE = (By.XPATH, "//div[@class='picker-wrapper-content']//"
                                 "div[@id='ispp-id-colorPicker-option-04--v01']")
    LINE_COLOR_RED = (By.XPATH, "//div[@class='picker-wrapper-content']//"
                                "div[@id='ispp-id-colorPicker-option-01--v01']")
    LINE_COLOR_PINK = (By.XPATH, "//div[@class='picker-wrapper-content']//"
                                 "div[@id='ispp-id-colorPicker-option-03--v01']")
    LINK_COLOR_GREEN = (By.XPATH, "//div[@class='picker-wrapper-content']//div[@id='ispp-id-colorPicker-option-06--v01']")
    SELECTED_BOTTLE_A_VOLUME = (
        By.XPATH, "//ics-info-list-item[@id ='ispp-id-solvent-bottle-size-0']//div[contains(text(),'L')]")
    SET_DEFAULT = (By.XPATH, "//ics-picker-button")
    RESET = (By.ID, "ispp-id-dialog-action-button")
    CANCEL_RESET = (By.ID, "ispp-id-dialog-cancel-button")


class PrimeSolventLocators:
    PRIMING_OPTIONS_BANNER = (By.ID, "ispp-id-replace-solvent-priming-options")
    PRIMING_PROGRESS_BANNER = (By.ID, "ispp-id-replace-solvent-priming-results")
    PRIME_DURATION_STEPPER = (By.XPATH, "//ics-input-stepper")
    PRIME_START_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")
    PRIMING_PROGRESS_STATUS_LABEL = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]")
    DONE_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'done')]")
    STOP_INFO_LINE_1 = (By.XPATH, "//ics-modal-info[@id ='ispp-id-workflow-interruption']//section[1]")
    STOP_INFO_LINE_2 = (By.XPATH, "//ics-modal-info[@id ='ispp-id-workflow-interruption']//section[2]")


class ReplaceSolventLocators:
    SOLVENT_LEVEL_PANEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[1]")
    EXPIRATION_PANEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[2]")
    PREPARED_BY_PANEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[3]")
    SOLVENT_NAME_PANEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[4]")
    REPLACE_SOLVENT_CANCEL_BUTTON = (By.XPATH, "//div[contains(@class,'global-overlay')][2]//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-cancel']")

    SOLVENT_NOTE_PANEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[5]")
    SOLVENT_NOTE_INFO_LABEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[5]//div[contains(@class,'subtitle')][1]//div")
    NOTE_DONE_BUTTON = (By.XPATH, "//div[contains(@class,'global-overlay')][3]//ics-primary-action//ics-tray[@ng-reflect-icon='ics-img-done']")

    # Solvent levels
    SOLVENT_LEVEL_SLIDER = (By.XPATH, "//div[@id='currentVolumeContainer']")
    SOLVENT_LEVEL_SLIDER_KNOB = (By.XPATH, "//div[@id='currentVolumeContainer']//div")
    SOLVENT_LEVEL_INFO_LABEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]//div")
    MAX_CHAR = (By.XPATH, "//textarea/following-sibling::div")
    # Empty = 0px
    # 1/8 = 33px
    # 1/4 = 66px
    # 3/8 = 99px
    # 1/2 = 132px
    # 5/8 = 165px
    # 3/4 = 198px
    # 7/8 = 231px
    # Full = 264px

    # Expiration Date
    MONTH_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[1]//ul")
    DAY_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[2]//ul")
    YEAR_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[3]//ul")
    EXPIRY_INFO_LABEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[2]//div[contains(@class,'subtitle')][1]//div")

    # Prepared by
    PREPARED_BY_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[1]//ul")
    PREPARED_BY_ADD_BUTTON = (By.XPATH, "//ics-picker-button[1]")
    PREPARED_BY_REMOVE_BUTTON = (By.XPATH, "//ics-picker-button[2]")
    PREPARED_BY_EDIT_BUTTON = (By.XPATH, "//ics-picker-button[3]")
    PREPARED_BY_INFO_LABEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[3]//div[contains(@class,'subtitle')][1]//div")
    OK_BUTTON = (By.ID, "ispp-id-dialog-action-button")

    # Solvent Name
    SOLVENT_NAME_PICKER = (By.XPATH, "//div[@class='picker']//ics-picker-base//div//div[4]//div[1]//ul")
    SOLVENT_NAME_ADD_BUTTON = (By.XPATH, "//ics-picker-button[1]")
    SOLVENT_NAME_REMOVE_BUTTON = (By.XPATH, "//ics-picker-button[2]")
    SOLVENT_NAME_EDIT_BUTTON = (By.XPATH, "//ics-picker-button[3]")
    SOLVENT_NAME_INFO_LABEL = (By.XPATH, "//ics-replace-solvent-settings//ics-info-list-item[4]//div[contains(@class,'subtitle')][1]//div")


class SolventDetailsLocators:
    SOLVENT_LEVEL_INFO_LABEL = (By.XPATH, "//ics-info-list-item[1]//div[contains(@class,'subtitle')][1]//div")
    EXPIRY_INFO_LABEL = (By.XPATH, "//ics-info-list-item[2]//div[contains(@class,'subtitle')][1]//div")
    PREPARED_BY_INFO_LABEL = (By.XPATH, "//ics-info-list-item[3]//div[contains(@class,'subtitle')][1]//div")
    SOLVENT_NOTE_INFO_LABEL = (By.XPATH, "//ics-info-list-item[4]//div[contains(@class,'subtitle')][1]//div")
