import os
import sys
import threading

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.constants import *
from utils.helper import Helper
from libraries.simulate_slave import SlaveSimulation
from utils.update_json import JSONHandler


class SimulateJSONData:
    def __init__(self, json_file_path):
        """
        Initialize the SimulateJSONData class.
        :param json_file_path: Path to the JSON file.
        """
        self.json_handler = JSONHandler(json_file_path)
        self.slave = SlaveSimulation()
        self.helper = Helper()
        self.simulation_dict = self.json_handler.read_json()
    def update_temeprature_zone(self,channel,simulation=True,value=None):
        """
        Update the temperature zone data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "TZ1").
        :param simulation: If True, generate random temperature zone values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            # get_current_value_in_reg = get_reg - 0
            # update_the_value = update_bit(get_current_value_in_reg,position,value)
            value = self.slave.set_temperature_zone(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=TZ,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating temperature zone: {e}")
    def update_temperature_sensing(self, channel, simulation=True, value=None):
        """
        Update the temperature sensing data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "TS1").
        :param simulation: If True, generate random temperature values.
        :param value: The value to set if simulation is disabled.
        """
        # try:
        if self.simulation_dict is None:
            raise ValueError("Simulation dictionary is not initialized.")
        else:

            value = self.slave.set_temperature(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=TS,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        # except Exception as e:
        #     print(f"Error updating temperature sensing: {e}")

    def update_tachometer_sensing(self, channel, simulation=True, value=None):
        """
        Update the tachometer sensing data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "TACHO1").
        :param simulation: If True, generate random tachometer values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            value = self.slave.set_taco_monitor(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=TM,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating tachometer sensing: {e}")

    def update_fault_monitoring(self, channel, simulation=True, value=None):
        """
        Update the fault monitoring data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "FAULT1").
        :param simulation: If True, generate random fault values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            
            value = self.slave.set_fault_monitor(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=FM,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating fault monitoring: {e}")

    def update_current_sensing(self, channel, simulation=True, value=None):
        """
        Update the current sensing data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "CS1").
        :param simulation: If True, generate random current values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            
            value = self.slave.set_current_sensing(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=CS,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating current sensing: {e}")

    def update_power_sensing(self, channel, simulation=True, value=None):
        """
        Update the power sensing data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "PS1").
        :param simulation: If True, generate random power values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            
            value = self.slave.set_power_sensing(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=PS,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating power sensing: {e}")

    def update_pwm_generator(self, channel, simulation=True, value=None):
        """
        Update the PWM generator data in the JSON file and simulate the Modbus slave.
        :param channel: The channel to update (e.g., "PWM1").
        :param simulation: If True, generate random PWM values.
        :param value: The value to set if simulation is disabled.
        """
        try:
            
            value = self.slave.set_pwm_generator(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=PWMG,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error updating PWM generator: {e}")

    def update_fan_open_load_enable(self, channel, simulation=True, value=None):
        """
        Retrieve the fan open load enable status from the JSON file.
        :param channel: The channel to retrieve (e.g., "FOLE1").
        :param simulation: If True, generate random fan open load enable values.
        :param value: The value to set if simulation is disabled.
        :return: The fan open load enable status.
        """
        try:
            
            value = self.slave.set_fan_open_load_enable(TS1, True, 22)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=FOLE,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error retrieving fan open load enable status: {e}")

    def update_fan_diagnostic_enable(self, channel, simulation=True, value=None):
        """
        Retrieve the fan diagnostic enable status from the JSON file.
        :param channel: The channel to retrieve (e.g., "FDE1").
        :param simulation: If True, generate random fan diagnostic enable values.
        :param value: The value to set if simulation is disabled.
        :return: The fan diagnostic enable status.
        """
        try:
            
            value = self.slave.set_fan_diagnostic_enable(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=FDE,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value
        except Exception as e:
            print(f"Error retrieving fan diagnostic enable status: {e}")

    def update_fan_enable(self, channel, simulation=True, value=None):
        """
        Retrieve the fan enable status from the JSON file.
        :param channel: The channel to retrieve (e.g., "FE1").
        :param simulation: If True, generate random fan enable values.
        :param value: The value to set if simulation is disabled.
        :return: The fan enable status.
        """
        try:
            
            value = self.slave.set_fan_enable(simulation, channel, value)
            self.helper.update_simulation_dict(
                self.simulation_dict,
                channel_name=FE,
                channel=channel,
                simulation=simulation,
                value=value,
            )
            return value

        except Exception as e:
            print(f"Error retrieving fan enable status: {e}")

    def simulate_all_fan_modules(self, channel_name, channel_list, start, end):
        """
        Simulate data for a list of channels.
        :param channel_list: List of channels to simulate data for.
        :param start: Start of the range for random values.
        :param end: End of the range for random values.
        """
        while True:
            self.update_temperature_sensing(channel_name, channel_list, start, end)


if __name__ == "__main__":
    # Example usage
    json_file_path = JSON_FILE_PATH

    # Initialize the simulation class
    simulator = SimulateJSONData(json_file_path)

    server_thread = threading.Thread(
        target=simulator.simulate_all_fan_modules, daemon=False
    )
    simulator.slave.slave.run_server()

    simulator.update_temperature_sensing(TS1, simulation=True, value=25)
    simulator.update_temperature_sensing(TS1, simulation=False, value=25)
    simulator.update_tachometer_sensing(TM1, simulation=True, value=100)
    simulator.update_tachometer_sensing(TM1, simulation=False, value=100)
    simulator.update_fault_monitoring(FM1, simulation=True, value=1)
    simulator.update_fault_monitoring(FM1, simulation=False, value=0)
    # simulator.update_current_sensing(CS1, simulation=True, value=10)
    # simulator.update_current_sensing(CS1, simulation=False, value=10)
    # simulator.update_power_sensing(PS1, simulation=True, value=100)
    # simulator.update_power_sensing(PS1, simulation=False, value=100)
    # simulator.update_pwm_generator(PWMG1, simulation=True, value=50)
    # simulator.update_pwm_generator(PWMG1, simulation=False, value=50)
    # simulator.update_fan_open_load_enable(FOLE1, simulation=True, value=1)
    # simulator.update_fan_open_load_enable(FOLE1, simulation=False, value=0)
    # simulator.update_fan_diagnostic_enable(FDE1, simulation=True, value=1)
    # simulator.update_fan_diagnostic_enable(FDE1, simulation=False, value=0)
    # simulator.update_fan_enable(FE1, simulation=True, value=1)
    # simulator.update_fan_enable(FE1, simulation=False, value=0)
    
