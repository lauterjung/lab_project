import unittest

from model.subject import Gender, Subject, SubjectType

class TypeOfSubject(unittest.TestCase):
    
    # TODO: create a common setup for the next tests
    
    def test_set_subject_codification(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        child_name = case_name+"F"
        child_2_name = case_name+"F2"
        alledged_father_name = case_name+"SP"
        alledged_mother_name = case_name+"SM"
        father_name = case_name+"P"
        biologic_child_1_name = case_name+"_FB1"
        biologic_child_2_name = case_name+"_FB2"
        auxiliary_mother_1_name = case_name+"_1M"
        auxiliary_mother_2_name = case_name+"_2M"
        auxiliary_father_1_name = case_name+"_1P"
        auxiliary_father_2_name = case_name+"_2P"
        auxiliary_child_1_1_name = case_name+"_1FB1"
        auxiliary_child_1_2_name = case_name+"_1FB2"
        auxiliary_child_2_1_name = case_name+"_2FB1"
        auxiliary_child_2_2_name = case_name+"_2FB2"
        maternal_grandmother_name = case_name+"MM"
        alledged_maternal_grandmother_name = case_name+"SMM"
        maternal_grandfather_name = case_name+"PM"
        alledged_maternal_grandfather_name = case_name+"SPM"
        paternal_grandmother_name = case_name+"MP"
        alledged_paternal_grandmother_name = case_name+"SMP"
        paternal_grandfather_name = case_name+"PP"
        alledged_paternal_grandfather_name = case_name+"SPP"
        maternal_uncle_1_name = case_name+"TM1"
        maternal_uncle_2_name = case_name+"TM2"
        alledged_maternal_uncle_1_name = case_name+"STM1"
        alledged_maternal_uncle_2_name = case_name+"STM2"
        paternal_uncle_1_name = case_name+"TP1"
        paternal_uncle_2_name = case_name+"TP2"
        alledged_paternal_uncle_1_name = case_name+"STP1"
        alledged_paternal_uncle_2_name = case_name+"STP2"
        another_1_name = case_name+"OUT1"
        another_2_name = case_name+"OUT2"
        
        mother = Subject(mother_name, [])
        child = Subject(child_name, [])
        child_2 = Subject(child_2_name, [])
        alledged_father = Subject(alledged_father_name, [])
        alledged_mother = Subject(alledged_mother_name, [])
        father = Subject(father_name, [])
        biologic_child_1 =  Subject(biologic_child_1_name, [])
        biologic_child_2 =  Subject(biologic_child_2_name, [])
        auxiliary_mother_1 =  Subject(auxiliary_mother_1_name, [])
        auxiliary_mother_2 =  Subject(auxiliary_mother_2_name, [])
        auxiliary_father_1 =  Subject(auxiliary_father_1_name, [])
        auxiliary_father_2 =  Subject(auxiliary_father_2_name, [])
        auxiliary_child_1_1 =  Subject(auxiliary_child_1_1_name, [])
        auxiliary_child_1_2 =  Subject(auxiliary_child_1_2_name, [])
        auxiliary_child_2_1 =  Subject(auxiliary_child_2_1_name, [])
        auxiliary_child_2_2 =  Subject(auxiliary_child_2_2_name, [])
        maternal_grandmother = Subject(maternal_grandmother_name, [])
        alledged_maternal_grandmother = Subject(alledged_maternal_grandmother_name, [])
        maternal_grandfather = Subject(maternal_grandfather_name, [])
        alledged_maternal_grandfather = Subject(alledged_maternal_grandfather_name, [])
        paternal_grandmother = Subject(paternal_grandmother_name, [])
        alledged_paternal_grandmother = Subject(alledged_paternal_grandmother_name, [])
        paternal_grandfather = Subject(paternal_grandfather_name, [])
        alledged_paternal_grandfather = Subject(alledged_paternal_grandfather_name, [])
        maternal_uncle_1 = Subject(maternal_uncle_1_name, [])
        maternal_uncle_2 = Subject(maternal_uncle_2_name, [])
        alledged_maternal_uncle_1 = Subject(alledged_maternal_uncle_1_name, [])
        alledged_maternal_uncle_2 = Subject(alledged_maternal_uncle_2_name, [])
        paternal_uncle_1 = Subject(paternal_uncle_1_name, [])
        paternal_uncle_2 = Subject(paternal_uncle_2_name, [])
        alledged_paternal_uncle_1 = Subject(alledged_paternal_uncle_1_name, [])
        alledged_paternal_uncle_2 = Subject(alledged_paternal_uncle_2_name, [])
        another_1 = Subject(another_1_name, [])
        another_2 = Subject(another_2_name, [])
                         
        self.assertEqual(mother.codification, "M")
        self.assertEqual(child.codification, "F")
        self.assertEqual(child_2.codification, "F2")
        self.assertEqual(alledged_father.codification, "SP")
        self.assertEqual(alledged_mother.codification, "SM")
        self.assertEqual(father.codification, "P")
        self.assertEqual(biologic_child_1.codification, "_FB1")
        self.assertEqual(biologic_child_2.codification, "_FB2")
        self.assertEqual(auxiliary_mother_1.codification, "_1M")
        self.assertEqual(auxiliary_mother_2.codification, "_2M")
        self.assertEqual(auxiliary_father_1.codification, "_1P")
        self.assertEqual(auxiliary_father_2.codification, "_2P")
        self.assertEqual(auxiliary_child_1_1.codification, "_1FB1")
        self.assertEqual(auxiliary_child_1_2.codification, "_1FB2")
        self.assertEqual(auxiliary_child_2_1.codification, "_2FB1")
        self.assertEqual(auxiliary_child_2_2.codification, "_2FB2")
        self.assertEqual(maternal_grandmother.codification, "MM")
        self.assertEqual(alledged_maternal_grandmother.codification, "SMM")
        self.assertEqual(maternal_grandfather.codification, "PM")
        self.assertEqual(alledged_maternal_grandfather.codification, "SPM")
        self.assertEqual(paternal_grandmother.codification, "MP")
        self.assertEqual(alledged_paternal_grandmother.codification, "SMP")
        self.assertEqual(paternal_grandfather.codification, "PP")
        self.assertEqual(alledged_paternal_grandfather.codification, "SPP")   
        self.assertEqual(maternal_uncle_1.codification, "TM1")
        self.assertEqual(maternal_uncle_2.codification, "TM2")
        self.assertEqual(alledged_maternal_uncle_1.codification, "STM1")
        self.assertEqual(alledged_maternal_uncle_2.codification, "STM2")
        self.assertEqual(paternal_uncle_1.codification, "TP1")
        self.assertEqual(paternal_uncle_2.codification, "TP2")
        self.assertEqual(alledged_paternal_uncle_1.codification, "STP1")
        self.assertEqual(alledged_paternal_uncle_2.codification, "STP2")
        self.assertEqual(another_1.codification, "OUT1")
        self.assertEqual(another_2.codification, "OUT2")
   
    def test_set_subject_type(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        child_name = case_name+"F"
        child_2_name = case_name+"F2"
        alledged_father_name = case_name+"SP"
        alledged_mother_name = case_name+"SM"
        father_name = case_name+"P"
        biologic_child_1_name = case_name+"_FB1"
        biologic_child_2_name = case_name+"_FB2"
        auxiliary_mother_1_name = case_name+"_1M"
        auxiliary_mother_2_name = case_name+"_2M"
        auxiliary_father_1_name = case_name+"_1P"
        auxiliary_father_2_name = case_name+"_2P"
        auxiliary_child_1_1_name = case_name+"_1FB1"
        auxiliary_child_1_2_name = case_name+"_1FB2"
        auxiliary_child_2_1_name = case_name+"_2FB1"
        auxiliary_child_2_2_name = case_name+"_2FB2"
        maternal_grandmother_name = case_name+"MM"
        alledged_maternal_grandmother_name = case_name+"SMM"
        maternal_grandfather_name = case_name+"PM"
        alledged_maternal_grandfather_name = case_name+"SPM"
        paternal_grandmother_name = case_name+"MP"
        alledged_paternal_grandmother_name = case_name+"SMP"
        paternal_grandfather_name = case_name+"PP"
        alledged_paternal_grandfather_name = case_name+"SPP"
        maternal_uncle_1_name = case_name+"TM1"
        maternal_uncle_2_name = case_name+"TM2"
        alledged_maternal_uncle_1_name = case_name+"STM1"
        alledged_maternal_uncle_2_name = case_name+"STM2"
        paternal_uncle_1_name = case_name+"TP1"
        paternal_uncle_2_name = case_name+"TP2"
        alledged_paternal_uncle_1_name = case_name+"STP1"
        alledged_paternal_uncle_2_name = case_name+"STP2"
        another_1_name = case_name+"OUT1"
        another_2_name = case_name+"OUT2"
        
        mother = Subject(mother_name, [])
        child = Subject(child_name, [])
        child_2 = Subject(child_2_name, [])
        alledged_father = Subject(alledged_father_name, [])
        alledged_mother = Subject(alledged_mother_name, [])
        father = Subject(father_name, [])
        biologic_child_1 =  Subject(biologic_child_1_name, [])
        biologic_child_2 =  Subject(biologic_child_2_name, [])
        auxiliary_mother_1 =  Subject(auxiliary_mother_1_name, [])
        auxiliary_mother_2 =  Subject(auxiliary_mother_2_name, [])
        auxiliary_father_1 =  Subject(auxiliary_father_1_name, [])
        auxiliary_father_2 =  Subject(auxiliary_father_2_name, [])
        auxiliary_child_1_1 =  Subject(auxiliary_child_1_1_name, [])
        auxiliary_child_1_2 =  Subject(auxiliary_child_1_2_name, [])
        auxiliary_child_2_1 =  Subject(auxiliary_child_2_1_name, [])
        auxiliary_child_2_2 =  Subject(auxiliary_child_2_2_name, [])
        maternal_grandmother = Subject(maternal_grandmother_name, [])
        alledged_maternal_grandmother = Subject(alledged_maternal_grandmother_name, [])
        maternal_grandfather = Subject(maternal_grandfather_name, [])
        alledged_maternal_grandfather = Subject(alledged_maternal_grandfather_name, [])
        paternal_grandmother = Subject(paternal_grandmother_name, [])
        alledged_paternal_grandmother = Subject(alledged_paternal_grandmother_name, [])
        paternal_grandfather = Subject(paternal_grandfather_name, [])
        alledged_paternal_grandfather = Subject(alledged_paternal_grandfather_name, [])
        maternal_uncle_1 = Subject(maternal_uncle_1_name, [])
        maternal_uncle_2 = Subject(maternal_uncle_2_name, [])
        alledged_maternal_uncle_1 = Subject(alledged_maternal_uncle_1_name, [])
        alledged_maternal_uncle_2 = Subject(alledged_maternal_uncle_2_name, [])
        paternal_uncle_1 = Subject(paternal_uncle_1_name, [])
        paternal_uncle_2 = Subject(paternal_uncle_2_name, [])
        alledged_paternal_uncle_1 = Subject(alledged_paternal_uncle_1_name, [])
        alledged_paternal_uncle_2 = Subject(alledged_paternal_uncle_2_name, [])
        another_1 = Subject(another_1_name, [])
        another_2 = Subject(another_2_name, [])
                         
        self.assertEqual(mother.subject_type, SubjectType.mother)
        self.assertEqual(child.subject_type, SubjectType.child)
        self.assertEqual(child_2.subject_type, SubjectType.child)
        self.assertEqual(alledged_father.subject_type, SubjectType.alledged_father)
        self.assertEqual(alledged_mother.subject_type, SubjectType.alledged_mother)
        self.assertEqual(father.subject_type, SubjectType.father)
        self.assertEqual(biologic_child_1.subject_type, SubjectType.biological_child)
        self.assertEqual(biologic_child_2.subject_type, SubjectType.biological_child)
        self.assertEqual(auxiliary_mother_1.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(auxiliary_mother_2.subject_type, SubjectType.auxiliary_mother)
        self.assertEqual(auxiliary_father_1.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(auxiliary_father_2.subject_type, SubjectType.auxiliary_father)
        self.assertEqual(auxiliary_child_1_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(auxiliary_child_1_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(auxiliary_child_2_1.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(auxiliary_child_2_2.subject_type, SubjectType.auxiliary_child)
        self.assertEqual(maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(alledged_maternal_grandmother.subject_type, SubjectType.maternal_grandmother)
        self.assertEqual(maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(alledged_maternal_grandfather.subject_type, SubjectType.maternal_grandfather)
        self.assertEqual(paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(alledged_paternal_grandmother.subject_type, SubjectType.paternal_grandmother)
        self.assertEqual(paternal_grandfather.subject_type, SubjectType.paternal_grandfather)
        self.assertEqual(alledged_paternal_grandfather.subject_type, SubjectType.paternal_grandfather)   
        self.assertEqual(maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(alledged_maternal_uncle_1.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(alledged_maternal_uncle_2.subject_type, SubjectType.maternal_uncle)
        self.assertEqual(paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(alledged_paternal_uncle_1.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(alledged_paternal_uncle_2.subject_type, SubjectType.paternal_uncle)
        self.assertEqual(another_1.subject_type, SubjectType.another)
        self.assertEqual(another_2.subject_type, SubjectType.another)

    def test_set_subject_gender(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        child_name = case_name+"F"
        child_2_name = case_name+"F2"
        alledged_father_name = case_name+"SP"
        alledged_mother_name = case_name+"SM"
        father_name = case_name+"P"
        biologic_child_1_name = case_name+"_FB1"
        biologic_child_2_name = case_name+"_FB2"
        auxiliary_mother_1_name = case_name+"_1M"
        auxiliary_mother_2_name = case_name+"_2M"
        auxiliary_father_1_name = case_name+"_1P"
        auxiliary_father_2_name = case_name+"_2P"
        auxiliary_child_1_1_name = case_name+"_1FB1"
        auxiliary_child_1_2_name = case_name+"_1FB2"
        auxiliary_child_2_1_name = case_name+"_2FB1"
        auxiliary_child_2_2_name = case_name+"_2FB2"
        maternal_grandmother_name = case_name+"MM"
        alledged_maternal_grandmother_name = case_name+"SMM"
        maternal_grandfather_name = case_name+"PM"
        alledged_maternal_grandfather_name = case_name+"SPM"
        paternal_grandmother_name = case_name+"MP"
        alledged_paternal_grandmother_name = case_name+"SMP"
        paternal_grandfather_name = case_name+"PP"
        alledged_paternal_grandfather_name = case_name+"SPP"
        maternal_uncle_1_name = case_name+"TM1"
        maternal_uncle_2_name = case_name+"TM2"
        alledged_maternal_uncle_1_name = case_name+"STM1"
        alledged_maternal_uncle_2_name = case_name+"STM2"
        paternal_uncle_1_name = case_name+"TP1"
        paternal_uncle_2_name = case_name+"TP2"
        alledged_paternal_uncle_1_name = case_name+"STP1"
        alledged_paternal_uncle_2_name = case_name+"STP2"
        another_1_name = case_name+"OUT1"
        another_2_name = case_name+"OUT2"
        
        mother = Subject(mother_name, [])
        child = Subject(child_name, [])
        child_2 = Subject(child_2_name, [])
        alledged_father = Subject(alledged_father_name, [])
        alledged_mother = Subject(alledged_mother_name, [])
        father = Subject(father_name, [])
        biologic_child_1 =  Subject(biologic_child_1_name, [])
        biologic_child_2 =  Subject(biologic_child_2_name, [])
        auxiliary_mother_1 =  Subject(auxiliary_mother_1_name, [])
        auxiliary_mother_2 =  Subject(auxiliary_mother_2_name, [])
        auxiliary_father_1 =  Subject(auxiliary_father_1_name, [])
        auxiliary_father_2 =  Subject(auxiliary_father_2_name, [])
        auxiliary_child_1_1 =  Subject(auxiliary_child_1_1_name, [])
        auxiliary_child_1_2 =  Subject(auxiliary_child_1_2_name, [])
        auxiliary_child_2_1 =  Subject(auxiliary_child_2_1_name, [])
        auxiliary_child_2_2 =  Subject(auxiliary_child_2_2_name, [])
        maternal_grandmother = Subject(maternal_grandmother_name, [])
        alledged_maternal_grandmother = Subject(alledged_maternal_grandmother_name, [])
        maternal_grandfather = Subject(maternal_grandfather_name, [])
        alledged_maternal_grandfather = Subject(alledged_maternal_grandfather_name, [])
        paternal_grandmother = Subject(paternal_grandmother_name, [])
        alledged_paternal_grandmother = Subject(alledged_paternal_grandmother_name, [])
        paternal_grandfather = Subject(paternal_grandfather_name, [])
        alledged_paternal_grandfather = Subject(alledged_paternal_grandfather_name, [])
        maternal_uncle_1 = Subject(maternal_uncle_1_name, [])
        maternal_uncle_2 = Subject(maternal_uncle_2_name, [])
        alledged_maternal_uncle_1 = Subject(alledged_maternal_uncle_1_name, [])
        alledged_maternal_uncle_2 = Subject(alledged_maternal_uncle_2_name, [])
        paternal_uncle_1 = Subject(paternal_uncle_1_name, [])
        paternal_uncle_2 = Subject(paternal_uncle_2_name, [])
        alledged_paternal_uncle_1 = Subject(alledged_paternal_uncle_1_name, [])
        alledged_paternal_uncle_2 = Subject(alledged_paternal_uncle_2_name, [])
        another_1 = Subject(another_1_name, [])
        another_2 = Subject(another_2_name, [])
                         
        self.assertEqual(mother.gender, Gender.female)
        self.assertEqual(child.gender, Gender.either)
        self.assertEqual(child_2.gender, Gender.either)
        self.assertEqual(alledged_father.gender, Gender.male)
        self.assertEqual(alledged_mother.gender, Gender.female)
        self.assertEqual(father.gender, Gender.male)
        self.assertEqual(biologic_child_1.gender, Gender.either)
        self.assertEqual(biologic_child_2.gender, Gender.either)
        self.assertEqual(auxiliary_mother_1.gender, Gender.female)
        self.assertEqual(auxiliary_mother_2.gender, Gender.female)
        self.assertEqual(auxiliary_father_1.gender, Gender.male)
        self.assertEqual(auxiliary_father_2.gender, Gender.male)
        self.assertEqual(auxiliary_child_1_1.gender, Gender.either)
        self.assertEqual(auxiliary_child_1_2.gender, Gender.either)
        self.assertEqual(auxiliary_child_2_1.gender, Gender.either)
        self.assertEqual(auxiliary_child_2_2.gender, Gender.either)
        self.assertEqual(maternal_grandmother.gender, Gender.female)
        self.assertEqual(alledged_maternal_grandmother.gender, Gender.female)
        self.assertEqual(maternal_grandfather.gender, Gender.male)
        self.assertEqual(alledged_maternal_grandfather.gender, Gender.male)
        self.assertEqual(paternal_grandmother.gender, Gender.female)
        self.assertEqual(alledged_paternal_grandmother.gender, Gender.female)
        self.assertEqual(paternal_grandfather.gender, Gender.male)
        self.assertEqual(alledged_paternal_grandfather.gender, Gender.male)   
        self.assertEqual(maternal_uncle_1.gender, Gender.either)
        self.assertEqual(maternal_uncle_2.gender, Gender.either)
        self.assertEqual(alledged_maternal_uncle_1.gender, Gender.either)
        self.assertEqual(alledged_maternal_uncle_2.gender, Gender.either)
        self.assertEqual(paternal_uncle_1.gender, Gender.either)
        self.assertEqual(paternal_uncle_2.gender, Gender.either)
        self.assertEqual(alledged_paternal_uncle_1.gender, Gender.either)
        self.assertEqual(alledged_paternal_uncle_2.gender, Gender.either)
        self.assertEqual(another_1.gender, Gender.either)
        self.assertEqual(another_2.gender, Gender.either)