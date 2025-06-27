@system @ALIST-231
Feature: System | Pressure Units workflow

  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Pressure units updated in Control Panel and Method Editor when changed from Console
    Given user sets the pressure unit "<kiosk_value>" in kiosk
    And Run Samples window is opened
    And Console is opened
    When user selects the pressure unit "<value>" in Console Settings window
    Then Console Pump window displays "<value>" pressure unit for System, Delta and Sample pressures
    And Control Panel window displays "<value>" pressure unit for System pressure
    When Method Editor is opened
    Then System pressure, sample pressure, primary pressure, accumulator pressure, degasser pressure, pressure limits are displayed in "<value>" pressure unit
    When kiosk is open
    Then the pressure unit is in "<kiosk_value>" for Delta pressure, system pressure and sample pressure

    Examples:
      | value | kiosk_value |
      | psi   | bar         |
      | bar   | kPa         |
      | kPa   | MPa         |


  @real_or_simulation @weekly @new @ignore
  Scenario Outline: Pressure units not updated in Console, Control Panel and Method Editor when changed from Kiosk
    Given user sets the pressure unit "<value>" in Console Setting window
    When user selects the pressure unit "<kiosk_value>" in kiosk
    Then the pressure unit is in "<kiosk_value>" for Delta, system and sample pressure in kiosk
    When Run Samples window is opened
    And Console is opened
    Then user confirms that Console Pump window displays "<value>" pressure unit for System, Delta and Sample pressures
    And Control Panel window displays "<value>" pressure unit for System pressure
    When Method Editor is opened
    Then System pressure, sample pressure, primary pressure, accumulator pressure, degasser pressure, pressure limits are displayed in "<value>" pressure unit

    Examples:
      | kiosk_value | value |
      | psi         | bar   |
      | bar         | kPa   |
      | kPa         | psi   |
      | MPa         | kPa   |