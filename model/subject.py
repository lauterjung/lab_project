import re
from enum import Enum

from model.genotype import Genotype

class SubjectType(Enum):
    mother = 1                  # M
    child = 2                   # F
    alledged_mother = 3         # SM
    alledged_father = 4         # SP
    father = 5                  # P
    biological_child = 6        # _FBx
    auxiliary_mother = 7        # _xM
    auxiliary_father = 8        # _xP
    auxiliary_child = 9         # _xFB 
    maternal_grandmother = 10   # [S]MM
    maternal_grandfather = 11   # [S]PM
    paternal_grandmother = 12   # [S]MP
    paternal_grandfather = 13   # [S]PP
    maternal_uncle = 14         # [S]TMx
    paternal_uncle = 15         # [S]TPx
    another = 99                # OUT

class Gender(Enum):
    male = 1
    female = 2
    either = 3

class Subject():
    codification: str
    subject_type: SubjectType
    gender: Gender
    
    def __init__(self, name: str, genetic_profile: list[Genotype]):
        self.name = name
        self.genetic_profile = genetic_profile # maybe remove from init or default empty list?
        self.codification = self.__set_subject_codification()
        self.subject_type = self.__set_subject_type()
        self.gender = self.__set_subject_gender()
        
    def __set_subject_codification(self) -> str:
        return re.findall(r"(?<=UD\d{6})_?[a-zA-Z0-9]+", self.name)[0]
        
    def __set_subject_type(self) -> SubjectType:
        if self.codification == "M":
            return SubjectType.mother
        elif bool(re.search(r'F\d*$', self.codification)):
            return SubjectType.child
        elif self.codification == "SM":
            return SubjectType.alledged_mother
        elif self.codification == "SP":
            return SubjectType.alledged_father
        elif self.codification == "P":
            return SubjectType.father
        elif bool(re.search(r'_FB\d*', self.codification)):
            return SubjectType.biological_child
        elif bool(re.search(r'_\d+M', self.codification)):
            return SubjectType.auxiliary_mother
        elif bool(re.search(r'_\d+P', self.codification)):
            return SubjectType.auxiliary_father
        elif bool(re.search(r'_\d+FB\d*', self.codification)):
            return SubjectType.auxiliary_child
        elif bool(re.search(r'S?MM', self.codification)):
            return SubjectType.maternal_grandmother
        elif bool(re.search(r'S?PM', self.codification)):
            return SubjectType.maternal_grandfather
        elif bool(re.search(r'S?MP', self.codification)):
            return SubjectType.paternal_grandmother
        elif bool(re.search(r'S?PP', self.codification)):
            return SubjectType.paternal_grandfather
        elif bool(re.search(r'S?TM', self.codification)):
            return SubjectType.maternal_uncle
        elif bool(re.search(r'S?TP', self.codification)):
            return SubjectType.paternal_uncle
        elif bool(re.search(r'OUT\d*', self.codification)):
            return SubjectType.another
    
    def __set_subject_gender(self) -> Gender:
        if self.subject_type == SubjectType.alledged_father or self.subject_type == SubjectType.father or \
           self.subject_type == SubjectType.auxiliary_father or self.subject_type == SubjectType.maternal_grandfather or \
           self.subject_type == SubjectType.paternal_grandfather:
            return Gender.male
        elif self.subject_type == SubjectType.mother or self.subject_type == SubjectType.alledged_mother or \
             self.subject_type == SubjectType.auxiliary_mother or self.subject_type == SubjectType.maternal_grandmother or \
             self.subject_type == SubjectType.paternal_grandmother:
            return Gender.female
        else:
            return Gender.either
            
    def get_genetic_profile_as_dictionary(self) -> dict[str: Genotype]:
        dict = {}
        for genotype in self.genetic_profile:
            dict[genotype.locus] = genotype
        return(dict)