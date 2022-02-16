
# OP_IGNORE?
from sre_constants import OP_IGNORE

from classes.lab_case import LabCase
from controller.database import LabCaseDB

class LabCaseController:
    
    def register_lab_case(case: LabCase):
        pass

class LabCaseControllerImpl(LabCaseController):
    def __init__(self, db: LabCaseDB):
        self.db = db
        
          
    def register_lab_case(self, case: LabCase):
        if self.db.fetch(case.case_id) == None:
            self.db.save(case)
        else:
            self.db.update(case)
            
    # def fetch(self, case: int) -> LabCase:
    # for saved_case in self.lab_cases:
    #     if(saved_case.case_id == case):
    #         return saved_case
    # return None