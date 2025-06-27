import glob
import os
from tempfile import gettempdir

from pathlib import Path
from pytest_bdd import scenarios, then
from pytest_bdd.parsers import cfparse

from utilities.datatables.datatable import datatable
from utilities.empower_utility import EmpowerConfiguration
from utilities.logger import Logger
from utilities.windows_registry_utility import get_registry_key_value, is_instrument_installed
from web_framework.ics.common.services import Services

logger = Logger(os.path.basename(__file__))

if __name__ == Path(__file__).stem:
    scenarios('../features/ics_driver_install.feature')


@then(datatable("the user should identify the following services running:"))
def identify_running_services(table):
    for row in table:
        Services.validate_service_status(row['Service name'])


@then(datatable("the user should identify the following files present on the system:"))
def identify_configuration_files(table, empower_configuration: EmpowerConfiguration):
    not_found_paths = []
    for row in table:
        file_path = row['File']
        logger.info(f"Checking if {file_path} exists..")

        file_path = file_path.replace("%empower%", empower_configuration.install_path) \
            .replace("%temp%", gettempdir())

        result = glob.glob(file_path)
        if not result:
            not_found_paths.append(file_path)

    assert not not_found_paths, f"Paths: [{not_found_paths}] was not found."

@then(cfparse('the user should identify the "{instrument_name}" instrument in the registries'))
def identify_instrument_in_registries(instrument_name: str):
    assert is_instrument_installed(instrument_name), f"Instrument: '{instrument_name}' was not found in registries."


@then(datatable("the user should identify the following registry values:"))
def identify_registry_values(table):
    for row in table:
        given_registry_key = row['Registry Key']
        given_registry_name = row['Registry Name']
        given_registry_data = row['Registry Data']

        logger.info(f"Checking if Registry - Data: {given_registry_data}, Name: {given_registry_name} and Key: {given_registry_key} exists in registries.")

        received_registry_data = get_registry_key_value(reg_name=given_registry_name, key=given_registry_key)
        if "=" in given_registry_data:
            logger.debug(f"Checking for equal. Received registry data: {received_registry_data} compared to data from FF: {given_registry_data}")
            assert str(given_registry_data).replace("=", "") == received_registry_data, logger.error(
                f"Registry - Data: {given_registry_data}, Name: {given_registry_name} or Key: {given_registry_key} not found.")
        else:
            logger.debug(f"Checking for containing. Received registry data: {received_registry_data} compared to data from FF: {given_registry_data}")
            assert given_registry_data in received_registry_data, logger.error(
                f"Registry - Data: {given_registry_data}, Name: {given_registry_name} or Key: {given_registry_key} not found.")
