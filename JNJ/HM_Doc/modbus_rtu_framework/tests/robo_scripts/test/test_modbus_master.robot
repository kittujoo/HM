*** Settings ***
Library    BuiltIn
Library    ../keywords/modbus_master_keywords.py    WITH NAME    ms
Library    ../keywords/fan_module_simulation_keywords.py    WITH NAME    fan_sim

Suite Setup    fan_sim.Start Modbus Simulation
Suite Teardown    fan_sim.Stop Modbus Simulation

*** Variables ***
${PORT}        COM4
${BAUDRATE}    9600
${UNIT_ID}     1




*** Test Cases ***
Test Connection
    [Tags]    smoke    connection
    ms.Connect Modbus Master    ${PORT}    ${BAUDRATE}
    Log    Connection successful
    ms.Disconnect Modbus Master
    Log    Disconnected successfully

Write and Read Holding Registers
    [Tags]    regression    hr    dataflow
    ${values}=    Evaluate    [10, 20, 30]
    ms.Connect Modbus Master    ${PORT}    ${BAUDRATE}
    ms.Write Modbus Registers    HR    0    ${values}    ${UNIT_ID}
    ${read_values}=    ms.Read Modbus Registers    HR    0    3    ${UNIT_ID}
    Should Be Equal    ${read_values}    ${values}
    ms.Disconnect Modbus Master

Invalid Port Handling
    [Tags]    negative    error
    Run Keyword And Expect Error    *    ms.Connect Modbus Master    COM99    ${BAUDRATE}

Read Without Connection
    [Tags]    negative    no-connection
    Run Keyword And Expect Error    *    ms.Read Modbus Registers    HR    0    3    ${UNIT_ID}

Write Invalid Data Type
    [Tags]    negative    data
    ms.Connect Modbus Master    ${PORT}    ${BAUDRATE}
    Run Keyword And Expect Error    *    ms.Write Modbus Registers    HR    0    abc    ${UNIT_ID}
    ms.Disconnect Modbus Master