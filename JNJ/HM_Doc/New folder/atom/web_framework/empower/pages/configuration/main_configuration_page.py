from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class MainConfigurationPage(WinAppBasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # self._logger = logging.getLogger(self.__class__.__name__)

    def click_new_system(self):
        new_system_button = self._driver.find_element_by_name('New System')
        new_system_button.click()
