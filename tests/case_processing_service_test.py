import unittest
from controller.case_processing_service import CaseProcessingService
from model.genotype import Genotype
from model.lab_case import LabCase

from model.subject import Subject

class CaseProcessingServiceTest(unittest.TestCase):
    def test_amelogenin_swap(self):
        case_processing_service = CaseProcessingService
        case_name = "UD990000"
        
        # mother_name = case_name+"M"
        # children_name = case_name+"F"
        # father_name = case_name+"SP"
        # auxiliary_mother_name = case_name+"_1M"
        # maternal_grandfather_name = case_name+"PM"
        # maternal_grandmother_name = case_name+"MM"
        # paternal_grandfather_name = case_name+"SPP"
        # paternal_grandmother_name = case_name+"SMP"

        # male_genotype = Genotype(kit="VE", locus="Amel", allele_1="X", allele_2="Y")
        # female_genotype = Genotype(kit="VE", locus="Amel", allele_1="X", allele_2="X")
        
        # father = Subject(father_name, [male_genotype])
        # mother = Subject(mother_name, [female_genotype])
        # male_children = Subject(children_name, [male_genotype])
        # female_children = Subject(children_name, [female_genotype])
        # auxiliary_mother =  Subject(auxiliary_mother_name, [female_genotype])
        # maternal_grandfather = Subject(maternal_grandfather_name, [male_genotype])
        # maternal_grandmother = Subject(maternal_grandmother_name, [female_genotype])
        # paternal_grandfather = Subject(paternal_grandfather_name, [male_genotype])
        # paternal_grandmother = Subject(paternal_grandmother_name, [female_genotype])
        
        # swapped_father = Subject(father_name, [female_genotype])
        # swapped_mother = Subject(mother_name, [male_genotype])
        # swapped_male_children = Subject(children_name, [female_genotype])
        # swapped_female_children = Subject(children_name, [male_genotype])
        # swapped_auxiliary_mother =  Subject(auxiliary_mother_name, [male_genotype])
        # swapped_maternal_grandfather = Subject(maternal_grandfather_name, [female_genotype])
        # swapped_maternal_grandmother = Subject(maternal_grandmother_name, [male_genotype])
        # swapped_paternal_grandfather = Subject(paternal_grandfather_name, [female_genotype])
        # swapped_paternal_grandmother = Subject(paternal_grandmother_name, [male_genotype])
        correct_case = LabCase(case_name)
        correct_case.subjects.append()
        
        swapped_case = LabCase(case_name)
        swapped_case.subjects.append()
        
        self.assertTrue(case_processing_service.check_amelogenin_swap(swapped_case))
        self.assertFalse(case_processing_service.check_amelogenin_swap(correct_case))
        pass
    
    def test_set_case_subtype(self):
        pass