from selenium.webdriver.common.by import By


class SolventManagerHomeScreenLocators:
    ### --- Main locators (All Pages) --- ###
    HOME_PAGE_ONE = (By.XPATH, "//li[1]//span[@class='page-dot']")
    HOME_PAGE_TWO = (By.XPATH, "//li[2]//span[@class='page-dot']")
    HOME_PAGE_THREE = (By.XPATH, "//li[3]//span[@class='page-dot']")

    ### --- Page One Locators --- ###
    FLOW_CONDITIONAL_CARD = (By.XPATH,
                             "//ics-condition-card[@id='ispp-id-qsm-conditionCard-flowRate']//div[@class='condition-card-information-area']")
    FLOW_RATE = (By.XPATH, "//ics-condition-card[@id='ispp-id-qsm-conditionCard-flowRate']//ics-condition-card-input")
    OFF_READ_BACK_MESSAGE = (By.XPATH, "//span[contains(text(),'OFF')]")
    FLOW_RATE_UNITS = (By.XPATH,
                       "//ics-condition-card[@id='ispp-id-qsm-conditionCard-flowRate']//div[contains(@class,'condition-card-readBackUnits')]")

    SYSTEM_PRESSURE_CARD = (By.XPATH, "//ics-condition-card[@id='ispp-id-qsm-pump-pressure']//div[@class='condition-card-information-area']")
    SYSTEM_PRESSURE_CARD_UNIT = (By.XPATH, "//ics-condition-card[@id='ispp-id-qsm-pump-pressure']//div[contains(@class,'readBackUnits')]")
    SYSTEM_PRESSURE_CARD_NUMBER_VALUE = (
        By.XPATH, "//div[@id='isppK-id-PUMP-pressure-condition']//ics-condition-card-input//span[@class='condition-card-firstVal']")
    SYSTEM_PRESSURE_CARD_DECIMAL_VALUE = (By.XPATH,
                                          "//div[@id='isppK-id-PUMP-pressure-condition']"
                                          "//ics-condition-card-input//span[@class='condition-card-input-second'][2]")

    DELTA_PRESSURE_CONDITION_CARD = (By.XPATH, "//div[@id='isppK-id-ftn-conditionCard-deltaPressure']")
    DELTA_PRESSURE_RANGE_LABEL = (By.XPATH, "//div[contains(@class,'condition-card-additional')]")

    SOLVENT_COMPOSITION_CONDITION_CARD = (By.XPATH, "//div[@class='solvent-composition-condition-card']")
    SOLVENT_A_COMPOSITION_BEFORE_DECIMAL_VALUE = (By.XPATH,
                                                  "//div[@id='isppK-id-ftn-conditionCard-solventComposition']"
                                                  "//div[@class='condition-card-values']/div[1]//span[2]")
    SOLVENT_A_COMPOSITION_AFTER_DECIMAL_VALUE = (By.XPATH,
                                                 "//div[@id='isppK-id-ftn-conditionCard-solventComposition']"
                                                 "//div[@class='condition-card-values']/div[1]//span[3]")
    SOLVENT_B_COMPOSITION_BEFORE_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[2]//span[2]")
    SOLVENT_B_COMPOSITION_AFTER_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[2]//span[3]")
    SOLVENT_C_COMPOSITION_BEFORE_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[3]//span[2]")
    SOLVENT_C_COMPOSITION_AFTER_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[3]//span[3]")
    SOLVENT_D_COMPOSITION_BEFORE_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[4]//span[2]")
    SOLVENT_D_COMPOSITION_AFTER_DECIMAL_VALUE = (By.XPATH, "//div[@class='condition-card-values']/div[4]//span[3]")
    SOLVENT_A_LINE = (By.XPATH,
                      "//div[@id='isppK-id-ftn-conditionCard-solventComposition']//div[@class='condition-card-values']"
                      "/div[1]//div[contains(@class,'condition-card-readBackUnits')]")
    SOLVENT_B_LINE = (By.XPATH,
                      "//div[@id='isppK-id-ftn-conditionCard-solventComposition']//div[@class='condition-card-values']"
                      "/div[2]//div[contains(@class,'condition-card-readBackUnits')]")
    SOLVENT_C_LINE = (By.XPATH,
                      "//div[@id='isppK-id-ftn-conditionCard-solventComposition']//div[@class='condition-card-values']"
                      "/div[3]//div[contains(@class,'condition-card-readBackUnits')]")
    SOLVENT_D_LINE = (By.XPATH,
                      "//div[@id='isppK-id-ftn-conditionCard-solventComposition']//div[@class='condition-card-values']"
                      "/div[4]//div[contains(@class,'condition-card-readBackUnits')]")
    SOLVENT_A_COLOR = (By.XPATH, "//ics-solvent-indicator[@id='ispp-id-solvent-bottle_0']//span")
    SOLVENT_B_COLOR = (By.XPATH, "//ics-solvent-indicator[@id='ispp-id-solvent-bottle_2']//span")
    SOLVENT_C_COLOR = (By.XPATH, "//ics-solvent-indicator[@id='ispp-id-solvent-bottle_4']//span")
    SOLVENT_D_COLOR = (By.XPATH, "//ics-solvent-indicator[@id='ispp-id-solvent-bottle_6']//span")
    SEAL_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-sealWash']//div[@class='condition-card-header-icon']/div/div")
    NEEDLE_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-needleWash']//div[@class='condition-card-header-icon']/div/div")

    ### --- Page Two Locators --- ###
    MOBILE_PHASE_A_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-solventA")
    MOBILE_PHASE_B_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-solventB")
    MOBILE_PHASE_C_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-solventC")
    MOBILE_PHASE_D_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-solventD")

    MOBILE_PHASE_A_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventA']//div[contains(@class,'custom-header-icon')]")
    MOBILE_PHASE_B_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventB']//div[contains(@class,'custom-header-icon')]")
    MOBILE_PHASE_C_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventC']//div[contains(@class,'custom-header-icon')]")
    MOBILE_PHASE_D_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventD']//div[contains(@class,'custom-header-icon')]")

    MOBILE_PHASE_A_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventA']//div[contains(@class,'condition-card-readBackUnits')]")
    MOBILE_PHASE_B_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventB']//div[contains(@class,'condition-card-readBackUnits')]")
    MOBILE_PHASE_C_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventC']//div[contains(@class,'condition-card-readBackUnits')]")
    MOBILE_PHASE_D_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-solventD']//div[contains(@class,'condition-card-readBackUnits')]")

    ### --- Page Three Locators --- ###
    FLOW_PATH_SCHEMATIC_ICON = (By.XPATH, "//ics-fluidic-path[@class ='fluidic-path']")
    FLOW_PATH_CONDITIONAL_CARD = (By.XPATH, "//div[@id='isppK-id-ftn-conditionCard-flow-path']")
    DISPLAYED_FLOW_PATH = (By.XPATH,
                           "//ics-condition-card[@id='ispp-id-qsm-conditionCard-flowPath']//ics-condition-card-input//span[@class='condition-card-firstVal']")

    VOLUME_PUMP_CONDITION_CARD = (By.ID, "ispp-id-qsm-conditionCard-volume-pumped")
    THRESHOLD_VOLUME_LABEL = (By.XPATH, "//div[contains(@class,'setpoint')]//ics-condition-card-input")
    CURRENT_VOLUME_PUMP = (By.XPATH,
                           "//ics-condition-card[@id='ispp-id-qsm-conditionCard-volume-pumped']"
                           "//div[contains(@class,'readBackValues')]//ics-condition-card-input")
    READ_BACK_MESSAGE = (By.XPATH, "//ics-condition-card[@id='ispp-id-qsm-conditionCard-volume-pumped']//div[contains(@class,'footer')]")

    ### --- Washes Locators --- ###
    MOBILE_PHASE_NEEDLE_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-needleWash")
    MOBILE_PHASE_SEAL_CONDITION_CARD = (By.ID, "isppK-id-qsm-conditionCard-sealWash")

    MOBILE_PHASE_NEEDLE_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-needleWash']//div[contains(@class,'custom-header-icon')]")
    MOBILE_PHASE_SEAL_CARD_COLOR = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-sealWash']//div[contains(@class,'custom-header-icon')]")

    MOBILE_PHASE_NEEDLE_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-needleWash']//div[contains(@class,'condition-card-readBackUnits')]")
    MOBILE_PHASE_SEAL_SECONDARY_LEVEL = (By.XPATH, "//div[@id='isppK-id-qsm-conditionCard-sealWash']//div[contains(@class,'condition-card-readBackUnits')]")
