@ALIST-258 @ICS @simulation @weekly @tuv @tuv_bio @method_editor_method_report_consistency @new @ignore
Feature: Method Editor Method report consistency
  The method report should contain a list of the parameters used in the method editor.
  The method report is an useful way to generate and visualise method information in a summarized view without opening the method editor.
  JIRA corresponding requirement: SRS-622


  #### Scenario testing titles and labels in intrument method report ###
  ### Importantant note: Fields which are not configured in the method will not appear in the report ###
  ### Important note: Fields which have the toggle disabled will not show a value in the report ###
  Scenario: Method report titles and labels
    Given an instrument method is opened
    And the following data channels are set to "On"
      | Data channel        |
      | Ambient Temperature |
      | System Pressure     |
      | Flow Rate           |
      | %A                  |
      | %B                  |
      | %C                  |
      | %D                  |
      | Primary             |
      | Accumulator         |
      | Degasser            |
      | Sample Temperature  |
      | Sample Pressure     |

    And the following options are set to "On"
      | Option                       |
      | Sample Temperature           |
      | Sample Temperature Tolerance |
      | Column Temperature           |
      | Column Temperature Tolerance |
      | Lamp                         |

    And the Wavelenght Mode is set to "Dual"
    When the instrument method is saved
    And the instrument method is reported
    And the instrument method report is opened
    Then the Instrument Method Report has the following labels
      | Label                                        | Expected text                             |
      | Method Information menu title                | Method Information                        |
      | Method Comments                              | Method Comments                           |
      | Method Modified                              | Method Modified User                      |
      | Method Locked                                | Method Locked                             |
      | Method Id                                    | Method Id                                 |
      | Old Id                                       | Old Id                                    |
      | Method Version                               | Method Version                            |
      | Method Edit User                             | Method Edit User                          |
      | Source S/W Info                              | Source S/W Info                           |
      | Alliance iS Instrument Setup main menu title | Alliance iS Instrument Setup              |
      | System submenu title                         | System                                    |
      | Ambient Temperature Data Channel Enabled     | Ambient Temperature Data Channel Enabled  |
      | Pump submenu title                           | Pump                                      |
      | Gradient Start                               | Gradient Start                            |
      | Low Pressure Limit                           | Low Pressure Limit                        |
      | High Pressure Limit                          | High Pressure Limit                       |
      | Flow Ramp Period                             | Flow Ramp Period                          |
      | Stroke Volume                                | Stroke Volume                             |
      | Seal Wash Period                             | Seal Wash Period                          |
      | System Pressure Data Channel Enabled         | System Pressure Data Channel Enabled      |
      | Flow Rate Data Channel Enabled               | Flow Rate Data Channel Enabled            |
      | % A Data Channel Enabled                     | % A Data Channel Enabled                  |
      | % B Data Channel Enabled                     | % B Data Channel Enabled                  |
      | % C Data Channel Enabled                     | % C Data Channel Enabled                  |
      | % D Data Channel Enabled                     | % D Data Channel Enabled                  |
      | Primary Pressure Data Channel Enabled        | Primary Pressure Data Channel Enabled     |
      | Accumulator Pressure Data Channel Enabled    | Accumulator Pressure Data Channel Enabled |
      | Degasser Pressure Data Channel Enabled       | Degasser Pressure Data Channel Enabled    |
      | Solvent A                                    | Solvent A                                 |
      | Solvent B                                    | Solvent B                                 |
      | Solvent C                                    | Solvent C                                 |
      | Solvent D                                    | Solvent D                                 |
      | Gradient Table table title                   | Gradient Table                            |
      | SM-FTN submenu title                         | SM-FTN                                    |
      | Draw Rate                                    | Draw Rate                                 |
      | Needle Placement                             | Needle Placement                          |
      | Sample Temperature Enabled                   | Sample Temperature Enabled                |
      | Sample Temperature                           | Sample Temperature                        |
      | Sample Temperature Tolerance Enabled         | Sample Temperature Tolerance Enabled      |
      | Sample Temperature Tolerance                 | Sample Temperature Tolerance              |
      | Seal Wash Solvent                            | Seal Wash Solvent                         |
      | Needle Wash Solvent                          | Needle Wash Solvent                       |
      | Wash Time                                    | Wash Time                                 |
      | Sample Temperature Data Channel Enabled      | Sample Temperature Data Channel Enabled   |
      | Sample Pressure Data Channel Enabled         | Sample Pressure Data Channel Enabled      |
      | TUV submenu title                            | TUV                                       |
      | Lamp On                                      | Lamp On                                   |
      | Wavelength Mode                              | Wavelength Mode                           |
      | Channel A Wavelength                         | Channel A Wavelength                      |
      | Channel B Wavelength                         | Channel B Wavelength                      |
      | Data rate                                    | Data rate                                 |
      | Filter behavior                              | Filter behavior                           |
      | Filter Time                                  | Filter Time                               |
      | Autozero On Inject Start                     | Autozero On Inject Start                  |
      | Autozero On Wavelength                       | Autozero On Wavelength Change             |
      | Column submenu title                         | Column                                    |
      | Column Temperature Enabled                   | Column Temperature Enabled                |
      | Column Temperature                           | Column Temperature                        |
      | Column Temperature Tolerance Enabled         | Column Temperature Tolerance Enabled      |
      | Column Temperature Tolerance                 | Column Temperature Tolerance              |
      | Column Temperature Data Channel Enabled      | Column Temperature Data Channel Enabled   |
      | Column Id                                    | Column Id                                 |
      | Column Name                                  | Column Name                               |

      # Scenario Testing that value fields not enabled or not filled are not reported #
      # Possible defect from rounding values #
  Scenario: All optional fields are turned off
    Given a method is configured with the following values
      | Setting                          | Value                         |
      | Ambient Temperature Data Channel | Off                           |
      | System Pressure Data Channel     | Off                           |
      | Flow Rate Data Channel           | Off                           |
      | %A Data Channel                  | Off                           |
      | %B Data Channel                  | Off                           |
      | %C Data Channel                  | Off                           |
      | %D Data Channel                  | Off                           |
      | Primary Data Channel             | Off                           |
      | Accumulator Data Channel         | Off                           |
      | Degasser Pressure                | Off                           |
      | Sample Temperature Data Channel  | Off                           |
      | Sample Pressure Data Channel     | Off                           |
      | Column Temperature Data channel  | Off                           |
      | Solvent A                        | Not configured                |
      | Solvent B                        | Not configured                |
      | Solvent C                        | Not configured                |
      | Solvent D                        | Not configured                |
      | Column                           | Other: Not an eConnect Column |
      | Comment                          | Empty                         |
      | FTN Set Compartment Temperature  | Off                           |
      | Seal wash                        | Not configured                |
      | Needle wash                      | Not configured                |
      | Wash time                        | 6                             |
      | sample Manager Advanced          | Default                       |
      | Column Compartment Temperature   | Off                           |
      | Gradient Start Option            | At injection                  |
      | Gradient End Stop Flow           | Disabled                      |
      | Pressure limits                  | 10 to 199                     |
      | Seal wash frequency              | 5                             |
      | Flow Ramp Period                 | 0.2                           |
      | Stroke volume                    | 100                           |
      | Lamp State                       | On                            |
      | Wavelength Mode                  | Single                        |
      | Data rate                        | 160                           |
      | Wavelength A                     | 300                           |
      | Filter                           | Normal                        |
      | Autozero On Inject Start         | Autozero                      |
      | Autozero On Wavelength Change    | Maintain baseline             |

    And with the following gradient table
      | Time (min) | Flow (ml/min) | %A   | %B   | %C   | % D  | Curve   |
      | Initial    | 1.000         | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 2.00       | 2.000         | 50.0 | 50.0 | 0.0  | 0.0  | 6       |

    When an Instrument Method Report is saved
    And the Instrument Method is reported
    And the Intrument Method report is opened
    Then the Instrument Method report has the following fields
      | Field                                     | Value                                                               |
      | Ambient Temperature Data Channel Enabled  | false                                                               |
      | Gradient Start                            | At Injection                                                        |
      | Low Pressure Limit                        | 10.00(bar)                                                          |
      | High Pressure Limit                       | 199.04 (bar)                                                        |
      | Flow ramp Period                          | 0.200(min)                                                          |
      | Stroke Volume                             | 100.0(µL)                                                           |
      | Seal Wash Period                          | 5.0(min)                                                            |
      | System Pressure Data Channel Enabled      | False                                                               |
      | Flow Rate Data Channel Enabled            | False                                                               |
      | %A Data Channel Enabled                   | False                                                               |
      | %B Data Channel Enabled                   | False                                                               |
      | %C Data Channel Enabled                   | False                                                               |
      | %D Data Channel Enabled                   | False                                                               |
      | Primary Pressure Data Channel Enabled     | False                                                               |
      | Accumulator Pressure Data Channel Enabled | False                                                               |
      | Degasser Pressure Data Channel Enabled    | False                                                               |
      | Draw Rate                                 | 100.00(µL/min)                                                      |
      | Needle Placement                          | 4.00(mm)                                                            |
      | Sample Temperature Enabled                | False                                                               |
      | Seal Wash Solvent                         | Not configured                                                      |
      | Wash time                                 | 6.0(s)                                                              |
      | Sample Temperature Data Channel Enabled   | False                                                               |
      | Sample Pressure Data Channel Enabled      | False                                                               |
      | Lamp On                                   | True                                                                |
      | Wavelength Mode                           | Single                                                              |
      | Channel A Wavelength                      | 300(nm)                                                             |
      | Data rate                                 | 160 Hz                                                              |
      | Filter behavior                           | Hamming Filter                                                      |
      | Filter Time                               | 0.01(s)                                                             |
      | Column Temperature Enabled                | False                                                               |
      | Column Temperature Data Channel Enabled   | False                                                               |
      | Column Name                               | Other: Not an eConnect Column, -1A, -1.0um, -1.0mm X -1mm +eConnect |

    And the gradient table contained in the report is as follows
      | Time (min) | Flow Rate (ml/min) | Solvent A (%) | Solvent B (%) | Solvent C (%) | Solvent D (%) | Curve |
      | 0.00       | 1.000              | 25.0          | 25.0          | 25.0          | 25.0          | 6     |
      | 2.00       | 2.000              | 50.0          | 50.0          | 0.0           | 0.0           | 6     |

      # Scenario Testing that all fields that are enabled appear in the repport and the values that are configured #

  Scenario: All fields in the method editor available and all posible options enabled
    Given a method is configured with the following values
      | Setting                          | Value                       |
      | Ambient Temperature Data Channel | On                          |
      | System Pressure Data Channel     | On                          |
      | Flow Rate Data Channel           | On                          |
      | %A Data Channel                  | On                          |
      | %B Data Channel                  | On                          |
      | %C Data Channel                  | On                          |
      | %D Data Channel                  | On                          |
      | Primary Data Channel             | On                          |
      | Accumulator Data Channel         | On                          |
      | Degasser Pressure                | On                          |
      | Sample Temperature Data Channel  | On                          |
      | Sample Pressure Data Channel     | On                          |
      | Column Temperature Data channel  | On                          |
      | Solvent A                        | Water                       |
      | Solvent B                        | Acetonitrile                |
      | Solvent C                        | Methanol                    |
      | Solvent D                        | Tetrahydrofuran             |
      | Column                           | Symmetry Shield RP18        |
      | Comment                          | This is a pertinent comment |
      | FTN Set Compartment Temperature  | On                          |
      | FTN Temperature Setpoint         | 40                          |
      | FTN Tolerance                    | 4                           |
      | Seal wash                        | Trifluoroacetic Acid        |
      | Needle wash                      | Formic Acid                 |
      | Wash time                        | 6                           |
      | sample Manager Advanced          | Custom                      |
      | Needle placement from bottom     | 6.0                         |
      | Syringe Draaw Rate               | 100.0                       |
      | Column Compartment Temperature   | On                          |
      | Column Temperature Setpoint      | 40                          |
      | Column Temperature Tolerance     | On                          |
      | Column Tolerance                 | 1                           |
      | Gradient Start Option            | Before                      |
      | Volumes delay                    | 100                         |
      | Gradient End Stop Flow           | Enabled                     |
      | Time period                      | 1                           |
      | Pressure limits                  | 10 to 199                   |
      | Seal wash frequency              | 5                           |
      | Flow Ramp Period                 | 0.2                         |
      | Stroke volume                    | 132                         |
      | Lamp State                       | On                          |
      | Wavelength Mode                  | Dual mode                   |
      | Data rate                        | 2                           |
      | Wavelength A                     | 300                         |
      | Wavelength B                     | 400                         |
      | Filter                           | Normal                      |
      | Autozero On Inject Start         | Autozero                    |
      | Autozero On Wavelength Change    | Maintain baseline           |

    And with the following gradient table
      | Time (min) | Flow (ml/min) | %A   | %B   | %C   | % D  | Curve   |
      | Initial    | 1.000         | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 2.00       | 2.000         | 50.0 | 50.0 | 0.0  | 0.0  | 6       |

    When an Instrument Method Report is saved
    And the Instrument Method is reported
    And the Instrument Method Report is opened
    Then the Instrument Method report has the following fields
      | Field                                     | Value                                                            |
      | Comment                                   | This is a pertinent comment                                      |
      | Ambient Temperature Data Channel Enabled  | true                                                             |
      | Gradient Start                            | Before Injection                                                 |
      | Delay volume                              | 100.00(µL)                                                       |
      | Low Pressure Limit                        | 10.00(bar)                                                       |
      | High Pressure Limit                       | 199.04 (bar)                                                     |
      | Flow ramp Period                          | 0.200(min)                                                       |
      | Stroke Volume                             | 132.0(µL)                                                        |
      | Seal Wash Period                          | 5.0(min)                                                         |
      | System Pressure Data Channel Enabled      | True                                                             |
      | Flow Rate Data Channel Enabled            | True                                                             |
      | %A Data Channel Enabled                   | True                                                             |
      | %B Data Channel Enabled                   | True                                                             |
      | %C Data Channel Enabled                   | True                                                             |
      | %D Data Channel Enabled                   | True                                                             |
      | Primary Pressure Data Channel Enabled     | True                                                             |
      | Accumulator Pressure Data Channel Enabled | True                                                             |
      | Degasser Pressure Data Channel Enabled    | True                                                             |
      | Solvent A                                 | Water                                                            |
      | Solvent B                                 | Acetonitrile                                                     |
      | Solvent C                                 | Methanol                                                         |
      | Solvent D                                 | Tetrahydrofuran                                                  |
      | Draw Rate                                 | 100.00(µL/min)                                                   |
      | Needle Placement                          | 6.00(mm)                                                         |
      | Sample Temperature Enabled                | True                                                             |
      | Sample Temperature                        | 40.00(°C)                                                        |
      | Sample Temperature Tolerance Enabled      | True                                                             |
      | Sample Temperature Tolerance              | 4.00(°C)                                                         |
      | Seal Wash Solvent                         | Trifluoroacetic Acid                                             |
      | Needle wash Solvent                       | Formic Acid                                                      |
      | Wash time                                 | 6.0(s)                                                           |
      | Sample Temperature Data Channel Enabled   | True                                                             |
      | Sample Pressure Data Channel Enabled      | True                                                             |
      | Lamp On                                   | True                                                             |
      | Wavelength Mode                           | Dual                                                             |
      | Channel A Wavelength                      | 300(nm)                                                          |
      | Channel B Wavelength                      | 400(nm)                                                          |
      | Data rate                                 | 2 Hz                                                             |
      | Filter behavior                           | Hamming Filter                                                   |
      | Filter Time                               | 1 (s)                                                            |
      | Autozero on Inject Start                  | Autozero                                                         |
      | Autozero on Wavelength Change             | Maintain Baseline                                                |
      | Column Temperature Enabled                | True                                                             |
      | Column Temperature                        | 40.00(°C)                                                        |
      | Column Temperature Tolerance Enabled      | True                                                             |
      | Column Temperature Tolerance              | 1.00(°C)                                                         |
      | Column Temperature Data Channel Enabled   | True                                                             |
      | Column Name                               | Symmetry Shield RP18 C18, 100A, 5.00um, 3.9mm X 150mm + eConnect |

    And the gradient table contained in the report is as follows
      | Time (min) | Flow Rate (ml/min) | Solvent A (%) | Solvent B (%) | Solvent C (%) | Solvent D (%) | Curve |
      | 0.00       | 1.000              | 25.0          | 25.0          | 25.0          | 25.0          | 6     |
      | 2.00       | 2.000              | 50.0          | 50.0          | 0.0           | 0.0           | 6     |
      | 3.00       | 0.000              | 50.0          | 50.0          | 0.0           | 0.0           | 11    |

      # Scenario with tolerances disabled but temperatures enabled #

  Scenario: Tolerances disabled but temperatures enabled
    Given a method is configured with the following values
      | Setting                        | Value |
      | FTN Temperature                | On    |
      | FTN Temperature Setpoint       | 40    |
      | FTN Tolerance                  | Off   |
      | Column Compartment Temperature | On    |
      | Column Temperature Setpoint    | 40    |
      | Column Temperature Tolerance   | Off   |

    When an Instrument Method Report is saved
    And the Instrument Method is reported
    And the Instrument Method Report is opened
    Then the Instrument Method report has the following values
      | Field                                | Value     |
      | Sample Temperature Enabled           | True      |
      | Sample Temperature                   | 40.00(°C) |
      | Sample Temperature Tolerance Enabled | False     |
      | Column Temperature Enabled           | True      |
      | Column Temperature                   | 40.00(°C) |
      | Column Temperature Tolerance Enabled | False     |


