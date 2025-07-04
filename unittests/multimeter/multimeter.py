from unittests.multimeter.unsupported_component_exception import UnsupportedException

class Multimeter:
    def measure_voltage(self, component) -> float:
        try:
            return component.get_voltage()
        except Exception as e:
            raise UnsupportedException(f"Can not measure voltage for component. Inner exception: {e}") from e
    
    def measure_resistance(self, component):
        try:
            return component.get_resistance()
        except Exception as e:
            raise UnsupportedException(f"Can not measure resistance for component. Inner exception: {e}") from e
    