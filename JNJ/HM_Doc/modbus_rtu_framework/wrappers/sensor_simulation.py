import pandas as pd
import random
from libraries.modbus_slave import ModbusSlave
from utils.excel_parser import read_registers_from_excel
from utils.constants import *
from libraries.simulate_slave import SensorSimulation as SS


class SensorSimulation:
    def __init__(self, slave):
        """
        Initialize the SensorSimulation wrapper.
        :param master: Instance of ModbusMaster to communicate with the slave.
        :param excel_file_path: Path to the Excel file containing sensor data.
        """
        self.slave = slave
        self.channel = read_registers_from_excel(DATA_FILE_PATH, REQUIRED_COLUMNS)

    def set_default_register_values(self, channels):
        """
        Set default values for all registers.
        :param channel: Channel object containing register information.
        :param reg_type: Register type (e.g., 'hr', 'ir', etc.).
        """
        

        try:
            # Set default values for the specified register type
            for channel in channels:
                df = df.loc[channel]

                ModbusSlave.set_values(
                    channel["reg_type"],
                    channel["reg_address"],
                    channel["default_value"],
                )
        except Exception as e:
            print(f"Error setting default register values: {e}")

    def get_random_values(self, start, end, count):
        """
        Generate a list of random values within a specified range.
        :param start: Start of the range.
        :param end: End of the range.
        :param count: Number of random values to generate.
        :param return: List of random values within the specified range.
        """
        try:
            return [random.randint(start, end) for _ in range(count)]
        except Exception as e:
            print(f"Error generating random values: {e}")
            return None

  
    
    def set_temperature_values(self, temparature, start_address):
        # get the random temperature values from the excel file
        temperature_values = [
            self.get_random_values(
                temparature["min_value"],
                temparature["max_value"],
                len(temperature_values),
            )
        ]
        for i in range(len(temperature_values)):
            ModbusSlave.set_values("hr", start_address + i, temperature_values[i])
        print(
            f"Set temperature values: {temperature_values} at address {start_address}"
        )

    def set_tachometer_values(self, taco_monitor, start_address):
        # get the random tachometer values from the excel file
        tachometer_values = [
            self.get_random_values(
                taco_monitor["min_value"],
                taco_monitor["max_value"],
                len(tachometer_values),
            )
        ]
        for i in range(len(tachometer_values)):
            ModbusSlave.set_values("hr", start_address + i, tachometer_values[i])
        print(f"Set tachometer values: {tachometer_values} at address {start_address}")

    def set_fault_monitor_values(self, fault_monitor, start_address):
        # get the random fault monitor values from the excel file
        fault_monitor_values = [
            self.get_random_values(
                fault_monitor["min_value"],
                fault_monitor["max_value"],
                len(fault_monitor_values),
            )
        ]
        for i in range(len(fault_monitor_values)):
            ModbusSlave.set_values("hr", start_address + i, fault_monitor_values[i])
        print(
            f"Set fault monitor values: {fault_monitor_values} at address {start_address}"
        )

    def set_current_sensing_values(self, current_sensing, start_address):
        # get the random current sensing values from the excel file
        current_sensing_values = [
            self.get_random_values(
                current_sensing["min_value"],
                current_sensing["max_value"],
                len(current_sensing_values),
            )
        ]
        for i in range(len(current_sensing_values)):
            ModbusSlave.set_values("hr", start_address + i, current_sensing_values[i])
        print(
            f"Set current sensing values: {current_sensing_values} at address {start_address}"
        )

    def set_power_sensing_values(self, power_sensing, start_address):
        # get the random power sensing values from the excel file
        power_sensing_values = [
            self.get_random_values(
                power_sensing["min_value"],
                power_sensing["max_value"],
                len(power_sensing_values),
            )
        ]
        for i in range(len(power_sensing_values)):
            ModbusSlave.set_values("hr", start_address + i, power_sensing_values[i])
        print(
            f"Set power sensing values: {power_sensing_values} at address {start_address}"
        )
    
    def set_temperature_values(self, temperature, start_address, values):
        pass
        

if __name__ == "__main__":
    # Example usage
    modbus_slave = ModbusSlave()
    sensor_simulation = SensorSimulation(modbus_slave, "files\\data.xlsx")

