import unittest
from controller.case_processing_service import CaseProcessingService
from model.genotype import Genotype
from model.lab_case import LabCase

from model.subject import Subject
from tests.utils.available_subjects import AvailableSubjects

class CaseProcessingServiceTest(unittest.TestCase):
    def setUp(self):
        self.all_subjects = AvailableSubjects()

    def test_amelogenin_swap(self):
        case_processing_service = CaseProcessingService
        
        male_genotype = Genotype("VE", "Amel", "X", "Y")
        female_genotype = Genotype("VE", "Amel", "X", "X")

        self.all_subjects.child.genetic_profile.append(male_genotype)

        self.all_subjects.child.genetic_profile.append(male_genotype)
        self.all_subjects.child_2.genetic_profile.append(male_genotype)
        self.all_subjects.biologic_child_1.genetic_profile.append(male_genotype)
        self.all_subjects.biologic_child_2.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_child_1_1.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_child_1_2.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_child_2_1.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_child_2_2.genetic_profile.append(male_genotype)
        self.all_subjects.maternal_uncle_1.genetic_profile.append(male_genotype)
        self.all_subjects.maternal_uncle_2.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_maternal_uncle_1.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_maternal_uncle_2.genetic_profile.append(male_genotype)
        self.all_subjects.paternal_uncle_1.genetic_profile.append(male_genotype)
        self.all_subjects.paternal_uncle_2.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_paternal_uncle_1.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_paternal_uncle_2.genetic_profile.append(male_genotype)
        self.all_subjects.another_1.genetic_profile.append(male_genotype)
        self.all_subjects.another_2.genetic_profile.append(male_genotype)

        self.all_subjects.mother.genetic_profile.append(female_genotype)
        self.all_subjects.alledged_father.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_mother.genetic_profile.append(female_genotype)
        self.all_subjects.father.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_mother_1.genetic_profile.append(female_genotype)
        self.all_subjects.auxiliary_mother_2.genetic_profile.append(female_genotype)
        self.all_subjects.auxiliary_father_1.genetic_profile.append(male_genotype)
        self.all_subjects.auxiliary_father_2.genetic_profile.append(male_genotype)
        self.all_subjects.maternal_grandmother.genetic_profile.append(female_genotype)
        self.all_subjects.alledged_maternal_grandmother.genetic_profile.append(female_genotype)
        self.all_subjects.maternal_grandfather.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_maternal_grandfather.genetic_profile.append(male_genotype)
        self.all_subjects.paternal_grandmother.genetic_profile.append(female_genotype)
        self.all_subjects.alledged_paternal_grandmother.genetic_profile.append(female_genotype)
        self.all_subjects.paternal_grandfather.genetic_profile.append(male_genotype)
        self.all_subjects.alledged_paternal_grandfather.genetic_profile.append(male_genotype)

        self.all_subjects.swapped_mother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_alledged_father.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_alledged_mother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_father.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_auxiliary_mother_1.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_auxiliary_mother_2.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_auxiliary_father_1.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_auxiliary_father_2.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_maternal_grandmother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_alledged_maternal_grandmother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_maternal_grandfather.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_alledged_maternal_grandfather.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_paternal_grandmother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_alledged_paternal_grandmother.genetic_profile.append(male_genotype)
        self.all_subjects.swapped_paternal_grandfather.genetic_profile.append(female_genotype)
        self.all_subjects.swapped_alledged_paternal_grandfather.genetic_profile.append(female_genotype)

        correct_case_trio = LabCase(self.all_subjects.case_name)
        correct_case_trio.subjects.append(self.all_subjects.mother, self.all_subjects.child, self.all_subjects.alledged_father)
        swapped_case_trio = LabCase(self.all_subjects.case_name)
        swapped_case_trio.subjects.append(self.all_subjects.swapped_mother, self.all_subjects.child, self.all_subjects.alledged_father)
        
        correct_case_duo = LabCase(self.all_subjects.case_name)
        correct_case_duo.subjects.append(self.all_subjects.child, self.all_subjects.alledged_father)
        swapped_case_duo = LabCase(self.all_subjects.case_name)
        swapped_case_duo.subjects.append(self.all_subjects.child, self.all_subjects.swapped_alledged_father)

        no_gender_case_complex = LabCase(self.all_subjects.case_name)
        no_gender_case_complex.subjects.append(self.all_subjects.child, self.all_subjects.paternal_uncle_1, self.all_subjects.maternal_uncle_1, self.all_subjects.another_1)

        # check swapp for the whole case or individually?
        self.assertTrue(case_processing_service.check_amelogenin_swap(swapped_case_trio))
        self.assertFalse(case_processing_service.check_amelogenin_swap(correct_case_trio))
        self.assertTrue(case_processing_service.check_amelogenin_swap(swapped_case_duo))
        self.assertFalse(case_processing_service.check_amelogenin_swap(correct_case_duo))
        self.assertFalse(case_processing_service.check_amelogenin_swap(no_gender_case_complex))
    
    def test_set_case_subtype(self):
        pass

    def tearDown(self):
        self.all_subjects.dispose()