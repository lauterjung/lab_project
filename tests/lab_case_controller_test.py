import unittest

from classes.lab_case import LabCase
from classes.subject import Subject, SubjectType
from controller.database import LabCaseDB
from controller.lab_case_controller import LabCaseController, LabCaseControllerImpl

class LabCaseControllerTest(unittest.TestCase):

    def test_register_lab_case(self):
        case_id = 1
        juridic_cases = ["12345", "12346"]
        card_numbers = ["123", "456"]
        
        lab_case = LabCase(juridic_cases, card_numbers)
        lab_case.case_id = case_id
        
        lab_case_db_mock = LabCaseDBMock()
        lab_case_controller = LabCaseControllerImpl(lab_case_db_mock)
        
        lab_case_controller.register_lab_case(lab_case)
        self.assertEquals(lab_case_db_mock.fetch(case_id), lab_case)

    def test_register_lab_case_updates_existing_case(self):
        case_id = 1
        juridic_cases = ["a"]
        card_numbers = ["a"]
        
        case = LabCase(juridic_cases, card_numbers)
        case.case_id = case_id
        
        database = LabCaseDBMock()
        database.save(case)
        
        updated_juridic_cases = ["a", "b"]
        updated_card_numbers = ["a", "b"]
        updated_case = LabCase(updated_juridic_cases, updated_card_numbers)
        updated_case.case_id = case_id

        controller = LabCaseControllerImpl(database)
        controller.register_lab_case(updated_case)
        
        fetched_case = database.fetch(case.case_id)
        
        self.assertEquals(len(database.lab_cases), 1)
        self.assertEquals(fetched_case.juridic_cases, updated_juridic_cases)

    def test_import_allele_table(self):
        file_path = "assets/allele_table_example.csv"

        case_id = 1
        juridic_cases = ["a"]
        card_numbers = ["a"]
        case = LabCase(juridic_cases, card_numbers)
        case.case_id = case_id

        database = LabCaseDBMock()
        database.save(case)

        controller = LabCaseControllerImpl(database)
        controller.import_allele_table(case, file_path)
        
        fetched_case = database.fetch(case.case_id)
        self.assertEquals(len(fetched_case.subjects), 1)

        fetched_subject = fetched_case.subjects[0]
        self.assertEquals(fetched_subject.type, SubjectType.child)
        self.assertEquals(fetched_subject.name, "UD000000F_VE")
        self.assertEquals(len(fetched_subject.genetic_profile), 4)

        
        
class LabCaseDBMock(LabCaseDB):
    lab_cases: list[LabCase]
    
    def __init__(self):
        self.lab_cases = []
    
    def save(self, case: LabCase):
        self.lab_cases.append(case)
    
    def fetch(self, case_id: int) -> LabCase:
        for saved_case in self.lab_cases:
            if(saved_case.case_id == case_id):
                return saved_case
        return None
    
    def update(self, case: LabCase):
        for i, saved_case in enumerate(self.lab_cases):
            if(saved_case.case_id == case.case_id):
                self.lab_cases[i] = case