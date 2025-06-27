  """
  Desc: Feature file for testing preconfigured methods, method sets and sample sets.
  There is an Empower project that will be restored and the needed items will be available.
  Details on how these were configured can be found in https://waterscorporation.atlassian.net/browse/ALIST-38
  Note that an Alliance iS pre-production configuration needs to be used (not beta unit) to be able to open the sample set.
  """


@ics @real @PP_unit @daily @ics_run_predefined_sample_sets_feature
Feature: ICS Run Predefined Sample Sets


  Background:
    Given pre-run checks for sample set validation acquisition are disabled
    And run checks for sample set validation acquisition are disabled
    And the "predefined_data" instrument version specific project is available in Empower
    And run samples application is open for the current project and system
    And Control Panel shows "IDLE" state


  Scenario Outline: Run predefined sample sets - completion workflow
    When the sample set "<sample_set_name>" is loaded
    And the acquisition starts
    Then the sample set acquisition completes successfully

    Examples:
      | sample_set_name   |
      | isocratic UV273nm |
