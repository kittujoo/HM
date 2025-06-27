  """
  Desc: Feature file for testing long running preconfigured methods, method sets and sample sets.

  There is an Empower project that will be restored and the needed items will be available.

  Notes:
  - an Alliance iS pre-production configuration needs to be used (not beta unit) to be able to open the sample set;
  - test run timeouts need to be modified according to the project run time;
  """


@ics_special @real @PP_unit @weekly @long @ics_predefined_long_running_sample_sets_feature
Feature: ICS Predefined Long Running Sample Sets


  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And the "predefined_long_running_data" project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state


  Scenario Outline: Run predefined sample sets - Full plate
    When the sample set "<sample_set_name>" is loaded
    And the acquisition starts
    Then the sample set acquisition completes successfully

    Examples:
      | sample_set_name              |
      | 144_Samples_Full_Plate_9_Day |
