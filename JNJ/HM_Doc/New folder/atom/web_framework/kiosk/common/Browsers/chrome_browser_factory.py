import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from utilities.logger import Logger
from web_framework.kiosk.common.Browsers.browser_factory import BrowserFactory

"""
    BrowserDriverFactory is responsible to build various browser drivers.
    
"""
logger = Logger("browser_driver_factory")


class BrowserDriverFactory(BrowserFactory):
    """ To create browser objects that encapsulates creation of
            selenium web driver
    Returns:
        Browser: WebDriver of Selenium

    """

    def __init__(self, headless: bool, results_folder: str, executable_path: str):
        super().__init__(headless)
        self._results_folder: str = results_folder
        self._executable_path: str = executable_path

    def create_web_driver(self, save_logs: bool = False):
        logger.debug("Creating browser")

        browser_log_path = os.path.join(self._results_folder, "chromium_browser.log")

        options = self.common_options()

        if save_logs:
            browser = webdriver.Chrome(executable_path=self._executable_path,
                                   options=options,
                                   desired_capabilities=options.to_capabilities(),
                                   service_args=["--verbose", f"--log-path={browser_log_path}"])
        else:
            browser = webdriver.Chrome(executable_path=self._executable_path,
                                       options=options,
                                       desired_capabilities=options.to_capabilities())
        set_viewport_size(browser, 1280, 800)
        return browser

    def stop(self):
        pass


def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)
