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
    
    def __init__(self,  name: str, ):
        self.name = name
        self.subjects = []

    def type_of_case(self) -> LabCaseType:
        
        individual_types = []
        for subject in self.subjects:
            individual_types.append(subject.subject_type.name)
                                                            
        if SubjectType.child.name not in individual_types:
            return LabCaseType.invalid
        
        if len(individual_types) == 2:
            if all(x in individual_types for x in [SubjectType.alledged_mother.name, SubjectType.child.name]) or \
               all(x in individual_types for x in [SubjectType.child.name, SubjectType.alledged_father.name]):
                   return LabCaseType.duo
        
        if len(individual_types) == 3:
            if all(x in individual_types for x in [SubjectType.alledged_mother.name, SubjectType.child.name, SubjectType.father.name]) or \
               all(x in individual_types for x in [SubjectType.mother.name, SubjectType.child.name, SubjectType.alledged_father.name]):
                    return LabCaseType.trio
        
        return LabCaseType.complex