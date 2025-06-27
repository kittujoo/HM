@kiosk @ALIST-228 @kiosk_instrument_config_screen
Feature: Kiosk | Instrument configuration screen

  @real @daily @quarantine @defect:INSISPP-8357
  Scenario Outline: To verify a valid dwell volume is being accepted and saved
    When User navigates to the instrument settings screen
    And User taps the "dwell-volume" panel
    And User enters "<dwell_value>"
    Then Information appears providing a warning about effects of changing this value
    When User saves the changes
    And User navigates to the instrument settings screen
    Then User validates the dwell value "<dwell_value>" was saved

    Examples:
      | dwell_value |
      | 1.250       |
      | 0.025       |
      | 10.000      |

  @real @daily
  Scenario Outline: To verify an invalid dwell volume is not being accepted
    When User navigates to the instrument settings screen
    And User taps the "dwell-volume" panel
    And User enters "<dwell_value>"
    Then User validates the error condition is met


    Examples:
      | dwell_value |
      | 0.015       |
      | 0.024       |
      | 10.01       |

  @real @daily
  Scenario Outline: To verify different pressure unit changes are being saved
    When User navigates to the instrument settings screen
    And User taps the "units" panel
    And User selects a "<pressure_unit>" option
    And User saves the changes
    And User navigates to the instrument settings screen
    And User taps the "units" panel
    Then User validates the "<pressure_unit>" option was saved
    When User saves the changes
    And User navigates to home screen
    Then User validates the pressure units in the dashboard is "<pressure_unit>"

    Examples:
      | pressure_unit |
      | MPa           |
      | kPa           |
      | bar           |
      | psi           |

  @real @daily
  Scenario Outline: To verify tubing kit
    When User navigates to the instrument settings screen
    And User taps the "tubing-kit" panel
    And User selects "<tubing_kit_option>"
    And User saves the changes
    And User navigates to the instrument settings screen
    And User taps the "tubing-kit" panel
    Then User validates the tubing kit option "<tubing_kit_option>" was saved

    Examples:
      | tubing_kit_option |
      | high flow         |
      | high ph           |
      | standard          |

  @real @daily @quarantine @defect:INSISPP-8357
  Scenario Outline: To verify the system configuration settings option is not changed when the user taps the cancel button
    When User navigates to the instrument settings screen
    And User taps the "dwell-volume" panel
    And User enters "<actual_dwell_value>"
    And User taps the "units" panel
    And User selects a "<actual_pressure_unit>" option
    And User taps the "tubing-kit" panel
    And User selects "<actual_tubing_kit_option>"
    And User saves the changes
    And User navigates to options screen
    Then User validates the "<actual_dwell_value>" "<actual_pressure_unit>" and "<actual_tubing_kit_option>" were saved
    When User navigates to the instrument settings screen
    And User taps the dwell-volume panel
    And User enters "<desired_dwell_value>"
    And User taps the "units" panel
    And User selects a "<desired_pressure_unit>" option
    And User taps the "tubing-kit" panel
    And User selects "<desired_tubing_kit_option>"
    And User cancels the settings
    Then User validates the "<actual_dwell_value>" "<actual_pressure_unit>" and "<actual_tubing_kit_option>" were saved

    Examples:
      | actual_dwell_value | actual_pressure_unit | actual_tubing_kit_option | desired_dwell_value | desired_tubing_kit_option | desired_pressure_unit |
      | 1.850              | psi                  | standard                 | 2.00                | high flow                 | bar                   |
      