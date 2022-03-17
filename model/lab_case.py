from enum import Enum

from model.subject import Subject, SubjectType

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

    # store details in case variables
    
    def __init__(self,  name: str):
        self.name = name
        self.subjects = []

    # TODO: needs to be moved to controller
