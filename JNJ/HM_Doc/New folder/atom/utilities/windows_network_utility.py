import subprocess
import time
import psutil
import os
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


class WindowsNetworkManagement:
    @staticmethod
    def get_network_interfaces():
        """
        Get a list of all network interfaces.

        Returns:
            list: A list of network interface names.
        """
        # Get a list of all network interfaces
        all_interfaces = psutil.net_if_addrs()
        interfaces = []

        for interface_name, interface_addresses in all_interfaces.items():
            interfaces.append(interface_name)
        return interfaces

    @staticmethod
    def toggle_network_interface(interface_name, enable=True, waiting_time=10):
        """
        Enable or disable a network interface.

        Args:
            interface_name (str): The name of the network interface.
            enable (bool): If True, enable the network interface; otherwise, disable it.
            waiting_time (int): Waiting time for os to enable or disable the network card
        """
        action = "enable" if enable else "disable"

        try:
            # Construct the PowerShell command to enable or disable the network interface
            powershell_command = f"{action}-NetAdapter -Name '{interface_name}'"

            # Use subprocess.Popen with stdout=PIPE and stderr=PIPE to capture output
            process = subprocess.Popen(['powershell', '-Command', powershell_command],
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE,
                                       text=True)

            # Send "Y" as input to confirm
            process.communicate(input="Y\n")

            # Wait for the process to finish
            process.wait()

            # Check if the network card was enabled or disabled in a time interval
            command_was_executed = False
            seconds_past = 0
            while ~command_was_executed:
                time.sleep(1)
                seconds_past += 1
                network_card_exist = WindowsNetworkManagement.check_network_card_availability(interface_name)
                if action == "enable":
                    if network_card_exist:
                        command_was_executed = True
                else:
                    if ~network_card_exist:
                        command_was_executed = True

                if seconds_past >= waiting_time:
                    break

            if command_was_executed:
                logger.info(f"Successfully {action}d network interface: {interface_name}")
            else:
                logger.info(f"Error {action}ing network interface: {interface_name}")

        except subprocess.CalledProcessError as e:
            logger.info(f"Error {action}ing network interface: {e}")

    @staticmethod
    def check_network_card_availability(interface_name):
        """
        Check if a network card is available or not.

        Args:
            interface_name (str): The name of the network interface.

        Return:
            True if is available, False otherwise.
        """
        network_interface_exist = False
        network_interfaces = WindowsNetworkManagement.get_network_interfaces()
        for network_interface in network_interfaces:
            if network_interface == interface_name:
                network_interface_exist = True
                break
        return network_interface_exist
