from pathlib import Path
from pytest_bdd import when, scenarios
from pytest_bdd.parsers import cfparse

# noinspection PyUnresolvedReferences
from tests.ICS.step_defs.message_center import check_message_center
from utilities.alarms.instrument_alarm_codes import QsmAlarms
from utilities.alarms.instrument_alarm_utility import InstrumentAlarmUtility
from utilities.logger import Logger

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_instrument_alarms.feature')

logger = Logger(__name__)


@when(cfparse('the "{alarm_name}" alarm is raised on Qsm with pressure value "{pressure}" and flow "{flow}"'))
def raise_alarm(alarm_name: str, pressure: str, flow: str, instrument_alarm_utility_config: InstrumentAlarmUtility):
    alarm_id = getattr(QsmAlarms, alarm_name)
    instrument_alarm_utility_config.raise_instrument_alarm("qsm", alarm_id.value, pressure, flow)
