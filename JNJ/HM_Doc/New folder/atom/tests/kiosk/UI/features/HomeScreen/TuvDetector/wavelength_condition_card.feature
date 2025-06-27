@kiosk @wavelength @ignore @reg @Link(https://code.waters.com/bitbucket/projects/OSQ/repos/orionisppintegrationtests/browse/Kiosk/tests/UI/features/HomeScreen/TuvDetector/wavelength_condition_card.feature)
Feature: Kiosk | Wavelength condition card

  Background:
    Given Navigate to the wavelength settings screen

  Scenario Outline: To verify that the current wavelength information in the settings screen is updated when the user selects the single wavelength mode

    When Enter the wavelength "<actual_first_wave_length>"
    And  Navigate to the wavelength conditional card
    Then Validate the single wave length info "<expected_first_wave_length>" on the condition card
    And  Navigate to the wavelength settings screen
    And  Validate wavelength current info "<expected_first_wave_length>" "<expected_second_wave_length>" "<expected_wavelength_mode>" on the setting screen

    Examples:
      | actual_first_wave_length | expected_first_wave_length | expected_second_wave_length | expected_wavelength_mode |
      | 300                      | 300 nm                     | NA                          | Single                   |

  @ui
  Scenario Outline: User cannot navigate to the wavelength conditional card screen when enters out of range wavelength

    When Enter the wavelength "<actual_first_wave_length>"
    And  Navigate to the wavelength conditional card
    Then Validate the user cannot navigate to the wavelength conditional card screen

    Examples:
      | actual_first_wave_length |
      | 7500                     |
      | 189                      |

  @ui
  Scenario Outline: To verify that the current wavelength information is updated in the settings screen when the user selects the dual wavelength mode

    When Select the dual wavelength mode
    And  Enter the dual wavelength "<actual_first_wave_length>" "<actual_second_wave_length>"
    And  Navigate to the wavelength conditional card
    Then Validate dual wavelength "<expected_first_wave_length>" "<expected_second_wave_length>" on the condition card
    And  Navigate to the wavelength settings screen
    And  Validate wavelength current info "<expected_first_wave_length>" "<expected_second_wave_length>" "<expected_wavelength_mode>" on the setting screen

    Examples:
      | actual_first_wave_length | actual_second_wave_length | expected_first_wave_length | expected_second_wave_length | expected_wavelength_mode |
      | 300                      | 700                       | 300 nm                     | 700 nm                      | Dual                     |


  Scenario Outline: To verify the current wavelength information is not update when the user enters the wavelength and taps the cancel button

    When Select the dual wavelength mode
    And  Enter the dual wavelength 254 700
    And  Navigate to the wavelength conditional card
    And  Navigate to the wavelength settings screen
    And  Enter the dual wavelength 457 675
    And  The user taps the cancel button
    Then Validate dual wavelength "<expected_first_wave_length>" "<expected_second_wave_length>" on the condition card
    And  Navigate to the wavelength settings screen
    And  Validate wavelength current info "<expected_first_wave_length>" "<expected_second_wave_length>" "<expected_wavelength_mode>" on the setting screen

    Examples:
      | expected_first_wave_length | expected_second_wave_length | expected_wavelength_mode |
      | 254 nm                     | 700 nm                      | Dual                     |












