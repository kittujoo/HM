"""
File_Name: prime_solvents_workflow_constants.py
Desc: This file contains the constants of the prime solvents workflow
__copyright__ = "Copyright (c) 2023 by Waters Corporation, all rights reserved."
__author__    = "Tyler Prada" Initial Check-in 4/25/23
__Modified__  = "Sharmila Vairamani" Update the script to ui changes -6/23/2023
"""


class PrimeSolventsWorkflowConstants:
    WelcomeFirstParagraph = "The priming process replaces solvent in the path from the reservoirs to the " \
                            "solvent manager. Priming is a timed operation that switches the vent valve to " \
                            "the “vent” position, to ensure minimal back pressure."
    WelcomeListParagraph = "Prime the system when performing these tasks:"
    WelcomeSecondParagraph = "Ensure that the solvent reservoirs contain enough solvent for adequate priming."
    expected_welcome_paragraph_text = [WelcomeFirstParagraph, WelcomeListParagraph, WelcomeSecondParagraph]

    WelcomeListFirstPoint = "Changing reservoirs or solvents"
    WelcomeListSecondPoint = "Running the system after it has been idle for more than four hours"
    WelcomeListThirdPoint = "Preparing a new system for use"
    expected_list_text = [WelcomeListFirstPoint, WelcomeListSecondPoint, WelcomeListThirdPoint]

    CautionFirstParagraph = "To prevent salts from precipitating in the system, introduce an intermediate solvent, " \
                            "such as water, when changing from buffers to high-organic-content solvents. " \
                            "When you switch from a strong buffer to an organic solvent, thoroughly flush the system " \
                            "with distilled water before you add the organic solvent."
    CautionSecondParagraph = "To avoid the harmful effects of personal contact with solvents, including inhalation, " \
                             "observe Good Laboratory Practice when you handle them. " \
                             "Consult the Material Safety Data Sheets for the solvents you use."
    expected_caution_list_text = [CautionFirstParagraph, CautionSecondParagraph]

    prime_by_line_not_selected = "Not enabled"
    prime_by_composition_not_selected = "Not enabled"

    prime_by_solvent_header = "Prime by Solvent Line"
    prime_by_solvent_duration = "Prime Duration (min)"
    prime_by_composition_header = "Prime by Composition"
    prime_by_composition_duration = "Prime by Composition"
    prime_summary_header = "Summary"
    time = 10
    prime_unit = 15
    StatusValidateText = "Status"
    WorkFlowCompleteState = "Complete"
    TimeToComplete = 900
    error_message = "The workflow is not completed "
