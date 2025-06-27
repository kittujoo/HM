import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pymodbus.client import ModbusSerialClient
from config.logger import logger


class ModbusMaster:
    def __init__(
        self, port="COM4", baudrate=9600, stopbits=1, bytesize=8, parity="N", timeout=1
    ):
        self.client = None
        self.port = port
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.parity = parity
        self.timeout = timeout
        

    def connect(self):
        
        """
        Connect to the Modbus slave.
        :return: True if connection is successful, False otherwise.
        """
        """
        Initialize the Modbus master with default configurations.
        """
        self.client = ModbusSerialClient(
            port=self.port,
            baudrate=self.baudrate,
            stopbits=self.stopbits,
            bytesize=self.bytesize,
            parity=self.parity,
            timeout=self.timeout,
        )
        logger.info(f"Connecting to Modbus slave on {self.port}...")
        if self.client.is_socket_open():
            logger.info("Socket is already open.")
            return True                                             
        return self.client.connect()

    def write_registers(self, register_type, address, values, slave_id=1):
        """
        Write values to the specified register type.
        :param register_type: Register type ('co', 'hr').
        :param address: Starting address to write values.
        :param values: List of values to write.
        :return: True if successful, False otherwise.
        """
        try:
            if register_type == "CO":
                result = self.client.write_coils(address=address, values=values, slave=slave_id)
            elif register_type == "HR":
                result = self.client.write_registers(address=address, values=values, slave=slave_id)
            else:
                raise ValueError(f"Invalid register type: {register_type}")

            return result 
        except Exception as e:
            logger.info(f"Error writing to {register_type} at address {address}: {e}")
            return False


    def read_registers(self, register_type, address, count, slave_id=1):
        """
        Read values from the specified register type.
        :param register_type: Register type ('di', 'co', 'hr', 'ir').
        :param address: Starting address to read values.
        :param count: Number of values to read.
        :return: List of values if successful, None otherwise.
        """
        try:
            if register_type == "DI":
                result = self.client.read_discrete_inputs(
                   address=address, count=count, slave=slave_id
                )
            elif register_type == "CO":
                result = self.client.read_coils(address=address, count=count, slave=slave_id)
            elif register_type == "HR":
                result = self.client.read_holding_registers(
                    address=address, count=count, slave=slave_id
                )
            elif register_type == "IR":
                result = self.client.read_input_registers(
                    address=address, count=count, slave=slave_id
                )
            else:
                raise ValueError(f"Invalid register type: {register_type}")

            if result.isError():
                return None
            return result.bits if register_type in ["DI", "CO"] else result.registers
        except Exception as e:
            logger.info(f"Error reading from {register_type} at address {address}: {e}")
            return None

    def close(self):
        """
        Close the Modbus master connection.
        """
        logger.info("Closing Modbus master connection...")
        self.client.close()


if __name__ == "__main__":
    pass
    #want read two master at a time in loop

    master1 = ModbusMaster(port="COM6")
    master2 = ModbusMaster(port="COM4")
    while True:
        # Read from master1
        hr_values_master1 = master1.read_registers("HR", 0, 22, slave_id=2)
        
        # Read from master2
        hr_values_master2 = master2.read_registers("HR", 0, 22, slave_id=2)

        # Print the results
        print(f"Master 1 -  HR: {hr_values_master1}")
        print(f"Master 2 -  HR: {hr_values_master2}")
        
        # write regeister random values address 25   
        write_values =  [random.randint(0,100) for i in range(5)]
        master1.write_registers("HR", 25, write_values, slave_id=1)
        # Write to master2  
        master2.write_registers("HR", 25, write_values, slave_id=2)
        # Add any additional processing or logic here
        # For example, you can write values to the registers or perform other operations
        read_values = master1.read_registers("HR", 25, 6, slave_id=2)
        print(f"Read values from master1: {read_values}")
        read_values = master2.read_registers("HR", 25, 6, slave_id=2)
        print(f"Read values from master2: {read_values}")

        # Add a delay if needed
        import time
        time.sleep(5)  # Adjust the sleep time as necessary
