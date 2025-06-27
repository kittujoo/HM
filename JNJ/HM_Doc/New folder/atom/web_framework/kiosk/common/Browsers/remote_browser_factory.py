import subprocess

from selenium import webdriver

from utilities.logger import Logger
from web_framework.kiosk.common.Browsers.browser_factory import BrowserFactory

"""
    BrowserDriverFactory is responsible to build various browser drivers.

"""
logger = Logger("browser_driver_factory")


class RemoteBrowserFactory(BrowserFactory):
    """ To create browser objects that encapsulates creation of
                selenium web driver
        Returns:
            Browser: WebDriver of Selenium

        """

    def __init__(self, host: str, username: str, password, headless: bool, executable_path: str):
        self._host = host
        self._username = username
        self._password = password
        self._executable_path = executable_path
        self._proc = None
        super().__init__(headless)

    def create_web_driver(self):
        logger.debug("Creating browser")

        options = self.common_options()

        command = f"psexec -accepteula -d -u {self._username} -p {self._password} -i 1 {self._executable_path} --port=4444"
        try:
            self._proc = subprocess.run(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE).returncode
        except Exception as e:
            logger.error(f"Failed to start chromedriver with psexec: [{e}]")
        browser = webdriver.Remote(command_executor=f"http://{self._host}:4444",
                                   options=options,
                                   desired_capabilities=options.to_capabilities(),
                                   )
        set_viewport_size(browser, 1280, 800)
        return browser

    def stop(self):
        if self._proc:
            command = f"pskill -t -accepteula {self._proc}"
            res = subprocess.run(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout = res.stdout.decode()
            if res.returncode:
                logger.info(f"Pskill failed to stop chromedriver process with exit code: [{res.returncode}] and stdout: [{stdout}]")


def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
            return [window.outerWidth - window.innerWidth + arguments[0],
              window.outerHeight - window.innerHeight + arguments[1]];
            """, width, height)
    driver.set_window_size(*window_size)
