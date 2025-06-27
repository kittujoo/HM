import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from robot.api.deco import keyword, library
from wrappers.fan_module_simulation import SimulateModbusSlave


@library
class FanModuleSimulationKeywords:
    def __init__(self):
        self.sds = None

    @keyword("Start Modbus Simulation")
    def start_modbus_simulation(self):
        """Initialize and start the Modbus simulation server."""
        self.sds = SimulateModbusSlave()
        self.sds.slave.start_server()
        self.sds.set_default_values()

    @keyword("Simulate Data")
    def simulate_data(self, times=3):
        """Simulate data updates a given number of times."""
        for _ in range(int(times)):
            self.sds.simulate_data()

    @keyword("Stop Modbus Simulation")
    def stop_modbus_simulation(self):
        """Stop the Modbus simulation server."""
        if self.sds:
            self.sds.slave.stop_server()

    @keyword("Update UI Dict")
    def update_ui_dict(self, flag, key, value):
        """Update the UI dictionary in the simulation."""
        return self.sds.update_ui_dict(flag, key, value)

    @keyword("Get Slave Values")
    def get_slave_values(self, reg_type, address, count):
        """Get values from the Modbus slave."""
        return self.sds.slave.get_values(reg_type, int(address), int(count))