from dataclasses import dataclass
from enum import Enum


class EventLogEnum(Enum):
    AuditEventType_SOFTWARE = 0
    AuditEventType_HARDWARE = 1
    AuditEventType_INSTALLATION = 2
    AuditEventType_GENERIC = 3


@dataclass
class EventLogConfiguration:
    # The user of the audit details
    user: str = "admin"
    # The audit event type for the details
    eventtype: EventLogEnum = EventLogEnum.AuditEventType_GENERIC
    # The user comments for the details
    comments: str = "manually added"
