class BatteryAssertions:

    def assert_that_car_battery_voltage_is_in_range(self, detected_voltage):
        assert 11.0 <= detected_voltage <= 13.0, (f"Voltage {detected_voltage}V is out of expected car battery range ("
                                                  f"11.0V - 13.0V)")
        return self

    def assert_that_car_battery_voltage_is_below_range(self, detected_voltage):
        assert detected_voltage < 11.0
        return self
