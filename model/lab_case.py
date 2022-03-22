from enum import Enum

from model.subject import Subject, SubjectType
from model.genotype import Genotype

class LabCaseType(Enum):
    invalid = 1
    duo = 2
    trio = 3
    complex = 4

class LabCase:
    juridic_cases: list[str]
    card_numbers: list[str]
    subjects: list[Subject]
    type_of_case: LabCaseType

    details_mutation: list[tuple] # Subject or self.Subject?
    # AttributeError: type object 'Genotype' has no attribute 'locus'
    details_amelogenin_swap: list[tuple]

    details_locus_paternity_index: list[tuple]
    # AttributeError: type object 'Genotype' has no attribute 'locus'
    combined_paternity_index: float
    number_of_inconsistencies: int

    def __init__(self,  name: str):
        self.name = name
        self.subjects = []
        self.details_amelogenin_swap = []