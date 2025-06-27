from dataclasses import dataclass


@dataclass
class SystemRepeatBehaviorNameWrapper:
    name: str = ""


@dataclass
class SystemMetaBeginWorkflowRequest:
    behaviors: SystemRepeatBehaviorNameWrapper
    context: str = ""
    terminalBehavior: str = ""


def generate_default_system_workflow_request():
    payload = SystemMetaBeginWorkflowRequest(
        context="Orion#Qsm",
        behaviors=SystemRepeatBehaviorNameWrapper(
            name="Qsm"
        ),
        terminalBehavior="Qsm"
    )
    return payload
