"""
Desc: This file contains the payload that needs to be send with System Reset request
"""
from dataclasses import dataclass


@dataclass
class SystemResetRequest:
    stopActivities: bool
    doInitialize: bool


def generate_stopping_activity_system_reset_request():
    payload = SystemResetRequest(
        stopActivities=True,
        doInitialize=False
    )
    return payload


def generate_only_initialize_system_reset_request():
    payload = SystemResetRequest(
        stopActivities=False,
        doInitialize=True
    )
    return payload


def generate_stopping_activity_with_initialization_system_reset_request():
    payload = SystemResetRequest(
        stopActivities=True,
        doInitialize=True
    )
    return payload
