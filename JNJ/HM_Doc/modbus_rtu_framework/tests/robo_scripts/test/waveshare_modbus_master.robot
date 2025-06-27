*** Settings ***
Library    BuiltIn
Library    ../keywords/modbus_master_keywords.py    WITH NAME    ms
Library    ../keywords/fan_module_simulation_keywords.py    WITH NAME   fan_sim

Suite Setup    fan_sim.Start Modbus Simulation
Suite Teardown    fan_sim.Stop Modbus Simulation

*** Variables ***


*** Test Cases ***
Connect And Disconnect Modbus Master
    [Tags]    smoke    connection
    ms.Connect Modbus Master    COM4    9600
    ms.Disconnect Modbus Master


*** Test Cases ***
Write And Read Modbus Registers
    ${REG_VALUES} =    Evaluate    [10, 20, 30]
    Connect Modbus Master    COM4    9600
    Write Modbus Registers   HR    0    ${REG_VALUES}    1
    ${values}=    Read Modbus Registers    HR    0    3    1
    Log    Read values: ${values}
    Should Be Equal    ${values}    ${REG_VALUES}
    Disconnect Modbus Master


