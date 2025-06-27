# noinspection PyUnresolvedReferences
from tests.ICS.conftest import *
# noinspection PyUnresolvedReferences
from tests.ICS.step_defs.message_center import *
# noinspection PyUnresolvedReferences
from tests.instruments.step_defs.instruments_alarms import *
# noinspection PyUnresolvedReferences
from tests.kiosk.UI.step_defs.DashBoard.test_dash_board_screen import *
# noinspection PyUnresolvedReferences
from tests.kiosk.UI.step_defs.HealthScreen.common_steps import *
# noinspection PyUnresolvedReferences
from tests.kiosk.UI.step_defs.SystemSettingsScreen.test_system_logs_screen import *

scenarios('../features/system_tuv_alarms_workflow.feature')

# all the steps are implemented in conftest, but we need this file to be able to run the feature files
