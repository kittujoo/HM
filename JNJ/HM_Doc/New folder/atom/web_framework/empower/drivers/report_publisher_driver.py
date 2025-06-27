from typing import Optional

from fixtures_win_app_driver import WinAppDriverHandler
from utilities.ics_reports_utilities import IcsReportsUtilities
from web_framework.empower.pages.common.file_save_page import FileType
from web_framework.empower.pages.report_publisher.report_publisher_page import ReportPublisherPage


class ReportPublisherDriver:

    @property
    def _report_publisher_page(self) -> ReportPublisherPage:
        if not self.__report_publisher_page:
            driver = self._win_app_driver_handler.attach_to_running_application("- Report Publisher")
            self.__report_publisher_page = ReportPublisherPage(driver)
        return self.__report_publisher_page

    def __init__(self, win_app_driver_handler: WinAppDriverHandler):
        self._win_app_driver_handler = win_app_driver_handler
        self.__report_publisher_page: Optional[ReportPublisherPage] = None

    def open_report_method(self):
        self._report_publisher_page.select_open_report_method()
        self._report_publisher_page.press_ok()

    def save_report(self, report_name, report_group_name):
        save_report = self._report_publisher_page
        save_report.select_report(report_name, report_group_name)
        save_report.press_save()
        save_report.type_report_name(report_name)
        save_report.press_save()
        if save_report.is_overwrite_dialog_opened():
            save_report.press_yes_by_name()

    def save_report_as(self, file_name: str, file_type: FileType):
        print_report = self._report_publisher_page
        file_save_page = print_report.open_save_as_window()
        file_save_page.set_file_path(file_name, file_type)
        file_save_page.click_save()

    @staticmethod
    def validate_report(json_file_name, json_key, report_file_name, report_key):
        report_validator = IcsReportsUtilities(json_file_name, report_file_name)
        key_mapping = {json_key: report_key}
        report_validator.validate_report(key_mapping)
