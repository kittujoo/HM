@system @ALIST-231 @system_qsm_alarms_feature
Feature: System | QSM Alarms Workflow

  Background:
    Given an instrument system in "IDLE" state is connected

  @real @weekly @new @ignore
  Scenario Outline: To verify QSM alarms for degaser are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with "<AtoD>" AtoD, pressure "<pressure>", maximum pressure limit "<max_pressure_limit>" and "<decay_Rate>" decay rate
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
      | alarm_type                                   | AtoD | pressure | max_pressure_limit | decay_Rate | message                                                             | issue                                                               |
      | DegasserFailedReachSetPoint                  | A    | 2.5      | NA                 | NA         | Degasser failed to reach set point: A, 2.5psi                       | Degasser failed to reach set point: A, 2.5psi                       |
      | DegasserHasNoVacuum                          | A    | 2.5      | NA                 | NA         | Degasser has no vacuum: A, 2.5 psi                                  | Degasser has no vacuum: A, 2.5 psi                                  |
      | DegasserHighPressure                         | A    | 3.5      | 3                  | NA         | Degasser pressure exceeded limit 3: A/, 3.5psi                      | Degasser pressure exceeded limit 3: A/, 3.5psi                      |
      | DegasserLowPressure                          | NA   | 0.1      | NA                 | NA         | Degasser low pressure 0.1psi                                        | Degasser low pressure 0.1psi                                        |
      | DegasserPressureDecayRateHigh                | NA   | 2.7      | N                  | 2.8        | Degasser decay rate 2.8psi/min is high at pressure 2.7psi           | Degasser decay rate 2.8psi/min is high at pressure 2.7psi           |
      | DegasserPressureDecayRateNormal              | NA   | 2.5      | NA                 | 2.4        | Degasser decay rate 2.4psi/min is normal at 2.5psi                  | Degasser decay rate 2.4psi/min is normal at 2.5psi                  |
      | DegasserTransducerOutOfRangeDuringHolding    | A    | 2.5      | NA                 | NA         | Degasser transducer A, 2,5psi is out of range during holding        | Degasser transducer A, 2,5psi is out of range during holding        |
      | DegasserTransducerOutOfRangeDuringInit       | A    | 2.5      | NA                 | NA         | Degasser transducer A, 2.5psi is out of range during initialization | Degasser transducer A, 2.5psi is out of range during initialization |
      | DegasserTransducerOutOfRangeDuringMonitoring | A    | 2.5      | NA                 | NA         | Degasser transducer A, 2.5psi is out of range during monitoring     | Degasser transducer A, 2.5psi is out of range during monitoring     |
      | DegasserTransducerOutOfRangeDuringPumping    | A    | 2.5      | NA                 | NA         | Degasser transducer A, 2.5psi is out of range during pumping        | Degasser transducer A, 2.5psi is out of range during pumping        |


  @real @weekly @new @ignore
  Scenario Outline: To verify QSM alarms for pump are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with pressure "<pressure>", low pressure limit "<max_pressure_limit>", high pressure limit "<high_pressure_limit>" and "<flow>" flow
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
      | alarm_type                          | pressure | low_pressure_limit | high_pressure_limit | flow | message                                                                   | issue                                                                     |
      | PumpAccumAxisLostSync               | NA       | NA                 | NA                  | NA   | Accumulator pump lost axis synchronization                                | Accumulator pump lost axis synchronization                                |
      | PumpAccumHomingRange                | NA       | NA                 | NA                  | NA   | Accumulator pump homing range error                                       | Accumulator pump homing range error                                       |
      | PumpAccumHomingRestriction          | NA       | NA                 | NA                  | NA   | Accumulator pump homing restriction                                       | Accumulator pump homing restriction                                       |
      | PumpAccumHWOverPressure             | 2.5      | NA                 | NA                  | 1.5  | Accumulator hardware over 2.5 psi at 1.5 mL/min                           | Accumulator hardware over 2.5 psi at 1.5 mL/min                           |
      | PumpAccumMotorAxisCouldNotBeHomed   | NA       | NA                 | NA                  | NA   | Accumulator pump motor axis could not be homed                            | Accumulator pump motor axis could not be homed                            |
      | PumpAccumMotorAxisTimeout           | NA       | NA                 | NA                  | NA   | Accumulator pump motor axis timeout                                       | Accumulator pump motor axis timeout                                       |
      | PumpAccumTransducerRange            | 3.5      | 2.3                | 2.7                 | NA   | Accumulator pump transducer pressure 3.5psi not within limits of 2.3, 2.7 | Accumulator pump transducer pressure 3.5psi not within limits of 2.3, 2.7 |
      | PumpACVDisconnected                 | NA       | NA                 | NA                  | NA   | Pump active check valve disconnected                                      | Pump active check valve disconnected                                      |
      | PumpBadState                        | NA       | NA                 | NA                  | NA   | Pump is not in a state that can honor a command                           | Pump is not in a state that can honor a command                           |
      | PumpMotorCurrent                    | NA       | NA                 | NA                  | NA   | Pump motor current error                                                  | Pump motor current error                                                  |
      | PumpPEMInitFailure                  | NA       | NA                 | NA                  | NA   | Pressure event monitor initialization failure                             | Pressure event monitor initialization failure                             |
      | PumpPEMRuntimeFailure               | NA       | NA                 | NA                  | NA   | Pressure event monitor runtime timeout                                    | Pressure event monitor runtime timeout                                    |
      | PumpPrimaryAxisLossOfSync           | NA       | NA                 | NA                  | NA   | Primary pump lost axis synchronization                                    | Primary pump lost axis synchronization                                    |
      | PumpPrimaryHomingRange              | NA       | NA                 | NA                  | NA   | Primary pump homing range error                                           | Primary pump homing range error                                           |
      | PumpPrimaryHomingRestriction        | NA       | NA                 | NA                  | NA   | Primary pump homing restriction                                           | Primary pump homing restriction                                           |
      | PumpPrimaryHWOverPressure           | 2.5      | NA                 | NA                  | 1.5  | Primary hardware over  2.5psi at 1.5mL/min                                | Primary hardware over  2.5psi at 1.5mL/min                                |
      | PumpPrimaryMotorAxisCouldNotBeHomed | NA       | NA                 | NA                  | NA   | Primary pump motor axis could not be homed                                | Primary pump motor axis could not be homed                                |
      | PumpPrimaryMotorAxisTimeout         | NA       | NA                 | NA                  | NA   | Primary pump motor axis timeout                                           | Primary pump motor axis timeout                                           |
      | PumpPrimaryTransducerRange          | 3.5      | 2.2                | 2.7                 | NA   | Primary pump transducer pressure 3.5psi not within limits of 2.2, 2.7     | Primary pump transducer pressure 3.5psi not within limits of 2.2, 2.7     |
      | PumpStrategy                        | NA       | NA                 | NA                  | NA   | Pump strategy not found                                                   | Pump strategy not found                                                   |
      | PumpSystemHighPressure              | 2.5      | NA                 | NA                  | 1.5  | Pump system over 2.5psi at 1.5mL/min                                      | Pump system over 2.5psi at 1.5mL/min                                      |
      | PumpSystemLowPressure               | 2.5      | NA                 | NA                  | 1.5  | Pump system under 2.5psi at 1.5mL/min                                     | Pump system under 2.5psi at 1.5mL/min                                     |


  @real @weekly @new @ignore
  Scenario Outline: To verify QSM alarms for solvent manager are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with flow "<flow>"
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
      | alarm_type                                        | flow | message                                                    | issue                                                      |
      | SolventManagerBadComposition: int = 8334          | NA   | Invalid composition                                        | Invalid composition                                        |
      | SolventManagerBadPacketList: int = 8335           | NA   | Unexpected packet count                                    | Unexpected packet count                                    |
      | SolventManagerBadState: int = 8320                | NA   | Solvent manager cannot respond to command in current state | Solvent manager cannot respond to command in current state |
      | SolventManagerFailedToReachTargetFlow: int = 8328 | 2.5  | Failed to reach target flow rate of 2.5ml/min              | Failed to reach target flow rate of 2.5ml/min              |
      | SolventManagerFlowRateRange: int = 8332           | NA   | Flow rate out of range                                     | Flow rate out of range                                     |
      | SolventManagerGradientTableEmpty: int = 8337      | NA   | Gradient table is empty                                    | Gradient table is empty                                    |
      | SolventManagerGradientTableFull: int = 8336       | NA   | Gradient table is full                                     | Gradient table is full                                     |
      | SolventManagerInitGPV: int = 8323                 | NA   | Failed to activate gradient proportioning valve            | Failed to activate gradient proportioning valve            |
      | SolventManagerInitPump: int = 8322                | NA   | Failed to initialize pump                                  | Failed to initialize pump                                  |
      | SolventManagerNoResponse: int = 8321              | NA   | No response from an asynchronous request                   | No response from an asynchronous request                   |
      | SolventManagerPrimePumpIntake: int = 8327         | NA   | Did not receive intake event                               | Did not receive intake event                               |
      | SolventManagerPrimePumpSetFlow: int = 8326        | 2.5  | Cannot change prime flow rate to 2,5mL/min                 | Cannot change prime flow rate to 2,5mL/min                 |
      | SolventManagerRampPumpGetFlow: int = 8330         | NA   | Failed to get flow rate                                    | Failed to get flow rate                                    |
      | SolventManagerRampPumpIntake: int = 8333          | NA   | Intake did not start                                       | Intake did not start                                       |
      | SolventManagerRampPumpSetFlow: int = 8329         | 2.5  | Failed to set flow rate to 2.5mL/min                       | Failed to set flow rate to 2.5mL/min                       |
      | SolventManagerRampRateRange: int = 8331           | NA   | Ramp rate out of range                                     | Ramp rate out of range                                     |


  @real @weekly @new @ignore
  Scenario Outline: To verify QSM alarms for vent valve are generated and verify in Empower message center
    When user generates the "<alarm_type>" alarm with vent valve position "<vent_valve_position>"
    Then user confirms the error states in control panel
    And  user validates the "<message>" is displayed in the Empower Message Center
    When User opens kiosk
    Then user confirms the error states in the header
    And the user confirms in the log the date is the current date
    And User confirms in log the category is error
    And User confirms in log that the source is QSM
    And user validates the "<issue>" is displayed in issue resolution field
    And User validates the issue resolution is red color

    Examples:
      | alarm_type                             | vent_valve_position | message                                                                          | issue                                                                            |
      | VentValveEdgeNotDetected: int = 8197   | System              | Vent valve edge was not detected while attempting to move to System              | Vent valve edge was not detected while attempting to move to System              |
      | VentValveMotionNotDetected: int = 8194 | Blocked             | Vent Valve motion was not detected. Attempting to move to Blocked                | Vent Valve motion was not detected. Attempting to move to Blocked                |
      | VentValveMoveFailure: int = 8196       | System              | Vent valve failed to move while attempting to move to System                     | Vent valve failed to move while attempting to move to System                     |
      | VentValveMoveThreshold: int = 8198     | System              | Encoder position exceeds vent valve motor position while moving to System        | Encoder position exceeds vent valve motor position while moving to System        |
      | VentValveNotHomed: int = 8192          | NA                  | Vent valve failed to home                                                        | Vent valve failed to home                                                        |
      | VentValveSensorNotFound: int = 8195    | System              | Vent valve index for the sensor was not found while attempting to move to System | Vent valve index for the sensor was not found while attempting to move to System |
