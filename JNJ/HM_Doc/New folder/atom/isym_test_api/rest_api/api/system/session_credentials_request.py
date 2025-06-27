"""
Desc: This file contains the payload that needs to be send with sessions credential request
"""
from dataclasses import dataclass


@dataclass
class SessionCredentials:
    applicationContext: str


def generate_default_sessions_credentials_request():
    payload = SessionCredentials(applicationContext="TestSession")
    return payload
