*** Settings ***
Library    BuiltIn
Library    ../keywords/new_waveshare_keyword.py    WITH NAME    ws

*** Test Cases ***
Write And Read PWM1
    ws.Connect Waveshare Master
    ws.Write PWM1    100
    ${val}=    ws.Read Taco1
    Log    Taco1 Value: ${val}
    ws.Disconnect Waveshare Master

Write And Read PWM2
    ws.Connect Waveshare Master
    ws.Write PWM2    77
    ${val}=    ws.Read Taco2
    Log    Taco2 Value: ${val}
    ws.Disconnect Waveshare Master

Write And Read PWM3
    ws.Connect Waveshare Master
    ws.Write PWM3    55
    ${val}=    ws.Read Taco3
    Log    Taco3 Value: ${val}
    ws.Disconnect Waveshare Master

Write And Read PWM4
    ws.Connect Waveshare Master
    ws.Write PWM4    200
    ${val}=    ws.Read Taco4
    Log    Taco4 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco5
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco5
    Log    Taco5 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco6
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco6
    Log    Taco6 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco7
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco7
    Log    Taco7 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco8
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco8
    Log    Taco8 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco9
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco9
    Log    Taco9 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco10
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco10
    Log    Taco10 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco11
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco11
    Log    Taco11 Value: ${val}
    ws.Disconnect Waveshare Master

Read Taco12
    ws.Connect Waveshare Master
    ${val}=    ws.Read Taco12
    Log    Taco12 Value: ${val}
    ws.Disconnect Waveshare Master

Read Relay
    ws.Connect Waveshare Master
    ${val}=    ws.Read Relay
    Log    Relay Value: ${val}
    ws.Disconnect Waveshare Master