
class BatteryAssertions:
    
    def assert_that_car_battery_voltage_is_in_range(detected_voltage):
        assert 11.0 <= detected_voltage <= 13.0, f"Voltage {detected_voltage}V is out of expected car battery range (11.0V - 13.0V)"
        
    def assert_that_car_battery_voltage_is_below_range(detected_voltage):
        assert detected_voltage < 11.0    