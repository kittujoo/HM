import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
import time
import threading

from config.logger import logger
from libraries.modbus_slave import ModbusSlave
from utils.excel_parser import read_registers_from_excel, save_df
from utils.constants import *
from utils.constants import DATA_FILE_PATH, REQUIRED_COLUMNS, REFRESH_RATE
from utils.helper import Helper


class SimulateModbusSlave:
    def __init__(
        self,
        port="COM3",
        baudrate=9600,
        stopbits=1,
        bytesize=8,
        parity="N",
        timeout=1,
        slave_ids=[1],
        excel_file=DATA_FILE_PATH,
        required_columns=REQUIRED_COLUMNS,
    ):
        """
        Initialize the Modbus slave with default configurations.
        """
        self.data = read_registers_from_excel(excel_file, required_columns)
        self.data["reg_value_simulation"] = 1  # Enable simulation by default
        self.data["reg_value_slave"] = 1  # Enable simulation by default
        self.slave = ModbusSlave(
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity,
            timeout=timeout,
            slave_ids=slave_ids,
        )
        self.helper = Helper()
        self.before_signed = None
        self.bit_value = None
        self.simulate_modbus_slave = None
        self.simulation_thread = None
        self.running = False

    def get_channel_data(self, channel, column_name):
        """
        Get data for a specific channel and column from the DataFrame.
        :param channel: The channel to retrieve data for.
        :param column_name: The column name to retrieve data from.
        :return: The value from the DataFrame for the specified channel and column.
        :raises KeyError: If the channel or column_name is not found in the DataFrame.
        """
        try:
            return self.data.loc[channel, column_name]
        except KeyError:
            raise (f"Channel {channel} or column {column_name} not found in data.")

    def resulation_updation(self, channel, value):
        """
        Update the resolution of the channel.
        :param channel: The channel to update.
        :param value: The value to set for the channel.
        :return: The updated value after applying the resolution.
        """
        try:
            return int(value * self.get_channel_data(channel, "resolution"))
        except KeyError:
            raise (f"Channel {channel} or resolution not found in data.")

    def update_ui_dict(self, simulation, channel, value):
        """
        Update the UI dictionary with the new value for the specified channel.
        :param simulation: If True, update the value in simulation mode.
        :param channel: The channel to update.
        :param value: The value to set for the channel.
        :return: The updated value for the channel after applying simulation logic.
        :raises KeyError: If the channel is not found in the DataFrame.
        """
        try:
            if simulation:
                self.data.loc[channel, "simulation"] = simulation
                return self.data.loc[channel, "simulation"], self.get_channel_data(
                    channel, "reg_value"
                )
            else:
                self.data.loc[channel, "simulation"] = simulation
                self.data.loc[channel, "reg_value"] = value
                return (
                    self.data.loc[channel, "simulation"],
                    self.data.loc[channel, "reg_value"],
                )

        except KeyError:
            raise (f"Channel {channel} not found in data.")

    def update_ui_checks_bit_value(self, channel, value, before_signed):
        try:
            if self.data.loc[channel, "reg_bit_flag"] < REG_BIT_FLAG:
                self.data.loc[channel, "reg_value"] = self.bit_value
                self.data.loc[
                    self.data["reg_address"]
                    == (self.get_channel_data(channel, "reg_address")),
                    "reg_value_simulation",
                ] = value
            elif before_signed != value:
                self.data.loc[channel, "reg_value"] = before_signed
                self.data.loc[
                    self.data["reg_address"]
                    == (self.get_channel_data(channel, "reg_address")),
                    "reg_value_simulation",
                ] = value
            else:
                self.data.loc[channel, "reg_value"] = value
                self.data.loc[
                    self.data["reg_address"]
                    == (self.get_channel_data(channel, "reg_address")),
                    "reg_value_simulation",
                ] = value
        except Exception as e:
            logger.error(
                f"Error updating UI checks bit value for channel {channel}: {e}"
            )
            raise (f"Error updating UI checks bit value for channel {channel}: {e}")

    def update_slave_regs(self, channel, slave_id=1, value=None):
        """
        Update the Modbus slave registers for a specific channel.
        :param channel: The channel to update.
        :param value: The value to set for the channel.
        :return: The updated value for the channel after applying simulation logic.
        :raises KeyError: If the channel is not found in the DataFrame.
        """
        try:
            # Check if the channel is in simulation mode
            if self.data.loc[channel, "simulation"]:

                # If the channel is in simulation mode, generate a random value
                if self.data.loc[channel, "reg_bit_flag"] < REG_BIT_FLAG:
                    # Generate a random value within the specified range
                    self.bit_value = self.helper.get_random_value(
                        self.get_channel_data(channel, "min_value"),
                        self.get_channel_data(channel, "max_value"),
                    )
                    # Update the bit value in the register value
                    value = self.helper.update_bit(
                        self.get_channel_data(channel, "reg_value_simulation"),
                        self.get_channel_data(channel, "reg_bit_flag"),
                        self.bit_value,
                    )
                else:
                    value = self.helper.get_random_value(
                        self.get_channel_data(channel, "min_value"),
                        self.get_channel_data(channel, "max_value"),
                    )

                # Convert to 16-bit signed integer if necessary
                before_signed = value
                value = self.helper.convert_to_16bit_signed(value)
                # Update the simulation data in the DataFrame
                value = self.resulation_updation(channel, value)
            else:
                value = self.get_channel_data(channel, "reg_value")

            self.update_ui_checks_bit_value(
                channel, value, before_signed
            )  # Update the UI dictionary

            self.slave.set_values(
                self.data.loc[channel, "reg_type"],
                self.data.loc[channel, "reg_address"],
                [value],
                slave_id=slave_id,
            )
            logger.info(
                f"Updated slave registers for channel: {channel}, reg_value: {value}, UI_value: {self.data.loc[channel, "reg_value"]}"
            )
        except KeyError:
            logger.error(f"Channel {channel} not found in data.")
            raise (f"Channel {channel} not found in data.")

    def set_default_values(self, slave_id=1):
        """
        Set default values for the registers in the Modbus slave.
        This method initializes the registers with default values from the DataFrame.
        """
        for channel in self.data.index:
            try:
                # Set default values for each channel
                self.data.loc[channel, "reg_value"] = self.data.loc[
                    channel, "default_value"
                ]
                self.slave.set_values(
                    self.data.loc[channel, "reg_type"],
                    self.data.loc[channel, "reg_address"],
                    [self.data.loc[channel, "default_value"]],
                    slave_id=slave_id,
                )

            except Exception as e:
                logger.error(f"Error setting default value for {channel}: {e}")
        logger.info(
            f"Successfully upadetd the default values: {self.data["reg_value"].to_dict()}"
        )

    def get_slave_data(self, channel, slave_id=1, address_count=1):
        """
        Get the current value from the Modbus slave for a specific channel.
        :param channel: The channel to retrieve data for.
        :return: The current value from the Modbus slave for the specified channel.
        :raises KeyError: If the channel is not found in the DataFrame.
        """

        reg_value = self.slave.get_values(
            self.get_channel_data(channel, "reg_type"),
            self.get_channel_data(channel, "reg_address"),
            address_count,
            slave_id=slave_id,
        )[0]
        self.data.loc[channel, "reg_value_slave"] = (
            reg_value  # Update the DataFrame with the slave value
        )
        logger.info(f"Channel: {channel}, Value from slave: {reg_value}")
        return reg_value

    def simulate_data(self, slave_id=1):
        """
        Simulate the data continuously for the given channels.
        :param channels: List of channels to simulate data for.
        """

        for channel in self.data.index:
            self.update_slave_regs(
                channel=channel, slave_id=slave_id
            )  # Update the slave registers for each channel
        time.sleep(REFRESH_RATE)

    def start_simulation(self, set_defaults=True,slave_id=1 ):
        """Start the simulation in a background thread."""
        self.slave.start_server()  # Start the Modbus server
        if set_defaults:
            self.set_default_values(slave_id=slave_id)  # Set default values before starting simulation
        if self.running:
            logger.info("Simulation already running.")
            return
        self.running = True
        self.simulation_thread = threading.Thread(
            target=self._run_simulation, args=(slave_id,), daemon=True
        )
        self.simulation_thread.start()
        logger.info("Simulation started.")

    def _run_simulation(self,slave_id=1):
        while self.running:
            self.simulate_data(slave_id=slave_id)

    def stop_simulation(self):
        """Stop the simulation thread."""
        if not self.running:
            logger.info("Simulation is not running.")
            return
        self.running = False
        if self.simulation_thread:
            self.simulation_thread.join(timeout=2)
            logger.info("Simulation stopped.")
            self.slave.stop_server()  # Stop the Modbus server

if __name__ == "__main__":
    pass
    # ########### SIMULATION STEPS ###########
    # # start the UI thread
    # # start the SLAVE thread
    # # start the SERVER thread

    # ############# Function Test Start ###########
    # # ================================================================================

    # Initialize the SimulateModbusSlave class
    # try:
    #     while True:
    #         sds = SimulateModbusSlave(port="COM3", slave_ids=[2])
    #         sds1 = SimulateModbusSlave(port="COM5", slave_ids=[2])
    #         sds.slave.start_server()  # Start the Modbus server
    #         sds1.slave.start_server()
    #         time.sleep(3)  # Wait for the server to start
    #         sds.set_default_values(slave_id=2)  # Set default values for the registers
    #         sds1.set_default_values(slave_id=2)  # Set default values for the registers
    #         # logger.info(sds.slave.stores)
    #         time.sleep(3)  # Wait for the server to start
    #         for i in range(300):
    #             sds.simulate_data(slave_id=2)  # Simulate data for the first slave
    #             sds1.simulate_data(slave_id=2)  # Simulate data for the second slave
    #             time.sleep(2)
    #         sds.slave.stop_server()  # Start the Modbus server
    #         sds1.slave.stop_server()
    # except KeyboardInterrupt as e:
    #     # Handle keyboard interrupt to stop the simulation gracefully
    #     logger.info("Simulation stopped by user.")

    # finally:
    #     sds.slave.stop_server()
    #     sds1.slave.stop_server()

    # ############# Function Test End ###########
    # # ================================================================================
    
    
    # ############# Simulation in thread ###########
    # # ================================================================================
    # sm1 = SimulateModbusSlave(port="COM3", slave_ids=[1])
    # sm1.start_simulation(set_defaults=True, slave_id=1)  # Start the simulation with default values
    # time.sleep(5)  # Allow some time for the simulation to run
    # sm1.stop_simulation()  # Stop the simulation gracefully
    # # ================================================================================
