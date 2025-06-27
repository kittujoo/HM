from selenium.webdriver.common.by import By

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.web_driver_common.constants import WIN_APP_BY


class InstrumentMethodCreationPage(WinAppBasePage):
    OVERWRITE_PAGE_LOCATOR = (By.XPATH, "//Window[@Name='Instrument Method Editor']")
    METHOD_NAME_INPUT_LOCATOR = (By.XPATH, "//Edit[@AutomationId='6188']")
    METHOD_COMMENT_INPUT_LOCATOR = (WIN_APP_BY, '7709')
    DIALOG_SAVE_BUTTON_LOCATOR = (WIN_APP_BY, '6189')
    DIALOG_OPEN_BUTTON_LOCATOR = (By.NAME, 'Open')
    UNSAVED_CHANGES_DIALOG_NO_BUTTON_LOCATOR = (WIN_APP_BY, '7')
    DISCARD_DIALOG_WINDOW_LOCATOR = (By.XPATH, "//Text[contains(@Name, 'Discard your changes')]")
    SAVE_DIALOG_WINDOW_LOCATOR = (By.XPATH, "//Text[contains(@Name, 'Save changes to')]")
    METHOD_LOCKED_BY_ADMIN_LOCATOR = (By.XPATH, '//*[contains(@Name, "currently being edited by System/Administrator")]')

    def __init__(self, driver):
        super().__init__(driver)
        # self._logger = logging.getLogger(self.__class__.__name__)

    def set_method_name(self, method_name):
        self.set_text(self.METHOD_NAME_INPUT_LOCATOR, method_name)

    def set_method_comment(self, method_comment):
        self.set_text(self.METHOD_COMMENT_INPUT_LOCATOR, method_comment)

    def click_dialog_save_button(self):
        self.click_on_element(self.DIALOG_SAVE_BUTTON_LOCATOR)

    def click_dialog_open_button(self):
        self.click_on_element(self.DIALOG_OPEN_BUTTON_LOCATOR)

    def click_unsaved_changes_dialog_no_button(self):
        self.click_on_element(self.UNSAVED_CHANGES_DIALOG_NO_BUTTON_LOCATOR)

    def is_cannot_save_method_dialog_opened(self):
        return self.is_displayed_with_timeout(3, self.METHOD_LOCKED_BY_ADMIN_LOCATOR)

    def close_unsaved_changes_dialog(self):
        self.click_unsaved_changes_dialog_no_button()

    def is_overwrite_dialog_opened(self) -> bool:
        return self.is_displayed_with_timeout(3, self.OVERWRITE_PAGE_LOCATOR)

    def is_save_dialog_displayed(self) -> bool:
        return self.is_displayed_with_timeout(5, self.SAVE_DIALOG_WINDOW_LOCATOR)

    def is_discard_dialog_displayed(self) -> bool:
        return self.is_displayed_with_timeout(5, self.DISCARD_DIALOG_WINDOW_LOCATOR)
