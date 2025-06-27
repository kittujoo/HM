"""
File_Name: prime_solvent.py
Desc: This file contains the constants of prime solvent
__copyright__ = "Copyright (c) 2020 by Waters Corporation, all rights reserved."
__author__    = "Sharmila Vairamani" Initial Check-in 08/19/2020

"""


class PrimeSolventErrorCodes:
    NoError = 0
    InvalidParameters = 7000
    InvalidState = 7004


class PrimeSolventStates:
    Ready = 'READY'  # component ready for priming action
    Busy = 'BUSY'  # component is priming
    Completed = 'COMPLETED'  # component is maintaining
    Error = 'ERROR'  # component is in error state


class PrimeSolventConstants:
    PrimingFlowRate = 0.5
