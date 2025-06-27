class Helper:
    @staticmethod
    def value_to_bits(value, bit_length=16):
        """
        Convert an integer value to its binary representation with a fixed bit length.
        :param value: The integer value to convert.
        :param bit_length: The number of bits to represent the value.
        :return: A binary string representation of the value.
        """
        return f"{value:0{bit_length}b}"

    @staticmethod
    def update_bit(value, bit_position, bit_value):
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

    @staticmethod
    def bits_to_value(bits):
        """
        Convert a binary string back to its integer value.
        :param bits: The binary string representation.
        :return: The integer value.
        """
        return int(bits, 2)


if __name__ == "__main__":
    helper = Helper()

    # Step 1: Convert the value 20 into a 16-bit binary representation
    original_value = 14
    bit_position = 1  # 0-15
    bit_value = 1  # 0 or 1
    binary_representation = helper.value_to_bits(original_value)
    print(f"Original Value: {original_value} ({binary_representation})")

    # Step 2: Update the 0th bit (LSB) to 1
    updated_value = helper.update_bit(original_value, 0, 1)
    updated_binary_representation = helper.value_to_bits(updated_value)
    print(f"Updated Value: {updated_value} ({updated_binary_representation})")

    # Step 3: Convert the updated binary representation back to an integer
    final_value = helper.bits_to_value(updated_binary_representation)
    print(f"Final Value: {final_value} (after updating the bit)")

    # Step 4: Write the updated value back to the register (simulated here)
    print(f"Writing {final_value} back to the register...")