from unittests.multimeter.components.resistor_connection import ResistorConnection
from unittests.multimeter.multimeter import Multimeter
from unittests.multimeter.components.battery import Battery
from unittests.multimeter.components.resistor import Resistor
import pytest
from unittests.multimeter.components.assertions.battery_assertions import BatteryAssertions
from unittests.multimeter.components.assertions.resistor_assertions import ResistorAssertions
from unittests.multimeter.unsupported_component_exception import UnsupportedException


class TestMultimeterMeasurement:

    @pytest.fixture
    def multimeter_instance(self):
        return Multimeter()

    @pytest.fixture
    def valid_car_battery(self):
        return Battery(nominal_voltage=12, measurement_should_be_valid=True)

    @pytest.fixture
    def old_car_battery(self):
        return Battery(nominal_voltage=12, measurement_should_be_valid=False)

    def test_valid_battery_measurement(self, multimeter_instance, valid_car_battery):
        detected_voltage = multimeter_instance.measure_voltage(valid_car_battery)
        BatteryAssertions().assert_that_car_battery_voltage_is_in_range(detected_voltage)

    def test_old_battery_measurement(self, multimeter_instance, old_car_battery):
        detected_voltage = multimeter_instance.measure_voltage(old_car_battery)
        BatteryAssertions().assert_that_car_battery_voltage_is_below_range(detected_voltage)

    def test_error_when_measuring_resistance_on_battery(self, multimeter_instance, valid_car_battery):
        with pytest.raises(UnsupportedException):
            multimeter_instance.measure_resistance(valid_car_battery)

    @pytest.mark.parametrize("incoming_voltage", [0.001, 1, 5, 12, 240])
    def test_voltage_dropped_fully_when_single_resistor_used(self, multimeter_instance, incoming_voltage):
        resistor = Resistor([1.0], None, incoming_voltage, ResistorConnection.IN_SERIES_TO_GROUND)
        voltage_after_drop = multimeter_instance.measure_voltage(resistor)
        ResistorAssertions().assert_that_voltage_after_resistor_was_dropped_fully(voltage_after_drop)

    @pytest.mark.parametrize("incoming_voltage", [0.001, 1, 5, 12, 240])
    def test_voltage_when_tapped_after_third_resistor(self, multimeter_instance, incoming_voltage):
        resistor = Resistor([1.0, 2.0, 3.0, 5.0, 10.0], 3, incoming_voltage, ResistorConnection.PART_OF_DIVIDER)
        voltage_after_drop = multimeter_instance.measure_voltage(resistor)
        ResistorAssertions().assert_that_voltage_after_resistor_was_not_dropped_fully(voltage_after_drop)

    @pytest.mark.parametrize("ohms", [
        [100, 200],  # Two resistors
        [220, 330, 470]  # Three resistors
    ])
    def test_resistance_returned(self, multimeter_instance, ohms):
        resistor = Resistor(ohms, None, None, ResistorConnection.IN_SERIES_TO_GROUND)
        measured_ohms = multimeter_instance.measure_resistance(resistor)
        ResistorAssertions().assert_that_resistance_was_measured_correctly(measured_ohms, ohms)
