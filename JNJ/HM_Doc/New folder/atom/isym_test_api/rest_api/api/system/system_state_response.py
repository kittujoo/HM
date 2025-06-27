from dataclasses import dataclass

from utilities.EnumBase import EnumBase


class SystemStateEnum(EnumBase):
    SystemStateEnum_DISCOVERING = "SystemStateEnum_DISCOVERING"
    SystemStateEnum_INITIALIZING = "SystemStateEnum_INITIALIZING"
    SystemStateEnum_ILLEGAL = "SystemStateEnum_ILLEGAL"
    SystemStateEnum_STARTFAILED = "SystemStateEnum_STARTFAILED"
    SystemStateEnum_EXCLUSIVEFAIL = "SystemStateEnum_EXCLUSIVEFAIL"
    SystemStateEnum_HALTING = "SystemStateEnum_HALTING"
    SystemStateEnum_HALTED = "SystemStateEnum_HALTED"
    SystemStateEnum_ERROR = "SystemStateEnum_ERROR"
    SystemStateEnum_REBOOTREQUIRED = "SystemStateEnum_REBOOTREQUIRED"
    SystemStateEnum_IDLE = "SystemStateEnum_IDLE"
    SystemStateEnum_BUSY = "SystemStateEnum_BUSY"
    SystemStateEnum_WORKFLOW = "SystemStateEnum_WORKFLOW"
    SystemStateEnum_WORKFLOWRECOVERING = "SystemStateEnum_WORKFLOWRECOVERING"
    SystemStateEnum_RESETTING = "SystemStateEnum_RESETTING"
    SystemStateEnum_EXCLUSIVEIDLE = "SystemStateEnum_EXCLUSIVEIDLE"
    SystemStateEnum_SETTINGMETHOD = "SystemStateEnum_SETTINGMETHOD"
    SystemStateEnum_ATMETHODCONDITIONS = "SystemStateEnum_ATMETHODCONDITIONS"
    SystemStateEnum_PREPARING = "SystemStateEnum_PREPARING"
    SystemStateEnum_RUNNING = "SystemStateEnum_RUNNING"
    SystemStateEnum_EXCLUSIVESTOPPING = "SystemStateEnum_EXCLUSIVESTOPPING"
    SystemStateEnum_WORKFLOWSTOPPING = "SystemStateEnum_WORKFLOWSTOPPING"
    SystemStateEnum_WORKFLOWSTOPPED = "SystemStateEnum_WORKFLOWSTOPPED"


@dataclass
class SystemStateResponse:
    state: SystemStateEnum
    sequence: int
    dataModelType: str
    dataModelVersion: int
