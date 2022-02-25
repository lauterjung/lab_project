from enum import Enum
import re

# from model.subject import Subject

class SubjectTypeEnum(Enum):
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
    
class SubjectType:
    type: SubjectTypeEnum
    gender: Gender
    
    def __init__(self, subject: str, codification: str, subject_type: SubjectTypeEnum, gender: Gender):
        self.subject = subject
        self.codification = self.__set_subject_codification
        self.subject_type = self.__set_subject_type
        self.gender = self.__set_subject_gender
        
    def __set_subject_codification(self):
        self.name = re.findall(r"(?<=UD\d{6})_?[a-zA-Z0-9]+", self.subject.name)[0]
        
    def __set_subject_type(self):
        if self.codification == "M":
            return SubjectTypeEnum.mother
        elif bool(re.search(r'F\d*$', self.codification)):
            return SubjectTypeEnum.child
        elif self.codification == "SM":
            return SubjectTypeEnum.alledged_mother
        elif self.codification == "SP":
            return SubjectTypeEnum.alledged_father
        elif self.codification == "P":
            return SubjectTypeEnum.father
        elif bool(re.search(r'_FB\d*', self.codification)):
            return SubjectTypeEnum.biological_child
        elif bool(re.search(r'_\d+M', self.codification)):
            return SubjectTypeEnum.auxiliary_mother
        elif bool(re.search(r'_\d+P', self.codification)):
            return SubjectTypeEnum.auxiliary_father
        elif bool(re.search(r'_\d+FB\d*', self.codification)):
            return SubjectTypeEnum.auxiliary_child
        elif bool(re.search(r'S?MM', self.codification)):
            return SubjectTypeEnum.maternal_grandmother
        elif bool(re.search(r'S?PM', self.codification)):
            return SubjectTypeEnum.maternal_grandfather
        elif bool(re.search(r'S?MP', self.codification)):
            return SubjectTypeEnum.paternal_grandmother
        elif bool(re.search(r'S?PP', self.codification)):
            return SubjectTypeEnum.paternal_grandfather
        elif bool(re.search(r'S?TM', self.codification)):
            return SubjectTypeEnum.maternal_uncle
        elif bool(re.search(r'S?TP', self.codification)):
            return SubjectTypeEnum.paternal_uncle
        elif bool(re.search(r'OUT\d*', self.codification)):
            return SubjectTypeEnum.another
    
    def __set_subject_gender(self):
        if self.subject_type == (SubjectTypeEnum.alledged_father | SubjectTypeEnum.father | SubjectTypeEnum.auxiliary_father | \
                                 SubjectTypeEnum.maternal_grandfather| SubjectTypeEnum.paternal_grandfather):
            return Gender.male
        elif self.subject_type == (SubjectTypeEnum.mother | SubjectTypeEnum.alledged_mother | SubjectTypeEnum.auxiliary_mother | \
                                   SubjectTypeEnum.maternal_grandmother| SubjectTypeEnum.paternal_grandmother):
            return Gender.female
        else:
            return Gender.either