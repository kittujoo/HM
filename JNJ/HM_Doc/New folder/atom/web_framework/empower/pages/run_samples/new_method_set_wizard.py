from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilities.logger import Logger
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY


class NewMethodSetWizard(WinAppBasePage):
    CREATE_NEW_BUTTON_LOCATOR = (WIN_APP_BY, '5046')
    INSTRUMENT_METHOD_DROPDOWN_LOCATOR = (By.XPATH, "//ComboBox[@AutomationId='4875']")
    NEW_METHOD_SET_INSTRUMENT_BACK_BUTTON_LOCATOR = (WIN_APP_BY, '12323')
    INSTRUMENT_NEXT_BUTTON_LOCATOR = (WIN_APP_BY, '12324')
    INSTRUMENT_FINISH_BUTTON_LOCATOR = (WIN_APP_BY, '12325')

    def __init__(self, driver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)

    def click_create_new_instrument_method(self):
        self.click_on_element(self.CREATE_NEW_BUTTON_LOCATOR)

    def select_instrument_method(self):
        self.click_on_element(self.INSTRUMENT_METHOD_DROPDOWN_LOCATOR)
        ActionChains(self._driver).send_keys(Keys.DOWN).perform()
        ActionChains(self._driver).send_keys(Keys.ENTER).perform()

    def select_default_method(self, processing_method=None, report_method=None, export_method=None):
        methods_to_process = [method for method in [processing_method, report_method, export_method] if method is not None]
        for method in methods_to_process:
            self.click_on_element((By.XPATH, "//ComboBox[@AutomationId='5128']"))
            action = ActionChains(self._driver)
            report_method_item = self.find_element((By.XPATH, f"//ListItem[@Name='{method}']"))
            action.move_to_element(report_method_item)
            action.click()
            action.perform()
        ActionChains(self._driver).send_keys(Keys.ENTER).perform()

    def click_finish(self):
        self.click_on_element(self.INSTRUMENT_FINISH_BUTTON_LOCATOR)

    def click_next(self):
        self.click_on_element(self.INSTRUMENT_NEXT_BUTTON_LOCATOR)

    def confirm_set_method_summary(self):
        self.click_on_element((WIN_APP_BY, '15332'))
