@kiosk @kiosk_channel_card_lamp_on_feature @ALIST-228
Feature: Kiosk | Channel Condition card tests when the lamp is on


  Background:
    Given Turn on the Lamp
    And User navigates to TUV home screen

  @real @daily @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To verify channel A card is updated when the user selects the single wavelength mode

    When Navigate to the channel A settings screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the wavelength "<actual_first_wavelength>"
    And User confirms the settings
    Then Validate Channel A condition card for "<expected_first_wavelength>" for "<lamp_state>"
    And User validates the TUV card reader for "<wavelength_mode>" "<expected_first_wavelength>" "<expected_second_wavelength>"

    Examples:
      | actual_first_wavelength | expected_first_wavelength | wavelength_mode | expected_second_wavelength | lamp_state |
      | 310                     | 310 nm                    | Single          | 310 nm                     | On         |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To verify channel A card is updated when the user selects the dual wavelength mode

    When Navigate to the channel A settings screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the dual wavelength "<actual_first_wavelength>" "<actual_second_wavelength>"
    And User confirms the settings
    Then Validate Channel A condition card for "<expected_first_wavelength>" for "<lamp_state>"
    And Validate Channel B condition card for "<expected_second_wavelength>" for "<lamp_state>"
    And User validates the TUV card reader for "<wavelength_mode>" "<expected_first_wavelength>" "<expected_second_wavelength>"

    Examples:
      | wavelength_mode | actual_first_wavelength | actual_second_wavelength | expected_first_wavelength | expected_second_wavelength | lamp_state |
      | Dual            | 300                     | 301                      | 300 nm                    | 301 nm                     | On         |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To verify the channel A card is not updated when the user taps the cancel button

    When Navigate to the channel A settings screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the dual wavelength "<actual_first_wavelength>" "<actual_second_wavelength>"
    And User confirms the settings
    And Navigate to the channel A settings screen
    And User selects the wavelength mode "Dual"
    And Enter the dual wavelength "320" "321"
    And User cancels the settings
    Then Validate dual wavelength "<expected_first_wavelength>" "<expected_second_wavelength>" on the condition card

    Examples:
      | wavelength_mode | actual_first_wavelength | actual_second_wavelength | expected_first_wavelength | expected_second_wavelength |
      | Dual            | 315                     | 317                      | 315 nm                    | 317 nm                     |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To validate text field in channel A settings Screen
    When Navigate to the channel A settings screen
    And User selects the wavelength mode "Dual"
    And Enter the dual wavelength "300" "301"
    And User confirms the settings
    And Navigate to the channel A settings screen
    And User selects the wavelength mode "Dual"
    And User enter the dual wavelength "<first_wavelength>" "<second_wavelength>"
    And User selects the wavelength mode "Single"
    And User selects the wavelength mode "Dual"
    Then Validate "<expected_second_wavelength>" in the settings screen

    Examples:
      | first_wavelength | second_wavelength | expected_second_wavelength |
      | 305              | 304               | 304 nm                     |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To verify channel B card is updated when the user selects the wavelength mode as dual

    When Navigate to the channel B settings Screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the dual wavelength "<actual_first_wavelength>" "<actual_second_wavelength>"
    And User confirms the settings
    Then Validate Channel A condition card for "<expected_first_wavelength>" for "<lamp_state>"
    And Validate Channel B condition card for "<expected_second_wavelength>" for "<lamp_state>"
    And User validates the TUV card reader for "<wavelength_mode>" "<expected_first_wavelength>" "<expected_second_wavelength>"

    Examples:
      | wavelength_mode | actual_first_wavelength | actual_second_wavelength | expected_first_wavelength | expected_second_wavelength | lamp_state |
      | Dual            | 320                     | 330                      | 320 nm                     | 330 nm                     | On         |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline: To verify the channel B card is not updated when the user taps the cancel button

    When Navigate to the channel B settings Screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the dual wavelength "<actual_first_wavelength>" "<actual_second_wavelength>"
    And User confirms the settings
    And Navigate to the channel B settings Screen
    And User selects the wavelength mode "Dual"
    And Enter the dual wavelength "300" "304"
    And User cancels the settings
    Then Validate dual wavelength "<expected_first_wavelength>" "<expected_second_wavelength>" on the condition card

    Examples:
      | wavelength_mode | actual_first_wavelength | actual_second_wavelength | expected_first_wavelength | expected_second_wavelength |
      | Dual            | 301                     | 315                      | 301 nm                    | 315 nm                     |


  @real @daily  @ignore #(INSISPP-8103 channel B condition card is not displayed in TUV card reader)
  Scenario Outline:  To verify channel B card is updated when the user selects the dual wavelength mode

    When Navigate to the channel A settings screen
    And User selects the wavelength mode "<wavelength_mode>"
    And Enter the dual wavelength "<actual_first_wavelength>" "<actual_second_wavelength>"
    And User confirms the settings
    Then Validate Channel A condition card for "<expected_first_wavelength>" for "<lamp_state>"
    Then Validate Channel B condition card for "<expected_second_wavelength>" for "<lamp_state>"
    And User validates the TUV card reader for "<wavelength_mode>" "<expected_first_wavelength>" "<expected_second_wavelength>"

    Examples:
      | actual_first_wavelength  | actual_second_wavelength | expected_first_wavelength | wavelength_mode | expected_second_wavelength | lamp_state |
      |  310                     | 315                      | 310 nm                    | Dual            | 315 nm                     | On         |

