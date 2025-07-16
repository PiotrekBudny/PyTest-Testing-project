from unittests.mechanic.diagnosis_type import DiagnosisType
from dataclasses import dataclass


@dataclass
class Diagnosis:
    diagnosis_type: DiagnosisType
    cost: int
