import os
import uuid
from dataclasses import dataclass
from time import sleep
from typing import Optional, List

from selenium.webdriver.remote.webdriver import WebDriver

from fixtures_win_app_driver import WinAppDriverHandler
from utilities.constants import EMPOWER_BIN_FOLDER
from utilities.logger import Logger
from web_framework.empower.pages.common.common_login_page import CommonLoginScreen
from web_framework.empower.pages.message_center.message_center_page import MessageCenterPage

logger = Logger(os.path.basename(__file__))


@dataclass
class Message:
    message_id: int
    type: str
    category: str
    date: str
    application: str
    user: str
    user_location: str
    project: str
    message: str


class MessageLog:

    def __init__(self, lines: List[Message]):
        if not lines:
            raise ValueError("Provided lines array was empty")
        self._lines: List[Message] = lines.copy()
        self._lines.sort(key=lambda x: x.message_id, reverse=True)

    def get_last_message(self):
        """returns last message details"""
        return self._lines[0]

    def get_messages(self):
        return self._lines.copy()

    def get_messages_after(self, message_id) -> List[Message]:
        """methods that takes as an argument a specific message id and returns a list of messages logged after the provided message id"""
        response = [x for x in self._lines if x.message_id >= message_id]
        return response


class MessageCenterDriver:
    @property
    def _driver(self):
        if not self.__driver:
            raise ValueError("Application was not initialized, run login_to_project ot attach_to_existed_application methods")
        return self.__driver

    @_driver.setter
    def _driver(self, value):
        self.__driver = value

    def __init__(self, win_app_driver_handler: WinAppDriverHandler, username: str, password: str, results_folder: str):
        self._win_app_driver_handler = win_app_driver_handler
        self._executable_path = f"{EMPOWER_BIN_FOLDER}\\MessageCenter.exe"
        self.__driver: Optional[WebDriver] = None
        self._results_folder: str = results_folder
        self._username = username
        self._password = password

    def login_to_project(self):
        login_driver = self._win_app_driver_handler.start_application(self._executable_path)
        login_page = CommonLoginScreen(login_driver)
        login_page.enter_username(self._username)
        # Second username set needs to fix issues when message center was opened on top of any other empower application
        login_page.enter_username(self._username)
        login_page.enter_password(self._password)
        login_page.press_ok()

        self.attach_to_existed_application()

    def attach_to_existed_application(self):
        self._driver = self._win_app_driver_handler.attach_to_running_application("- Message Center")

    def get_log(self):
        file_path = os.path.join(self._results_folder, f"message_center_log_{uuid.uuid4()}.txt")
        page = MessageCenterPage(self._driver)
        page.save_log_to(file_path)
        sleep(3)
        with open(file_path, 'r') as f:
            contents = f.readlines()
        log = self.parse_log(contents)
        return log

    def parse_log(self, lines) -> MessageLog:
        # Split the text into lines

        messages = []

        # Parse the data rows
        for line in lines[1:]:
            if line == '\x00':
                continue
            row = line.split('\t')
            message = Message(
                message_id=int(row[1]),
                type=row[2],
                category=row[3],
                date=row[4],
                application=row[5],
                user=row[6],
                user_location=row[7],
                project=row[8],
                message=row[9]
            )
            messages.append(message)
        return MessageLog(messages)
