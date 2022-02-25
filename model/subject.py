import re

from model.genotype import Genotype
from model.subject_type import SubjectType

class Subject():
    subject_type: SubjectType
    
    def __init__(self, name: str, genetic_profile: list[Genotype]):
        self.name = name
        self.genetic_profile = genetic_profile
        