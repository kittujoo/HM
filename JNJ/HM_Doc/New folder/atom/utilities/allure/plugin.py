import argparse
import os

import allure
import allure_commons
from allure_commons.logger import AllureFileLogger
from allure_commons.types import LabelType, LinkType

from .pytest_bdd_listener import PytestBDDListener
from .utils import SEVERITY_VALUES


def cleanup_factory(plugin):
    def clean_up():
        name = allure_commons.plugin_manager.get_name(plugin)
        allure_commons.plugin_manager.unregister(name=name)

    return clean_up


def add_allure_options(parser):
    parser.getgroup("reporting").addoption('--alluredir',
                                           action="store",
                                           dest="allure_report_dir",
                                           metavar="DIR",
                                           default=None,
                                           help="Generate Allure report in the specified directory (may not exist)")

    parser.getgroup("reporting").addoption('--clean-alluredir',
                                           action="store_true",
                                           dest="clean_alluredir",
                                           help="Clean alluredir folder if it exists")

    parser.getgroup("reporting").addoption('--allure-no-capture',
                                           action="store_false",
                                           dest="attach_capture",
                                           help="Do not attach pytest captured logging/stdout/stderr to report")

    parser.getgroup("reporting").addoption('--inversion',
                                           action="store",
                                           dest="inversion",
                                           default=False,
                                           help="Run tests not in testplan")

    def label_type(type_name):
        def a_label_type(value):
            atoms = set(value.split(','))
            return set((type_name, atom) for atom in atoms)

        return a_label_type

    def severity_label():
        def a_label_type(string):
            atoms = set(string.split(','))
            if invalid_values := [atom for atom in atoms if atom not in SEVERITY_VALUES]:
                raise argparse.ArgumentTypeError(
                    f'Illegal severity label detected: {invalid_values} '
                    f'only {SEVERITY_VALUES} are allowed')
            result = [(LabelType.SEVERITY, allure.severity_level(atom)) for atom in atoms]
            return result

        return a_label_type

    general = parser.getgroup("general")
    general.addoption('--allure-severities',
                      action="store",
                      dest="allure_severities",
                      metavar="SEVERITIES_SET",
                      default={},
                      type=severity_label(),
                      help=f"""Comma-separated list of severity names.
                                             Tests only with these severities will be run.
                                             Possible values are: {SEVERITY_VALUES}.""")

    general.addoption('--allure-epics',
                      action="store",
                      dest="allure_epics",
                      metavar="EPICS_SET",
                      default={},
                      type=label_type(LabelType.EPIC),
                      help="""Comma-separated list of epic names.
                                             Run tests that have at least one of the specified feature labels.""")

    general.addoption('--allure-features',
                      action="store",
                      dest="allure_features",
                      metavar="FEATURES_SET",
                      default={},
                      type=label_type(LabelType.FEATURE),
                      help="""Comma-separated list of feature names.
                                             Run tests that have at least one of the specified feature labels.""")

    general.addoption('--allure-stories',
                      action="store",
                      dest="allure_stories",
                      metavar="STORIES_SET",
                      default={},
                      type=label_type(LabelType.STORY),
                      help="""Comma-separated list of story names.
                                             Run tests that have at least one of the specified story labels.""")

    general.addoption('--allure-ids',
                      action="store",
                      dest="allure_ids",
                      metavar="IDS_SET",
                      default={},
                      type=label_type(LabelType.ID),
                      help="""Comma-separated list of IDs.
                                             Run tests that have at least one of the specified id labels.""")

    def cf_type(string):
        type_name, values = string.split("=", 1)
        atoms = set(values.split(","))
        return [(type_name, atom) for atom in atoms]

    general.addoption('--allure-label',
                      action="append",
                      dest="allure_labels",
                      metavar="LABELS_SET",
                      default=[],
                      type=cf_type,
                      help="""List of labels to run in format label_name=value1,value2.
                                             "Run tests that have at least one of the specified labels.""")

    def link_pattern(string):
        pattern = string.split(':', 1)
        if not pattern[0]:
            raise argparse.ArgumentTypeError('Link type is mandatory.')

        if len(pattern) != 2:
            raise argparse.ArgumentTypeError('Link pattern is mandatory')
        # available_link_types = [LinkType.LINK, LinkType.ISSUE, LinkType.TEST_CASE]
        # if pattern[0] not in available_link_types:
        #     raise argparse.ArgumentTypeError(f'Link type should be one of {available_link_types}, but was {pattern[0]}')
        return pattern

    general.addoption('--allure-link-pattern',
                      action="append",
                      dest="allure_link_pattern",
                      metavar="LINK_TYPE:LINK_PATTERN",
                      default=[],
                      type=link_pattern,
                      help="""Url pattern for link type. Allows short links in test,
                                             like 'issue-1'. Text will be formatted to full url with python
                                             str.format().""")


def apply_allure_reporting(config):
    report_dir = config.option.allure_report_dir
    clean = config.option.clean_alluredir

    if report_dir:
        report_dir = os.path.abspath(report_dir)

        pytest_bdd_listener = PytestBDDListener(config)
        config.pluginmanager.register(pytest_bdd_listener)
        allure_commons.plugin_manager.register(pytest_bdd_listener)
        config.add_cleanup(cleanup_factory(pytest_bdd_listener))

        file_logger = AllureFileLogger(report_dir, clean)
        allure_commons.plugin_manager.register(file_logger)
        config.add_cleanup(cleanup_factory(file_logger))
