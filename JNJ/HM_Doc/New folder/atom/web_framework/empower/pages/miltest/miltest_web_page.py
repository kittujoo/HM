import abc
from typing import Callable

from selenium.webdriver.remote.webdriver import WebDriver

from web_framework.web_driver_common.WinAppBasePage import WinAppBasePage
from web_framework.empower.pages.miltest.miltest_rest_client import MiltestRestClient


class MiltestWebPage(WinAppBasePage, metaclass=abc.ABCMeta):
    def __init__(self, driver: WebDriver, miltest_rest_client_creator: Callable[[str], MiltestRestClient]):
        super().__init__(driver)
        self._miltest_rest_client_creator = miltest_rest_client_creator
        self._miltest_rest_client = None

    @property
    def miltest_rest(self) -> MiltestRestClient:
        if not self._miltest_rest_client:
            handler = self._get_miltest_handler()
            self._miltest_rest_client = self._miltest_rest_client_creator(handler)
        return self._miltest_rest_client

    @abc.abstractmethod
    def _get_miltest_handler(self):
        raise NotImplementedError
