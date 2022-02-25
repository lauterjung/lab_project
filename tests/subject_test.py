import unittest

from model.subject import Subject
from model.subject_type import SubjectType

class TypeOfSubject(unittest.TestCase):
    
    def test_set_subject_codification(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        children_name = case_name+"F"
        father_name = case_name+"SP"
        biologic_children_name = case_name+"FB1"
        # auxiliary_children_name = case_name+"_1FB1"
        auxiliary_mother_name = case_name+"_1M"

        father = Subject(father_name, [])
        mother = Subject(mother_name, [])
        children = Subject(children_name, [])
        biologic_children =  Subject(biologic_children_name, [])
        # auxiliary_children =  Subject(auxiliary_children_name, [])
        auxiliary_mother =  Subject(auxiliary_mother_name, [])
        
        father_subject_type = SubjectType(father)
        mother_subject_type = SubjectType(mother)
        children_subject_type = SubjectType(children)
        biologic_children_subject_type =  SubjectType(biologic_children)
        # auxiliary_children_subject_type =  SubjectType(auxiliary_children)
        auxiliary_mother_subject_type =  SubjectType(auxiliary_mother)
        
        self.assertEqual(mother_subject_type.codification, "M")
        self.assertEqual(children_subject_type.codification, "F")
        self.assertEqual(father_subject_type.codification, "SP")
        self.assertEqual(biologic_children_subject_type.codification, "FB1")
        # self.assertEqual(auxiliary_children_subject_type.codification, "_1FB1")
        self.assertEqual(auxiliary_mother_subject_type.codification, "_1M")