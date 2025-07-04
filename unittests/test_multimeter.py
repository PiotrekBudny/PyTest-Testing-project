from unittests.multimeter.multimeter import Multimeter
from unittests.multimeter.components.battery import Battery
import pytest
from unittests.multimeter.components.assertions.battery_assertions import BatteryAssertions
from unittests.multimeter.unsupported_component_exception import UnsupportedException

class TestMultimeterMeasurment:
    
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
        
        BatteryAssertions.assert_that_car_battery_voltage_is_in_range(detected_voltage)
    
    def test_old_battery_measurement(self, multimeter_instance, old_car_battery):
        detected_voltage = multimeter_instance.measure_voltage(old_car_battery)
        
        BatteryAssertions.assert_that_car_battery_voltage_is_below_range(detected_voltage)
        
    def test_error_when_measuring_resistance_on_battery(self, multimeter_instance, valid_car_battery):
        with pytest.raises(UnsupportedException):
            multimeter_instance.measure_resistance(valid_car_battery)
    
    