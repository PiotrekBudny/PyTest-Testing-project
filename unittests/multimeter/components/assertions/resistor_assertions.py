import pytest


class ResistorAssertions:

    def assert_that_voltage_after_resistor_was_dropped_fully(self, detected_voltage):
        assert detected_voltage == 0
        return self

    def assert_that_voltage_after_resistor_was_not_dropped_fully(self, detected_voltage):
        assert detected_voltage > 0
        return self

    def assert_that_resistance_was_measured_correctly(self, detected_resistance, expected_resistances):
        assert detected_resistance == pytest.approx(sum(expected_resistances), rel=0.05)
        return self

    # Add exact voltage validation
