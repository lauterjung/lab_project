from enum import Enum

from model.subject import Subject

class LabCaseType(Enum):
    invalid = 1
    duo = 2
    trio = 3
    maternity_duo = 4
    maternity_trio = 5
    complex = 6

class LabCaseSubType(Enum):
    invalid = 1
    inclusion = 2
    exclusion = 3
    swap = 4
    potential_swap = 5
    mutation_mother = 6
    mutation_father = 7
    complex = 8

class LabCase:
    juridic_cases: list[str]
    card_numbers: list[str]
    subjects: list[Subject]
    type_of_case: LabCaseType
    subtype_of_case: list[LabCaseSubType]

    child_x_alledged_father: list[str] # to be removed
    mother_x_alledged_father: list[str] # to be removed
    mother_x_child: list[str] # to be removed

    amelogenin_swap: list[tuple[bool, Subject]]
    inconsistencies: list[Subject, Subject, int, list[str]]
    inconsistencies_vector: list

    def __init__(self,  name: str):
        self.name = name
        self.container = name
        self.subjects = []
        self.amelogenin_swap = []
        self.child_x_alledged_father = [] # to be removed
        self.mother_x_alledged_father = [] # to be removed
        self.mother_x_child = [] # to be removed
        self.inconsistencies = []
        self.inconsistencies_vector = []
        self.subtype_of_case = []
        