from unittests.mechanic.car import Car
from unittests.mechanic.diagnosis_type import DiagnosisType
from unittests.mechanic.diagnosis import Diagnosis


class MechanicDiagnosisEngine:
    def __init__(self, car: Car):
        self.car = car

    def diagnose(self) -> list[Diagnosis]:

        list_of_issues = []

        if self.car.smells_a_lot:
            list_of_issues.append(Diagnosis(DiagnosisType.CHANGE_FUEL_FILTER, 50))
        if self.car.sounds_bad:
            list_of_issues.append(Diagnosis(DiagnosisType.REPLACE_MUFFLER, 100))
        if self.car.battery_level == 'low':
            list_of_issues.append(Diagnosis(DiagnosisType.RECHARGE_BATTERY, 0))
        if self.car.does_oil_leak:
            list_of_issues.append(Diagnosis(DiagnosisType.REPLACE_SEAL, 75))

        if len(list_of_issues) == 0:
            list_of_issues.append(Diagnosis(DiagnosisType.UNKNOWN_ISSUE, 200))

        return list_of_issues
