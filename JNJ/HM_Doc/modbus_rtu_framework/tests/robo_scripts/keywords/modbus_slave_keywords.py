import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from libraries.modbus_slave import ModbusSlave

class ModbusSlaveLibrary:
    def __init__(self):
        self.slave = None

    def start_modbus_slave(self, port='COM3', baudrate=9600, stopbits=1, bytesize=8, parity='N', timeout=1):
        """Start the Modbus slave server."""
        self.slave = ModbusSlave(port, baudrate, stopbits, bytesize, parity, timeout)
        self.slave.start_server()

    def stop_modbus_slave(self):
        """Stop the Modbus slave server."""
        if self.slave:
            self.slave.stop_server()

    def set_modbus_values(self, register_type, address, values):
        """Set values in the specified Modbus register."""
        if self.slave:
            self.slave.set_values(register_type, int(address), [int(v) for v in values.split(',')])

    def get_modbus_values(self, register_type, address, count):
        """Get values from the specified Modbus register."""
        if self.slave:
            return self.slave.get_values(register_type, int(address), int(count))
        

# To use in Robot Framework, add this to your test suite:
# Library    modbus_slave_keywords.py