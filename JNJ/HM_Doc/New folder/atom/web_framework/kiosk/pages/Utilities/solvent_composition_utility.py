from dataclasses import dataclass

from utilities.logger import Logger
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventComposition import SolventComposition
from web_framework.kiosk.common.Models.SolventManagerCardReader.SolventLine import SolventLine
from web_framework.kiosk.pages.Locators.User.solvent_composition_locators import SolventCompositionLocators
from web_framework.kiosk.pages.base_page import BasePage
from web_framework.kiosk.pages.Locators.Home.SolventManager.flow_condition_card import SolventCompositionTabScreen as Solvent_comp


@dataclass
class SolventDetails:
    solvent_a: str
    solvent_b: str
    solvent_c: str
    solvent_d: str


class SolventCompositionUtilities(BasePage):

    def __init__(self, driver, base_url, **kwargs):
        super().__init__(driver=driver, base_url=base_url, **kwargs)
        self.selected_solvent_details = None
        self.logger = Logger(self.__class__.__name__)

    def enter_composition(self, solvent_composition):

        solvent_list = solvent_composition.get_solvent_lines()
        for solvent in solvent_list:
            if solvent.line_id == "A":
                edit_field_locator = Solvent_comp.SOLVENT_A_EDIT_FIELD

            elif solvent.line_id == "B":
                edit_field_locator = Solvent_comp.SOLVENT_B_EDIT_FIELD

            elif solvent.line_id == "C":
                edit_field_locator = Solvent_comp.SOLVENT_C_EDIT_FIELD

            else:
                edit_field_locator = Solvent_comp.SOLVENT_D_EDIT_FIELD

            self.tap(edit_field_locator)
            self.enter_value_for_specific_module(edit_field_locator, solvent.percentage_value)

    def build_solvent_composition(self, solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4):

        solvent_composition = SolventComposition()
        solvent_composition.add(solvent_line_1)
        solvent_composition.add(solvent_line_2)
        solvent_composition.add(solvent_line_3)
        solvent_composition.add(solvent_line_4)
        return solvent_composition

    def reset_composition(self):
        if self.is_toggle_button_enabled(SolventCompositionLocators.RESET_COMPOSITION_BUTTON):
            self.tap(SolventCompositionLocators.RESET_COMPOSITION_BUTTON)
        else:
            self.logger.info(" The solvent composition button is disabled")

    def selected_and_get_solvent_details(self, line_1, line_2, line_3, line_4):
        self.reset_composition()
        solvent_line_1 = SolventLine.parse(line_1)
        solvent_line_2 = SolventLine.parse(line_2)
        solvent_line_3 = SolventLine.parse(line_3)
        solvent_line_4 = SolventLine.parse(line_4)
        solvent_composition = self.build_solvent_composition(solvent_line_1, solvent_line_2, solvent_line_3, solvent_line_4)
        self.enter_composition(solvent_composition)
        entered_solvent_a = self.get_user_input_text(
            SolventCompositionLocators.SOLVENT_A_EDIT_FIELD)
        entered_solvent_b = self.get_user_input_text(
            SolventCompositionLocators.SOLVENT_B_EDIT_FIELD)
        entered_solvent_c = self.get_user_input_text(
            SolventCompositionLocators.SOLVENT_C_EDIT_FIELD)
        entered_solvent_d = self.get_user_input_text(
            SolventCompositionLocators.SOLVENT_D_EDIT_FIELD)
        solvent_details = self.build_solvent_composition(entered_solvent_a, entered_solvent_b, entered_solvent_c, entered_solvent_d)

        return solvent_details

    def get_expected_composition(self, line_1, line_2, line_3, line_4):
        data = []
        for line in [line_1, line_2, line_3, line_4]:
            key, _, value = line.split(",")
            data.append(f"{key}: {value}%")
        result = ", ".join(data)
        return result