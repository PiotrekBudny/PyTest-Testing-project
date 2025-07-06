from enum import Enum, auto


class ResistorConnection(Enum):
    STANDALONE = auto()
    IN_SERIES_TO_GROUND = auto()
    PART_OF_DIVIDER = auto()
