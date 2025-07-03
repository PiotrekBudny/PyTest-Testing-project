from .utils.realistic_voltage_simulator import RealisticVoltageSimulator

class Battery:
    def __init__(self, nominal_voltage, measurement_should_be_valid):
        self.nominal_voltage = nominal_voltage
        self.measurement_should_be_valid = measurement_should_be_valid
        
    def get_voltage(self) -> float:
        return RealisticVoltageSimulator.make_voltage_real(self, self.nominal_voltage, self.measurement_should_be_valid)
