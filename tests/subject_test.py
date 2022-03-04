import unittest

from model.subject import Gender, Subject, SubjectType

class TypeOfSubject(unittest.TestCase):
    def setUp(self):
        self.case_name = "UD990000"
        
        self.mother_name = self.case_name+"M"
        self.child_name = self.case_name+"F"
        self.child_2_name = self.case_name+"F2"
        self.alledged_father_name = self.case_name+"SP"
        self.alledged_mother_name = self.case_name+"SM"
        self.father_name = self.case_name+"P"
        self.biologic_child_1_name = self.case_name+"_FB1"
        self.biologic_child_2_name = self.case_name+"_FB2"
        self.auxiliary_mother_1_name = self.case_name+"_1M"
        self.auxiliary_mother_2_name = self.case_name+"_2M"
        self.auxiliary_father_1_name = self.case_name+"_1P"
        self.auxiliary_father_2_name = self.case_name+"_2P"
        self.auxiliary_child_1_1_name = self.case_name+"_1FB1"
        self.auxiliary_child_1_2_name = self.case_name+"_1FB2"
        self.auxiliary_child_2_1_name = self.case_name+"_2FB1"
        self.auxiliary_child_2_2_name = self.case_name+"_2FB2"
        self.maternal_grandmother_name = self.case_name+"MM"
        self.alledged_maternal_grandmother_name = self.case_name+"SMM"
        self.maternal_grandfather_name = self.case_name+"PM"
        self.alledged_maternal_grandfather_name = self.case_name+"SPM"
        self.paternal_grandmother_name = self.case_name+"MP"
        self.alledged_paternal_grandmother_name = self.case_name+"SMP"
        self.paternal_grandfather_name = self.case_name+"PP"
        self.alledged_paternal_grandfather_name = self.case_name+"SPP"
        self.maternal_uncle_1_name = self.case_name+"TM1"
        self.maternal_uncle_2_name = self.case_name+"TM2"
        self.alledged_maternal_uncle_1_name = self.case_name+"STM1"
        self.alledged_maternal_uncle_2_name = self.case_name+"STM2"
        self.paternal_uncle_1_name = self.case_name+"TP1"
        self.paternal_uncle_2_name = self.case_name+"TP2"
        self.alledged_paternal_uncle_1_name = self.case_name+"STP1"
        self.alledged_paternal_uncle_2_name = self.case_name+"STP2"
        self.another_1_name = self.case_name+"OUT1"
        self.another_2_name = self.case_name+"OUT2"
        
        self.mother = Subject(self.mother_name, [])
        self.child = Subject(self.child_name, [])
        self.child_2 = Subject(self.child_2_name, [])
        self.alledged_father = Subject(self.alledged_father_name, [])
        self.alledged_mother = Subject(self.alledged_mother_name, [])
        self.father = Subject(self.father_name, [])
        self.biologic_child_1 =  Subject(self.biologic_child_1_name, [])
        self.biologic_child_2 =  Subject(self.biologic_child_2_name, [])
        self.auxiliary_mother_1 =  Subject(self.auxiliary_mother_1_name, [])
        self.auxiliary_mother_2 =  Subject(self.auxiliary_mother_2_name, [])
        self.auxiliary_father_1 =  Subject(self.auxiliary_father_1_name, [])
        self.auxiliary_father_2 =  Subject(self.auxiliary_father_2_name, [])
        self.auxiliary_child_1_1 =  Subject(self.auxiliary_child_1_1_name, [])
        self.auxiliary_child_1_2 =  Subject(self.auxiliary_child_1_2_name, [])
        self.auxiliary_child_2_1 =  Subject(self.auxiliary_child_2_1_name, [])
        self.auxiliary_child_2_2 =  Subject(self.auxiliary_child_2_2_name, [])
        self.maternal_grandmother = Subject(self.maternal_grandmother_name, [])
        self.alledged_maternal_grandmother = Subject(self.alledged_maternal_grandmother_name, [])
        self.maternal_grandfather = Subject(self.maternal_grandfather_name, [])
        self.alledged_maternal_grandfather = Subject(self.alledged_maternal_grandfather_name, [])
        self.paternal_grandmother = Subject(self.paternal_grandmother_name, [])
        self.alledged_paternal_grandmother = Subject(self.alledged_paternal_grandmother_name, [])
        self.paternal_grandfather = Subject(self.paternal_grandfather_name, [])
        self.alledged_paternal_grandfather = Subject(self.alledged_paternal_grandfather_name, [])
        self.maternal_uncle_1 = Subject(self.maternal_uncle_1_name, [])
        self.maternal_uncle_2 = Subject(self.maternal_uncle_2_name, [])
        self.alledged_maternal_uncle_1 = Subject(self.alledged_maternal_uncle_1_name, [])
        self.alledged_maternal_uncle_2 = Subject(self.alledged_maternal_uncle_2_name, [])
        self.paternal_uncle_1 = Subject(self.paternal_uncle_1_name, [])
        self.paternal_uncle_2 = Subject(self.paternal_uncle_2_name, [])
        self.alledged_paternal_uncle_1 = Subject(self.alledged_paternal_uncle_1_name, [])
        self.alledged_paternal_uncle_2 = Subject(self.alledged_paternal_uncle_2_name, [])
        self.another_1 = Subject(self.another_1_name, [])
        self.another_2 = Subject(self.another_2_name, [])
    
    def test_set_subject_codification(self):
        self.assertEqual(self.mother.codification, "M")
        self.assertEqual(self.child.codification, "F")
        self.assertEqual(self.child_2.codification, "F2")
        self.assertEqual(self.alledged_father.codification, "SP")
        self.assertEqual(self.alledged_mother.codification, "SM")
        self.assertEqual(self.father.codification, "P")
        self.assertEqual(self.biologic_child_1.codification, "_FB1")
        self.assertEqual(self.biologic_child_2.codification, "_FB2")
        self.assertEqual(self.auxiliary_mother_1.codification, "_1M")
        self.assertEqual(self.auxiliary_mother_2.codification, "_2M")
        self.assertEqual(self.auxiliary_father_1.codification, "_1P")
        self.assertEqual(self.auxiliary_father_2.codification, "_2P")
        self.assertEqual(self.auxiliary_child_1_1.codification, "_1FB1")
        self.assertEqual(self.auxiliary_child_1_2.codification, "_1FB2")
        self.assertEqual(self.auxiliary_child_2_1.codification, "_2FB1")
        self.assertEqual(self.auxiliary_child_2_2.codification, "_2FB2")
        self.assertEqual(self.maternal_grandmother.codification, "MM")
        self.assertEqual(self.alledged_maternal_grandmother.codification, "SMM")
        self.assertEqual(self.maternal_grandfather.codification, "PM")
        self.assertEqual(self.alledged_maternal_grandfather.codification, "SPM")
        self.assertEqual(self.paternal_grandmother.codification, "MP")
        self.assertEqual(self.alledged_paternal_grandmother.codification, "SMP")
        self.assertEqual(self.paternal_grandfather.codification, "PP")
        self.assertEqual(self.alledged_paternal_grandfather.codification, "SPP")   
        self.assertEqual(self.maternal_uncle_1.codification, "TM1")
        self.assertEqual(self.maternal_uncle_2.codification, "TM2")
        self.assertEqual(self.alledged_maternal_uncle_1.codification, "STM1")
        self.assertEqual(self.alledged_maternal_uncle_2.codification, "STM2")
        self.assertEqual(self.paternal_uncle_1.codification, "TP1")
        self.assertEqual(self.paternal_uncle_2.codification, "TP2")
        self.assertEqual(self.alledged_paternal_uncle_1.codification, "STP1")
        self.assertEqual(self.alledged_paternal_uncle_2.codification, "STP2")
        self.assertEqual(self.another_1.codification, "OUT1")
        self.assertEqual(self.another_2.codification, "OUT2")
   
    def test_set_subject_type(self):
        self.assertEqual(self.mother.subject_type, SubjectType.mother)
        self.assertEqual(self.child.subject_type, SubjectType.child)
        self.assertEqual(self.child_2.subject_type, SubjectType.child)
        self.assertEqual(self.alledged_father.subject_type, SubjectType.alledged_father)
        self.assertEqual(self.alledged_mother.subject_type, SubjectType.alledged_mother)
        self.assertEqual(self.father.subject_type, SubjectType.father)
        self.assertEqual(self.biologic_child_1.subject_type, SubjectType.biological_child)
        self.assertEqual(self.biologic_child_2.subject_type, SubjectType.biological_child)
        self.assertEqual(self.auxiliary_mother_1.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(self.auxiliary_mother_2.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(self.auxiliary_father_1.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(self.auxiliary_father_2.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(self.auxiliary_child_1_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.auxiliary_child_1_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.auxiliary_child_2_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.auxiliary_child_2_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(self.alledged_maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(self.maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(self.alledged_maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(self.paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(self.alledged_paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(self.paternal_grandfather.subject_type, SubjectType.paternal_grandfather)
        self.assertEqual(self.alledged_paternal_grandfather.subject_type, SubjectType.paternal_grandfather)   
        self.assertEqual(self.maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.alledged_maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.alledged_maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.alledged_paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.alledged_paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.another_1.subject_type, SubjectType.another)
        self.assertEqual(self.another_2.subject_type, SubjectType.another)

    def test_set_subject_gender(self):
        self.assertEqual(self.mother.gender, Gender.female)
        self.assertEqual(self.child.gender, Gender.either)
        self.assertEqual(self.child_2.gender, Gender.either)
        self.assertEqual(self.alledged_father.gender, Gender.male)
        self.assertEqual(self.alledged_mother.gender, Gender.female)
        self.assertEqual(self.father.gender, Gender.male)
        self.assertEqual(self.biologic_child_1.gender, Gender.either)
        self.assertEqual(self.biologic_child_2.gender, Gender.either)
        self.assertEqual(self.auxiliary_mother_1.gender, Gender.female)
        self.assertEqual(self.auxiliary_mother_2.gender, Gender.female)
        self.assertEqual(self.auxiliary_father_1.gender, Gender.male)
        self.assertEqual(self.auxiliary_father_2.gender, Gender.male)
        self.assertEqual(self.auxiliary_child_1_1.gender, Gender.either)
        self.assertEqual(self.auxiliary_child_1_2.gender, Gender.either)
        self.assertEqual(self.auxiliary_child_2_1.gender, Gender.either)
        self.assertEqual(self.auxiliary_child_2_2.gender, Gender.either)
        self.assertEqual(self.maternal_grandmother.gender, Gender.female)
        self.assertEqual(self.alledged_maternal_grandmother.gender, Gender.female)
        self.assertEqual(self.maternal_grandfather.gender, Gender.male)
        self.assertEqual(self.alledged_maternal_grandfather.gender, Gender.male)
        self.assertEqual(self.paternal_grandmother.gender, Gender.female)
        self.assertEqual(self.alledged_paternal_grandmother.gender, Gender.female)
        self.assertEqual(self.paternal_grandfather.gender, Gender.male)
        self.assertEqual(self.alledged_paternal_grandfather.gender, Gender.male)   
        self.assertEqual(self.maternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.maternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.alledged_maternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.alledged_maternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.paternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.paternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.alledged_paternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.alledged_paternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.another_1.gender, Gender.either)
        self.assertEqual(self.another_2.gender, Gender.either)