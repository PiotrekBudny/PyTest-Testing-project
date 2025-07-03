import random

class RealisticVoltageSimulator:
    
    def make_voltage_real(self, voltage, measurement_should_be_valid):
        if measurement_should_be_valid == True:
            min_v = max(0, voltage - 1)
            max_v = voltage + 1
            return round(random.uniform(min_v, max_v), 2)
        else:
            min_v = max(0, voltage - 5)
            max_v = voltage - 3
            return round(random.uniform(min_v, max_v), 2)