from enum import Enum, auto


class DiagnosisType(Enum):
    CHANGE_FUEL_FILTER = auto()
    REPLACE_MUFFLER = auto()
    RECHARGE_BATTERY = auto()
    REPLACE_SEAL = auto()
    UNKNOWN_ISSUE = auto()

