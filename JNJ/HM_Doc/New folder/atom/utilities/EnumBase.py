from enum import Enum


class EnumBase(Enum):

    @classmethod
    def from_string(cls, value):
        try:
            return cls[value]
        except KeyError:
            raise ValueError(f"Value [{value}] cannot be parsed to {cls.__name__}") from None
