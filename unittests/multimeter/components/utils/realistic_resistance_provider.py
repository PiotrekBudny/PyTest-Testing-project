import random
from typing import List


class RealisticResistanceProvider:
    def __init__(self, nominal_resistances: list):
        self.nominal_resistances = nominal_resistances

    def get_actual_resistances(self) -> list[float]:
        resistor_tolerance_rating: int = random.randint(-5, 5)
        resistance_percentage_against_nominal = 100 + resistor_tolerance_rating

        list_of_resistances = []

        for resistor_index in range(len(self.nominal_resistances)):
            list_of_resistances.append(self.nominal_resistances[resistor_index]
                                       * (resistance_percentage_against_nominal / 100))

        return list_of_resistances
