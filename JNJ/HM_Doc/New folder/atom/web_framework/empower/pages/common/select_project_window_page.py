from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class SelectProjectWindowPage(WinAppBasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_project(self, project_name):
        self._driver.find_element_by_name(project_name).click()
