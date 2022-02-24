import unittest

from model.subject import Subject

class TypeOfCase(unittest.TestCase):
    
    def test_set_subject_type(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        children_name = case_name+"F"
        father_name = case_name+"SP"
        biologic_children_name = case_name+"FB1"
        auxiliary_children_name = case_name+"_1FB1"
        auxiliary_mother_name = case_name+"_1M"

        father = Subject(father_name, [])
        mother = Subject(mother_name, [])
        children = Subject(children_name, [])
        biologic_children =  Subject(biologic_children_name, [])
        auxiliary_children =  Subject(auxiliary_children_name, [])
        auxiliary_mother =  Subject(auxiliary_mother_name, [])
        
        self.assertEqual(mother.type, "M")
        self.assertEqual(children.type, "F")
        self.assertEqual(father.type, "SP")
        self.assertEqual(biologic_children.type, "FB1")
        self.assertEqual(auxiliary_children.type, "1FB1")
        self.assertEqual(auxiliary_mother.type, "1M")