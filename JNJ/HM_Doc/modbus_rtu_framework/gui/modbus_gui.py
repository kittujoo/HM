import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import tkinter as tk
from tkinter import ttk, messagebox
from core.modbus_client import ModbusClientWrapper
from config.logger import BASE_ADDRESSES

class ModbusGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modbus RTU GUI - Fan & HPR")
        self.geometry("800x600")
        self.client = None

        self.controller_type = tk.StringVar(value="FAN")
        self.port = tk.StringVar(value="COM4")
        self.baudrate = tk.IntVar(value=9600)

        self.setup_ui()

    def setup_ui(self):
        # Top section for COM setup
        frm = ttk.Frame(self)
        frm.pack(pady=10)

        ttk.Label(frm, text="Port:").pack(side=tk.LEFT)
        ttk.Entry(frm, textvariable=self.port, width=10).pack(side=tk.LEFT)
        ttk.Label(frm, text="Baudrate:").pack(side=tk.LEFT)
        ttk.Entry(frm, textvariable=self.baudrate, width=10).pack(side=tk.LEFT)
        ttk.Button(frm, text="Connect", command=self.connect).pack(side=tk.LEFT)

        # Dropdown to choose controller
        ttk.Combobox(frm, textvariable=self.controller_type, values=["FAN", "HPR","SCADA","IT RACK"], state="readonly").pack(side=tk.LEFT)

        # Frame for temperature/fan controls
        self.control_frame = ttk.LabelFrame(self, text="Controllers")
        self.control_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.generate_blocks()

    def generate_blocks(self):
        for widget in self.control_frame.winfo_children():
            widget.destroy()

        for temp_idx in range(4):  # Temp 1 to Temp 4
            block = ttk.LabelFrame(self.control_frame, text=f"Temp {temp_idx + 1}")
            block.grid(row=temp_idx, column=0, padx=10, pady=5, sticky="w")
            # ttk.Entry(row=temp_idx, textvariable="Temp", width=10)
            # row = ttk.Frame(block)
            # ttk.Label(row, text=f"Temp: {temp_idx + 1}").pack(side=tk.LEFT)
            # ttk.Entry(row, textvariable=0, width=10, state='readonly').pack(side=tk.LEFT, padx=2)
            for fan_idx in range(4):  # 4 Fans per Temp
                row = ttk.Frame(block)
                row.pack(fill=tk.X, pady=2)

                temp_var = tk.StringVar()
                fan_var = tk.StringVar()

                # ttk.Label(row, text=f"Fan {fan_idx + 1} Temp:").pack(side=tk.LEFT)
                # ttk.Entry(row, textvariable=temp_var, width=10, state='readonly').pack(side=tk.LEFT, padx=2)
                ttk.Label(row, text=f"Fan: {fan_idx + 1}").pack(side=tk.LEFT)
                fan_entry = ttk.Entry(row, textvariable=fan_var, width=10)
                fan_entry.pack(side=tk.LEFT, padx=2)

                ttk.Button(row, text="Read", command=lambda t=temp_idx, f=fan_idx: self.read_data(t, f)).pack(side=tk.LEFT, padx=5)
                ttk.Button(row, text="Write", command=lambda t=temp_idx, f=fan_idx, var=fan_var: self.write_data(t, f, var)).pack(side=tk.LEFT)

                # Save vars
                setattr(self, f"temp_{temp_idx}_{fan_idx}", temp_var)
                setattr(self, f"fan_{temp_idx}_{fan_idx}", fan_var)

    def get_address(self, temp_idx, fan_idx):
        base = BASE_ADDRESSES[self.controller_type.get()]
        temp_addr = base + temp_idx * 10 + fan_idx * 2
        fan_addr = temp_addr + 1
        return temp_addr, fan_addr

    def read_data(self, temp_idx, fan_idx):
        if not self.client:
            return

        temp_addr, fan_addr = self.get_address(temp_idx, fan_idx)
        temp = self.client.read_holding_register(temp_addr)
        fan = self.client.read_holding_register(fan_addr)

        temp_c = round(temp / 10.0, 1) if temp is not None else "--"
        getattr(self, f"temp_{temp_idx}_{fan_idx}").set(f"{temp_c} °C")
        getattr(self, f"fan_{temp_idx}_{fan_idx}").set(str(fan) if fan is not None else "--")

    def write_data(self, temp_idx, fan_idx, fan_var):
        if not self.client:
            return

        try:
            value = int(fan_var.get())
            _, fan_addr = self.get_address(temp_idx, fan_idx)
            self.client.write_holding_register(fan_addr, value)
        except ValueError:
            messagebox.showerror("Input Error", "Enter a valid number")

    def connect(self):
        self.client = ModbusClientWrapper()
        if self.client.connect():
            messagebox.showinfo("Connected", "Modbus Connected Successfully")
            self.generate_blocks()
        else:
            messagebox.showerror("Connection Error", "Failed to connect to Modbus")

if __name__ == "__main__":
    app = ModbusGUI()
    app.mainloop()
