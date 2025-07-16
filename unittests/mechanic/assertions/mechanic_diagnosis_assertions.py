from unittests.mechanic.diagnosis_type import DiagnosisType
from unittests.mechanic.diagnosis import Diagnosis


class MechanicEngineAssertions:

    def __init__(self, list_of_issues: list[Diagnosis]):
        self.list_of_issues = list_of_issues

    def assert_that_diagnosis_was_correctly_given_with_price(self, diagnosis_type: DiagnosisType, cost: int):
        diagnosis = Diagnosis(diagnosis_type=diagnosis_type, cost=cost)
        assert diagnosis in self.list_of_issues
        return self
