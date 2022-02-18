from enum import Enum
        
# class SubjectType(Enum):
#     mother = 1
#     child = 2
#     alledged_father = 3

class Subject():
    def __init__(self, type: str, name: str): #, genotype: list[str]):
        self.type = type
        self.name = name
        #self.genotype = genotype