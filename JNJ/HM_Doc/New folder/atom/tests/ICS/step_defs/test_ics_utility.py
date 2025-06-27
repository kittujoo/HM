import os
import time

from pathlib import Path
from pytest_bdd import given, when, then, scenarios
from pytest_bdd.parsers import cfparse
from datetime import datetime

from utilities.windows_network_utility import WindowsNetworkManagement
from utilities.universal_win_time import WindowsTimeManagement
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_demo_utilities.feature')

currentTime = datetime.now()


@given(cfparse('the current configuration contain network card "{network_card_name}"'))
def current_configuration_contain_network_card(network_card_name: str):
    logger.info(f"[NETWORK CARD DEMO] - check the {network_card_name} network card is available")
    network_interface_exist = WindowsNetworkManagement.check_network_card_availability(network_card_name)
    assert network_interface_exist, f"The network card {network_card_name} is not available"


@when(cfparse('disable the "{network_card_name}" network card'))
def disable_network_card_by_name(network_card_name: str):
    logger.info(f"[NETWORK CARD DEMO] - disable the {network_card_name} network card")
    WindowsNetworkManagement.toggle_network_interface(network_card_name, False)


@then(cfparse('the "{network_card_name}" is disabled'))
def check_network_card_is_disabled(network_card_name: str):
    logger.info(f"[NETWORK CARD DEMO] - check if {network_card_name} network card is disabled")
    network_interface_exist = WindowsNetworkManagement.check_network_card_availability(network_card_name)
    assert ~network_interface_exist, f"The network card {network_card_name} is not disabled"


@when(cfparse('enable the "{network_card_name}" network card'))
def enable_network_card_by_name(network_card_name: str):
    logger.info(f"[NETWORK CARD DEMO] - enable the {network_card_name} network card")
    WindowsNetworkManagement.toggle_network_interface(network_card_name, True)


@then(cfparse('the "{network_card_name}" is enabled'))
def check_network_card_is_enabled(network_card_name: str):
    logger.info(f"[NETWORK CARD DEMO] - check the {network_card_name} network card is enabled")
    network_interface_exist = WindowsNetworkManagement.check_network_card_availability(network_card_name)
    assert network_interface_exist, f"The network card {network_card_name} is not available"


@given(cfparse('the current clock time is saved'))
def save_the_current_clock_time():
    global currentTime
    currentTime = datetime.now()


@when(cfparse('change the clock by add one hour and five minutes'))
def change_the_clock_by_add_one_hour_and_five_minutes():
    logger.info(f"[CLOCK DEMO] - Add one hour and five minutes to current time: {currentTime}")
    WindowsTimeManagement.modify_system_time(0, 0, 0, 1, 5, 0)


@then(cfparse('the new system time is updated with plus one hour and five minutes'))
def check_the_clock_after_add_one_hour_and_five_minutes():
    logger.info(f"[CLOCK DEMO] - verify new time with plus one hour and five minutes: {datetime.now()}")
    new_time = datetime.now()
    assert new_time.hour == currentTime.hour + 1, "Hour comparison fail on adding one hour"
    assert new_time.minute >= currentTime.minute + 5, "Minutes comparison fail on adding 5 minutes"


@when(cfparse('change the clock by subtract one hour and five minutes'))
def change_the_clock_by_subtract_one_hour_and_five_minutes():
    global currentTime
    currentTime = datetime.now()
    logger.info(f"[CLOCK DEMO] - Subtract one hour and five minutes to current time: {currentTime}")
    WindowsTimeManagement.modify_system_time(0, 0, 0, -1, -5, 0)


@when(cfparse('sleep ten seconds'))
def change_the_clock_sleep_ten_seconds():
    logger.info("[CLOCK DEMO] - Sleep for 10 seconds.")
    time.sleep(10)


@then(cfparse('the new system time is updated with minus one hour and five minutes'))
def check_the_clock_after_subtract_one_hour_and_five_minutes():
    logger.info(f"[CLOCK DEMO] - verify new time with plus one hour and five minutes: {datetime.now()}")
    new_time = datetime.now()
    assert new_time.hour == currentTime.hour-1, "Hour comparison fail on one hour subtraction"
    assert new_time.minute >= currentTime.minute-5, "Minutes comparison fail on five minutes subtraction"
