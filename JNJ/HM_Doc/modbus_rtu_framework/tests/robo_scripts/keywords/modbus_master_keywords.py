import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from robot.api.deco import keyword, library
from libraries.modbus_master import ModbusMaster

from utils.excel_parser import read_registers_from_excel

"""
df = excel sheet read (Path)
ff1 = df(ff1)
modbus_connect()
read/write

"""


@library
class ModbusMasterKeywords:
    def __init__(self):
        self.client = None

    @keyword("Connect Modbus Master")
    def connect_modbus_master(
        self, port="COM4", baudrate=9600, stopbits=1, bytesize=8, parity="N", timeout=1
    ):
        """Connect to a Modbus slave as master."""
        self.client = ModbusMaster(
            port=port,
            baudrate=baudrate,
            stopbits=stopbits,
            bytesize=bytesize,
            parity=parity,
            timeout=timeout,
        )
        if not self.client.connect():
            raise Exception("Failed to connect to Modbus slave.")

    @keyword("Disconnect Modbus Master")
    def disconnect_modbus_master(self):
        """Disconnect the Modbus master."""
        if self.client:
            self.client.close()
            self.client = None

    @keyword("Write Modbus Registers")
    def write_modbus_registers(self, reg_type, address, values, unit=1):
        """Write values to holding registers."""
        if not self.client:
            raise Exception("Modbus master is not connected.")
        try:
            values = [int(v) for v in values]
        except ValueError as e:
            raise ValueError(f"Invalid value in list: {values}") from e
        result = self.client.write_registers(
            str(reg_type), int(address), values, slave_id=int(unit)
        )
        return result

    @keyword("Read Modbus Registers")
    def read_modbus_registers(self, reg_type, address, count, unit=1):
        """Read values from holding registers."""
        if not self.client:
            raise Exception("Modbus master is not connected.")
        result = self.client.read_registers(
            str(reg_type), int(address), int(count), slave_id=int(unit)
        )

        return result
    

if __name__ == "__main__":
    # Example usage
    modbus = ModbusMasterKeywords()
    modbus.connect_modbus_master(port="COM4", baudrate=9600)
    try:
        modbus.write_modbus_registers("HR", 0, [10, 20, 30], unit=1)
        values = modbus.read_modbus_registers("HR", 0, 3)
        print(f"Read values: {values}")
    finally:
        modbus.disconnect_modbus_master()
