import os
import re

import sshtunnel

from utilities.logger import Logger
from utilities.telnet_connection import TelnetConnection

logger = Logger(os.path.basename(__file__))

SSH_PORT = 22
TELNET_PORT = 23


class InstrumentAlarmUtility:
    """Utility used for raising instrument alarms"""

    def __init__(self, hostname, username, password, jump_server_username, jump_server_password, ispp_hostname,
                 isym_hostname, telnet_username, telnet_password, components_config):
        self.hostname = hostname
        self.jump_server_username = jump_server_username
        self.jump_server_password = jump_server_password
        self.ispp_hostname = ispp_hostname
        self.isym_hostname = isym_hostname
        self.telnet_username = telnet_username
        self.telnet_password = telnet_password
        self.username = username
        self.password = password
        self.components_config = components_config

    def raise_instrument_alarm(self, component, alarm_id, *args):
        """Raise an alarm based on the instrument components and alarm name"""
        component_ip = self.get_component_ip(component)
        logger.info(f"Establishing SSH tunneling to ISPP: {self.ispp_hostname}")
        with self.open_ssh_tunnel((self.hostname, SSH_PORT), (self.ispp_hostname, SSH_PORT),
                                  self.jump_server_username,
                                  self.jump_server_password) as tunnel1:
            logger.info(f"Establishing SSH tunneling to ISYM: {self.isym_hostname}")
            with self.open_ssh_tunnel(('localhost', tunnel1.local_bind_port), (self.isym_hostname, SSH_PORT),
                                      self.username,
                                      self.password) as tunnel2:
                logger.info(f"Establishing SSH tunneling to {component}")
                with self.open_ssh_tunnel(('localhost', tunnel2.local_bind_port),
                                          (component_ip, TELNET_PORT),
                                          self.username, self.password) as tunnel3:
                    return self.handle_telnet_connection(tunnel3, alarm_id, *args)

    @staticmethod
    def open_ssh_tunnel(address, remote_bind, username, password):
        """Open an SSH tunnel"""
        try:
            tunnel = sshtunnel.open_tunnel(
                ssh_address_or_host=address,
                remote_bind_address=remote_bind,
                ssh_username=username,
                ssh_password=password
            )
            tunnel.start()
            return tunnel
        except Exception as e:
            logger.error(f"Failed to open SSH tunnel: {e}")
            raise

    def get_component_ip(self, component: str):
        """Get the IP address of a component"""
        try:
            return self.components_config[component.lower()].hostname
        except Exception as e:
            logger.error(f"Failed to get component IP: {e}")
            raise

    def handle_telnet_connection(self, tunnel, alarm_id, *args):
        """Handle Telnet connection and raise alarm"""
        with TelnetConnection("localhost", self.username, self.password, tunnel.local_bind_port) as telnet:
            logger.debug('Connection to Telnet OK...')
            telnet.read_until_console_available()
            telnet.send_command(command="system")
            telnet.read_until_console_available()
            telnet.send_command(command="manager")
            res = str(telnet.read_until_console_available())
            if "CONSOLE" in res:
                alarm_raise_result = self.raise_alarm(telnet, alarm_id, *args)
                return alarm_raise_result
            else:
                logger.error(f"Console is not available: {res}")
                raise

    @staticmethod
    def raise_alarm(telnet, alarm_id, *args):
        """Raise an alarm using a telnet connection"""
        telnet.send_command(command=f"alarmlistcodes {alarm_id}")
        result = telnet.read_until_console_available()
        list_codes_output = result.decode()

        if "[" in list_codes_output and "]" in list_codes_output:
            found_codes = re.findall(r"\[([^\[\]]*?)]", list_codes_output)
            alarm_details = re.findall(r"]\s*([^\[]*?)CONSOLE", list_codes_output)
            internal_code = found_codes[0] if found_codes else 'Alarm id not captured'

            # Parameter count validation - if the number of parameters in the alarm details does not match the number of arguments provided, log a warning
            parameter_count_details = alarm_details[0].count('%')
            if parameter_count_details != len(args):
                logger.warning(
                    f"Number of arguments in alarm details {parameter_count_details} does not match number of arguments provided {len(args)}")

            logger.debug(
                f"Raising alarm with Id: {alarm_id} Internal Id: {internal_code} Alarm details: \"{alarm_details}\" and Arguments: {args}")
            parameters = ["alarmraise", internal_code, *args]
            telnet.send_command(command=" ".join(parameters))
            res = telnet.read_until_console_available()
            logger.debug(f"Alarm raised successfully: {res}")
            return res
        else:
            message = f"Failed to obtain alarm id: {list_codes_output}"
            logger.error(message)
            raise ValueError(message)
