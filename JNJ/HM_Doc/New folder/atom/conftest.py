import logging
import os
from os.path import dirname

import pytest
from _pytest.config.argparsing import Parser
from selenium.webdriver.remote import remote_connection

from argument_constants import RUN_ON_LOCAL, HEADLESS, ENVIRONMENT, ISPP_HOSTNAME, notset
from utilities.allure.plugin import add_allure_options, apply_allure_reporting
from utilities.assert_timeout import AssertTimeout
from utilities.logger import Logger

remote_connection.LOGGER.setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.ERROR)
logging.getLogger("urllib3.connectionpool").setLevel(logging.ERROR)

if not os.path.exists("results"):
    os.makedirs("results")

pytest_plugins = ['fixtures_configurations', 'fixtures_kiosk_driver', 'fixtures_logging', 'fixtures_rest_api_asserts', 'fixtures_rest_api_drivers',
                  'fixtures_ssh_connections', 'fixtures_ui_drivers', 'fixtures_ui_pages', 'fixtures_universal_tools', 'hooks', 'fixtures_win_app_driver',
                  'fixtures_empower_drivers']

logger = Logger(os.path.basename(__file__))


@pytest.fixture(scope='function')
def context():
    return {}


@pytest.fixture(scope='session')
def assert_timeout(settings):
    return AssertTimeout(timeout=settings.default_assert_timeout_in_seconds, poll=settings.default_assert_polling_interval_in_seconds)


@pytest.fixture(scope='session')
def results_folder():
    return os.path.join(dirname(os.path.realpath(__file__)), "results")


def pytest_addoption(parser: Parser):
    parser.addoption(f"--{ENVIRONMENT}", action="store", required=True, choices=["DEFAULT", "SIMULATION", "REAL", "CDS"],
                     help="Type of target environment")
    parser.addoption("--atom_unit_testing", action="store_true", default=False, help="Notifies atom testing framework to not load "
                                                                                     "zmq specific plugins to successfully run unit tests")
    parser.addoption(f"--{HEADLESS}", action="store_true", default=True, help="Set browser mode - headless or not, default behaviour - headless")
    parser.addoption("--no-headless", dest='headless', action='store_false')
    parser.addoption(f"--{RUN_ON_LOCAL}", action="store_true", default=False)
    parser.addoption(f"--{ISPP_HOSTNAME}", action="store", default=notset, help="Hostname for ispp location (Kiosk)")
    parser.addoption("--test_filter", dest="markexpr", action="store", default="", help="only run tests matching given mark expression.  "
                                                                                        "example: --test_filter='mark1 and not mark2'.")
    add_allure_options(parser)


def pytest_configure(config):
    apply_allure_reporting(config)
