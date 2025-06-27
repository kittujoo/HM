from selenium.webdriver.common.by import By


class SetupScreenLocators:
    SETUP_HEADER = (By.XPATH, "//div[contains(@class,'expansion-panel-container')]/div[1]")
    STARTUP_WORKFLOW_START = (By.XPATH, "//ics-info-list-item[1]//div[contains(@class,'info-list-item-content')]")
    SHUTDOWN_WORKFLOW_START = (By.XPATH, "//ics-info-list-item[@ng-reflect-title ='Shutdown']/div")
    STARTUP_INS_ACQUISITION = (By.XPATH,
                               '//ics-info-list-item//div[@class="info-list-item"]/div[contains(text(),"Startup")]')
    SOLVENTS_PANEL = (By.XPATH, "//ics-info-list-item[2]//div[contains(@class,'info-list-item-content')]")
