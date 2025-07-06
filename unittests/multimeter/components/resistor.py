from unittests.multimeter.components.component import Component
from unittests.multimeter.components.utils.realistic_resistance_provider import RealisticResistanceProvider
from unittests.multimeter.components.resistor_connection import ResistorConnection


class Resistor(Component):
    def __init__(self, resistor_values: list, resistor_tap_index, incoming_voltage, connection: ResistorConnection):
        self.resistor_tap_index = resistor_tap_index
        self.resistor_values = RealisticResistanceProvider(resistor_values).get_actual_resistances()
        self.incoming_voltage = incoming_voltage
        self.connection = connection

    def get_resistance(self) -> float:
        return sum(self.resistor_values)

    def get_voltage(self) -> float:
        is_there_a_single_resistor = len(self.resistor_values) == 1

        match self.connection:
            case ResistorConnection.IN_SERIES_TO_GROUND:
                if is_there_a_single_resistor:
                    return 0.0
                else:
                    raise Exception("Incorrect resistor configuration")
            case ResistorConnection.STANDALONE:
                if is_there_a_single_resistor:
                    return self.incoming_voltage
                else:
                    raise ValueError("Invalid resistor configuration")
            case ResistorConnection.PART_OF_DIVIDER:
                if self.resistor_tap_index >= len(self.resistor_values):
                    raise IndexError("Tap index out of range")
                return self.__calculate_voltage_for_part_of_divider(self.resistor_tap_index)

    def __calculate_voltage_for_part_of_divider(self, resistance_tap_index: int) -> float:
        total_resistance = 0.0
        resistance_tested = 0.0

        number_of_resistors = len(self.resistor_values)

        for resistor_index in range(number_of_resistors):
            total_resistance += self.resistor_values[resistor_index]
            if resistor_index > resistance_tap_index:
                resistance_tested += self.resistor_values[resistor_index]

        voltage_output = self.incoming_voltage * (resistance_tested / total_resistance)

        return voltage_output







