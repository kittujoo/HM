from dataclasses import dataclass


@dataclass
class SessionCredentials:
    applicationContext: str


@dataclass
class Session:
    sessionId: str
    userId: str
    authorizationBearerToken: str
    applicationContext: str
    dataModelType: str
    dataModelVersion: int
