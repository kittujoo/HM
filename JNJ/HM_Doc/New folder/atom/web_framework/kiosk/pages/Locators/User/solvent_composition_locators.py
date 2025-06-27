from selenium.webdriver.common.by import By


class SolventCompositionLocators:

    RESET_COMPOSITION_BUTTON = (By.ID, "ispp-id-qsmFlowRateCondition-resetCompositionBtn")
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
