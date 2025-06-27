from web_framework.web_driver_common.constants import WIN_APP_BY
from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage


class CommonLoginScreen(WinAppBasePage):

    PROJECT_FIELD_LOCATOR = (WIN_APP_BY, '6039')
    USERNAME_FIELD_LOCATOR = (WIN_APP_BY, '6043')
    PASSWORD_FIELD_LOCATOR = (WIN_APP_BY, '6048')

    def __init__(self, driver):
        super().__init__(driver)
        # self._logger = logging.getLogger(self.__class__.__name__)

    def enter_project(self, project_name):
        self.clear_and_set_text(self.PROJECT_FIELD_LOCATOR, project_name)

    def enter_username(self, username):
        self.clear_and_set_text(self.USERNAME_FIELD_LOCATOR, username)

    def enter_password(self, password):
        self.clear_and_set_text(self.PASSWORD_FIELD_LOCATOR, password)
