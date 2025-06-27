from functools import partial

import allure_commons
import pytest
from allure_commons.lifecycle import AllureLifecycle
from allure_commons.model2 import Parameter, StatusDetails
from allure_commons.model2 import Status
from allure_commons.utils import host_tag, thread_tag
from allure_commons.utils import now
from allure_commons.utils import uuid4
from pytest_bdd.parser import Feature, Scenario

from .label_builder import LabelBuilder
from .utils import get_full_name, get_name, get_params, get_outcome_status, get_status, get_pytest_report_status, process_step, get_outcome_status_details
from .utils import get_status_details
from .utils import get_step_name
from .utils import get_uuid


class PytestBDDListener:
    def __init__(self, config):
        self.label_builder = LabelBuilder(config)
        self.lifecycle = AllureLifecycle()
        self.host = host_tag()
        self.thread = thread_tag()

    def _scenario_finalizer(self, scenario):
        for step in scenario.steps:
            step_uuid = get_uuid(str(id(step)))
            with self.lifecycle.update_step(uuid=step_uuid) as step_result:
                if step_result:
                    step_result.status = Status.SKIPPED
                    self.lifecycle.stop_step(uuid=step_uuid)

    @allure_commons.hookimpl
    def start_step(self, uuid, title, params):
        parameters = [Parameter(name=name, value=value) for name, value in params.items()]
        with self.lifecycle.start_step(None, uuid) as step:
            step.name = title
            step.parameters = parameters

    @allure_commons.hookimpl
    def stop_step(self, uuid, exc_type, exc_val, exc_tb):

        with self.lifecycle.update_step(uuid=uuid) as step_result:
            step_result.status = get_status(exc_val)
            if exc_val:
                details = get_status_details(exc_val)
                step_result.statusDetails = details

        self.lifecycle.stop_step(uuid=uuid)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_setup(self, item):
        container_uuid = uuid4()
        with self.lifecycle.start_container(container_uuid) as container:
            container.name = item.name + "_container"
        yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_call(self, item):
        test_uuid = uuid4()

        with self.lifecycle.update_container() as container:
            container.children.append(test_uuid)

        with self.lifecycle.schedule_test_case(uuid=test_uuid) as test_result:
            test_result.historyId = get_uuid(item.nodeid)
            test_result.parameters = get_params(item)
        yield
        with self.lifecycle.update_test_case() as test_result:
            if not test_result.stop:
                test_result.stop = now()

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_before_scenario(self, request, feature: Feature, scenario: Scenario):
        before_fixture_uuid = uuid4()
        with self.lifecycle.start_before_fixture(uuid=before_fixture_uuid) as before:
            before.name = "pytest_bdd_before_scenario"
            before.start = now()

        full_name = get_full_name(feature, scenario)
        name = get_name(request.node, scenario)

        with self.lifecycle.update_test_case() as test_result:
            test_result.fullName = full_name
            test_result.name = name
            test_result.start = now()
            test_result.description = "\n".join(scenario.description) if scenario.description else None
            self.label_builder.generate_labels(scenario, test_result)

        outcome = yield

        status = get_outcome_status(outcome)
        with self.lifecycle.update_before_fixture(before_fixture_uuid) as before:
            before.status = status
        self.lifecycle.stop_before_fixture(before_fixture_uuid)

        with self.lifecycle.update_test_case() as test_result:
            test_result.start = now()

        if status != Status.PASSED:
            self.report_skipped_steps(scenario.steps)

        finalizer = partial(self._scenario_finalizer, scenario)
        request.node.addfinalizer(finalizer)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_after_scenario(self, request, feature, scenario):
        with self.lifecycle.update_test_case() as test_result:
            test_result.stop = now()

        after_fixture_uuid = uuid4()
        with self.lifecycle.start_after_fixture(uuid=after_fixture_uuid) as after:
            after.name = "pytest_bdd_after_scenario"
            after.start = now()
        outcome = yield
        with self.lifecycle.update_after_fixture(uuid=after_fixture_uuid) as after:
            after.status = get_outcome_status(outcome)
        self.lifecycle.stop_after_fixture(uuid=after_fixture_uuid)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_before_step(self, request, feature, scenario, step, step_func):
        uuid = get_uuid(str(id(step)))
        with self.lifecycle.start_step(uuid=uuid) as step_result:
            step_result.name = process_step(self.lifecycle, step)
        yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_after_step(self, request, feature, scenario, step, step_func, step_func_args):
        outcome = yield
        uuid = get_uuid(str(id(step)))
        status = get_outcome_status(outcome)
        status_details = get_outcome_status_details(outcome) if status != Status.PASSED else None
        with self.lifecycle.update_step(uuid=uuid) as step_result:
            step_result.status = status
            step_result.statusDetails = status_details
        self.lifecycle.stop_step(uuid=uuid)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_step_error(self, request, feature, scenario, step, step_func, step_func_args, exception):
        uuid = get_uuid(str(id(step)))
        status = get_status(exception)
        with self.lifecycle.update_step(uuid=uuid) as step_result:
            step_result.status = status
            step_result.statusDetails = get_status_details(exception)
            step_name = step_result.name
        self.lifecycle.stop_step(uuid=uuid)
        self.report_skipped_steps(scenario.steps[scenario.steps.index(step) + 1:])
        start_of_pytest_bdd_step_error_hooks = now()
        outcome = yield
        if outcome and outcome.excinfo:
            after_fixture_uuid = uuid4()
            with self.lifecycle.start_after_fixture(uuid=after_fixture_uuid) as after:
                after.name = f"pytest_bdd_step_error ({step_name})"
                after.start = start_of_pytest_bdd_step_error_hooks
                after.stop = now()
                after.status = get_outcome_status(outcome)
                after.statusDetails = get_outcome_status_details(outcome)
            self.lifecycle.stop_after_fixture(uuid=after_fixture_uuid)

    @pytest.hookimpl(hookwrapper=True)
    def pytest_bdd_step_func_lookup_error(self, request, feature, scenario, step, exception):
        uuid = get_uuid(str(id(step)))
        with self.lifecycle.start_step(uuid=uuid) as step_result:
            step_result.name = get_step_name(step)
            step_result.status = Status.UNKNOWN
        self.lifecycle.stop_step(uuid=uuid)
        self.report_skipped_steps(scenario.steps[scenario.steps.index(step) + 1:])
        yield

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        report = (yield).get_result()

        status = get_status(call.excinfo.value) if call.excinfo else get_pytest_report_status(report)

        status_details = None
        if call.excinfo:
            message = call.excinfo.exconly()
            if hasattr(report, 'wasxfail'):
                reason = report.wasxfail
                message = (f'XFAIL {reason}' if reason else 'XFAIL') + '\n\n' + message
            trace = report.longreprtext
            status_details = StatusDetails(
                message=message,
                trace=trace)

        stage = report.when

        with self.lifecycle.update_test_case() as test_result:

            if test_result and stage == "setup":
                test_result.status = status
                test_result.statusDetails = status_details

            if test_result and stage == "call":
                if test_result.status not in [Status.PASSED, Status.FAILED]:
                    test_result.status = status
                    test_result.statusDetails = status_details

            if test_result and stage == "teardown":
                if test_result.status == Status.PASSED and status != Status.PASSED:
                    test_result.status = status
                    test_result.statusDetails = status_details

        if report.when == 'teardown':
            self.lifecycle.write_test_case()
            self.lifecycle.write_container()

    @allure_commons.hookimpl
    def attach_data(self, body, name, attachment_type, extension):
        self.lifecycle.attach_data(uuid4(), body, name=name, attachment_type=attachment_type, extension=extension)

    @allure_commons.hookimpl
    def attach_file(self, source, name, attachment_type, extension):
        self.lifecycle.attach_file(uuid4(), source, name=name, attachment_type=attachment_type, extension=extension)

    def report_skipped_steps(self, steps):
        for step in steps:
            uuid = get_uuid(str(id(step)))
            with self.lifecycle.start_step(uuid=uuid) as step_result:
                step_result.name = process_step(self.lifecycle, step)
                step_result.status = Status.SKIPPED
            self.lifecycle.stop_step(uuid=uuid)
