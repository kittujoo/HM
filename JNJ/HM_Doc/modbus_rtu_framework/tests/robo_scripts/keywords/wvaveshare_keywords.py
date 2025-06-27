import os
import sys
import json
from robot.api.deco import keyword, library

# Adjust path as needed for your project structure
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from libraries.modbus_master import ModbusMaster
from utils.constants import CONFIG_PATH



@library
class WaveshareKeywords:
    def __init__(self):
        self.master = None
        self.device_config = None
        self.device_port = None
        self.device_slave = 1  # Default slave id

    @keyword("Load Waveshare Config")
    def load_waveshare_config(self, device_group):
        """Load device config from JSON for a given device group (e.g., 'fan_fault')."""
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        if device_group not in config:
            raise Exception(f"Device group '{device_group}' not found in config.")
        self.device_config = config[device_group]
        # self.device_port = self.device_config["device"]["port"]
        # Optionally, set slave id if present in config
        self.device_slave = self.device_config["device"].get("slave_id", 1)

    @keyword("Connect Waveshare Device")
    def connect_waveshare_device(self, device_group):
        """Connect to the Waveshare device for the given group (loads config)."""
        self.load_waveshare_config(device_group)
        self.master = ModbusMaster(
            port=self.device_config["device"]["port"],
            baudrate=self.device_config["device"]["baudrate"],
            stopbits=self.device_config["device"]["stopbits"],
            bytesize=self.device_config["device"]["bytesize"],
            parity=self.device_config["device"]["parity"],
            timeout=1,
        )
        if not self.master.connect():
            raise Exception(
                f"Failed to connect to Waveshare device on {self.device_port}"
            )

    @keyword("Disconnect Waveshare Device")
    def disconnect_waveshare_device(self):
        """Disconnect from the Waveshare device."""
        if self.master:
            self.master.close()
            self.master = None

    @keyword("Write Waveshare Channel")
    def write_waveshare_channel(self, device_group, channel_key, value):
        """
        Write a value to a specific channel (e.g., 'ff1') in the device group (e.g., 'fan_fault').
        """
        self.load_waveshare_config(device_group)
        channel = self.device_config.get(channel_key)
        function_code = self.device_config.get("function_code", "HR")

        if not channel:
            raise Exception(
                f"Channel '{channel_key}' not found in group '{device_group}'"
            )
        address = channel["chanel"] - 1  # Assuming Modbus address starts at 0
        # Write to holding register (HR)
        result = self.master.write_registers(
            function_code, address, [int(value)], slave_id=self.device_slave
        )
        return result

    @keyword("Read Waveshare Channel")
    def read_waveshare_channel(self, device_group, channel_key):
        """
        Read a value from a specific channel (e.g., 'ff1') in the device group (e.g., 'fan_fault').
        """
        self.load_waveshare_config(device_group)
        channel = self.device_config.get(channel_key)
        function_code = self.device_config.get("function_code", "HR")
        if not channel:
            raise Exception(
                f"Channel '{channel_key}' not found in group '{device_group}'"
            )
        address = channel["chanel"] - 1  # Assuming Modbus address starts at 0
        # Read from holding register (HR)
        result = self.master.read_registers(
            function_code, address, 1, slave_id=self.device_slave
        )
        if isinstance(result, list) and result:
            return result[0]
        return result

    # Convenience keywords for all channels in all groups
    @keyword("Enable FF1")
    def enable_ff1(self):
        return self.write_waveshare_channel("fan_fault", "ff1", 1)

    @keyword("Disable FF1")
    def disable_ff1(self):
        return self.write_waveshare_channel("fan_fault", "ff1", 0)

    @keyword("Get FF1 Value")
    def get_ff1_value(self):
        return self.read_waveshare_channel("fan_fault", "ff1")

    @keyword("Enable FF2")
    def enable_ff2(self):
        return self.write_waveshare_channel("fan_fault", "ff2", 1)

    @keyword("Disable FF2")
    def disable_ff2(self):
        return self.write_waveshare_channel("fan_fault", "ff2", 0)

    @keyword("Get FF2 Value")
    def get_ff2_value(self):
        return self.read_waveshare_channel("fan_fault", "ff2")

    @keyword("Enable FF3")
    def enable_ff3(self):
        return self.write_waveshare_channel("fan_fault", "ff3", 1)

    @keyword("Disable FF3")
    def disable_ff3(self):
        return self.write_waveshare_channel("fan_fault", "ff3", 0)

    @keyword("Get FF3 Value")
    def get_ff3_value(self):
        return self.read_waveshare_channel("fan_fault", "ff3")

    @keyword("Enable FE1")
    def enable_fe1(self):
        return self.write_waveshare_channel("fan_enable", "fe1", 1)

    @keyword("Disable FE1")
    def disable_fe1(self):
        return self.write_waveshare_channel("fan_enable", "fe1", 0)

    @keyword("Get FE1 Value")
    def get_fe1_value(self):
        return self.read_waveshare_channel("fan_enable", "fe1")

    @keyword("Enable FE2")
    def enable_fe2(self):
        return self.write_waveshare_channel("fan_enable", "fe2", 1)

    @keyword("Disable FE2")
    def disable_fe2(self):
        return self.write_waveshare_channel("fan_enable", "fe2", 0)

    @keyword("Get FE2 Value")
    def get_fe2_value(self):
        return self.read_waveshare_channel("fan_enable", "fe2")

    @keyword("Enable FE3")
    def enable_fe3(self):
        return self.write_waveshare_channel("fan_enable", "fe3", 1)

    @keyword("Disable FE3")
    def disable_fe3(self):
        return self.write_waveshare_channel("fan_enable", "fe3", 0)

    @keyword("Get FE3 Value")
    def get_fe3_value(self):
        return self.read_waveshare_channel("fan_enable", "fe3")

    @keyword("Enable FOL1")
    def enable_fol1(self):
        return self.write_waveshare_channel("fan_open_load", "fol1", 1)

    @keyword("Disable FOL1")
    def disable_fol1(self):
        return self.write_waveshare_channel("fan_open_load", "fol1", 0)

    @keyword("Get FOL1 Value")
    def get_fol1_value(self):
        return self.read_waveshare_channel("fan_open_load", "fol1")
    
    @keyword("Enable FOL2")
    def enable_fol2(self):
        return self.write_waveshare_channel("fan_open_load", "fol2", 1)
    
    @keyword("Disable FOL2")
    def disable_fol2(self):
        return self.write_waveshare_channel("fan_open_load", "fol2", 0)

    @keyword("Get FOL2 Value")
    def get_fol2_value(self):
        return self.read_waveshare_channel("fan_open_load", "fol2")
    
    @keyword("Enable FOL3")
    def enable_fol3(self):
        return self.write_waveshare_channel("fan_open_load", "fol3", 1)
    @keyword("Disable FOL3")
    def disable_fol3(self):
        return self.write_waveshare_channel("fan_open_load", "fol3", 0) 

    @keyword("Get FOL3 Value")
    def get_fol3_value(self):
        return self.read_waveshare_channel("fan_open_load", "fol3")
    
    @keyword("Enable FD1")
    def enable_fd1(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd1", 1)
    @keyword("Disable FD1")
    def disable_fd1(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd1", 0)

    @keyword("Get FD1 Value")
    def get_fd1_value(self):
        return self.read_waveshare_channel("fan_diagnostic", "fd1")
    
    @keyword("Enable FD2")
    def enable_fd2(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd2", 1) 
    @keyword("Disable FD2")
    def disable_fd2(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd2", 0)     

    @keyword("Get FD2 Value")
    def get_fd2_value(self):
        return self.read_waveshare_channel("fan_diagnostic", "fd2")
    
    @keyword("Enable FD3")
    def enable_fd3(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd3", 1)
    @keyword("Disable FD3")
    def disable_fd3(self):
        return self.write_waveshare_channel("fan_diagnostic", "fd3", 0)

    @keyword("Get FD3 Value")
    def get_fd3_value(self):
        return self.read_waveshare_channel("fan_diagnostic", "fd3")


if __name__ == "__main__":
    pass
    # Example usage
    keywords = WaveshareKeywords()
    keywords.connect_waveshare_device("fan_fault")
