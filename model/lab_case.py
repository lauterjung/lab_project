from ast import Sub
from enum import Enum

from model.subject import Subject, SubjectType
from model.genotype import Genotype

class LabCaseType(Enum):
    invalid = 1
    duo = 2
    trio = 3
    # maternity = 4
    complex = 4

class LabCase:
    juridic_cases: list[str]
    card_numbers: list[str]
    subjects: list[Subject]
    type_of_case: LabCaseType

    details_mutation: list[tuple[str, Subject, Subject]]
    details_amelogenin_swap: list[tuple[bool, Subject]] # (True, Subject)

    locus_paternity_index = list[tuple[str, float]] # (Genotype.locus, IP)
    combined_paternity_index: float
    number_of_inconsistencies: int

    def __init__(self,  name: str):
        self.name = name
        self.subjects = []
        self.details_amelogenin_swap = []