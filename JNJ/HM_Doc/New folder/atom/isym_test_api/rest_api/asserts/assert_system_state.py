from isym_test_api.rest_api.api.system.system_state_response import SystemStateEnum
from isym_test_api.rest_api.drivers.system.system_state_driver import SystemStateDriver
from utilities.assert_timeout import AssertTimeout


class AssertSystemState(object):

    def __init__(self, system_state_driver: SystemStateDriver, assert_timeout: AssertTimeout):
        self._system_state_driver = system_state_driver
        self._assert_timeout = assert_timeout

    def state_is_at_method_conditions(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_ATMETHODCONDITIONS, timeout_in_seconds)

    def state_is_busy(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_BUSY, timeout_in_seconds)

    def state_is_discovering(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_DISCOVERING, timeout_in_seconds)

    def state_is_error(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_ERROR, timeout_in_seconds)

    def state_is_exclusive_idle(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_EXCLUSIVEIDLE, timeout_in_seconds)

    def state_is_exclusivefail(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_EXCLUSIVEFAIL, timeout_in_seconds)

    def state_is_halted(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_HALTED, timeout_in_seconds)

    def state_is_halting(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_HALTING, timeout_in_seconds)

    def state_is_idle(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_IDLE, timeout_in_seconds)

    def state_is_illegal(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_ILLEGAL, timeout_in_seconds)

    def state_is_initializing(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_INITIALIZING, timeout_in_seconds)

    def state_is_preparing(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_PREPARING, timeout_in_seconds, 1)

    def state_is_rebootrequired(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_REBOOTREQUIRED, timeout_in_seconds)

    def state_is_resetting(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_RESETTING, timeout_in_seconds)

    def state_is_running(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_RUNNING, timeout_in_seconds)

    def state_is_setting_method(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_SETTINGMETHOD, timeout_in_seconds)

    def state_is_startfailed(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_STARTFAILED, timeout_in_seconds)

    def state_is_workflow(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_WORKFLOW, timeout_in_seconds)

    def state_is_workflow_recovering(self, timeout_in_seconds=None):
        self._state_is(SystemStateEnum.SystemStateEnum_WORKFLOWRECOVERING, timeout_in_seconds)

    def _state_is(self, state, timeout_in_seconds, polling_period_in_seconds=2):
        self._assert_timeout.are_equal(lambda: self._system_state_driver.get_system_state().state, state, "Unexpected system state", timeout_in_seconds,
                                       polling_period_in_seconds)
