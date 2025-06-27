"""
File_Name: sm_configuration_settings.py
Desc: This is the data-holder class which holds the solvent line data for the solvent composition screen
__copyright__ = "Copyright (c) 2021 by Waters Corporation, all rights reserved."
__author__    = " Sharmila Vairamani " Initial Check-in 02/15/2021

"""
from utilities.logger import Logger
import os

logger = Logger(os.path.basename(__file__))

class SolventComposition:
    def __init__(self):
        self.solvent_list = []

    def __str__(self):
        logger.debug("from SolventComposition")
        for solvent in self.solvent_list:
            print(solvent)
        return ""

    def add(self, solvent_line):
        if solvent_line is not None:
            self.solvent_list.append(solvent_line)

    def get_solvent_lines(self):
        return self.solvent_list


