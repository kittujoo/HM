from dataclasses import dataclass

from utilities.EnumBase import EnumBase


class EnvironmentType(EnumBase):
    REAL = "REAL"
    SIMULATION = "SIMULATION"
    CDS = "CDS"
    DEFAULT = "DEFAULT"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()


@dataclass
class ComponentConfiguration:
    hostname: str
    username: str
    password: str
