import unittest

from model.lab_case import LabCase, LabCaseType
from model.subject import Subject
from controller.database import LabCaseDB
from controller.lab_case_controller import LabCaseController, LabCaseController

class LabCaseControllerTest(unittest.TestCase):

    def test_register_lab_case(self):

        case_name = "UD990000"
        
        lab_case = LabCase(case_name)
        
        lab_case_db_mock = LabCaseDBMock()
        lab_case_controller = LabCaseController(lab_case_db_mock)
        
        lab_case_controller.register_lab_case(lab_case)
        self.assertEquals(lab_case_db_mock.fetch(lab_case.name), lab_case)

    def test_register_lab_case_updates_existing_case(self):
        
        name = "UD990000"
        case = LabCase(name)
        
        juridic_cases = ["a"]
        card_numbers = ["a"]
        
        case.juridic_cases = juridic_cases
        case.card_numbers = card_numbers
        
        database = LabCaseDBMock()
        database.save(case)
        
        updated_juridic_cases = ["a", "b"]
        updated_card_numbers = ["a", "b"]
        
        updated_case = LabCase(name)
        updated_case.juridic_cases = updated_juridic_cases
        updated_case.card_numbers = updated_card_numbers
        
        controller = LabCaseController(database)
        controller.register_lab_case(updated_case)
        
        fetched_case = database.fetch(case.name)
        
        self.assertEquals(len(database.lab_cases), 1)
        self.assertEquals(fetched_case.juridic_cases, updated_juridic_cases)

    def test_import_allele_table(self):
        file = "tests/assets/allele_table_example.csv"

        id = 1
        name = "UD990000"
        case = LabCase(name)

        database = LabCaseDBMock()
        database.save(case)

        controller = LabCaseController(database)
        controller.import_allele_table(case, file)
        
        fetched_case = database.fetch(case.name)
        self.assertEquals(len(fetched_case.subjects), 1)

        fetched_subject = fetched_case.subjects[0]
        self.assertEquals(fetched_subject.name, "UD000000F_VE")
        self.assertEquals(len(fetched_subject.genetic_profile), 4)
        self.assertEquals(fetched_subject.genetic_profile[0].kit, "VE")
    
    def test_set_type_of_case(self):
        case_name = "UD990000"
        
        mother_name = case_name+"M"
        father_name = case_name+"P"
        children_name = case_name+"F"
        alledged_father_name = case_name+"SP"
        alledged_mother_name = case_name+"SM"
        uncle_name = case_name+"STP1"

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
        
        database = LabCaseDBMock()
        controller = LabCaseController(database)

        lab_case_INVALID.type_of_case = controller.set_type_of_case(lab_case_INVALID)
        lab_case_TRIO_AF.type_of_case = controller.set_type_of_case(lab_case_TRIO_AF)
        lab_case_TRIO_AM.type_of_case = controller.set_type_of_case(lab_case_TRIO_AM)
        lab_case_DUO_AF.type_of_case = controller.set_type_of_case(lab_case_DUO_AF)
        lab_case_DUO_AM.type_of_case = controller.set_type_of_case(lab_case_DUO_AM)
        lab_case_COMPLEX.type_of_case = controller.set_type_of_case(lab_case_COMPLEX)

        self.assertEquals(lab_case_INVALID.type_of_case, LabCaseType.invalid)
        self.assertEquals(lab_case_TRIO_AF.type_of_case, LabCaseType.trio)
        self.assertEquals(lab_case_TRIO_AM.type_of_case, LabCaseType.maternity_trio)
        self.assertEquals(lab_case_DUO_AF.type_of_case, LabCaseType.duo)
        self.assertEquals(lab_case_DUO_AM.type_of_case, LabCaseType.maternity_duo)
        self.assertEquals(lab_case_COMPLEX.type_of_case, LabCaseType.complex)
        
class LabCaseDBMock(LabCaseDB):
    lab_cases: list[LabCase]
    
    def __init__(self):
        self.lab_cases = []
    
    def save(self, case: LabCase):
        self.lab_cases.append(case)
        # TODO: if exists
    
    def fetch(self, name: str) -> LabCase:
        for saved_case in self.lab_cases:
            if(saved_case.name == name):
                return saved_case
        return None
    
    def update(self, case: LabCase):
        for i, saved_case in enumerate(self.lab_cases):
            if(saved_case.name == case.name):
                self.lab_cases[i] = case