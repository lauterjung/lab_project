import unittest

from classes.lab_case import LabCase
from controller.database import LabCaseDB
from controller.lab_case_controller import LabCaseController, LabCaseControllerImpl


class LabCaseControllerTest(unittest.TestCase):

    def test_register_lab_case(self):
        caseID = 1
        juridic_cases = ["12345", "12346"]
        card_numbers = ["123", "456"]
        
        lab_case = LabCase(juridic_cases, card_numbers)
        lab_case.caseID = caseID
        
        lab_case_db_mock = LabCaseDBMock()
        lab_case_controller = LabCaseControllerImpl(lab_case_db_mock)
        
        lab_case_controller.register_lab_case(lab_case)
        self.assertEquals(lab_case_db_mock.fetch(caseID), lab_case)
        
class LabCaseDBMock(LabCaseDB):
    
    lab_cases: list[LabCase]
    
    def __init__(self):
        self.lab_cases = []
    
    def save(self, case: LabCase):
        self.lab_cases.append(case)
    
    def fetch(self, case: int) -> LabCase:
        for saved_case in self.lab_cases:
            if(saved_case.caseID == case):
                return saved_case
            
        return None

