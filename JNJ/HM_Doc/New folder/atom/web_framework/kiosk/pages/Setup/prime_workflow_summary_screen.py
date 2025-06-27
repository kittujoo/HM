from utilities.assert_timeout import AssertTimeout
from web_framework.kiosk.common.Constants.UI.WorkflowConstants.prime_solvents_workflow_constants import \
    PrimeSolventsWorkflowConstants
from web_framework.kiosk.common.Constants.wait_time_constants import WaitTimeConstants
from utilities.logger import Logger
from utilities.string_utility import convert_to_list, remove_substring
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Locators.Setup.prime_solvents_workflow_locators import PrimeSolventsWorkflowLocators, PrimeSummaryLocators
from web_framework.kiosk.pages.base_page import BasePage


class PrimeSummaryScreen(BasePage):

    def __init__(self, driver, base_url, assert_timeout: AssertTimeout, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.logger = Logger(self.__class__.__name__)
        self.screen_name = "Prime Solvents summary Screen"
        self.assert_time_out = assert_timeout

    def validate_setup_selection_screen(self):
        locator = PrimeSolventsWorkflowLocators.START_PANEL
        screen_name = "setup selection screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_welcome_screen(self):
        locator = PrimeSolventsWorkflowLocators.WELCOME_PAGE_BANNER
        screen_name = "welcome screen"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_solvent_by_line_details(self, solvent_lines, prime_time):
        solvent_list = convert_to_list(solvent_lines)
        prime_time_solvents = remove_substring(prime_time, ':00')

        if len(solvent_list) == 4:
            current_solvent_by_line = f"Prime solvent {solvent_list[0]}, solvent {solvent_list[1]}, " \
                                      f"solvent {solvent_list[2]} then solvent {solvent_list[3]} each for for " \
                                      f"{prime_time_solvents} minutes"
            self.logger.info(f'current_solvent_by_line====>>>{current_solvent_by_line}')

        elif len(solvent_list) == 3:
            current_solvent_by_line = f"Prime solvent {solvent_list[0]}, solvent {solvent_list[1]} " \
                                      f"then solvent {solvent_list[2]} each for {prime_time_solvents} minutes"
            self.logger.info(f'current_solvent_by_line====>>>{current_solvent_by_line}')

        elif len(solvent_list) == 2:
            current_solvent_by_line = f"Prime solvent {solvent_list[0]} then solvent {solvent_list[1]} " \
                                      f"each for {prime_time_solvents} minutes"
            self.logger.info(f'current_solvent_by_line====>>>{current_solvent_by_line}')

        elif len(solvent_list) == 1:
            current_solvent_by_line = f"Prime solvent {solvent_list[0]} each for {prime_time_solvents} minutes"
            self.logger.info(f'current_solvent_by_line====>>>{current_solvent_by_line}')

        return current_solvent_by_line

    def get_solvent_composition(self, line_1, line_2, line_3, line_4):
        """
        Prime using 25% solvent A, 25% solvent B, 25% solvent C and 25% solvent D for 2 minutes
        """
        composition_data_list = [line_1, line_2, line_3, line_4]
        composition_list = []

        for i in range(len(composition_data_list)):
            composition = SolventLine.get_percentage_value(composition_data_list[i])
            composition_list.append(composition)
        return composition_list

    def get_solvent_by_composition_details(self, line_1, line_2, line_3, line_4, prime_duration):
        solvent_composition = self.get_solvent_composition(line_1, line_2, line_3, line_4)
        self.logger.info(f'solvent_composition====>>>{solvent_composition}')
        self.logger.info(f"prime_duration =={prime_duration}")
        prime_time_solvents = remove_substring(prime_duration, ':00')
        # prime_time_solvents = remove_substring(prime_duration, ':00')
        self.logger.info(f"prime_time_solvents =={prime_time_solvents}")

        result = all(solvent_composition)
        current_solvent_by_composition = ""
        if result:
            current_solvent_by_composition = f"Prime using A: {solvent_composition[0]}%, " \
                                             f"B: {solvent_composition[1]}%, " \
                                             f"C: {solvent_composition[2]}%, " \
                                             f"D: {solvent_composition[3]}% for for {prime_time_solvents} minutes"
        return current_solvent_by_composition

    def get_solvent_by_final_details(self, line_1, line_2, line_3, line_4, flow_rate, eq_duration):
        "Maintain 0.5 mL/min using 25% solvent A, 25% solvent B, 25% solvent C and 25% solvent D for 10 minutes"
        solvent_composition = self.get_solvent_composition(line_1, line_2, line_3, line_4)
        self.logger.info(f'solvent_composition====>>>{solvent_composition}')
        self.logger.info(f"flow_rate =={flow_rate}")

        result = all(solvent_composition)
        current_final_details = ""
        if result:
            current_final_details = f"Maintain {flow_rate} mL/min using A: {solvent_composition[0]}%," \
                                    f" B: {solvent_composition[1]}%," \
                                    f" C: {solvent_composition[2]}%," \
                                    f" D: {solvent_composition[3]}% for {eq_duration} minutes"
        return current_final_details

    def validate_prime_summary_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSummaryLocators.PRIME_SUMMARY_HEADER,
            PrimeSolventsWorkflowConstants.prime_summary_header, WaitTimeConstants.SmallWait)

    def validate_status_screen(self):
        self.validate_simple_text_wait_condition(
            PrimeSummaryLocators.RESULTS_HEADER,
            PrimeSolventsWorkflowConstants.StatusValidateText, WaitTimeConstants.SmallWait)

    def validate_stepper_button_minus_state(self, state):
        if not state:
            assert self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_MINUS), f"Stepper button minus is not into expected state." \
                                                                                         "Expected: Disabled, Actual: Enabled"
        else:
            assert not self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_MINUS), f"Stepper button minus is not into expected state." \
                                                                                             "Expected: Enabled, Actual: Disabled"

    def validate_stepper_button_plus_state(self, state):
        if not state:
            assert self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_PLUS), f"Stepper button plus is not into expected state." \
                                                                                        "Expected: Disabled, Actual: Enabled"
        else:
            assert not self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_PLUS), f"Stepper button plus is not into expected state." \
                                                                                            "Expected: Enabled, Actual: Disabled"

    def validate_stepper_button_reset_state(self, state):
        if not state:
            assert self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_RESET), f"Stepper button reset is not into expected state." \
                                                                                         "Expected: Disabled, Actual: Enabled"
        else:
            assert not self.is_disabled(PrimeSolventsWorkflowLocators.STEPPER_BUTTON_RESET), f"Stepper button reset is not into expected state." \
                                                                                             "Expected: Enabled, Actual: Disabled"
