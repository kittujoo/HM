from selenium.webdriver.common.by import By

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class ChromatographicSelectionPage(WinAppBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self._logger = logging.getLogger(self.__class__.__name__)

    def is_system_selection_opened(self, timeout=10):
        return self.is_displayed_with_timeout(timeout, (By.NAME, 'Select Desired Chromatography System'))

    def select_system(self, system_name):
        system_item = self._driver.find_element_by_name(system_name)
        system_item.click()
