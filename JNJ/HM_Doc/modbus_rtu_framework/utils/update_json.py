import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
from utils.constants import *
import random


class JSONHandler:
    def __init__(self, file_path):
        """
        Initialize the JSONHandler with the path to the JSON file.
        :param file_path: Path to the JSON file.
        """
        self.file_path = file_path

    def read_json(self):
        """
        Read and return the contents of the JSON file.
        :return: Parsed JSON data as a dictionary.
        """
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file {self.file_path}: {e}")
            return None

    def write_json(self, data):
        """
        Write the provided data to the JSON file.
        :param data: Dictionary to write to the JSON file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(data, file, indent=4)
                # print(f"Successfully updated JSON file at {self.file_path}")
        except Exception as e:
            print(f"Error writing JSON to file {self.file_path}: {e}")

    def update_simulation_data_to_json(
        self, channel_name, channel, simulation_value, value
    ):
        """
        Update the simulation value for a specific channel in the JSON file.
        :param channel_name: The name of the channel (e.g., "TEMPERATURE_SENSING").
        :param channel: The channel to update (e.g., "TS1").
        :param simulation_value: The new simulation value (True/False).
        :param value: The new value to set for the channel.
        """
        # Read the existing data from the JSON file
        data = self.read_json()
        if data is not None:
            try:
                # Update the simulation value for the specified channel
                data[channel_name][channel]["simulation"] = simulation_value
                data[channel_name][channel]["value"] = value
                self.write_json(data)
                print(
                    f"Updated simulation value for {channel} to simulation: {simulation_value}, value: {value}"
                )
            except KeyError as e:
                print(f"Error: Key not found in JSON data: {e}")

    def update_simulation(self, channel_name, channel, simulation_value, value):
        """
        Update the simulation value for a specific channel in the JSON file.
        :param channel_name: The name of the channel (e.g., "TEMPERATURE_SENSING").
        :param channel: The channel to update (e.g., "TS1").
        :param simulation_value: The new simulation value (True/False).
        :param value: The new value to set for the channel.
        """

        # Read the existing data from the JSON file
        data = self.read_json()
        if data is not None:
            try:
                print("before update", data[channel_name][channel])
                # Update the simulation value for the specified channel
                data[channel_name][channel]["simulation"] = simulation_value
                data[channel_name][channel]["value"] = value
                print(
                    f"Updated simulation value for {channel} to simulation: {simulation_value}, value: {value}"
                )
                print("after update", data[channel_name][channel])
            except KeyError as e:
                print(f"Error: Key not found in JSON data: {e}")

    def simulate_data(self, channel_name, channel_list, start, end):
        """
        Simulate data for a list of channels.
        :param channel_list: List of channels to simulate data for.
        :param start: Start of the range for random values.
        :param end: End of the range for random values.
        """
        for channel in channel_list:
            # print(f"Simulating data for {channel}")
            value = random.randint(start, end)
            simulation = random.choice([True, False])
            json_handler.update_simulation_data_to_json(
                channel_name, channel, simulation, value
            )


if __name__ == "__main__":
    # Example usage
    json_handler = JSONHandler(JSON_FILE_PATH)

    # Update the simulation value for a specific channel
    temp_channel = [TS1, TS2, TS3, TS4]
    taco_channel = [TM1, TM2, TM3, TM4, TM5, TM6, TM7, TM8, TM9, TM10, TM11, TM12]
    fault_channel = [FM1, FM2, FM3]

    json_handler.simulate_data(TS1[:-1], temp_channel, -10, 20)
    json_handler.simulate_data(TM1[:-1], taco_channel, 0, 1400)
    json_handler.simulate_data(FM1[:-1], fault_channel, 0, 1)

    # json_handler.update_simulation(
    #     channel_name=TS,
    #     channel=TS1,
    #     simulation_value=True,
    #     value=0,
    # )
