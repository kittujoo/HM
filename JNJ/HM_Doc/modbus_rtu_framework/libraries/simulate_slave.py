import random
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.constants import *
from utils.excel_parser import read_registers_from_excel
from utils.helper import Helper
from libraries.modbus_slave import ModbusSlave


class SlaveSimulation:
    def __init__(self):
        """
        Initialize the SlaveSimulation class.
        """
        self.simulation_enabled = True  # Enable simulation by default
        self.sensor_data = {}  # Store sensor data for each channel
        self.sensor = read_registers_from_excel(DATA_FILE_PATH, REQUIRED_COLUMNS)
        self.slave = ModbusSlave()
        self.helper = Helper()

    def set_temperature(self, simulation, channel, value):
        """
        Simulate or set temperature values for a specific channel.
        :param simulation: If True, generate random temperature values.
        :param channel: The channel number for the temperature sensor.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the temperature sensor.
        """
        channel = self.sensor.loc[channel]

        if simulation:

            value = self.helper.get_random_value(
                channel["min_value"], channel["max_value"]
            )

        if not (-32768 <= value <= 32767):
            raise ValueError("Value out of range for 16-bit signed integer.")
        # Convert to unsigned 16-bit integer
        value = value if value >= 0 else (1 << 16) + value

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_taco_monitor(self, simulation, channel, value):
        """
        Simulate or set tachometer values for a specific channel.
        :param simulation: If True, generate random tachometer values.
        :param channel: The channel number for the tachometer sensor.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the tachometer.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_fault_monitor(self, simulation, channel, value):
        """
        Set the fan fault status for a specific channel.
        :param channel: The channel number for the fan fault sensor.
        :param value: The value to set (0 for no fault, 1 for fault).
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])
        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_current_sensing(self, simulation, channel, value):
        """
        Simulate or set current sensing values for a specific channel.
        :param simulation: If True, generate random current sensing values.
        :param channel: The channel number for the current sensing sensor.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the current sensing sensor.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_power_sensing(self, simulation, channel, value):
        """
        Simulate or set power sensing values for a specific channel.
        :param simulation: If True, generate random power sensing values.
        :param channel: The channel number for the power sensing sensor.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the power sensing sensor.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_pwm_generator(self, simulation, channel, value):
        """
        Simulate or set PWM generator values for a specific channel.
        :param simulation: If True, generate random PWM values.
        :param channel: The channel number for the PWM generator.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the PWM generator.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_fan_open_load_enable(self, simulation, channel, value):
        """
        Simulate or set fan open load enable values for a specific channel.
        :param simulation: If True, generate random fan open load enable values.
        :param channel: The channel number for the fan open load enable.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the fan open load enable.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_fan_diagnostic_enable(self, simulation, channel, value):
        """
        Simulate or set fan diagnostic enable values for a specific channel.
        :param simulation: If True, generate random fan diagnostic enable values.
        :param channel: The channel number for the fan diagnostic enable.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the fan diagnostic enable.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def set_fan_enable(self, simulation, channel, value):
        """
        Simulate or set fan enable values for a specific channel.
        :param simulation: If True, generate random fan enable values.
        :param channel: The channel number for the fan enable.
        :param value: The value to set if simulation is disabled.
        :return: The value set for the fan enable.
        """
        channel = self.sensor.loc[channel]
        if simulation:

            value = self.get_random_value(channel["min_value"], channel["max_value"])

        self.slave.set_values(channel["reg_type"], channel["reg_address"], [value])
        return value

    def get_temperature(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the temperature sensor.
        :return: A dictionary containing all sensor data.
        """
        channel = self.sensor.loc[channel]
        temperature = self.slave.get_values(
            channel["reg_type"], channel["reg_address"], 1
        )
        return temperature

    def get_taco_monitor(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the tachometer sensor.
        :return: A dictionary containing all sensor data.
        """
        taco_monitor = self.set_taco_monitor(self.simulation_enabled, channel, None)
        return taco_monitor

    def get_fault_monitor(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the fan fault sensor.
        :return: A dictionary containing all sensor data.
        """
        fault_monitor = self.set_fault_monitor(self.simulation_enabled, channel, None)
        return fault_monitor

    def get_current_sensing(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the current sensing sensor.
        :return: A dictionary containing all sensor data.
        """
        current_sensing = self.set_current_sensing(
            self.simulation_enabled, channel, None
        )
        return current_sensing

    def get_power_sensing(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the power sensing sensor.
        :return: A dictionary containing all sensor data.
        """
        power_sensing = self.set_power_sensing(self.simulation_enabled, channel, None)
        return power_sensing

    def get_pwm_generator(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the PWM generator.
        :return: A dictionary containing all sensor data.
        """
        pwm_generator = self.set_pwm_generator(self.simulation_enabled, channel, None)
        return pwm_generator

    def get_fan_open_load_enable(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the fan open load enable.
        :return: A dictionary containing all sensor data.
        """
        fan_open_load_enable = self.set_fan_open_load_enable(
            self.simulation_enabled, channel, None
        )
        return fan_open_load_enable

    def get_fan_diagnostic_enable(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the fan diagnostic enable.
        :return: A dictionary containing all sensor data.
        """
        fan_diagnostic_enable = self.set_fan_diagnostic_enable(
            self.simulation_enabled, channel, None
        )
        return fan_diagnostic_enable

    def get_fan_enable(self, channel):
        """
        Retrieve simulated sensor data.
        :param channel: The channel number for the fan enable.
        :return: A dictionary containing all sensor data.
        """
        fan_enable = self.set_fan_enable(self.simulation_enabled, channel, None)
        return fan_enable


if __name__ == "__main__":

    sensor_simulation = SlaveSimulation()
#     # Example usage
#     # sensor_simulation.slave.run_server()
#     print(sensor_simulation.get_temperature(TS1))
#     # print(sensor_simulation.get_taco_monitor(TM1))
#     # print(sensor_simulation.get_fault_monitor(FM1))
#     # print(sensor_simulation.get_current_sensing(CS1))
#     # print(sensor_simulation.get_power_sensing(PS))
#     # print(sensor_simulation.set_temperature(True, TS1, None))
#     # print(sensor_simulation.set_temperature(False, TS1, 100))
