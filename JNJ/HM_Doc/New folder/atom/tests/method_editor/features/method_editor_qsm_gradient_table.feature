@ALIST-230 @method_editor @simulation @daily @tuv @pda @tuv_bio @pda_bio @method_editor_gradient_table_feature @new @ignore
Feature: Method Editor | QSM Gradient Table
  The Gradient Table is a list of events that allows the user to change the flow and/or gradient composition during a run.
  The Gradient End Stop Flow can be enabled to allow the system to perform a Stop Flow after the gradient has been executed.
  The gradient lines should be sorted in ascending order of time.
  JIRA corresponding requirement: SRS-195.

  Background:
    Given an acquisition method that contains default settings is open
    And the Pump menu is open
    And the Gradient Table menu is open

      ### Scenario Testing Labels and Default values ###

  Scenario: Titles and descriptions are displayed - default view
    Then the Gradient Table menu title is "Gradient Table"
    And the Gradient Table title text is "Select a table row to edit"
    And the "Pump" menu is highlighted
    And the "Gradient Table" menu is highlighted
    And the Time setting table title text is "Time (min)"
    And the Flow setting table title text is "Flow (ml/min)"
    And the Pump Channel A composition table title text is "%A"
    And the Pump Channel B composition table title text is "%B"
    And the Pump Channel C composition table title text is "%C"
    And the Pump Channel D composition table title text is "%D"
    And the Gradient Curve setting table title text is "Curve"
    And the Channel A summary text is "A:Not configured"
    And the Channel B summary text is "B:Not configured"
    And the Channel C summary text is "C:Not configured"
    And the Channel D summary text is "D:Not configured"

  Scenario: Summary text options change when mobile phase fields are configured
    Given the Solvent A mobile phase option is set to Acetonitrile
    Then the Channel A summary text is "A:Acetonitrile"
    Given the Solvent B mobile phase option is set to Methanol
    Then the Channel B summary text is "B:Methanol"
    Given the Solvent C mobile phase option is set to Water
    Then the Channel C summary text is "C:Water"
    Given the Solvent D mobile phase option is set to Tetrahydrofuran
    Then the Channel A summary text is "D:Tetrahydrofuran"

  Scenario: Titles and descriptions are displayed - First gradient row selected
    When the gradient first row is clicked
    Then the gradient first row is highlighted
    And only the gradient first row is highlighted
    And the gradient row setting menu is opened on the right
    And the Time input box title text is "Time (min)"
    And the Timpe input box hint text is "0.0 to 600.0"
    And the Flow input box title text is "Flow (ml/min)"
    And the Flow input box hint text is "0.001 to 10.000"
    And the Pump Channel A composition input box title text is "%A"
    And the Pump Channel A composition hint text is "0.0 to 100.0"
    And the Pump Channel B composition input box title text is "%B"
    And the Pump Channel B composition hint text is "0.0 to 100.0"
    And the Pump Channel C composition input box title text is "%C"
    And the Pump Channel C composition hint text is "0.0 to 100.0"
    And the Pump Channel D composition input box title text is "%D"
    And the Pump Channel D composition hint text is "0.0 to 100.0"
    And the Gradient Curve setting select box title text is "Curve"
    And the Validate button is present
    And the Cancel button is present
    And the Delete Gradient Row button is present

  Scenario: Default values are displayed on the first gradient row - default view
    Then the Time setting first row value is "Initial"
    And the Flow setting first row value is "1.000"
    And the Pump Channel A composition first row value is "100.0"
    And the Pump Channel B composition first row value is "0.0"
    And the Pump Channel C composition first row value is "0.0"
    And the Pump Channel D composition first row value is "0.0"
    And the Gradient Curve setting first row value is "Initial"

      ### Potential defect, default values are rounded values to integer ###
  Scenario: Default values are displayed on the first gradient row settings - First gradient line selected
    When the gradient first line is clicked
    Then the gradient first line is highlighted
    And the Time input box value is "Initial"
    And the Flow setting first row value is "1.000"
    And the Pump Channel A composition input box value is "100.0"
    And the Pump Channel B composition input box value is "0.0"
    And the Pump Channel C composition input box value is "0.0"
    And the Pump Channel D composition input box value is "0.0"
    And the Gradient Curve input box value value is "Initial"

      ### Scenarios testing favorites and filtering ###

  Scenario: Gradient Table can be set as Favorite
    When the Gradient Table setting group is set as Favorite
    And the Favorite Settings menu is opened
    Then only the Gradient Table menu title is available

  Scenario Outline: Setting can be searched for
    When the System menu is opened
    And "<Search Text>" is entered into the search bar
    Then the Gradient Table setting group is displayed
    And the "Pump" menu is highlighted
    And the "Gradient Table" menu is highlighted

    Examples:
      | Search Text    |
      | Gradient       |
      | Gradient Table |

      ### Scenarios testing input box values and gradient rows ###

  Scenario Outline: Default values can be changed on the first gradient row settings - First gradient line selected
    Given the gradient first line is clicked
    And the gradient first line is highlighted
    When the Time input is set to "<Time>"
    And the Flow input is set to "<Flow>"
    And the Pump Channel A composition input is set to "<A_composition>"
    And the Pump Channel B composition input is set to "<B_composition>"
    And the Pump Channel C composition input is set to "<C_composition>"
    And the Pump Channel D composition input is set to "<D_composition>"
    And the Gradient Curve input value is set to "<Gradient_Curve>"
    And the settings are validated
    Then the Time input has value set to "<Time>"
    And the Flow input has value set to "<Flow>"
    And the Pump Channel A composition input has value set to "<A_composition>"
    And the Pump Channel B composition input has value set to "<B_composition>"
    And the Pump Channel C composition input has value set to "<C_composition>"
    And the Pump Channel D composition input has value set to "<D_composition>"
    And the Gradient Curve input value has value set to set to "<Gradient_Curve>"


    Examples:
      | Time    | Flow  | A_composition | B_composition | C_composition | D_composition | Gradient_Curve |
      | Initial | 0.500 | 25.0          | 25.0          | 25.0          | 25.0          | Initial        |

  Scenario: Append gradient line adds another line to the existing gradient table

    When the append new gradient line button is clicked
    Then a new gradient line is added

  Scenario: Delete gradient line deletes the currently selected gradient line
    Given a second line exists in the gradient table
    And the gradient table row is selected
    When the Delete Gradient Row button is clicked
    Then the currently selected gradient row is deleted

  Scenario: Cancel button does not save the changes
    When the gradient table is configured with the following data
      | Time    | Flow  | %A   | %B   | %C   | %D   | Curve   |
      | Initial | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 1.00    | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | 6       |

    And the second line is selected
    And the values are modified to the following
      | Time | Flow  | %A   | %B   | %C   | %D   | Curve |
      | 0.50 | 1.000 | 10.0 | 15.0 | 30.0 | 45.0 | 11    |

    And the cancel button is clicked
    Then the gradient table remains configured with the following values
      | Time    | Flow  | %A   | %B   | %C   | %D   | Curve   |
      | Initial | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 1.00    | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | 6       |

  Scenario: Slide bar available to the right of the table and mixed valid values in the gradient table
    When the gradient table is configured with the following data
      | Time    | Flow   | %A    | %B    | %C    | %D    | Curve   |
      | Initial | 0.500  | 100.0 | 0.0   | 0.0   | 0.0   | Initial |
      | 1.00    | 1.000  | 0.0   | 100.0 | 0.0   | 0.0   | 1       |
      | 2.00    | 2.000  | 0.0   | 0.0   | 100.0 | 0.0   | 2       |
      | 3.00    | 3.000  | 0.0   | 0.0   | 0.0   | 100.0 | 3       |
      | 4.00    | 4.000  | 25.0  | 25.0  | 25.0  | 25.0  | 4       |
      | 5.00    | 5.000  | 12.5  | 12.3  | 12.4  | 62.8  | 5       |
      | 6.00    | 6.000  | 12.5  | 62.8  | 12.3  | 12.4  | 6       |
      | 7.00    | 7.000  | 12.4  | 12.5  | 62.8  | 12.3  | 7       |
      | 8.00    | 8.000  | 62.8  | 12.4  | 12.3  | 12.5  | 8       |
      | 9.00    | 9.000  | 25.0  | 25.0  | 25.0  | 25.0  | 9       |
      | 10.00   | 10.000 | 25.0  | 25.0  | 25.0  | 25.0  | 10      |
      | 11.00   | 5.000  | 25.0  | 25.0  | 25.0  | 25.0  | 11      |

    Then a slide bar appears to the right of the table allowing to browse
    And no issues are raised

  Scenario: The gradient table rows are sorted based on asceding time value

    When the gradient table is configured with the following data
      | Time    | Flow   | %A    | %B    | %C    | %D    | Curve   |
      | Initial | 0.500  | 100.0 | 0.0   | 0.0   | 0.0   | Initial |
      | 1.00    | 1.000  | 0.0   | 100.0 | 0.0   | 0.0   | 1       |
      | 3.00    | 2.000  | 0.0   | 0.0   | 100.0 | 0.0   | 2       |
      | 2.00    | 3.000  | 0.0   | 0.0   | 0.0   | 100.0 | 3       |
      | 4.00    | 4.000  | 25.0  | 25.0  | 25.0  | 25.0  | 4       |
      | 6.00    | 5.000  | 12.5  | 12.3  | 12.4  | 62.8  | 5       |
      | 5.00    | 6.000  | 12.5  | 62.8  | 12.3  | 12.4  | 6       |
      | 8.00    | 7.000  | 12.4  | 12.5  | 62.8  | 12.3  | 7       |
      | 7.00    | 8.000  | 62.8  | 12.4  | 12.3  | 12.5  | 8       |
      | 11.00   | 9.000  | 25.0  | 25.0  | 25.0  | 25.0  | 9       |
      | 10.00   | 10.000 | 25.0  | 25.0  | 25.0  | 25.0  | 10      |
      | 9.00    | 5.000  | 25.0  | 25.0  | 25.0  | 25.0  | 11      |

    Then the gradient table is configured with the following data
      | Time    | Flow   | %A    | %B    | %C    | %D    | Curve   |
      | Initial | 0.500  | 100.0 | 0.0   | 0.0   | 0.0   | Initial |
      | 1.00    | 1.000  | 0.0   | 100.0 | 0.0   | 0.0   | 1       |
      | 2.00    | 3.000  | 0.0   | 0.0   | 0.0   | 100.0 | 3       |
      | 3.00    | 2.000  | 0.0   | 0.0   | 100.0 | 0.0   | 2       |
      | 4.00    | 4.000  | 25.0  | 25.0  | 25.0  | 25.0  | 4       |
      | 5.00    | 6.000  | 12.5  | 62.8  | 12.3  | 12.4  | 6       |
      | 6.00    | 5.000  | 12.5  | 12.3  | 12.4  | 62.8  | 5       |
      | 7.00    | 8.000  | 62.8  | 12.4  | 12.3  | 12.5  | 8       |
      | 8.00    | 7.000  | 12.4  | 12.5  | 62.8  | 12.3  | 7       |
      | 9.00    | 5.000  | 25.0  | 25.0  | 25.0  | 25.0  | 11      |
      | 10.00   | 10.000 | 25.0  | 25.0  | 25.0  | 25.0  | 10      |
      | 11.00   | 9.000  | 25.0  | 25.0  | 25.0  | 25.0  | 9       |

    And no issues are raised

      # Scenarios testing the mechanism for error-ing the fields #

  Scenario Outline: Time input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the Time input is set to "<Time>"
    Then the Time input is in error
    And the change cannot be validated

    Examples:
      | Time  |
      | -1    |
      | 700   |
      | 10000 |

  Scenario Outline: Flow input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the Flow input is set to "<Flow>"
    Then the Flow input is in error
    And the change cannot be validated

    Examples:
      | Time   |
      | -1     |
      | 0.0001 |
      | 10000  |

  Scenario Outline: %A input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %A input is set to "<%A>"
    Then the %A input is in error
    And the change cannot be validated

    Examples:
      | Time  |
      | -1    |
      | 121   |
      | 10000 |


  Scenario Outline: %B input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %B input is set to "<%B>"
    Then the %B input is in error
    And the change cannot be validated

    Examples:
      | Time  |
      | -1    |
      | 121   |
      | 10000 |

  Scenario Outline: %C input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %C input is set to "<%C>"
    Then the %C input is in error
    And the change cannot be validated

    Examples:
      | Time  |
      | -1    |
      | 121   |
      | 10000 |

  Scenario Outline: %D input validation error
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %D input is set to "<%D>"
    Then the %D input is in error
    And the change cannot be validated

    Examples:
      | Time  |
      | -1    |
      | 121   |
      | 10000 |


  Scenario Outline: Time input validation error clears when a valid value is entered
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the Time input is in error
    And the change cannot be validated
    When the Time input is set to valid value "<Time>"
    Then the Time input is no longer in error
    And the change can be validated

    Examples:
      | Time |
      | 1    |
      | 5    |
      | 10   |

  Scenario Outline: Flow input validation error
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the Flow input is in error
    And the change cannot be validated
    When the Flow input is set to valid value "<Flow>"
    Then the Flow input is no longer in error
    And the change can be validated

    Examples:
      | Time  |
      | 1     |
      | 1.200 |
      | 2.500 |

  Scenario: %A input validation error
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the %A input is in error
    And the change cannot be validated
    When the %A input is set to "100.0"
    Then the %A input is no longer in error
    And the change can be validated


  Scenario: %B input validation error
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the %B input is in error
    And the change cannot be validated
    When the %B input is set to "100.0"
    Then the %B input is no longer in error
    And the change can be validated

  Scenario: %C input validation error
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the %C input is in error
    And the change cannot be validated
    When the %C input is set to "100.0"
    Then the %C input is no longer in error
    And the change can be validated

  Scenario: %D input validation error
    Given a gradient table with two lines is configured
    And the second gradient line is selected
    And the %D input is in error
    And the change cannot be validated
    When the %D input is set to "100.0"
    Then the %D input is no longer in error
    And the change can be validated

      ### Scenarios for testing the input of non-numerical characters ###

  Scenario Outline: Time input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the Time input is set to "<Time>"
    Then the Time input is in error
    And the Time input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | Time        |
      | abc         |
      | !#$         |
      | empty input |

  Scenario Outline: Flow input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the Flow input is set to "<Flow>"
    Then the Flow input is in error
    And the Flow input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | Flow        |
      | abc         |
      | !#$         |
      | empty input |

  Scenario Outline: %A input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %A input is set to "<%A>"
    Then the %A input is in error
    And the %A input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | %A          |
      | abc         |
      | !#$         |
      | empty input |

  Scenario Outline: %B input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %B input is set to "<%B>"
    Then the %B input is in error
    And the %B input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | %B          |
      | abc         |
      | !#$         |
      | empty input |

  Scenario Outline: %C input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %C input is set to "<%C>"
    Then the %C input is in error
    And the %C input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | %C          |
      | abc         |
      | !#$         |
      | empty input |

  Scenario Outline: %D input non-numerical charactes cannot be validated
    Given a gradient table with two lines is configured
    When the second gradient line is selected
    And the %D input is set to "<%D>"
    Then the %D input is in error
    And the %D input hint text is "Required"
    And the input box is empty
    And the change cannot be validated

    Examples:
      | %D          |
      | abc         |
      | !#$         |
      | empty input |


  Scenario: Gradient table values for time and flow are rounded when too many decimal are entered
    Given a gradient table is configured with the following values
      | Time      | Flow      | %A   | %B   | %C   | %D   | Curve   |
      | Initial   | 0.5001111 | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 1.0012145 | 0.500999  | 25.0 | 25.0 | 25.0 | 25.0 | 6       |
      | 1.7899    | 0.48999   | 25.0 | 25.0 | 25.0 | 25.0 | 6       |
      | 1.499999  | 0.499999  | 25.0 | 25.0 | 25.0 | 25.0 | 6       |

    When the changes are validated
    Then the gradient table is configured with the following data
      | Time    | Flow  | %A   | %B   | %C   | %D   | Curve   |
      | Initial | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | Initial |
      | 1.00    | 0.501 | 25.0 | 25.0 | 25.0 | 25.0 | 6       |
      | 1.79    | 0.490 | 25.0 | 25.0 | 25.0 | 25.0 | 6       |
      | 1.50    | 0.500 | 25.0 | 25.0 | 25.0 | 25.0 | 6       |

  Scenario: Valid values are saved when the method is saved and reopened
    Given a gradient table is configured with the following data
      | Time    | Flow   | %A    | %B    | %C    | %D    | Curve   |
      | Initial | 0.500  | 100.0 | 0.0   | 0.0   | 0.0   | Initial |
      | 1.00    | 1.000  | 0.0   | 100.0 | 0.0   | 0.0   | 1       |
      | 2.00    | 3.000  | 0.0   | 0.0   | 0.0   | 100.0 | 3       |
      | 3.00    | 2.000  | 0.0   | 0.0   | 100.0 | 0.0   | 2       |
      | 4.00    | 4.000  | 25.0  | 25.0  | 25.0  | 25.0  | 4       |
      | 5.00    | 6.000  | 12.5  | 62.8  | 12.3  | 12.4  | 6       |
      | 6.00    | 5.000  | 12.5  | 12.3  | 12.4  | 62.8  | 5       |
      | 7.00    | 8.000  | 62.8  | 12.4  | 12.3  | 12.5  | 8       |
      | 8.00    | 7.000  | 12.4  | 12.5  | 62.8  | 12.3  | 7       |
      | 9.00    | 5.000  | 25.0  | 25.0  | 25.0  | 25.0  | 11      |
      | 10.00   | 10.000 | 25.0  | 25.0  | 25.0  | 25.0  | 10      |
      | 11.00   | 9.000  | 25.0  | 25.0  | 25.0  | 25.0  | 9       |

    When the method is saved
    And the method is closed and reopened
    Then the gradient table is configured with the following data
      | Time    | Flow   | %A    | %B    | %C    | %D    | Curve   |
      | Initial | 0.500  | 100.0 | 0.0   | 0.0   | 0.0   | Initial |
      | 1.00    | 1.000  | 0.0   | 100.0 | 0.0   | 0.0   | 1       |
      | 2.00    | 3.000  | 0.0   | 0.0   | 0.0   | 100.0 | 3       |
      | 3.00    | 2.000  | 0.0   | 0.0   | 100.0 | 0.0   | 2       |
      | 4.00    | 4.000  | 25.0  | 25.0  | 25.0  | 25.0  | 4       |
      | 5.00    | 6.000  | 12.5  | 62.8  | 12.3  | 12.4  | 6       |
      | 6.00    | 5.000  | 12.5  | 12.3  | 12.4  | 62.8  | 5       |
      | 7.00    | 8.000  | 62.8  | 12.4  | 12.3  | 12.5  | 8       |
      | 8.00    | 7.000  | 12.4  | 12.5  | 62.8  | 12.3  | 7       |
      | 9.00    | 5.000  | 25.0  | 25.0  | 25.0  | 25.0  | 11      |
      | 10.00   | 10.000 | 25.0  | 25.0  | 25.0  | 25.0  | 10      |
      | 11.00   | 9.000  | 25.0  | 25.0  | 25.0  | 25.0  | 9       |

  Scenario: Fields with non-valid values remain error when the method is saved
    Given a gradient table is configured with the following data
      | Time    | Flow  | %A    | %B  | %C  | %D  | Curve   |
      | Initial | 0.500 | 100.0 | 0.0 | 0.0 | 0.0 | Initial |
      | 100000  | 200   | 200   | 200 | 200 | 200 | 1       |

    When the method is saved
    Then the Time input is in error
    And the Flow input is in error
    And the %A input is in error
    And the %B input is in error
    And the %C input is in error
    And the %D input is in error

  Scenario: Non-valid values are discarded when the method is closed and reopened
    Given a gradient table is configured with the following data
      | Time    | Flow  | %A    | %B   | %C   | %D   | Curve   |
      | Initial | 0.500 | 100.0 | 0.0  | 0.0  | 0.0  | Initial |
      | 1.00    | 0.500 | 25.0  | 25.0 | 25.0 | 25.0 | 1       |

    And the method is saved
    When the gradient table is configured with the following data
      | Time    | Flow  | %A    | %B  | %C  | %D  | Curve   |
      | Initial | 0.500 | 100.0 | 0.0 | 0.0 | 0.0 | Initial |
      | 100000  | 200   | 200   | 200 | 200 | 200 | 1       |

    And the method is saved
    And the method is closed and reopened
    Then the gradient table is configured with the following data
      | Time    | Flow  | %A    | %B   | %C   | %D   | Curve   |
      | Initial | 0.500 | 100.0 | 0.0  | 0.0  | 0.0  | Initial |
      | 1.00    | 0.500 | 25.0  | 25.0 | 25.0 | 25.0 | 1       |

    And there are no issues
