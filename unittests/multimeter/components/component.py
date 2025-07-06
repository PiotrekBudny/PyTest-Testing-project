from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_voltage(self) -> float:
        pass

    @abstractmethod
    def get_resistance(self) -> float:
        pass
