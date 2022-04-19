import unittest
from controller.case_processing_service import CaseProcessingService
from model.lab_case import LabCase, LabCaseType
from model.subject import Subject

# from model.subject import Subject
from tests.utils.test_setup import TestSetup

class CaseProcessingServiceTest(unittest.TestCase):
    def setUp(self):
        self.test_setup = TestSetup()

    def test_populate_lab_case(self):
        self.assertTrue(0)

    def test_define_type_of_case(self):
        self.assertTrue(0)

    def test_check_subject_amelogenin_swap(self):
        case_processing_service = CaseProcessingService()

        self.assertTrue(case_processing_service.check_subject_amelogenin_swap(self.test_setup.swapped_mother))
        self.assertTrue(case_processing_service.check_subject_amelogenin_swap(self.test_setup.swapped_alledged_father))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.mother))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.alledged_father))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.child))

    def test_check_case_amelogenin_swap(self):
        case_processing_service = CaseProcessingService()

        result_swapped_case_trio = case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_trio)
        result_swapped_case_trio_2 = case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_trio_2)
        result_correct_case_trio = case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_trio)
        result_swapped_case_duo = case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_duo)
        result_correct_case_duo = case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_duo)
        result_no_gender_case_complex = case_processing_service.check_case_amelogenin_swap(self.test_setup.no_gender_case_complex)

        self.assertEquals(result_swapped_case_trio, [(True, self.test_setup.swapped_mother)])
        # self.assertListEqual(result_swapped_case_trio_2, [(True, self.test_setup.swapped_mother), (True, self.test_setup.swapped_alledged_father)])
        self.assertEquals(result_correct_case_trio, [])
        # why next assert isn't working?
        self.assertEquals(result_swapped_case_duo, [(True, self.test_setup.swapped_alledged_father_duo)])
        self.assertEquals(result_correct_case_duo, [])
        self.assertEquals(result_no_gender_case_complex, [])
        
    def test_check_swap_trio(self):
        case_processing_service = CaseProcessingService()

        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_000), [0, 0, 0]) 
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_200), [2, 0, 0])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_400), [4, 0, 0])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_020), [0, 2, 0])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_040), [0, 4, 0])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_002), [0, 0, 2])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_004), [0, 0, 4])
        self.assertEqual(case_processing_service.check_inconcistencies_trio(self.test_setup.case_111), [1, 1, 1])

    def test_set_type_of_case(self):
        case_processing_service = CaseProcessingService()
        case_name = "UD990000"
        
        mother_name = case_name + "M"
        father_name = case_name + "P"
        children_name = case_name + "F"
        alledged_father_name = case_name + "SP"
        alledged_mother_name = case_name + "SM"
        uncle_name = case_name + "STP1"

        mother = Subject(mother_name, [])
        father = Subject(father_name, [])
        alledged_mother = Subject(alledged_mother_name, [])
        children = Subject(children_name, [])
        alledged_father = Subject(alledged_father_name, [])
        uncle = Subject(uncle_name, [])
        
        lab_case_INVALID = LabCase(case_name)
        lab_case_INVALID.subjects = [mother, alledged_father]

        lab_case_TRIO_AF = LabCase(case_name)
        lab_case_TRIO_AF.subjects = [mother, children, alledged_father]

        lab_case_TRIO_AM = LabCase(case_name)
        lab_case_TRIO_AM.subjects = [alledged_mother, children, father]
        
        lab_case_DUO_AF = LabCase(case_name)
        lab_case_DUO_AF.subjects = [children, alledged_father]
        
        lab_case_DUO_AM = LabCase(case_name)
        lab_case_DUO_AM.subjects = [alledged_mother, children]
        
        lab_case_COMPLEX = LabCase(case_name)
        lab_case_COMPLEX.subjects = [mother, children, uncle]

        lab_case_INVALID.type_of_case = case_processing_service.define_type_of_case(lab_case_INVALID)
        lab_case_TRIO_AF.type_of_case = case_processing_service.define_type_of_case(lab_case_TRIO_AF)
        lab_case_TRIO_AM.type_of_case = case_processing_service.define_type_of_case(lab_case_TRIO_AM)
        lab_case_DUO_AF.type_of_case = case_processing_service.define_type_of_case(lab_case_DUO_AF)
        lab_case_DUO_AM.type_of_case = case_processing_service.define_type_of_case(lab_case_DUO_AM)
        lab_case_COMPLEX.type_of_case = case_processing_service.define_type_of_case(lab_case_COMPLEX)

        self.assertEquals(lab_case_INVALID.type_of_case, LabCaseType.invalid)
        self.assertEquals(lab_case_TRIO_AF.type_of_case, LabCaseType.trio)
        self.assertEquals(lab_case_TRIO_AM.type_of_case, LabCaseType.maternity_trio)
        self.assertEquals(lab_case_DUO_AF.type_of_case, LabCaseType.duo)
        self.assertEquals(lab_case_DUO_AM.type_of_case, LabCaseType.maternity_duo)
        self.assertEquals(lab_case_COMPLEX.type_of_case, LabCaseType.complex)
        
    # def test_set_case_subtype(self):
    #     case_processing_service = CaseProcessingService()

    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.ready) 
    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.exclusion) 
    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.swap) 
    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.mutation_mother) 
    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.mutation_father) 
    #     self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.other) 