from web_framework.kiosk.pages.Locators.Setup.startup_workflow_locators import (StartupWorkflowLocators, StartupPrimeSolventsLocators,
                                                                                StartupAdditionalPrimeSolventsLocators, StartupEquilibrationLocators,
                                                                                StartupDetectorLampLocators, StartupWelcomeLocators,
                                                                                StartupTemperatureControlLocators)
from web_framework.kiosk.pages.Utilities.solvent_composition_utility import SolventCompositionUtilities


class StartupWorkflowSetupScreen(SolventCompositionUtilities):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.selected_solvent_summary_details = None

    def validate_welcome_screen(self):
        locator = StartupWorkflowLocators.WELCOME_PAGE_BANNER
        screen_name = "Welcome Screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_prime_solvent_screen(self):
        locator = StartupPrimeSolventsLocators.PRIME_SOLVENTS_PAGE_BANNER
        screen_name = "Prime solvent screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_detector_screen(self):
        locator = StartupDetectorLampLocators.DETECTOR_LAMP_PAGE_BANNER
        screen_name = "Detector lamp screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_seal_wash(self):
        locator = StartupAdditionalPrimeSolventsLocators.SEAL_WASH_PAGE_BANNER
        screen_name = "Seal wash screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_needle_wash(self):
        locator = StartupAdditionalPrimeSolventsLocators.NEEDLE_WASH_PAGE_BANNER
        screen_name = "Needle wash screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_sample_metering_pump_duration(self):
        locator = StartupAdditionalPrimeSolventsLocators.METERING_PUMP_PAGE_BANNER
        screen_name = "Metering pump duration screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_sample_metering_pump_composition(self):
        locator = StartupAdditionalPrimeSolventsLocators.METERING_PUMP_PAGE_SOLVENT_A
        screen_name = "Metering pump composition screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_temperature_control_screen(self):
        locator = StartupTemperatureControlLocators.TEMPERATURE_CONTROL_PAGE_BANNER
        screen_name = "Temperature Control screen of startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_equilibration_screen(self):
        locator = StartupEquilibrationLocators.EQUILIBRATION_PAGE_BANNER
        screen_name = "Equilibration screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_equilibration_flow_screen(self):
        locator = StartupEquilibrationLocators.EQ_FLOW_PAGE_BANNER
        screen_name = "Equilibration screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_equilibration_composition_screen(self):
        locator = StartupEquilibrationLocators.EQ_COMPOSITION_PAGE_BANNER
        screen_name = "Equilibration screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def validate_equilibration_duration_screen(self):
        locator = StartupEquilibrationLocators.EQ_DURATION_PAGE_BANNER
        screen_name = "Equilibration screen for the startup workflow"
        self.validate_screen(locator, screen_name, self.wait_time)

    def get_welcome_paragraph_text(self) -> list:
        return [self.get_text(StartupWelcomeLocators.WELCOME_PARAGRAPH_ONE),
                self.get_text(StartupWelcomeLocators.WELCOME_LIST_PARAGRAPH)]

    def get_welcome_list_text(self) -> list:
        return [self.get_text(StartupWelcomeLocators.WELCOME_LIST_FIRST_POINT),
                self.get_text(StartupWelcomeLocators.WELCOME_LIST_SECOND_POINT),
                self.get_text(StartupWelcomeLocators.WELCOME_LIST_THIRD_POINT)]

    def get_stepper_locator(self, stepper_component: str):
        stepper_text_dictionary = {
            "priming_duration": StartupPrimeSolventsLocators.PRIMING_DURATION_STEPPER,
            "seal_stepper": StartupAdditionalPrimeSolventsLocators.PRIME_SEAL_STEPPER
        }

        if stepper_component in stepper_text_dictionary:
            stepper = stepper_text_dictionary[stepper_component]
            return stepper

        assert False, f"Unexpected stepper component => {stepper_component}"

    def enter_flow_rate(self, flow_rate_value: str):
        self.validate_equilibration_screen()
        self.enter_value(flow_rate_value)
        self.tap_next_button()

    def enable_toggle(self, locator: tuple):
        is_toggle_button_enabled = self.is_toggle_button_enabled(locator)

        if not is_toggle_button_enabled:
            self.logger.info("*** Toggle button is not enabled")
            self.tap(locator)
        else:
            self.logger.info("** The toggle button is enabled, no action needed")
