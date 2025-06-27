*** Settings ***
Library    ../keywords/wvaveshare_keywords.py    WITH NAME    ws

Suite Setup    ws.Connect Waveshare Device    fan_fault
Suite Teardown    ws.Disconnect Waveshare Device

*** Test Cases ***
Enable And Read FF1
    [Tags]    smoke    ff1
    ws.Enable FF1
    ${val}=    ws.Get FF1 Value
    Log    FF1 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FF1

Enable And Read FF2
    [Tags]    regression    ff2
    ws.Enable FF2
    ${val}=    ws.Get FF2 Value
    Log    FF2 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FF2

Enable And Read FF3
    [Tags]    regression    ff3
    ws.Enable FF3
    ${val}=    ws.Get FF3 Value
    Log    FF3 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FF3

Enable And Read FE1
    [Tags]    smoke    fe1
    ws.Connect Waveshare Device    fan_enable
    ws.Enable FE1
    ${val}=    ws.Get FE1 Value
    Log    FE1 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FE1
    ws.Disconnect Waveshare Device

Enable And Read FE2
    [Tags]    regression    fe2
    ws.Connect Waveshare Device    fan_enable
    ws.Enable FE2
    ${val}=    ws.Get FE2 Value
    Log    FE2 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FE2
    ws.Disconnect Waveshare Device

Enable And Read FE3
    [Tags]    regression    fe3
    ws.Connect Waveshare Device    fan_enable
    ws.Enable FE3
    ${val}=    ws.Get FE3 Value
    Log    FE3 Value: ${val}
    Should Be Equal    ${val}    1
    ws.Disable FE3
    ws.Disconnect Waveshare Device

Read FOL1
    [Tags]    fol1
    ws.Connect Waveshare Device    fan_open_load
    ${val}=    ws.Get FOL1 Value
    Log    FOL1 Value: ${val}
    ws.Disconnect Waveshare Device

Read FOL2
    [Tags]    fol2
    ws.Connect Waveshare Device    fan_open_load
    ${val}=    ws.Get FOL2 Value
    Log    FOL2 Value: ${val}
    ws.Disconnect Waveshare Device

Read FOL3
    [Tags]    fol3
    ws.Connect Waveshare Device    fan_open_load
    ${val}=    ws.Get FOL3 Value
    Log    FOL3 Value: ${val}
    ws.Disconnect Waveshare Device

Read FD1
    [Tags]    fd1
    ws.Connect Waveshare Device    fan_diagnostic
    ${val}=    ws.Get FD1 Value
    Log    FD1 Value: ${val}
    ws.Disconnect Waveshare Device

Read FD2
    [Tags]    fd2
    ws.Connect Waveshare Device    fan_diagnostic
    ${val}=    ws.Get FD2 Value
    Log    FD2 Value: ${val}
    ws.Disconnect Waveshare Device

Read FD3
    [Tags]    fd3
    ws.Connect Waveshare Device    fan_diagnostic
    ${val}=    ws.Get FD3 Value
    Log    FD3 Value: ${val}
    ws.Disconnect Waveshare Device