import os
from typing import List, Optional
from uuid import UUID

from _pytest.main import Failed
from _pytest.outcomes import Skipped
from allure_commons.lifecycle import AllureLifecycle
from allure_commons.model2 import Parameter
from allure_commons.model2 import Status
from allure_commons.model2 import StatusDetails
from allure_commons.types import LabelType, Severity
from allure_commons.utils import md5, format_exception
from allure_commons.utils import uuid4
from pytest_bdd.parser import Step

ALLURE_SUPPORTED_LABELS = [LabelType.EPIC,
                           LabelType.FEATURE,
                           LabelType.STORY,
                           LabelType.PARENT_SUITE,
                           LabelType.SUITE,
                           LabelType.SUB_SUITE,
                           LabelType.SEVERITY,
                           LabelType.THREAD,
                           LabelType.HOST,
                           LabelType.TAG,
                           LabelType.ID,
                           LabelType.FRAMEWORK,
                           LabelType.LANGUAGE,
                           LabelType.MANUAL]
ALLURE_UNIQUE_LABELS = [
    LabelType.SEVERITY,
    LabelType.FRAMEWORK,
    LabelType.HOST,
    LabelType.SUITE,
    LabelType.PARENT_SUITE,
    LabelType.SUB_SUITE
]

allure_label_examples = [
    "@allure.id:1",
    "@allure.label.customLabelName:LabelValue",
    "@allure.severity:blocker",
]

SEVERITY_VALUES = [item.value for item in Severity]


def get_step_name(step):
    return f"{step.keyword} {step.name}"


def _is_table(lines: List[str]):
    return all(line.startswith("|") and line.endswith("|") for line in lines)


def process_step(lifecycle: AllureLifecycle, step: Step):
    lines = step.name.splitlines()
    extra_lines = lines[1:]
    if extra_lines and _is_table(extra_lines):
        name = lines[0]
        new_table = []
        for line in extra_lines:
            parsed_row = [item.strip() for item in line.split("|") if item]
            new_table.append("\t".join(parsed_row))
        lifecycle.attach_data(uuid=uuid4(), body="\n".join(new_table), name="Data table", attachment_type="text/tab-separated-values", extension="csv")
    else:
        name = step.name

    return f"{step.keyword} {name}"


def get_name(node, scenario):
    if hasattr(node, 'callspec'):
        parts = node.nodeid.rsplit("[")
        params = parts[-1]
        return f"{scenario.name} [{params}"
    return scenario.name


def get_full_name(feature, scenario):
    feature_path = os.path.normpath(feature.rel_filename)
    return f"{feature_path}:{scenario.name}"


def get_uuid(*args):
    return str(UUID(md5(*args)))


def get_status_details(exception: Optional[BaseException]):
    message = str(exception)
    trace = format_exception(type(exception), exception)
    return StatusDetails(message=message, trace=trace) if message or trace else None


def get_pytest_report_status(pytest_report):
    pytest_statuses = ('failed', 'passed', 'skipped')
    statuses = (Status.FAILED, Status.PASSED, Status.SKIPPED)
    for pytest_status, status in zip(pytest_statuses, statuses):
        if getattr(pytest_report, pytest_status):
            return status


def get_params(node):
    if hasattr(node, 'callspec'):
        params = dict(node.callspec.params)
        outline_params = params.pop('_pytest_bdd_example', {})
        params.update(outline_params)
        return [Parameter(name=name, value=value) for name, value in params.items()]


def get_outcome_status(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    return get_status(exception)


def get_outcome_status_details(outcome):
    exception_type, exception, exception_traceback = outcome.excinfo or (None, None, None)
    return get_status_details(exception)


def get_status(exception):
    if exception:
        if isinstance(exception, AssertionError) or isinstance(exception, Failed):
            return Status.FAILED
        elif isinstance(exception, Skipped):
            return Status.SKIPPED
        return Status.BROKEN
    else:
        return Status.PASSED


def format_allure_link(config, name, link_type):
    pattern = dict(config.option.allure_link_pattern).get(link_type, '{}')
    return pattern.format(name)
