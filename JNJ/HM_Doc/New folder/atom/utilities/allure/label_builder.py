import os
from enum import Enum

from allure_commons.model2 import Label, TestResult, Link
from allure_commons.types import LabelType, LinkType
from allure_commons.utils import host_tag, thread_tag, platform_label
from pytest_bdd.parser import Feature, Scenario

from utilities.allure.utils import format_allure_link, SEVERITY_VALUES
from utilities.logger import Logger


class ResultTags(Enum):
    FLAKY = "FLAKY"
    KNOWN = "KNOWN"
    MUTED = "MUTED"


class LabelBuilder:
    logger = Logger(os.path.basename(__file__))
    COMPOSITE_TAG_DELIMITER = ":"

    SEVERITY = "SEVERITY"
    ISSUE_LINK = "DEFECT"
    TMS_LINK = "TMS"
    PLAIN_LINK = "LINK"
    OWNER = "OWNER"

    def __init__(self, config):
        self._config = config

    def generate_labels(self, scenario: Scenario, test_result: TestResult):
        feature: Feature = scenario.feature
        tags = feature.tags.union(scenario.tags)
        scenario_labels = []
        scenario_links = []
        for tag in tags:
            if self.COMPOSITE_TAG_DELIMITER in tag:
                tag_parts = tag.split(self.COMPOSITE_TAG_DELIMITER, 1)
                if len(tag_parts) < 2 or not tag_parts[1]:
                    continue

                tag_key = tag_parts[0].upper()
                tag_value = tag_parts[1]

                # Handle composite named links
                if tag_key.startswith(self.PLAIN_LINK + "."):
                    link_type = tag_key.split(".")[1]
                    scenario_links.append(self.try_get_named_link(link_type.lower(), tag_value))
                elif tag_key == self.SEVERITY:
                    self.validate_severity_value(tag_value)
                    scenario_labels.append(Label(name=LabelType.SEVERITY, value=tag_value.lower()))
                elif tag_key == self.TMS_LINK:
                    scenario_links.append(self.create_link(LinkType.TEST_CASE, tag_value))
                elif tag_key == self.ISSUE_LINK:
                    scenario_links.append(self.create_link(LinkType.ISSUE, tag_value))
                elif tag_key == self.PLAIN_LINK:
                    scenario_links.append(Link(name=tag_value, url=tag_value, type=None))
                elif tag_key == self.OWNER:
                    scenario_labels.append(Label(name=self.OWNER.lower(), value=tag_value))
                else:
                    self.logger.debug(f"Composite tag {tag_key} is not supported. adding it as RAW")
            elif tag in SEVERITY_VALUES:
                scenario_labels.append(Label(name=LabelType.SEVERITY, value=tag))
            # TODO investigate why results tags should be ommited
            # elif not self.is_result_tag(tag):
            scenario_labels.append(Label(name=LabelType.TAG, value=tag))

        # TODO apply labels provided by pytest args
        # self.scenario_labels.extend(ResultsUtils.getProvidedLabels())
        scenario_labels.extend([
            Label(name=LabelType.HOST, value=host_tag()),
            Label(name=LabelType.THREAD, value=thread_tag()),
            Label(name=LabelType.FRAMEWORK, value="pytest-bdd"),
            Label(name=LabelType.LANGUAGE, value=platform_label()),
            Label(name=LabelType.FEATURE, value=feature.name),
            Label(name=LabelType.STORY, value=scenario.name),
            Label(name=LabelType.SUITE, value=feature.name)
        ])
        test_result.labels.extend(scenario_labels)
        test_result.links.extend(scenario_links)

    def is_result_tag(self, tag: str):
        return tag in [item.value for item in ResultTags]

    def create_link(self, link_type: str, link_value: str):
        url = format_allure_link(self._config, link_value, link_type)
        return Link(type=link_type, url=url, name=link_value)

    def try_get_named_link(self, link_type: str, link_name: str):
        if not link_type or not link_name:
            self.logger.warning(f"Composite named link @{self.PLAIN_LINK}.{link_type}={link_name} has wrong format. Skipping")
            return None

        url = format_allure_link(self._config, link_name, link_type)
        return Link(type=link_type, url=url, name=link_name)

    @staticmethod
    def validate_severity_value(value):
        if value not in SEVERITY_VALUES:
            raise ValueError(f"Invalid severity value: [{value}], known severities values are: [{SEVERITY_VALUES}]")
