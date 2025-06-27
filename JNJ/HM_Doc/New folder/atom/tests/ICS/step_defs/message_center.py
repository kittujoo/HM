from pytest_bdd import then
from pytest_bdd.parsers import cfparse

from web_framework.empower.drivers.message_center_driver import MessageCenterDriver
from web_framework.empower.drivers.run_samples_driver import RunSamplesDriver


@then(cfparse('the message center shows "{message}" message'))
@then(cfparse('user validates the "{message}" is displayed in Empower Message Center'))
def check_message_center(message: str, message_center_driver: MessageCenterDriver, run_samples_driver: RunSamplesDriver):
    run_samples_driver.run_samples_page.click_message_center_button()
    message_center_driver.attach_to_existed_application()
    log = message_center_driver.get_log()
    actual_message = log.get_last_message().message
    assert message in actual_message, "Unexpected Message Center last message. Expected containing [{message}] but was [{actual_message}]"
