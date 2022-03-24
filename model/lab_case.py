from ast import Sub
from enum import Enum

from model.subject import Subject, SubjectType
from model.genotype import Genotype

class LabCaseType(Enum):
    invalid = 1
    duo = 2
    trio = 3
    maternity_duo = 4
    maternity_trio = 5
    complex = 6

class LabCaseSubType(Enum):
    ready = 1
    inclusion = 2
    exclusion = 3
    swap = 4
    mutation_mother = 5
    mutation_father = 6
    other = 99 # just in case to help debugging

class LabCase:
    juridic_cases: list[str]
    card_numbers: list[str]
    subjects: list[Subject]
    type_of_case: LabCaseType
    subtype_of_case: LabCaseSubType

    child_x_alledged_father: list[str]
    mother_x_alledged_father: list[str]
    mother_x_child: list[str]

    details_amelogenin_swap: list[tuple[bool, Subject]] # (True, Subject)

    locus_paternity_index = list[tuple[str, float]] # (Genotype.locus, IP)
    combined_paternity_index: float
    number_of_inconsistencies: int

    def __init__(self,  name: str):
        self.name = name
        self.subjects = []
        self.details_amelogenin_swap = []
        self.child_x_alledged_father = []
        self.mother_x_alledged_father = []
        self.mother_x_child = []