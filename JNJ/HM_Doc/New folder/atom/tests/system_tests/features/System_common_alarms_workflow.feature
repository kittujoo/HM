@system @ALIST-231 @system_common_alarms_feature
Feature: System | Common Alarms Workflow

  Background:
    Given an instrument system in "IDLE" state is connected

  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms without parameters for QSM moduleare are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm for QSM module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is QSM
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type             | message                                                             | issue                                                               |
      | PayloadOutOfRange      | Payload is out of range                                             | Payload is out of range                                             |
      | PayloadVersionMismatch | Payload version does not match expected version                     | Payload version does not match expected version                     |
      | ResourceNotAvailable   | Resource not available                                              | Resource not available                                              |
      | ApplicationResources   | Application resource error                                          | Application resource error                                          |
      | ResetFailed            | Reset instrument failed                                             | Reset instrument failed                                             |
      | MessageHandlerNotFound | Message handler not found                                           | Message handler not found                                           |
      | SocketConnection       | Listener socket error                                               | Listener socket error                                               |
      | NetworkReceive         | Error receiving data from socke                                     | Error receiving data from socke                                     |
      | NetworkSend            | Error sending data                                                  | Error sending data                                                  |
      | InvalidMessage         | Invalid message                                                     | Invalid message                                                     |
      | ChannelSubscription    | Failed to subscribe to data channel or get subscription list        | Failed to subscribe to data channel or get subscription list        |
      | EventSubscription      | Failed to subscribe to event notifications or get subscription list | Failed to subscribe to event notifications or get subscription list |
      | InstrumentStateChange  | Error changing instrument state                                     | Error changing instrument state                                     |
      | FailedToCreateCap      | Failed to create CAP                                                | Failed to create CAP                                                |
      | ThermistorInoperative  | Thermistor read failure                                             | Thermistor read failure                                             |
      | UnknownError           | Unknown error                                                       | Unknown error                                                       |
      | ResetNVRAMFailed       | Reset NVRAM failed                                                  | Reset NVRAM failed                                                  |
      | NetworkTimeProtocol    | SNTP error                                                          | SNTP error                                                          |
      | LeakSensorNotPresent   | Leak sensor 1 is not present                                        | Leak sensor 1 is not present                                        |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms with parameters for QSM module are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with "<fuse>", "<leak_detid>", "<temp>", "<control>", "<power>", "<subm_id>, <fan_id>" parameters for QSM module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is QSM
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type          | fuse | Leak_detid | temp | control | power | subm_id | fan_id | message                                                         | issue                                                           |
      | FuseBlown           | 1    | NA         | NA   | NA      | NA    | NA      | NA     | Fuse 1 has blown                                                | Fuse 1 has blown                                                |
      | LeakDetected        | NA   | 1          | NA   | NA      | NA    | NA      | NA     | Leak detector 1 has detected a leak                             | Leak detector 1 has detected a leak                             |
      | TemperatureSensor   | NA   | NA         | 20   | OFF     | NA    | NA      | NA     | Temperature sensor failure with set point 20 degC, state is OFF | Temperature sensor failure with set point 20 degC, state is OFF |
      | TemperatureFailSafe | NA   | NA         | NA   | NA      | 70    | NA      | NA     | Temperature failsafe triggered with heater/cooler power = 70%   | Temperature failsafe triggered with heater/cooler power = 70%   |
      | InternalCondition   | NA   | NA         | NA   | NA      | NA    | 1       | NA     | Internal error in submodule 1, not related to user input        | Internal error in submodule 1, not related to user input        |
      | FanFailure          | 1    | NA         | NA   | NA      | NA    | NA      | 1      | Fan 1 has failed                                                | Fan 1 has failed                                                |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms without parameters for FTN moduleare are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm for FTN module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is FTN
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type             | message                                                             | issue                                                               |
      | PayloadOutOfRange      | Payload is out of range                                             | Payload is out of range                                             |
      | PayloadVersionMismatch | Payload version does not match expected version                     | Payload version does not match expected version                     |
      | ResourceNotAvailable   | Resource not available                                              | Resource not available                                              |
      | ApplicationResources   | Application resource error                                          | Application resource error                                          |
      | ResetFailed            | Reset instrument failed                                             | Reset instrument failed                                             |
      | MessageHandlerNotFound | Message handler not found                                           | Message handler not found                                           |
      | SocketConnection       | Listener socket error                                               | Listener socket error                                               |
      | NetworkReceive         | Error receiving data from socke                                     | Error receiving data from socke                                     |
      | NetworkSend            | Error sending data                                                  | Error sending data                                                  |
      | InvalidMessage         | Invalid message                                                     | Invalid message                                                     |
      | ChannelSubscription    | Failed to subscribe to data channel or get subscription list        | Failed to subscribe to data channel or get subscription list        |
      | EventSubscription      | Failed to subscribe to event notifications or get subscription list | Failed to subscribe to event notifications or get subscription list |
      | InstrumentStateChange  | Error changing instrument state                                     | Error changing instrument state                                     |
      | FailedToCreateCap      | Failed to create CAP                                                | Failed to create CAP                                                |
      | ThermistorInoperative  | Thermistor read failure                                             | Thermistor read failure                                             |
      | UnknownError           | Unknown error                                                       | Unknown error                                                       |
      | ResetNVRAMFailed       | Reset NVRAM failed                                                  | Reset NVRAM failed                                                  |
      | NetworkTimeProtocol    | SNTP error                                                          | SNTP error                                                          |
      | LeakSensorNotPresent   | Leak sensor 1 is not present                                        | Leak sensor 1 is not present                                        |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms with parameters for QSM module are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with "<fuse>", "<leak_detid>", "<temp>", "<control>", "<power>", "<subm_id>", "<fan_id>" parameters for FTN module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is FTN
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type          | fuse | Leak_detid | temp | control | power | subm_id | fan_id | message                                                         | issue                                                           |
      | FuseBlown           | 1    | NA         | NA   | NA      | NA    | NA      | NA     | Fuse 1 has blown                                                | Fuse 1 has blown                                                |
      | LeakDetected        | NA   | 1          | NA   | NA      | NA    | NA      | NA     | Leak detector 1 has detected a leak                             | Leak detector 1 has detected a leak                             |
      | TemperatureSensor   | NA   | NA         | 20   | OFF     | NA    | NA      | NA     | Temperature sensor failure with set point 20 degC, state is OFF | Temperature sensor failure with set point 20 degC, state is OFF |
      | TemperatureFailSafe | NA   | NA         | NA   | NA      | 70    | NA      | NA     | Temperature failsafe triggered with heater/cooler power = 70%   | Temperature failsafe triggered with heater/cooler power = 70%   |
      | InternalCondition   | NA   | NA         | NA   | NA      | NA    | 1       | NA     | Internal error in submodule 1, not related to user input        | Internal error in submodule 1, not related to user input        |
      | FanFailure          | 1    | NA         | NA   | NA      | NA    | NA      | 1      | Fan 1 has failed                                                | Fan 1 has failed                                                |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms without parameters for TUV moduleare are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm for TUV module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is TUV
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type             | message                                                             | issue                                                               |
      | PayloadOutOfRange      | Payload is out of range                                             | Payload is out of range                                             |
      | PayloadVersionMismatch | Payload version does not match expected version                     | Payload version does not match expected version                     |
      | ResourceNotAvailable   | Resource not available                                              | Resource not available                                              |
      | ApplicationResources   | Application resource error                                          | Application resource error                                          |
      | ResetFailed            | Reset instrument failed                                             | Reset instrument failed                                             |
      | MessageHandlerNotFound | Message handler not found                                           | Message handler not found                                           |
      | SocketConnection       | Listener socket error                                               | Listener socket error                                               |
      | NetworkReceive         | Error receiving data from socke                                     | Error receiving data from socke                                     |
      | NetworkSend            | Error sending data                                                  | Error sending data                                                  |
      | InvalidMessage         | Invalid message                                                     | Invalid message                                                     |
      | ChannelSubscription    | Failed to subscribe to data channel or get subscription list        | Failed to subscribe to data channel or get subscription list        |
      | EventSubscription      | Failed to subscribe to event notifications or get subscription list | Failed to subscribe to event notifications or get subscription list |
      | InstrumentStateChange  | Error changing instrument state                                     | Error changing instrument state                                     |
      | FailedToCreateCap      | Failed to create CAP                                                | Failed to create CAP                                                |
      | ThermistorInoperative  | Thermistor read failure                                             | Thermistor read failure                                             |
      | UnknownError           | Unknown error                                                       | Unknown error                                                       |
      | ResetNVRAMFailed       | Reset NVRAM failed                                                  | Reset NVRAM failed                                                  |
      | NetworkTimeProtocol    | SNTP error                                                          | SNTP error                                                          |
      | LeakSensorNotPresent   | Leak sensor 1 is not present                                        | Leak sensor 1 is not present                                        |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms with parameters for TUV module are generated and verify in Empower message center
    When user generates the "<alarm>_type" alarm with "<fuse>", "<leak_detid>", "<temp>", "<control>", "<power>", "<subm_id>", "<fan_id>" parameters for TUV module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is TUV
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type          | fuse | Leak_detid | temp | control | power | subm_id | fan_id | message                                                         | issue                                                           |
      | FuseBlown           | 1    | NA         | NA   | NA      | NA    | NA      | NA     | Fuse 1 has blown                                                | Fuse 1 has blown                                                |
      | LeakDetected        | NA   | 1          | NA   | NA      | NA    | NA      | NA     | Leak detector 1 has detected a leak                             | Leak detector 1 has detected a leak                             |
      | TemperatureSensor   | NA   | NA         | 20   | OFF     | NA    | NA      | NA     | Temperature sensor failure with set point 20 degC, state is OFF | Temperature sensor failure with set point 20 degC, state is OFF |
      | TemperatureFailSafe | NA   | NA         | NA   | NA      | 70    | NA      | NA     | Temperature failsafe triggered with heater/cooler power = 70%   | Temperature failsafe triggered with heater/cooler power = 70%   |
      | InternalCondition   | NA   | NA         | NA   | NA      | NA    | 1       | NA     | Internal error in submodule 1, not related to user input        | Internal error in submodule 1, not related to user input        |
      | FanFailure          | 1    | NA         | NA   | NA      | NA    | NA      | 1      | Fan 1 has failed                                                | Fan 1 has failed                                                |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms without parameters for Chc moduleare are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm for Chc module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is Chc
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type             | message                                                             | issue                                                               |
      | PayloadOutOfRange      | Payload is out of range                                             | Payload is out of range                                             |
      | PayloadVersionMismatch | Payload version does not match expected version                     | Payload version does not match expected version                     |
      | ResourceNotAvailable   | Resource not available                                              | Resource not available                                              |
      | ApplicationResources   | Application resource error                                          | Application resource error                                          |
      | ResetFailed            | Reset instrument failed                                             | Reset instrument failed                                             |
      | MessageHandlerNotFound | Message handler not found                                           | Message handler not found                                           |
      | SocketConnection       | Listener socket error                                               | Listener socket error                                               |
      | NetworkReceive         | Error receiving data from socke                                     | Error receiving data from socke                                     |
      | NetworkSend            | Error sending data                                                  | Error sending data                                                  |
      | InvalidMessage         | Invalid message                                                     | Invalid message                                                     |
      | ChannelSubscription    | Failed to subscribe to data channel or get subscription list        | Failed to subscribe to data channel or get subscription list        |
      | EventSubscription      | Failed to subscribe to event notifications or get subscription list | Failed to subscribe to event notifications or get subscription list |
      | InstrumentStateChange  | Error changing instrument state                                     | Error changing instrument state                                     |
      | FailedToCreateCap      | Failed to create CAP                                                | Failed to create CAP                                                |
      | ThermistorInoperative  | Thermistor read failure                                             | Thermistor read failure                                             |
      | UnknownError           | Unknown error                                                       | Unknown error                                                       |
      | ResetNVRAMFailed       | Reset NVRAM failed                                                  | Reset NVRAM failed                                                  |
      | NetworkTimeProtocol    | SNTP error                                                          | SNTP error                                                          |
      | LeakSensorNotPresent   | Leak sensor 1 is not present                                        | Leak sensor 1 is not present                                        |


  @real @weekly @new @ignore
  Scenario Outline: To verify Common alarms with parameters for Chc module are generated and verify in Empower message center
    When user generates the "<alarm>_type" alarm with "<fuse>", "<leak_detid>", "<temp>", "<control>", "<power>", "<subm_id>", "<fan_id>" parameters for Chc module
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is Chc
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type          | fuse | Leak_detid | temp | control | power | subm_id | fan_id | message                                                         | issue                                                           |
      | FuseBlown           | 1    | NA         | NA   | NA      | NA    | NA      | NA     | Fuse 1 has blown                                                | Fuse 1 has blown                                                |
      | LeakDetected        | NA   | 1          | NA   | NA      | NA    | NA      | NA     | Leak detector 1 has detected a leak                             | Leak detector 1 has detected a leak                             |
      | TemperatureSensor   | NA   | NA         | 20   | OFF     | NA    | NA      | NA     | Temperature sensor failure with set point 20 degC, state is OFF | Temperature sensor failure with set point 20 degC, state is OFF |
      | TemperatureFailSafe | NA   | NA         | NA   | NA      | 70    | NA      | NA     | Temperature failsafe triggered with heater/cooler power = 70%   | Temperature failsafe triggered with heater/cooler power = 70%   |
      | InternalCondition   | NA   | NA         | NA   | NA      | NA    | 1       | NA     | Internal error in submodule 1, not related to user input        | Internal error in submodule 1, not related to user input        |
      | FanFailure          | 1    | NA         | NA   | NA      | NA    | NA      | 1      | Fan 1 has failed                                                | Fan 1 has failed                                                |
