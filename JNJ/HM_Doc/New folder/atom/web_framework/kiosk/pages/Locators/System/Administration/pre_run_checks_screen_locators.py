from selenium.webdriver.common.by import By


class PreRunChecksScreenLocators:
    PRE_RUN_CHECKS_MENU = (By.XPATH, "//div[contains(@class,'secondary-panel-header-title') and contains(text(),'Pre-Run Checks')]")

    COLUMN_INSTALLED_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[1]//ics-toggle")
    COLUMN_MATCHES_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[2]//ics-toggle")
    PERFORMANCE_MAINTENANCE_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[3]//ics-toggle")
    SYSTEM_QUALIFIED_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[4]//ics-toggle")
    MOBILE_PHASE_EXPIRED_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[5]//ics-toggle")
    SAMPLE_PLATES_INSTALLED_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[6]//ics-toggle")
    SAMPLE_PLATES_MATCH_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[7]//ics-toggle")
    VIALS_PRESENT_TOGGLE = (By.XPATH, "//ics-vertical-scrolling-list-toggle-item[8]//ics-toggle")
