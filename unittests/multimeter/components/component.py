from typing import Protocol


class VoltageMeasurable(Protocol):
    def get_voltage(self) -> float:
        ...

    def get_resistance(self) -> float:
        ...