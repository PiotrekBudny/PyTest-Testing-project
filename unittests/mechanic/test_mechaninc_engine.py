import pytest

from unittests.mechanic.car import Car
from unittests.mechanic.mechanic_diagnosis_engine import MechanicDiagnosisEngine
from unittests.mechanic.assertions.mechanic_diagnosis_assertions import MechanicEngineAssertions
from unittests.mechanic.diagnosis_type import DiagnosisType


class TestMechanicEngine:

    @pytest.fixture
    def car_with_low_battery_and_oil_leak(self):
        return Car(battery_level='low', does_oil_leak=True, sounds_bad=False, smells_a_lot=False)

    @pytest.fixture
    def car_without_any_issues(self):
        return Car(battery_level='high', does_oil_leak=False, sounds_bad=False, smells_a_lot=False)

    def test_oil_leak__diagnosis_response_and_low_battery(self, car_with_low_battery_and_oil_leak):
        mechanic_engine = MechanicDiagnosisEngine(car_with_low_battery_and_oil_leak)
        list_of_issues = mechanic_engine.diagnose()

        MechanicEngineAssertions(list_of_issues) \
            .assert_that_diagnosis_was_correctly_given_with_price(DiagnosisType.REPLACE_SEAL, 75) \
            .assert_that_diagnosis_was_correctly_given_with_price(DiagnosisType.RECHARGE_BATTERY, 0)

    def test_car_with_no_issue_going_to_mechanic(self, car_without_any_issues):
        mechanic_engine = MechanicDiagnosisEngine(car_without_any_issues)
        list_of_issues = mechanic_engine.diagnose()

        MechanicEngineAssertions(list_of_issues) \
            .assert_that_diagnosis_was_correctly_given_with_price(DiagnosisType.UNKNOWN_ISSUE, 200)
