from enum import Enum

from model.subject import Subject

class LabCaseType(Enum):
    invalid = 1
    duo = 2
    trio = 3
    complex = 4

class LabCase:
    juridic_cases: list[str]
    card_numbers: list[str]
    subjects: list[Subject]
    
    def __init__(self,  name: str, ):
        self.name = name
        self.subjects = []

    def type_of_case(self):
        
        individual_types = []
        for subject in self.subjects:
            individual_types.append(subject.type)
        
        if "F" not in individual_types:
            return LabCaseType.invalid
        
        if len(individual_types) == 2:
            if all(x in individual_types for x in ["SM", "F"]) or \
               all(x in individual_types for x in ["F", "SP"]):
                   return LabCaseType.duo
        
        if len(individual_types) == 3:
            if all(x in individual_types for x in ["SM", "F", "P"]) or \
               all(x in individual_types for x in ["M", "F", "SP"]):
                    return LabCaseType.trio
        
        return LabCaseType.complex