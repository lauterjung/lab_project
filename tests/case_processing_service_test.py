import unittest
from controller.case_processing_service import CaseProcessingService, LabCaseSubType
from model.genotype import Genotype
from model.lab_case import LabCase

# from model.subject import Subject
from tests.utils.test_setup import TestSetup

class CaseProcessingServiceTest(unittest.TestCase):
    def setUp(self):
        self.test_setup = TestSetup()

    def test_check_subject_amelogenin_swap(self):
        case_processing_service = CaseProcessingService()

        self.assertTrue(case_processing_service.check_subject_amelogenin_swap(self.test_setup.swapped_mother))
        self.assertTrue(case_processing_service.check_subject_amelogenin_swap(self.test_setup.swapped_alledged_father))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.mother))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.alledged_father))
        self.assertFalse(case_processing_service.check_subject_amelogenin_swap(self.test_setup.child))

    def test_check_case_amelogenin_swap(self):
        case_processing_service = CaseProcessingService()

        self.assertTrue(case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_trio))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_trio))
        self.assertTrue(case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_duo))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_duo))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.no_gender_case_complex))
    
    def test_check_swap_trio(self):
        case_processing_service = CaseProcessingService()

        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_000), [0, 0, 0]) 
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_200), [2, 0, 0])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_400), [4, 0, 0])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_020), [0, 2, 0])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_040), [0, 4, 0])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_002), [0, 0, 2])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_004), [0, 0, 4])
        self.assertEqual(case_processing_service.check_swap_trio(self.test_setup.case_111), [1, 1, 1])

    def test_set_case_subtype(self):
        case_processing_service = CaseProcessingService()

        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.ready) 
        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.exclusion) 
        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.swap) 
        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.mutation_mother) 
        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.mutation_father) 
        self.assertEqual(case_processing_service.set_case_subtype(), LabCaseSubType.other) 