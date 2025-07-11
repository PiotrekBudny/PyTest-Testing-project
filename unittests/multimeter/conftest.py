import pytest
from unittests.multimeter.multimeter import Multimeter
from unittests.multimeter.components.battery import Battery


@pytest.fixture
def multimeter_instance():
    return Multimeter()


@pytest.fixture
def valid_car_battery():
    return Battery(nominal_voltage=12, measurement_should_be_valid=True)


@pytest.fixture
def old_car_battery():
    return Battery(nominal_voltage=12, measurement_should_be_valid=False)


@pytest.fixture
def standard_resistors_set() -> list[float]:
    return [1.0, 2.0, 3.0, 5.0, 10.0]
