import unittest

from model.subject import Gender, SubjectType
from tests.utils.test_setup import TestSetup

class TypeOfSubject(unittest.TestCase):
    def setUp(self):
        self.test_setup = TestSetup()
        
    def test_set_subject_codification(self):
        self.assertEqual(self.test_setup.mother.codification, "M")
        self.assertEqual(self.test_setup.child.codification, "F")
        self.assertEqual(self.test_setup.child_2.codification, "F2")
        self.assertEqual(self.test_setup.alledged_father.codification, "SP")
        self.assertEqual(self.test_setup.alledged_mother.codification, "SM")
        self.assertEqual(self.test_setup.father.codification, "P")
        self.assertEqual(self.test_setup.biologic_child_1.codification, "_FB1")
        self.assertEqual(self.test_setup.biologic_child_2.codification, "_FB2")
        self.assertEqual(self.test_setup.auxiliary_mother_1.codification, "_1M")
        self.assertEqual(self.test_setup.auxiliary_mother_2.codification, "_2M")
        self.assertEqual(self.test_setup.auxiliary_father_1.codification, "_1P")
        self.assertEqual(self.test_setup.auxiliary_father_2.codification, "_2P")
        self.assertEqual(self.test_setup.auxiliary_child_1_1.codification, "_1FB1")
        self.assertEqual(self.test_setup.auxiliary_child_1_2.codification, "_1FB2")
        self.assertEqual(self.test_setup.auxiliary_child_2_1.codification, "_2FB1")
        self.assertEqual(self.test_setup.auxiliary_child_2_2.codification, "_2FB2")
        self.assertEqual(self.test_setup.maternal_grandmother.codification, "MM")
        self.assertEqual(self.test_setup.alledged_maternal_grandmother.codification, "SMM")
        self.assertEqual(self.test_setup.maternal_grandfather.codification, "PM")
        self.assertEqual(self.test_setup.alledged_maternal_grandfather.codification, "SPM")
        self.assertEqual(self.test_setup.paternal_grandmother.codification, "MP")
        self.assertEqual(self.test_setup.alledged_paternal_grandmother.codification, "SMP")
        self.assertEqual(self.test_setup.paternal_grandfather.codification, "PP")
        self.assertEqual(self.test_setup.alledged_paternal_grandfather.codification, "SPP")
        self.assertEqual(self.test_setup.maternal_uncle_1.codification, "TM1")
        self.assertEqual(self.test_setup.maternal_uncle_2.codification, "TM2")
        self.assertEqual(self.test_setup.alledged_maternal_uncle_1.codification, "STM1")
        self.assertEqual(self.test_setup.alledged_maternal_uncle_2.codification, "STM2")
        self.assertEqual(self.test_setup.paternal_uncle_1.codification, "TP1")
        self.assertEqual(self.test_setup.paternal_uncle_2.codification, "TP2")
        self.assertEqual(self.test_setup.alledged_paternal_uncle_1.codification, "STP1")
        self.assertEqual(self.test_setup.alledged_paternal_uncle_2.codification, "STP2")
        self.assertEqual(self.test_setup.another_1.codification, "OUT1")
        self.assertEqual(self.test_setup.another_2.codification, "OUT2")

    def test_set_subject_type(self):
        self.assertEqual(self.test_setup.mother.subject_type, SubjectType.mother)
        self.assertEqual(self.test_setup.child.subject_type, SubjectType.child)
        self.assertEqual(self.test_setup.child_2.subject_type, SubjectType.child)
        self.assertEqual(self.test_setup.alledged_father.subject_type, SubjectType.alledged_father)
        self.assertEqual(self.test_setup.alledged_mother.subject_type, SubjectType.alledged_mother)
        self.assertEqual(self.test_setup.father.subject_type, SubjectType.father)
        self.assertEqual(self.test_setup.biologic_child_1.subject_type, SubjectType.biological_child)
        self.assertEqual(self.test_setup.biologic_child_2.subject_type, SubjectType.biological_child)
        self.assertEqual(self.test_setup.auxiliary_mother_1.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(self.test_setup.auxiliary_mother_2.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(self.test_setup.auxiliary_father_1.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(self.test_setup.auxiliary_father_2.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(self.test_setup.auxiliary_child_1_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.test_setup.auxiliary_child_1_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.test_setup.auxiliary_child_2_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.test_setup.auxiliary_child_2_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(self.test_setup.maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(self.test_setup.alledged_maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(self.test_setup.maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(self.test_setup.alledged_maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(self.test_setup.paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(self.test_setup.alledged_paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(self.test_setup.paternal_grandfather.subject_type, SubjectType.paternal_grandfather)
        self.assertEqual(self.test_setup.alledged_paternal_grandfather.subject_type, SubjectType.paternal_grandfather)   
        self.assertEqual(self.test_setup.maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.test_setup.maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.test_setup.alledged_maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.test_setup.alledged_maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(self.test_setup.paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.test_setup.paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.test_setup.alledged_paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.test_setup.alledged_paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(self.test_setup.another_1.subject_type, SubjectType.another)
        self.assertEqual(self.test_setup.another_2.subject_type, SubjectType.another)

    def test_set_subject_gender(self):
        self.assertEqual(self.test_setup.mother.gender, Gender.female)
        self.assertEqual(self.test_setup.child.gender, Gender.either)
        self.assertEqual(self.test_setup.child_2.gender, Gender.either)
        self.assertEqual(self.test_setup.alledged_father.gender, Gender.male)
        self.assertEqual(self.test_setup.alledged_mother.gender, Gender.female)
        self.assertEqual(self.test_setup.father.gender, Gender.male)
        self.assertEqual(self.test_setup.biologic_child_1.gender, Gender.either)
        self.assertEqual(self.test_setup.biologic_child_2.gender, Gender.either)
        self.assertEqual(self.test_setup.auxiliary_mother_1.gender, Gender.female)
        self.assertEqual(self.test_setup.auxiliary_mother_2.gender, Gender.female)
        self.assertEqual(self.test_setup.auxiliary_father_1.gender, Gender.male)
        self.assertEqual(self.test_setup.auxiliary_father_2.gender, Gender.male)
        self.assertEqual(self.test_setup.auxiliary_child_1_1.gender, Gender.either)
        self.assertEqual(self.test_setup.auxiliary_child_1_2.gender, Gender.either)
        self.assertEqual(self.test_setup.auxiliary_child_2_1.gender, Gender.either)
        self.assertEqual(self.test_setup.auxiliary_child_2_2.gender, Gender.either)
        self.assertEqual(self.test_setup.maternal_grandmother.gender, Gender.female)
        self.assertEqual(self.test_setup.alledged_maternal_grandmother.gender, Gender.female)
        self.assertEqual(self.test_setup.maternal_grandfather.gender, Gender.male)
        self.assertEqual(self.test_setup.alledged_maternal_grandfather.gender, Gender.male)
        self.assertEqual(self.test_setup.paternal_grandmother.gender, Gender.female)
        self.assertEqual(self.test_setup.alledged_paternal_grandmother.gender, Gender.female)
        self.assertEqual(self.test_setup.paternal_grandfather.gender, Gender.male)
        self.assertEqual(self.test_setup.alledged_paternal_grandfather.gender, Gender.male)
        self.assertEqual(self.test_setup.maternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.test_setup.maternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.test_setup.alledged_maternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.test_setup.alledged_maternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.test_setup.paternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.test_setup.paternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.test_setup.alledged_paternal_uncle_1.gender, Gender.either)
        self.assertEqual(self.test_setup.alledged_paternal_uncle_2.gender, Gender.either)
        self.assertEqual(self.test_setup.another_1.gender, Gender.either)
        self.assertEqual(self.test_setup.another_2.gender, Gender.either)
    
    # TODO:
    def test_get_genetic_profile_as_dictionary(self):
        pass