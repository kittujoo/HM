import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QGroupBox, QComboBox, QTextEdit
)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from core.modbus_client import ModbusClient
from pymodbus.exceptions import ModbusIOException

class TempFanBox(QGroupBox):
    def __init__(self, title, start_address, client_getter, log_callback):
        super().__init__(title)
        self.title = title
        self.client_getter = client_getter
        self.start_address = start_address
        self.log = log_callback

        layout = QHBoxLayout()

        self.temp_label = QLabel("Temp: ")
        layout.addWidget(self.temp_label)

        self.inputs = [QLineEdit() for _ in range(1)]
        for inp in self.inputs:
            inp.setPlaceholderText("--`C")
            layout.addWidget(inp)
        
        self.update_btn = QPushButton("Update")
        self.simulate_btn = QPushButton("Sim'n ON/OFF")
        self.update_btn.clicked.connect(self.write_registers)
        self.simulate_btn.clicked.connect(self.simulation_toggle)
        layout.addWidget(self.update_btn)
        layout.addWidget(self.simulate_btn)

        self.setLayout(layout)

    def update_temperature(self, value):
        self.temp_label.setText(f"Temp: {value}°C")


    def simulation_toggle(self):
        client = self.client_getter()
        if not client:
            self.log("Error: Modbus not connected")
            return

        try:
            pass #need to uodate the simulation state
        except Exception as e:
            self.log(f"Exception: {e}")

    def write_registers(self):
        client = self.client_getter()
        if not client:
            self.log("Error: Modbus not connected")
            return

        try:
            values = [int(inp.text()) if inp.text().isdigit() else 0 for inp in self.inputs]
            result = client.write_holding_registers(self.start_address, values, unit=1)
            if result.isError():
                self.log(f"Write failed at address {self.start_address}")
            else:
                self.log(f"Wrote to HR[{self.start_address}]: {values}")
        except Exception as e:
            self.log(f"Exception: {e}")

class ModbusTempGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modbus RTU - Temperature & Fan Control")
        self.client = None

        main_layout = QVBoxLayout()

        # Serial Settings
        conn_layout = QHBoxLayout()
        self.port_combo = QComboBox()
        self.port_combo.addItems(["COM3", "COM4", "COM5"])
        self.baud_combo = QComboBox()
        self.baud_combo.addItems(["9600", "19200"])

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.connect_modbus)

        conn_layout.addWidget(QLabel("Port:"))
        conn_layout.addWidget(self.port_combo)
        conn_layout.addWidget(QLabel("Baudrate:"))
        conn_layout.addWidget(self.baud_combo)
        conn_layout.addWidget(self.connect_btn)

        main_layout.addLayout(conn_layout)

        # Boxes
        self.temp_boxes = []
        for i in range(3):
            box = TempFanBox(f"Temperature", start_address=10 + i*4, client_getter=lambda: self.client, log_callback=self.append_log)
            self.temp_boxes.append(box)
            main_layout.addWidget(box)

        # Read button
        # self.read_btn = QPushButton("Read Temperatures")
        # self.read_btn.clicked.connect(self.read_temperatures)
        # main_layout.addWidget(self.read_btn)

        # Log area
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        main_layout.addWidget(self.log_area)

        self.setLayout(main_layout)

    def append_log(self, msg):
        self.log_area.append(msg)

    def connect_modbus(self):
        port = self.port_combo.currentText()
        baudrate = int(self.baud_combo.currentText())

        self.client = ModbusClient(
            port=port,
            baudrate=baudrate,
            stopbits=1,
            bytesize=8,
            parity='N',
            timeout=1
        )

        if self.client.connect():
            self.append_log(f"[Connected] Port={port}, Baud={baudrate}")
        else:
            self.append_log("[Error] Failed to connect")

    def read_temperatures(self):
        if not self.client:
            self.append_log("Error: Not connected to Modbus")
            return

        try:
            result = self.client.read_input_register(0, 4, unit=1)
            if result.isError():
                self.append_log("Error reading input registers")
                return

            for i, val in enumerate(result.registers):
                self.temp_boxes[i].update_temperature(val)
            self.append_log(f"Read IR[0-3]: {result.registers}")
        except Exception as e:
            self.append_log(f"Exception: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ModbusTempGUI()
    gui.show()
    sys.exit(app.exec_())
