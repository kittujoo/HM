from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from utilities.logger import Logger
from utilities.string_utility import str_to_bool
from web_framework.empower.pages.common.file_save_page import FileSavePage, FileSavePageLocators
from web_framework.empower.pages.configuration.instrument_method_creation_page import InstrumentMethodCreationPage
from web_framework.method_editor.pages.method_editor_base_page import MethodEditorBasePage
from web_framework.method_editor.pages.method_editor_left_panel import MethodEditorLeftPanel
from web_framework.web_driver_common.element import is_element_visible, is_element_present


class MethodEditorMainPage(MethodEditorBasePage):
    TOOLBAR_SAVE_BUTTON_LOCATOR = (By.NAME, "Save")
    BELL_ICON_LOCATOR = (By.XPATH, "//Image[@Name='bell icon']")
    BELL_ICON_WITHOUT_ERRORS = (By.XPATH, "//Image[@Name='bell icon']//following-sibling::Text[contains(@Name, 'No Issues')]")
    BELL_ICON_WITH_ERRORS = (By.XPATH, "//Image[@Name='bell icon']//following-sibling::Text[@Name='Issues']")
    ERROR_NOTIFICATION_ELEMENT_LOCATOR = (By.XPATH, "//Image[@Name='bell icon']//following-sibling::Text[@Name='Issues']//following::List//Document")
    METHOD_EDITOR_HEADER_LOCATOR = (By.XPATH, "//Text[@Name='Alliance iS Method Editor']")
    EXPORT_TO_JSON_BUTTON = (By.XPATH, "//Text[@Name='Export to JSON']")
    SEARCH_ICON_LOCATOR = (By.XPATH, "//Image[@Name='search-icon']")
    SEARCH_INPUT_LOCATOR = (By.XPATH, "//Edit[@Name='Search']")

    FILE_SAVE_PAGE_LOCATORS = FileSavePageLocators(
        file_path=(By.XPATH, "//ComboBox[@AutomationId='FileNameControlHost']/Edit"),
        file_path_dropdown=(By.XPATH, "//ComboBox[@AutomationId='FileNameControlHost']/Button"),
        save_button=(By.XPATH, "//Button[@AutomationId='1' and @Name='Save']"),
        cancel_button=(By.XPATH, "//Button[@AutomationId='2' and @Name='Cancel']")
    )

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self._logger = Logger(self.__class__.__name__)
        self._left_panel = MethodEditorLeftPanel(driver)
        self._file_save_page = FileSavePage(driver, self.FILE_SAVE_PAGE_LOCATORS)
        self.save_method_window: InstrumentMethodCreationPage = InstrumentMethodCreationPage(driver)

    @property
    def left_panel(self):
        return self._left_panel

    def validate_opened(self):
        is_visible = is_element_visible(self._driver, self.METHOD_EDITOR_HEADER_LOCATOR, 5)
        assert is_visible, "Failed to open Method Editor main window"

    def is_issue_notification_present(self):
        return is_element_present(self._driver, self.BELL_ICON_WITH_ERRORS, 1)

    def is_issue_notification_absent(self):
        return is_element_present(self._driver, self.BELL_ICON_WITHOUT_ERRORS, 1)

    def get_issues_notifications(self):
        self.open_notifications_panel()
        elements = self._driver.find_elements(*self.ERROR_NOTIFICATION_ELEMENT_LOCATOR)
        issues = []
        for element in elements:
            text_elements = element.find_elements(By.XPATH, "//Text")
            title = text_elements[0].get_attribute("Name")
            description = text_elements[1].get_attribute("Name")
            issues.append({"title": title, "description": description})

        return issues

    def open_issue_element(self, issue_title: str):
        self.open_notifications_panel()
        elements = self._driver.find_elements(*self.ERROR_NOTIFICATION_ELEMENT_LOCATOR)
        for element in elements:
            text_elements = element.find_elements(By.XPATH, "//Text")
            title = text_elements[0].get_attribute("Name")
            if issue_title == title:
                element.click()
            else:
                raise Exception(f"Issue with a title: {issue_title} could not be found")

    def open_notifications_panel(self):
        is_open = self.is_notification_panel_open()
        if is_open:
            return
        self.click_on_element(self.BELL_ICON_LOCATOR)
        assert self.is_notification_panel_open(), "Failed to open notifications panel"

    def is_notification_panel_open(self) -> bool:
        state = self.get_element_attribute(self.BELL_ICON_WITH_ERRORS, "IsOffscreen")
        return not str_to_bool(state)

    def search_text(self, text: str):
        self.click_on_element(self.SEARCH_ICON_LOCATOR)
        self.set_text(self.SEARCH_INPUT_LOCATOR, str(text))

    def click_hamburger_menu(self):
        text_element = self.find_element(self.METHOD_EDITOR_HEADER_LOCATOR)
        ActionChains(self._driver).move_to_element_with_offset(text_element, -10, 0).click().perform()

    def click_export_to_json(self) -> FileSavePage:
        self.click_on_element(self.EXPORT_TO_JSON_BUTTON)
        return self._file_save_page

    def select_issue(self, issue_title):
        issues = self.get_issues_notifications()
        for issue in issues:
            if (issue['title']) == issue_title:
                issue_locator = self.get_issue_locator(issue_title)
                issue_panel = self._driver.find_element(*issue_locator)
                issue_panel.click()
                return
        assert False, f"The issue title does not exist. issue_title = {issue['title']}"

    def get_issue_locator(self, title: str):
        xpath: tuple[str, str] = (By.XPATH, f"//Text[@Name='Issues']//following-sibling::List//Text[@Name='{title}']")
        return xpath