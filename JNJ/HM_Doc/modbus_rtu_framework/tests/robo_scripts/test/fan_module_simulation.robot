*** Settings ***
Library    BuiltIn
Library    ../keywords/fan_module_simulation_keywords.py


*** Test Cases ***
Run Modbus Simulation
    Start Modbus Simulation
    Simulate Data    5
    ${values}=    Get Slave Values    HR    0    3
    Log    ${values}
    Stop Modbus Simulation




