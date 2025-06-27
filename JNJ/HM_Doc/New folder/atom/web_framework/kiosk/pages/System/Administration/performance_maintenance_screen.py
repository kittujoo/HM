import re
from web_framework.kiosk.pages.Locators.System.Administration.performace_maintenence_screen_locators import \
    PerformanceMaintenanceScreenLocators
from web_framework.kiosk.pages.Locators.System.Administration.system_qualification_screen_locators import \
    SystemQualificationScreenLocators
from web_framework.kiosk.pages.base_page import BasePage
from datetime import timedelta, datetime


class PerformanceMaintenanceScreen(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)

    def validate_performance_maintenance_screen(self):
        locator = PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_MENU
        screen_name = "Performance Maintenance Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_add_or_edit_note_screen(self):
        locator = PerformanceMaintenanceScreenLocators.ADD_OR_EDIT_NOTE_TITLE
        screen_name = "Add or Edit Note Screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def set_performance_maintenance_toggle_status(self, current_toggle_state):
        self.wait_time_to_load_value(PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_MENU)
        if current_toggle_state != self.is_toggle_component_enabled(
                PerformanceMaintenanceScreenLocators.PERFORMANCE_MAINTENANCE_TOGGLE):
            self.set_toggle_button(SystemQualificationScreenLocators.SYSTEM_QUALIFICATION_TOGGLE, current_toggle_state)

    def get_selected_expiry_performance_maintenance(self) -> str:
        actual_month = self.get_text(PerformanceMaintenanceScreenLocators.MAINTENANCE_EXPIRATION_LABEL)
        string_to_remove = re.search(r'\d+', actual_month)
        current_month_selected = string_to_remove.group()
        return current_month_selected

    def get_expiry_date_from_current_date(self, desired_months) -> str:
        today = datetime.today()
        expiry_date = today + timedelta(days=31 * int(desired_months))
        while expiry_date.day != today.day:
            expiry_date -= timedelta(days=1)
        formatted_expiry_date = expiry_date.strftime("%d %B %Y")
        return formatted_expiry_date

    def enter_note_content(self, text):
        self.clear_text_area(PerformanceMaintenanceScreenLocators.ADD_ENTRY_TEXT_AREA)
        self.enter_string(text)
