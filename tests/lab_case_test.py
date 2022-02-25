import unittest

from model.lab_case import LabCase, LabCaseType
from model.subject import Subject

class TypeOfCase(unittest.TestCase):
    
    def test_get_case_type(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        children_name = case_name+"F"
        alledged_father_name = case_name+"SP"
        alledged_mother_name = case_name+"SM"
        uncle_name = case_name+"STP1"
        genotype = []
        genetic_profile = genotype

        mother = Subject(mother_name, genetic_profile)
        alledged_mother = Subject(alledged_mother_name, genetic_profile)
        children = Subject(children_name, genetic_profile)
        alledged_father = Subject(alledged_father_name, genetic_profile)
        uncle = Subject(uncle_name, genetic_profile)
        
        lab_case_TRIO = LabCase(case_name)
        lab_case_TRIO.subjects = [mother, children, alledged_father]
        
        lab_case_DUO_AF = LabCase(case_name)
        lab_case_DUO_AF.subjects = [children, alledged_father]
        
        lab_case_DUO_AM = LabCase(case_name)
        lab_case_DUO_AM.subjects = [alledged_mother, children]
        
        lab_case_COMPLEX = LabCase(case_name)
        lab_case_COMPLEX.subjects = [mother, children, uncle]
        
        self.assertEquals(lab_case_TRIO.type_of_case(), LabCaseType.trio)
        self.assertEquals(lab_case_DUO_AF.type_of_case(), LabCaseType.duo)
        self.assertEquals(lab_case_DUO_AM.type_of_case(), LabCaseType.duo)
        self.assertEquals(lab_case_COMPLEX.type_of_case(), LabCaseType.complex)