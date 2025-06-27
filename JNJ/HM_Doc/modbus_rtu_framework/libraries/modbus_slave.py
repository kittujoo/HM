import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import random
import threading
import time
from pymodbus.datastore import (
    ModbusSlaveContext,
    ModbusSequentialDataBlock,
    ModbusServerContext,
)
from pymodbus.server import StartSerialServer
from config.logger import logger


class ModbusSlave:
    def __init__(
        self,
        port="COM3",
        baudrate=9600,
        stopbits=1,
        bytesize=8,
        parity="N",
        timeout=1,
        slave_ids=[1],
    ):
        self.port = port
        self.baudrate = baudrate
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.parity = parity
        self.timeout = timeout

        # Initialize Modbus registers for multiple slaves
        self.stores = {}
        for slave_id in slave_ids:
            self.stores[slave_id] = ModbusSlaveContext(
                di=ModbusSequentialDataBlock(0, [0] * 100),
                co=ModbusSequentialDataBlock(0, [0] * 100),
                hr=ModbusSequentialDataBlock(0, [0] * 100),
                ir=ModbusSequentialDataBlock(0, [0] * 100),
            )

        self.context = ModbusServerContext(slaves=self.stores, single=False)
        self.server_thread = None
        self.running = False  # Control flag for the server

    def start_server(self):
        """
        Start the Modbus server in a separate thread.
        """

        def run_server():
            try:
                logger.info("Starting Modbus server for multiple slaves...")
                StartSerialServer(
                    context=self.context,
                    port=self.port,
                    baudrate=self.baudrate,
                    stopbits=self.stopbits,
                    bytesize=self.bytesize,
                    parity=self.parity,
                    timeout=self.timeout,
                )
            except Exception as e:
                logger.error(f"Error starting Modbus server: {e}")
        logger.info("Starting Modbus server with the port: %s", self.port)
        self.running = True
        self.server_thread = threading.Thread(target=run_server, daemon=True)
        self.server_thread.start()

    def stop_server(self):
        """
        Stop the Modbus server by terminating the thread.
        """
        if self.server_thread and self.server_thread.is_alive():
            logger.info("Stopping Modbus server with the port: %s", self.port)
            self.running = False
            self.server_thread.join(timeout=1)  # Wait for the thread to terminate
            logger.info("Modbus server with the port: %s stopped", self.port)

    def set_values(self, reg_type, address, values, slave_id=1):
        """
        Set values in the specified register type for a given slave.
        """
        function_code = self._get_function_code(reg_type)

        if slave_id in self.stores:
            self.stores[slave_id].setValues(function_code, address, values)
        else:
            logger.error(f"Slave ID {slave_id} not found.")

    def get_values(self, reg_type, address, count, slave_id=1):
        """
        Get values from the specified register type for a given slave.
        """
        function_code = self._get_function_code(reg_type)
        
        if slave_id in self.stores:
            return self.stores[slave_id].getValues(function_code, address, count)
        else:
            logger.error(f"Slave ID {slave_id} not found.")
            return []

    def _get_function_code(self, register_type):
        codes = {"DI": 2, "CO": 1, "HR": 3, "IR": 4}
        return codes.get(register_type, None)

    # Add any other existing functions here, updating them to accept slave_id as needed.


if __name__ == "__main__":
    pass

    # slave = ModbusSlave(slave_ids=[1, 2, 3])
    # # print("Starting Modbus slave server...",(slave.context.slaves))
    # print(slave.stores)
    # # print(slave.sla)
    # slave.start_server()
    # for i in range(10):
    #     random_values = [random.randint(0, 100) for _ in range(10)]
    #     slave.set_values("HR", 0, random_values, slave_id=1)
    #     random_values = [random.randint(0, 100) for _ in range(10)]
    #     slave.set_values("HR", 0, random_values, slave_id=2)
    #     random_values = [random.randint(0, 100) for _ in range(10)]
    #     slave.set_values("HR", 0, random_values, slave_id=3)
    #     logger.info(f"Values from slave 1: {slave.get_values('HR', 0, len(random_values), slave_id=1)}")
    #     logger.info(f"Values from slave 2: {slave.get_values('HR', 0, len(random_values), slave_id=2)}")
    #     logger.info(f"Values from slave 3: {slave.get_values('HR', 0, len(random_values), slave_id=3)}")
    #     time.sleep(5)

    # slave.stop_server()

    # modbus_slave = ModbusSlave(slave_ids=[2])
    # try:
    #     modbus_slave.start_server()  # Start the server in the main thread
    #     logger.info("Modbus server is running. Press Ctrl+C to stop.")

    #     while True:
    #         # 10 randiom values for testing
    #         random_values = [random.randint(0, 100) for i in range(10)]
    #         modbus_slave.set_values(
    #             "HR", 0, random_values, slave_id=2
    #         )  # Example to set values in Holding Registers
    #         logger.info(
    #             modbus_slave.get_values("HR", 0, 10)
    #         )  # Example to get values from Holding Registers
    #         time.sleep(5)
    # except KeyboardInterrupt:
    #     modbus_slave.stop_server()  # Stop the server on keyboard interrupt

    # modbus_slave1 = ModbusSlave(port='COM3',slave_ids=[1])
    # modbus_slave2 = ModbusSlave(port='COM4',slave_ids=[2])
    # try:
    #     modbus_slave1.start_server()  # Start the server in the main thread
    #     modbus_slave2.start_server()  # Start the server in the main thread
    #     logger.info("Modbus server is running. Press Ctrl+C to stop.")

    #     while True:
    #         # 10 randiom values for testing
    #         random_values = [random.randint(0, 100) for i in range(10)]
    #         modbus_slave1.set_values(
    #             "HR", 0, random_values, slave_id=1
    #         )  # Example to set values in Holding Registers
    #         logger.info(f"Values from {modbus_slave1.port}: {modbus_slave1.get_values('HR', 0, 10,slave_id=1)}")  # Example to get values from Holding Registers
            
    #         # 10 randiom values for testing
    #         random_values = [random.randint(0, 100) for i in range(10)]
    #         modbus_slave2.set_values(
    #             "HR", 0, random_values, slave_id=2
    #         )  # Example to set values in Holding Registers
    #         logger.info(f"Values from {modbus_slave2.port}: {modbus_slave2.get_values('HR', 0, 10,slave_id=2)}")
       
    #         time.sleep(5)
    # except KeyboardInterrupt:
    #     modbus_slave1.stop_server()  # Stop the server on keyboard interrupt
    #     modbus_slave2.stop_server()  # Stop the server on keyboard interrupt