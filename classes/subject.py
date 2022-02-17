from enum import Enum
        
class SubjectType(Enum):
    mother = 1
    child = 2
    alledged_father = 3

class Subject():
    def __init__(self, type: SubjectType, name: str, genetic_profile: list[str]):
        self.type = type
        self.name = name
        self.genetic_profile = genetic_profile