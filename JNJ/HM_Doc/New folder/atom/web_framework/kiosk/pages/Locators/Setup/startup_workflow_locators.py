from selenium.webdriver.common.by import By


class StartupWorkflowLocators:
    WELCOME_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Welcome')]")
    START_BUTTON = (
        By.XPATH, "//div[@class='secondary-panel-footer-actions']//ics-primary-action//div[@class='primary-action']")


class SolventLinesOptionLocators:
    SOLVENT_LINE_A = (By.XPATH,
                      "//ics-info-list-item[@id='ispp-id-instrument-startup-solvent-lines-select-solvent-info-list-item']//li[1]//mat-checkbox")
    SOLVENT_LINE_B = (By.XPATH,
                      "//ics-info-list-item[@id='ispp-id-instrument-startup-solvent-lines-select-solvent-info-list-item']//li[2]//mat-checkbox")

    SOLVENT_LINE_C = (By.XPATH,
                      "//ics-info-list-item[@id='ispp-id-instrument-startup-solvent-lines-select-solvent-info-list-item']//li[3]//mat-checkbox")

    SOLVENT_LINE_D = (By.XPATH,
                      "//ics-info-list-item[@id='ispp-id-instrument-startup-solvent-lines-select-solvent-info-list-item']//li[4]/mat-checkbox")


class StartupWelcomeLocators:
    WELCOME_PARAGRAPH_ONE = (By.XPATH, "//ics-instrument-startup-overview//div/p[1]")
    WELCOME_LIST_PARAGRAPH = (By.XPATH, "//ics-instrument-startup-overview/div/div[1]/div[1]/div")
    WELCOME_LIST_FIRST_POINT = (By.XPATH, "//ics-instrument-startup-overview//div//ul//li[1]")
    WELCOME_LIST_SECOND_POINT = (By.XPATH, "//ics-instrument-startup-overview//div//ul//li[2]")
    WELCOME_LIST_THIRD_POINT = (By.XPATH, "//ics-instrument-startup-overview//div//ul//li[3]")
    RECOMMENDATION_TEXT = (By.XPATH, "//div[@class='information-card-description']")


class StartupPrimeSolventsLocators:
    PRIME_SOLVENTS_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Prime Solvents')]")
    PRIMING_DURATION_STEPPER = (By.XPATH, "//ics-input-stepper[@ng-reflect-name='primingDuration']")
    PRIMING_DURATION_FIELD = (By.XPATH, "//input[@type='text']")


class StartupAdditionalPrimeSolventsLocators:
    SEAL_WASH_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-seal-wash")
    METERING_PUMP_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-sample-metering-pump")
    METERING_PUMP_PAGE_SOLVENT_A = (By.ID, "editField_0")
    NEEDLE_WASH_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-needle-wash")
    PRIME_TOGGLE = (By.XPATH, "//div[@class='ics-toggle']//mat-slide-toggle")
    PRIME_NEEDLE_TOGGLE = (By.XPATH, "//*[@id='ispp-id-instrument-startup-needle-wash-toggle']//mat-slide-toggle")
    PRIME_SAMPLE_METERING_TOGGLE = (By.XPATH, "//*[@id='ispp-id-instrument-startup-sample-metering-pump-toggle']//mat-slide-toggle")
    PRIME_NEEDLE_STEPPER = (By.XPATH, "//ics-input-stepper[@ng-reflect-id='ispp-id-prime-needle-wash-step']")
    PRIME_SAMPLE_METERING_STEPPER = (By.XPATH, "//ics-input-stepper[@formcontrolname='sampleMeteringPumpValue']")
    # There's a typo in the ID it's supposed to say "stepper" but the r is missing, this is purposeful for now
    PRIME_SEAL_STEPPER = (By.XPATH, "//ics-input-stepper[@ng-reflect-id='ispp-id-prime-seal-wash-steppe']//div")


class StartupTemperatureControlLocators:
    TEMPERATURE_CONTROL_PAGE_BANNER = (
        By.ID, "ispp-id-instrument-startup-workflow-temperature-control")
    SAMPLE_TEMPERATURE_TOGGLE = (By.XPATH,
                                 "//ics-toggle[@id='ispp-id-instrument-startup-toggle-sampleTemperature']//mat-slide-toggle")
    SAMPLE_TEMPERATURE_LIST = (
        By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-sam']//div//div//div[1]//ul")
    COLUMN_TEMPERATURE_TOGGLE = (By.XPATH,
                                 "//ics-toggle[@id='ispp-id-instrument-startup-toggle-columnTemperature']//mat-slide-toggle")
    COLUMN_TEMPERATURE_PANEL = (
        By.XPATH, "//section[@formgroupname='columnTemperature']//ics-info-list-icon")
    COLUMN_TEMPERATURE_NUMBER_LIST = (
        By.XPATH, "//ics-picker-base[@ng-reflect-id='ispp-id-instrument-startup-col']//div//div//div[1]//ul")


class StartupDetectorLampLocators:
    DETECTOR_LAMP_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Detector Lamp')]")
    UV_LAMP_TOGGLE = (By.XPATH, "//ics-toggle[@id='ispp-id-instrument-startup-detector-lamp-toggle']//mat-slide-toggle")


class StartupEquilibrationLocators:
    EQUILIBRATION_PAGE_BANNER = (By.XPATH, "//div[@class='current step' and contains(text(),'Equilibration')]")
    EQ_FLOW_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-equilibration-flow")
    EQ_COMPOSITION_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-equilibration-composition")
    EQ_DURATION_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-equilibration-duration")
    FLOW_RATE_TOGGLE = (By.XPATH,
                        "//ics-toggle[@id='ispp-id-instrument-startup-equilibration-flow-toggle']//div[@class='ics-toggle']//mat-slide-toggle")
    FLOW_RATE_FIELD = (By.XPATH, "//ics-edit-field//div[contains(@class,'edit-field')]//input")
    WAIT_MINUTES_STEPPER = (By.XPATH, "//ics-input-stepper[@id='ispp-id-equilibration-duration-minutes-stepper']")
    EQUILIBRATE_TOGGLE_BUTTON = (By.XPATH, "//*[@id='ispp-id-instrument-startup-equilibration-duration-toggle']//mat-slide-toggle")


class StartupSummaryLocators:
    SUMMARY_PAGE_BANNER = (By.ID, "ispp-id-instrument-startup-workflow-summary")
    STARTUP_PROGRESS_BANNER = (By.XPATH,
                               "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]//div[contains(text(),'In progress')]")
    STARTUP_COMPLETE_BANNER = (By.XPATH,
                               "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]//div[contains(text(),'Complete')]")
    WORKFLOW_STOPPED_UNEXPECTEDLY = (By.XPATH, "//div[contains(text(),'Workflow stopped')]")
    STATUS_LABEL = (By.XPATH, "//ics-progressing-info-list-item//div[contains(@class,'subtitle')][1]")
    STOP_BUTTON = (By.XPATH, "//div[contains(@class,'secondary')]//ics-primary-action")

    PRIME_MOBILE_PHASE_SOLVENTS = (
        By.XPATH, "//div[contains(text(),'Prime Mobile Phase Solvents')]/parent::div//div[@class='ng-star-inserted']")
    MOBILE_PHASE_PRIME_DURATION = (
        By.XPATH,
        "//ics-info-list-item[@ng-reflect-title='Mobile Phase Prime Duration']//div[@class='ng-star-inserted']")
    PRIME_SEAL_WASH = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Prime Seal Wash']//div[@class='ng-star-inserted']")
    PRIME_NEEDLE_WASH = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Prime Needle Wash']//div[@class='ng-star-inserted']")
    SAMPLE_METER_PUMP = (
        By.XPATH,
        "//ics-info-list-item[@ng-reflect-title='Prime Sample Metering Pump']//div[@class='ng-star-inserted']")
    SAMPLE_METER_PUMP_COMPOSITION = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Composition']//div[@class='ng-star-inserted']")
    SAMPLE_TEMPERATURE = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Sample Temperature']//div[@class='ng-star-inserted']")
    COLUMN_TEMPERATURE = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Column Temperature']//div[@class='ng-star-inserted']")
    LAMP_CONTROL = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Lamp Control']//div[@class='ng-star-inserted']")
    SET_FINAL_CONDITIONS = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Set Final Conditions']//div[@class='ng-star-inserted']")
    EQUILIBRATION_COMPOSITION = (
        By.XPATH, "//ics-info-list-item[@ng-reflect-title='Equilibration Composition']//div[@class='ng-star-inserted']")
    EQUILIBRATE = (By.XPATH, "//ics-info-list-item[@ng-reflect-title='Equilibrate']//div[@class='ng-star-inserted']")
