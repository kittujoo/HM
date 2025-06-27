# Running Robot Framework Test Scripts

## Prerequisites

- **Python 3.8+** installed on your system.
- **Robot Framework** installed:
  ```bash
  pip install -r requirements.txt
modbus_rtu_framework/
└── tests/
    └── robo_scripts/
        ├── keywords/
        │   ├── modbus_master_keywords.py
        │   └── fan_module_simulation_keywords.py
        ├── results/
        └── test/
            ├── test_modbus_master.robot
            └── ...

### How to Run the Robot Scripts
- **Navigate to the test folder in your terminal:**
```bash   
cd modbus_rtu_framework/tests/robo_scripts/test
robot --outputdir ../results test_modbus_master.robot
robot --outputdir ../results .
```
Run a specific Robot Framework test file (for example, test_modbus_master.robot):
```bash   
robot --outputdir ../results test_modbus_master.robot
```
This will execute the test and store the logs and reports in the results folder.
View the results:
```bash   
robot --outputdir ../results .
```

After the test run, open modbus_rtu_framework/tests/robo_scripts/results/log.html in your browser to see detailed logs.
report.html provides a summary report.
#### Notes
- The suite setup and teardown in your .robot files will automatically start and stop the Modbus slave simulation.
- You can run all .robot files in the test folder at once:
Make sure your serial ports and Modbus devices are correctly configured and available.
- Let your team know to check the log.html for debugging and test details!

