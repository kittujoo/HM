from selenium.webdriver.common.by import By


class AboutScreenLocators:
    # Header
    HEADER = (By.XPATH, "//ics-dynamic-component//div[contains(@class,'-title') and contains(text(),'About')]")
    BACK_BUTTON = (By.XPATH, "//ics-primary-action[contains(@class,'back')]")

    # Buttons
    SOFTWARE_BUTTON = (By.ID, "ispp-id-about-system-software-tab")
    HARDWARE_BUTTON = (By.ID, "ispp-id-about-system-hardaware-tab") # Typo
    SUPPORT_BUTTON = (By.ID, "ispp-id-about-system-support-tab")

    # Software
    BUILD_VERSION = (By.XPATH, "//div[@class='info-list-item-subtitle ng-star-inserted']//div[@class='ng-star-inserted']")

    # Hardware
    PRODUCT_MODEL = (By.XPATH,"//*[@id='ispp-id-about-system-productModel']//div[@class='ng-star-inserted']")
    PRODUCT_VARIANT = (By.XPATH,"//*[@id='ispp-id-about-system-productVariant']//div[@class='ng-star-inserted']")
    SERIAL_NUMBER = (By.XPATH,"//*[@id='ispp-id-about-system-sn']//div[@class='ng-star-inserted']")

    # Support
    MANUFACTURER = (By.XPATH, "//ics-info-list-item[@class='manufacturer-item']//div[@class='ng-star-inserted']")
    SUPPORT_WEBSITE = (By.XPATH, "//ics-info-list-item[@ng-reflect-subtitle='help.waters.com']//div[@class='ng-star-inserted']")
    QR_CODE = (By.XPATH, "//div[@class='qr-code']//qrcode")
    QR_LABEL_TITLE = (By.XPATH, "//div[@class='qr-label']//div[@class='title']")
    QR_LABEL_SUBTITLE = (By.XPATH, "//div[@class='qr-label']//div[@class='subtitle']")
