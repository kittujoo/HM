import abc

from selenium.webdriver.chrome.options import Options


class BrowserFactory(metaclass=abc.ABCMeta):

    def __init__(self, headless: bool):
        self._headless: bool = headless

    @abc.abstractmethod
    def create_web_driver(self):
        """Creates instance of a new browser"""
        raise NotImplementedError

    def common_options(self):
        options = Options()
        options.headless = self._headless
        options.add_argument("--log-level=3")
        options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_experimental_option('w3c', False)

        return options

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError
