from pymodbus.server import StartSerialServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
import serial.tools.list_ports
import serial


def test_modbus_rtu():
    """
    Test function to check Modbus RTU communication.
    This function attempts to start a Modbus RTU server on all available serial ports.
    """

    # Define a data store with Holding Registers
    store = ModbusSlaveContext(
        hr={0: 123, 1: 456, 2: 789},  # Example holding register values
    )
    context = ModbusServerContext(slaves=store, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = "MyModbusDevice"
    identity.ProductCode = "MD"
    identity.VendorUrl = "http://example.com"
    identity.ProductName = "Modbus RTU Slave"
    identity.ModelName = "PythonModbusServer"
    identity.MajorMinorRevision = "1.0"

    # Start the server
    StartSerialServer(
        context=context,
        identity=identity,
        port="COM5",
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=1,
    )


def try_port(port):
    try:
        store = ModbusSlaveContext(hr={0: 0})
        context = ModbusServerContext(slaves=store, single=True)
        identity = ModbusDeviceIdentification()
        print(f"Trying {port}...")
        StartSerialServer(context, identity=identity, port=port, timeout=1)
    except Exception as e:
        print(f"Failed on {port}: {e}")


def check_port(port):
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=1)
        print(f"{port} is accessible.")
        ser.close()
    except Exception as e:
        print(f"{port} access failed: {e}")


if __name__ == "__main__":
    # ports = serial.tools.list_ports.comports()
    # for port in ports:
    #     check_port(port.device)
    
    # try_port("COM4")
    
    test_modbus_rtu()
