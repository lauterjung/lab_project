import unittest

from model.lab_case import LabCase
from model.subject import Subject

class TypeOfCase(unittest.TestCase):
    
    def test_set_subject_type(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        children_name = case_name+"F"
        father_name = case_name+"SP"
        genotype = []
        genetic_profile = genotype
        
        father = Subject(father_name, genetic_profile)
        mother = Subject(mother_name, genetic_profile)
        children = Subject(children_name, genetic_profile)
        
        self.assertEqual(mother.type, "M")
        self.assertEqual(children.type, "F")
        self.assertEqual(father.type, "SP")

    def test_get_case_type(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        children_name = case_name+"F"
        father_name = case_name+"SP"
        uncle_name = case_name+"STP1"
        genotype = []
        genetic_profile = genotype

        mother = Subject(mother_name, genetic_profile)
        children = Subject(children_name, genetic_profile)
        father = Subject(father_name, genetic_profile)
        uncle = Subject(uncle_name, genetic_profile)
        
        lab_case_TRIO = LabCase(case_name)
        lab_case_TRIO.subjects = [mother, children, father]
        
        lab_case_DUO_AF = LabCase(case_name)
        lab_case_DUO_AF.subjects = [children, father]
        
        lab_case_DUO_AM = LabCase(case_name)
        lab_case_DUO_AM.subjects = [mother, children]
        
        lab_case_COMPLEX = LabCase(case_name)
        lab_case_COMPLEX.subjects = [mother, children, uncle]
        
        self.assertEquals(lab_case_TRIO.type_of_case(), "TRIO")
        self.assertEquals(lab_case_DUO_AF.type_of_case(), "DUO")
        self.assertEquals(lab_case_DUO_AM.type_of_case(), "DUO")
        self.assertEquals(lab_case_COMPLEX.type_of_case(), "COMPLEX")