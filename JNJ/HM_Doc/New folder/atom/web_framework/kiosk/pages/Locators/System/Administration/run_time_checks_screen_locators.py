from selenium.webdriver.common.by import By


class RunTimeChecksScreenLocators:
    RUN_TIME_CHECKS_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Run Time Checks')]")

    MOBILE_PHASE_LOW_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[1]//ics-toggle")
    WASH_SOLVENT_LOW_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[2]//ics-toggle")
    LEAK_DETECTED_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[3]//ics-toggle")
    VIAL_MISSING_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[4]//ics-toggle")

    MOBILE_PHASE_10_PERCENT = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[1]//div[contains(text(),'10%')]")
    WASH_SOLVENT_10_PERCENT = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[2]//div[contains(text(),'10%')]")
