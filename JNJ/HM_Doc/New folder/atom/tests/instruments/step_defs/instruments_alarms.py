from datetime import datetime

from pytest_bdd import when
from pytest_bdd.parsers import cfparse

from utilities.alarms.instrument_alarm_codes import TuvAlarms
from utilities.alarms.instrument_alarm_utility import InstrumentAlarmUtility


@when(cfparse('User generates an "{alarm_type}" TUV alarm'))
def raise_alarm(alarm_type: str, context, instrument_alarm_utility_config: InstrumentAlarmUtility):
    alarm_id = TuvAlarms[alarm_type]
    # TODO theres should be datetime with timezone of instrument clock
    context["alarm_set_time"] = datetime.now().replace(tzinfo=None)
    context["alarm_id"] = alarm_id
    instrument_alarm_utility_config.raise_instrument_alarm("tuv", alarm_id.value)
