import unittest
from controller.case_processing_service import CaseProcessingService
from model.genotype import Genotype
from model.lab_case import LabCase

# from model.subject import Subject
from tests.utils.test_setup import TestSetup

class CaseProcessingServiceTest(unittest.TestCase):
    def setUp(self):
        self.test_setup = TestSetup()

    def test_check_case_amelogenin_swap(self):
        case_processing_service = CaseProcessingService

        self.assertTrue(case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_trio))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_trio))
        self.assertTrue(case_processing_service.check_case_amelogenin_swap(self.test_setup.swapped_case_duo))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.correct_case_duo))
        self.assertFalse(case_processing_service.check_case_amelogenin_swap(self.test_setup.no_gender_case_complex))
    
    def test_set_case_subtype(self):
        pass