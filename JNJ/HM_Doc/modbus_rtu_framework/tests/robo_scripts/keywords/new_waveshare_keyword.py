import os
import sys
import json
from robot.api.deco import keyword, library

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from libraries.modbus_master import ModbusMaster
from utils.constants import CONFIG_PATH
from config.logger import logger


@library
class WaveshareMasterKeywords:
    def __init__(self):
        self.master = None
        self.config = None
        self.device_params = None

    def load_config(self):
        if self.config is None:
            with open(CONFIG_PATH, "r") as f:
                self.config = json.load(f)
        self.device_params = self.config["device"]

    @keyword("Connect Waveshare Master")
    def connect_waveshare_master(self):
        """Connect to the Waveshare Modbus master using config."""
        self.load_config()
        self.master = ModbusMaster(
            port=self.device_params["port"],
            baudrate=self.device_params["baudrate"],
            stopbits=self.device_params["stopbits"],
            bytesize=self.device_params["bytesize"],
            parity=self.device_params["parity"],
            timeout=1,
        )
        if not self.master.connect():
            raise Exception(
                f"Failed to connect to device on {self.device_params['port']}"
            )
        logger.info("Modbus master connected.")

    @keyword("Disconnect Waveshare Master")
    def disconnect_waveshare_master(self):
        """Disconnect the Modbus master."""
        if self.master:
            self.master.close()
            self.master = None

    def get_reg_info(self, key):
        self.load_config()
        if key not in self.config:
            raise Exception(f"Register '{key}' not found in config.")
        reg = self.config[key]
        return reg["function_code"], reg["reg_address"] - 1, reg["slave_id"]

    # PWM write keywords
    @keyword("Write PWM1")
    def write_pwm1(self, value):

        fc, addr, slave = self.get_reg_info("pwm1")
        return self.master.write_registers(fc, addr, [int(value)], slave_id=slave)

    @keyword("Write PWM2")
    def write_pwm2(self, value):

        fc, addr, slave = self.get_reg_info("pwm2")
        return self.master.write_registers(fc, addr, [int(value)], slave_id=slave)

    @keyword("Write PWM3")
    def write_pwm3(self, value):

        fc, addr, slave = self.get_reg_info("pwm3")
        return self.master.write_registers(fc, addr, [int(value)], slave_id=slave)

    @keyword("Write PWM4")
    def write_pwm4(self, value):

        fc, addr, slave = self.get_reg_info("pwm4")
        return self.master.write_registers(fc, addr, [int(value)], slave_id=slave)

    # Taco and relay read keywords
    @keyword("Read Taco1")
    def read_taco1(self):

        fc, addr, slave = self.get_reg_info("taco1")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco2")
    def read_taco2(self):

        fc, addr, slave = self.get_reg_info("taco2")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco3")
    def read_taco3(self):

        fc, addr, slave = self.get_reg_info("taco3")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco4")
    def read_taco4(self):

        fc, addr, slave = self.get_reg_info("taco4")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco5")
    def read_taco5(self):

        fc, addr, slave = self.get_reg_info("taco5")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco6")
    def read_taco6(self):

        fc, addr, slave = self.get_reg_info("taco6")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco7")
    def read_taco7(self):

        fc, addr, slave = self.get_reg_info("taco7")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco8")
    def read_taco8(self):

        fc, addr, slave = self.get_reg_info("taco8")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco9")
    def read_taco9(self):

        fc, addr, slave = self.get_reg_info("taco9")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco10")
    def read_taco10(self):

        fc, addr, slave = self.get_reg_info("taco10")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco11")
    def read_taco11(self):

        fc, addr, slave = self.get_reg_info("taco11")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Taco12")
    def read_taco12(self):

        fc, addr, slave = self.get_reg_info("taco12")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]

    @keyword("Read Relay")
    def read_relay(self):

        fc, addr, slave = self.get_reg_info("relay")
        return self.master.read_registers(fc, addr, 1, slave_id=slave)[0]


if __name__ == "__main__":
    # i want test this script directly
    waveshare = WaveshareMasterKeywords()
    waveshare.connect_waveshare_master()
    logger.info("Connected to Waveshare Modbus master.")
    # Example usage
    try:
        logger.info("Writing PWM1 with value 100...")
        waveshare.write_pwm1(100)
        logger.info("Reading Taco1...")
        taco1_value = waveshare.read_taco1()
        logger.info(f"Taco1 value: {taco1_value}")
        waveshare.disconnect_waveshare_master()
    except Exception as e:
        waveshare.disconnect_waveshare_master()
        logger.info(f"Error: {e}")
