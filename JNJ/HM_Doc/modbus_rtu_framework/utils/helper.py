import random
import string
from datetime import datetime, timedelta


class Helper:

    def __init__(self):
        pass

    def get_random_value(self, start, end):
        """
        Generate a list of random values within a specified range.
        :param start: Start of the range.
        :param end: End of the range.
        :param return: List of random values within the specified range.
        """
        try:
            return random.randint(start, end)
        except Exception as e:
            print(f"Error generating random values: {e}")
            return None

    def update_simulation_dict(
        self, dict_name, channel_name, channel, simulation, value
    ):
        """
        Simulate data for a list of channels.
        :param dict_name: Dictionary to update.
        :param channel_name: Name of the channel to update.
        :param channel: The channel to update (e.g., "TS1").
        :param simulation: The new simulation value (True/False).
        :return: The new value to set for the channel.
        """
        try:
            # print(f"before update channel_name: {channel_name}, channel: {channel}, simulation: {simulation}, value: {value}")
            # Update the simulation value for the specified channel
            dict_name[channel_name][channel]["simulation"] = simulation
            dict_name[channel_name][channel]["value"] = value

            # print(f"after update channel_name: {channel_name}, channel: {channel}, simulation: {simulation}, value: {value}")
        except Exception as e:
            print(f"Error updating simulation dictionary: {e}")
            return None

    def update_bit(self, value, bit_position, bit_value):
        """
        Update a specific bit in an integer value.
        :param value: The original integer value.
        :param bit_position: The position of the bit to update (0-based, from the right).
        :param bit_value: The new value of the bit (0 or 1).
        :return: The updated integer value.
        """
        if bit_value not in (0, 1):
            raise ValueError("bit_value must be 0 or 1")

        if bit_value == 1:
            # Set the bit
            return value | (1 << bit_position)
        else:
            # Clear the bit
            return value & ~(1 << bit_position)

    def convert_to_16bit_signed(self, value):
        """
        Convert a value to a 16-bit signed integer.
        :param value: The value to convert.
        :return: The converted value as a 16-bit signed integer.
        """
        if not (-32768 <= value <= 32767):
            raise ValueError("Value out of range for 16-bit signed integer.")
        return value if value >= 0 else (1 << 16) + value
    
if __name__ == "__main__":
    helper = Helper()
    original_value = 3
    bit_position = 0  # 0-15
    bit_value = 0  # 0 or 1
    
    #0000 0000 0000 0100
    #0000 0000 0000 0110
    

    updated_value = helper.update_bit(original_value, bit_position, bit_value)
    print(f"Original Value: {original_value}, Updated Value: {updated_value}")
